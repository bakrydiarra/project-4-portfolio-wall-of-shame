from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Persona(models.Model):
    shamefull_nickname = models.CharField(max_length=50, unique=True, blank=False)
    slug = models.SlugField(max_length=50, unique=True, null=False)
    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='placard_persona')
    shameful_pic = CloudinaryField('image', default='placeholder')
    shameful_song = models.CharField(max_length=100, blank=False)
    shameful_tv_show = models.CharField(max_length=100, blank=False)
    shameful_habit = models.CharField(max_length=150, blank=False)
    shameful_story = models.TextField()
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(User, related_name='placard_likes', blank=True)

    class Meta:
        ordering = ['-created_on']

    def __str__(self):
        return self.shamefull_nickname

    def number_of_likes(self):
        return self.likes.count()

    def number_of_comments(self):
        return self.comments.count()

    def get_absolute_url(self):
        return reverse('persona-details')

    def save(self, *args, **Kwargs):
        if not self.slug:
            self.slug = slugify(self.shamefull_nickname)
        return super().save(*args, **Kwargs)
