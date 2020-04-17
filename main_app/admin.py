from django.contrib import admin
from .models import Movie, Profile, Following
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.models import User

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

# Register your models here.
admin.site.register(Movie)
admin.site.register(Profile)
admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)
admin.site.register(Following)