from django.db import models
from django.utils import timezone

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=256, blank=False, null=False)
    nickname = models.CharField(max_length=256, blank=False, null=False)
    age = models.IntegerField(blank=True, null=True)
    created = models.DateTimeField(default= timezone.now())
    modified = models.DateTimeField(default= timezone.now())

    def __str__(self):
        return 'name: {0} | nickname: {1} | age: {2}'.format(self.name, self.nickname, self.age)

    def save(self, *args, **kwargs):
        if not self.id:
            self.created = timezone.now()
        
        self.modified = timezone.now()

        return super().save(*args, **kwargs)  # Call the "real" save() method.
    
