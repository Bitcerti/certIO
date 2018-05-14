from django.contrib import admin
from .models.profile import Profile
from .models.user import User

# Register your models here.

admin.site.register(Profile)

admin.site.register(User)