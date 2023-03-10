from django.db import models
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField


class Persona(models.Model):
    shamefull_nickname = models.CharField(
        max_length=50, unique=True, blank=False)
    slug = models.SlugField(max_length=50, unique=True, null=False)
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='author_persona'
        )
    shameful_pic = CloudinaryField('image', default='placeholder')
    shameful_song = models.CharField(max_length=100, blank=False)
    shameful_tv_show = models.CharField(max_length=100, blank=False)
    shameful_habit = models.CharField(max_length=150, blank=False)
    shameful_story = models.TextField()
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)
    likes = models.ManyToManyField(
        User, related_name='placard_likes', blank=True
        )

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


class Comment(models.Model):

    persona = models.ForeignKey(
        Persona, on_delete=models.CASCADE, related_name='comments'
        )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='author_comments'
        )
    content = models.CharField(max_length=2000)
    created_on = models.DateTimeField(auto_now=True)
    updated_on = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ['created_on']

    def __str__(self):
        return f'{self.user} commented persona {self.persona}'


class Like(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='author_likes'
        )
    persona = models.ForeignKey(
        Persona, on_delete=models.CASCADE, related_name='persona_likes'
        )

    def __str__(self):
        return f'{self.user} liked {self.persona}'
