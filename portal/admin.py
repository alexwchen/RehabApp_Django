from django.contrib import admin 
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

from portal.models import article
from portal.models import user_extra_field,user_audio

# Patient Article Admin
class portal_article_Admin(admin.ModelAdmin):
    fieldsets = [
    ('Title', {'fields':['title', 'authors', 'text']}),
    ]
admin.site.register(article, portal_article_Admin)

#--------------------------------------------------------

# User Extra Feild Admin
class user_extra_field_Admin(admin.ModelAdmin):
    fieldsets = [
    ('Title', {'fields':['user', 'gender']}),
    ]
admin.site.register(user_extra_field, user_extra_field_Admin)

class UserExtraInline(admin.StackedInline):
    model = user_extra_field
    extra = 0

#--------------------------------------------------------

# User Extra Feild Admin
class user_audio_Admin(admin.ModelAdmin):
    fieldsets = [
    ('Title', {'fields':['user', 'docfile']}),
    ]
admin.site.register(user_audio, user_audio_Admin)

class UserAudioInline(admin.StackedInline):
    model = user_audio
    extra = 0

# User Admin
class UserAdmin(UserAdmin):
    inlines = [UserExtraInline, UserAudioInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)

