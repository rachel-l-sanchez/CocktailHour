from django.contrib import admin
from .models import Cocktail
from django.contrib.auth.admin import UserAdmin
from .forms import UserRegistrationForm
from django.contrib import admin 

# class CustomUserAdmin(UserAdmin):
#     model = User
#     add_form = UserRegistrationForm
#     fieldsets = (
#         *UserAdmin.fieldsets,
#         (
#             'Registration Form',
#             {
#                 'fields': (
#                     'username',
#                 )
#             }
#         )
#     )


admin.site.register(Cocktail)
# admin.site.register(User, UserAdmin)