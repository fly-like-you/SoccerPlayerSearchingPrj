from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=10)
    position = models.CharField(max_length=5)
    team_name = models.CharField(max_length=30)
    pass_success_rate = models.IntegerField()
    shoot_success_rate = models.IntegerField()

    def __str__(self):
        return f'[{self.pk}] {self.name}'
# Create your models here.
