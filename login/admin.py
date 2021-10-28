from django.contrib import admin
from .models import Login

# Register your models here.

@admin.register(Login)
class Login(admin.ModelAdmin):
    list_display = ('nome_completo', 'email')
    readonly_fields = ('senha',)
