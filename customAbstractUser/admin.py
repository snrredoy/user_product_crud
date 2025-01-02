from django.contrib import admin
# from .models import CustomAbstractUser
from .models import CustomAbstractBaseUser
from django.contrib.auth.admin import UserAdmin
from .forms import CustomUserCreationForm , CustomUserChangeForm

# Register your models here.
class CustomUserAdmin(UserAdmin):
    add_form= CustomUserCreationForm
    form = CustomUserChangeForm
    model = CustomAbstractBaseUser

    list_display = ['email' ,'first_name' , 'last_name' , 'is_staff' , 'is_active' ]
    list_filter = ['email' , 'is_staff' , 'is_active' ]

    fieldsets = (
        (None , {'fields' : ('email' , 'password' , 'first_name' , 'last_name' )}),
        ('Permissions' , {'fields' : ('is_staff' , 'is_active' , 'is_superuser')}),
    )

    add_fieldsets = (
        (None , {
            'classes' : ('wide',),
            'fields' : ('email' , 'password1' , 'password2' , 'is_staff' , 'is_active' , 'is_superuser')
        }),
    )

    search_fields = ['email']
    ordering = ['email']

admin.site.register(CustomAbstractBaseUser , CustomUserAdmin)