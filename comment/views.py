from django.shortcuts import render, get_object_or_404, redirect
from .forms import CommentForm
from doctor.models import Doctor, Visit

def doctor_comments(request, doctor_id):
    # Retrieve the doctor based on URL parameters
    doctor = get_object_or_404(Doctor, id=doctor_id)
    
    # Retrieve all approved comments for the specified doctor
    comments = Comment.objects.filter(doctor=doctor, is_approved=True).order_by('-created_at')
    
    return render(request, 'doctor_comments.html', {'doctor': doctor, 'comments': comments})

def create_comment(request, doctor_id, visit_id):
    # Retrieve doctor and visit based on URL parameters
    doctor = get_object_or_404(Doctor, id=doctor_id)
    visit = get_object_or_404(Visit, id=visit_id)
    
    if request.method == 'POST':
        form = CommentForm(request.POST, doctor=doctor, visit=visit, user=request.user)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.user = request.user  # Set the logged-in user
            comment.save()
            return redirect('doctor_comments', doctor_id=doctor_id)
    else:
        form = CommentForm(doctor=doctor, visit=visit, user=request.user)

    return render(request, 'create_comment.html', {'form': form, 'doctor': doctor})