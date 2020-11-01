from django.db import models
from django.contrib.auth.models import User
from django_resized import ResizedImageField
from hood.models import Neighborhood


class Profile(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE)
    id_number = models.IntegerField(default=0)
    neighborhood = models.ForeignKey(
        Neighborhood, null=True, on_delete=models.CASCADE, blank=True)
    profile_picture = ResizedImageField(size=[300, 300], quality=75,
                                        default='default.jpg', upload_to='profile_pics/')

    def __str__(self):
        return f'{self.user.username} UserProfile'
