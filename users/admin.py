from django.contrib import admin
from .models import Menu_name, Module_name, Module_action, Privilege, Role

# Register your models here.


class ModuleNameTable(admin.ModelAdmin):
    list_display = ['menuname', 'modulename']


class ModuleActionTable(admin.ModelAdmin):
    list_display = ['menuname', 'modulename', 'url']


class PrivilegeTable(admin.ModelAdmin):
    list_display = ['role', 'menuname', 'modulename', 'url', 'is_allowed']


admin.site.register(Menu_name)
admin.site.register(Module_name, ModuleNameTable)
admin.site.register(Module_action, ModuleActionTable)
admin.site.register(Privilege, PrivilegeTable)
admin.site.register(Role)