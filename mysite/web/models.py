from django.db import models
from django.utils import timezone
from django.urls import reverse

# first we need to models for our web app
# the first model is for posts and the second is for comments
# auth.User defined from user class i.e inbuilt django class


class Post(models.Model):
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    title = models.CharField(max_length=1000)
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)


# user defined method that is called immediately after creating the post form

# this publsh method is used to save  the post.
# this is just a model method here , this method is called in views.py file ...

    def publish(self):
        self.published_date = timezone.now()
        self.save()
# to filter unnecessary comments , this method is used

    def approve_comments(self):
        return self.comments.filter(approved_comment=True)

# this function tells that after successfully registering that form redirect to....
# post_detail is a html page which shows the details of the selected post with id = self.pk

    def get_absolute_url(self):
        return reverse("post_detail", kwargs={'pk': self.pk})

# when return a post by saying post.objects.all we get this output from def __str

    def __str__(self):
        return self.title

# ---------for comments --------
# the comment class is connected to Post class by the variable post
# teh foreign key var post is useful to us in the further sections ...check views.py


class Comment(models.Model):
    post = models.ForeignKey('web.Post', related_name='comments', on_delete=models.CASCADE)
    author = models.CharField(max_length=255)
    content = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    # app comment is a boolean , helps in approval or disapproval , connected to the class Post

    approved_comment = models.BooleanField(default=False)

    def approve(self):
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
        return reverse("post_list")

    def __str__(self):
        return self.content



















