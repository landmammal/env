from django.db import models

# Create your models here.
class User(models.Model):
    name = models.CharField(max_length=256, blank=False, null=False)
    nickname = models.CharField(max_length=256, blank=False, null=False)
    age = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return 'name: {0} | nickname: {1} | age: {2}'.format(self.name, self.nickname, self.age)
    
