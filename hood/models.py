from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class Neighborhood(models.Model):
    hood_name = models.CharField(max_length=30)
    location = models.CharField(max_length=30)
    occupants_count = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.hood_name


class Occupant(models.Model):
    name = models.CharField(max_length=30, null=True)
    id_number = models.IntegerField(null=True)
    neighborhood = models.ForeignKey(
        Neighborhood, null=True, on_delete=models.CASCADE, blank=True)
    email = models.EmailField(null=True, blank=True)
    date_created = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Tag(models.Model):
    name = models.CharField(max_length=30, null=True)

    def __str__(self):
        return self.name


class Business(models.Model):
    business_name = models.CharField(max_length=30)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, blank=True)
    neighborhood = models.ForeignKey(
        Neighborhood, null=True, on_delete=models.CASCADE)
    business_email = models.EmailField(null=True, blank=True)
    tag = models.ManyToManyField(Tag)

    def __str__(self):
        return self.business_name


class Post(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    date_posted = models.DateTimeField(default=timezone.now)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save_post(self):
        self.save()

    def get_absolute_url(self):
        return reverse('post-detail', kwargs={'pk': self.pk})
