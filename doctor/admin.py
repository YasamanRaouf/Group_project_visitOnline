from django.contrib import admin
from .models import Doctor


@admin.register(Doctor)
class DoctorAdmin(admin.ModelAdmin):
    list_display = [
        'doctor_id',
        # 'user__full_name',
        'get_user_full_name',
        'specialty',
        'price',
        'is_active',
    ]
#
    sortable_by = [
        'doctor_id',
    ]

    list_editable = [
        # 'user__full_name',
        'specialty',
        'price',
        'is_active',
    ]
#
    search_fields = [
        'doctor_id',
        # 'user__full_name',
        'get_user_full_name',
    ]

    def get_user_full_name(self, obj):
        return f"{obj.user.first_name} {obj.user.last_name}"

    get_user_full_name.short_description = 'Full Name'
