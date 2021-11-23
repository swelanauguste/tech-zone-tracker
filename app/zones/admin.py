from django.contrib import admin
from .models import User, Profile, Zone, Agency


admin.site.register(User)
admin.site.register(Profile)
admin.site.register(Zone)
admin.site.register(Agency)
