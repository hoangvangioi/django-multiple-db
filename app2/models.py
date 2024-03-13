from django.db import models
from django.utils.translation import gettext_lazy as _

# Create your models here.

class App2(models.Model):
    name = models.CharField(_("Name"), max_length=50)
    content = models.CharField(_("Content"), max_length=255)
    
    def __str__(self):
        return self.name