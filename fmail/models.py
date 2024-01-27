from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from PIL import Image
from django.urls import reverse


class Mail(models.Model):
    datetime = models.DateTimeField(default=timezone.now)
    title = models.CharField(max_length=100)
    info = models.TextField()
    sender = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='sender')
    reciever = models.ForeignKey(User, on_delete=models.DO_NOTHING, related_name='reciever')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('mail-detail', kwargs={'pk': self.pk})


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='profile-pics', default='default.jpg')

    def __str__(self):
        return f'{self.user.username}\'s Profile'

    def save(self, *args, **kwargs):
        super().save()

        img = Image.open(self.image.path)
        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)
