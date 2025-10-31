from django.contrib import admin
from .models import Ley, Tema, Historial, Decreto

admin.site.register(Ley)
admin.site.register(Tema)
admin.site.register(Historial)
admin.site.register(Decreto)