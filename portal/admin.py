from django.contrib import admin 
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


from portal.models import project
from portal.models import user_project

class portal_projects_Admin(admin.ModelAdmin):                             
    fieldsets = [
    ('Title', {'fields':['title', 'authors']}), 
    ]

admin.site.register(project, portal_projects_Admin)

class portal_user_projects_Admin(admin.ModelAdmin):                             
    fieldsets = [
    ('Title', {'fields':['title', 'authors', 'user']}), 
    ]

admin.site.register(user_project, portal_user_projects_Admin)

class ProjectInline(admin.StackedInline):
    model = user_project
    extra = 0

class UserAdmin(UserAdmin):
    inlines = [ProjectInline, ]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)


