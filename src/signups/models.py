from django.db import models
from django.utils.encoding import smart_str
# Create your models here.


class Signup(models.Model):
    first_name = models.CharField(max_length=120, null=True, blank=True)
    last_name = models.CharField(max_length=120, null=True, blank=True)
    email = models.EmailField()
    timestamp = models.DateTimeField(auto_now_add=True, auto_now=False)
    updated = models.DateTimeField(auto_now_add=False, auto_now=True)
    
    class Meta:
        verbose_name = "Signup"
        verbose_name_plural = "Signups"
    
    def __str__(self):
        return smart_str(self.email)
    