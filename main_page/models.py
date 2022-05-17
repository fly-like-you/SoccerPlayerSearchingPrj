from django.db import models

class Player(models.Model):
    name = models.CharField(max_length=10)
    position = models.CharField(max_length=5)
    team_name = models.CharField(max_length=30)
    pass_success_rate = models.IntegerField()
    shoot_success_rate = models.IntegerField()

    def __str__(self):
        return f'[{self.pk}] {self.name}'

    def get_absolute_url(self):
        return f'/main_page/{self.pk}/'
# Create your models here.
