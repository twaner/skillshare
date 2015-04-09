from django.contrib import admin

from .models import Signup

# Admin Models

class SignupAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email', 'timestamp']

    class Meta:
        model = Signup
    
# Register your models here.

admin.site.register(Signup, SignupAdmin)
