from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.admin import UserAdmin
from django.utils.translation import gettext_lazy as _


# Register your models here.
class MyUserAdmin(UserAdmin):
    ordering = ['id']
    list_display = ['email', 'name', 'face_image']
    fieldsets = (
        (None, {'fields':
                    ('email',
                     'password')}),
        (_('Permissions'), {'fields':
                                ('is_active',
                                 'is_staff',
                                 'is_superuser')}),
        (_('Important dates'), {'fields':
                                    ('last_login',)})

    )
    add_fieldsets = (
        (None,
         {
             'classes': ('wide',),
             'fields':
                 (
                     'name',
                     'email',
                     'password1',
                     'password2',
                     'is_active',
                     'is_staff',
                     'is_superuser',
                     'face_image'
                 )}),
    )


User = get_user_model()
admin.site.register(User, MyUserAdmin)
