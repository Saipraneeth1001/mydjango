from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.contrib.auth import get_user_model


user = get_user_model()


class Post(models.Model):
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=1000)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)


# when we submit the  publish button using any kind of form then we call this function
# this function just adds the published date to the above model and we will deal with where
# its gonna appear

    def publish(self):
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title


class Comment(models.Model):

    post = models.ForeignKey('blog.Post', related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=255)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def get_absolute_url(self):
        return reverse('post_list')

    def __str__(self):
        return self.text

