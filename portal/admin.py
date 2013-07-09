from django.contrib import admin 
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User


from portal.models import project
from portal.models import user_project
from portal.models import article
from portal.models import user_extra_field

class portal_projects_Admin(admin.ModelAdmin):                             
    fieldsets = [
    ('Title', {'fields':['title', 'authors']}), 
    ]

admin.site.register(project, portal_projects_Admin)


class portal_article_Admin(admin.ModelAdmin):
    fieldsets = [
    ('Title', {'fields':['title', 'authors', 'text']}),
    ]
admin.site.register(article, portal_article_Admin)

#--------------------------------------------------------

class user_extra_field_Admin(admin.ModelAdmin):
    fieldsets = [
    ('Title', {'fields':['user', 'gender']}),
    ]
admin.site.register(user_extra_field, user_extra_field_Admin)

class UserExtraInline(admin.StackedInline):
    model = user_extra_field
    extra = 0

class portal_user_projects_Admin(admin.ModelAdmin):                             
    fieldsets = [
    ('Title', {'fields':['title', 'authors', 'user']}), 
    ]

admin.site.register(user_project, portal_user_projects_Admin)

class ProjectInline(admin.StackedInline):
    model = user_project
    extra = 0

class UserAdmin(UserAdmin):
    inlines = [ProjectInline, UserExtraInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

