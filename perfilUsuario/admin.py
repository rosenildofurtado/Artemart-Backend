from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User

from perfilUsuario.models import Perfil

# Define an inline admin descriptor for Employee model
# which acts a bit like a singleton
class PerfilInline(admin.StackedInline):
    model = Perfil
    can_delete = False
    verbose_name_plural = 'perfil'

# Define a new User admin
class UserAdmin(BaseUserAdmin):
    inlines = (PerfilInline,)

# Re-register UserAdmin
admin.site.unregister(User)
admin.site.register(User, UserAdmin)

from perfilUsuario.models import Perfil

admin.site.register(Perfil)