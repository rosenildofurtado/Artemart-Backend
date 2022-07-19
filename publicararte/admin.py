from django.contrib import admin

from publicararte.models import Categoria, Tematica, Arte, Tags

admin.site.register(Arte)
admin.site.register(Tags)
admin.site.register(Categoria)
admin.site.register(Tematica)