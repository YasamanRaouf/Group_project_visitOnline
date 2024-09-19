from django.contrib import admin
from .models import Comment


def approve_comments(modeladmin, request, queryset):
    queryset.update(is_approved=True)
    modeladmin.message_user(request, "Selected comments have been approved.")

approve_comments.short_description = "Approve selected comments"


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('user', 'doctor', 'visit', 'rating', 'created_at', 'is_approved')
    search_fields = ('user__email', 'doctor__name', 'text')
    list_filter = ('rating', 'created_at', 'is_approved')
    actions = [approve_comments]