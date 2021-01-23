from django.db import models
from django.utils import timezone
from django.urls import reverse

# Create your models here.


class Post(models.Model):
    # Model1 - Post
    #  DESCRIPTION:
    # each posted blog should be connected
    # to a connected to the model. Where the users
    # inputted infromation is stored and allow to have drafts
    #
    author = models.ForeignKey('auth.User', on_delete=models.CASCADE) # each post is connected to an autherised user
    title = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(blank=True, null=True)

    def publish(self):
    # DESCRIPTION:
    # this method, saves the published date at the time its beeen uploaded
    #Publish date is not always set or saved.
    #This method will be used when the user submit their blog
        self.published_date = timezone.now()
        self.save()

    def get_absolute_url(self):
        #DESCRIPTION:
        # once you created an instance of the post, this method would send you
        # back to the post detail pafe with the pk correspond to it.
        return reverse('post_detail', kwargs={'pk':self.pk})

    def approve_comments(self):
    #DESCRIPTION:
    #There will be a list of comments that will correspond to a blog
    # some of these commnets will be approved comments and some will not
    # this method will filer out the unapproved comments. and show only approved
    # one.
        return self.comments.filter(approved_comment=True)

    def __str__(self):
        return self.title

class Comment(models.Model):
    # Model 2 - Comment
    #DESCRIPTION:
    # Very similar to the Post Model, any user can comment on a blog post
    # contain similar features - auther, text and created. adding on an attribute
    # aproved comment.
    post =  models.ForeignKey('blogapp.Post', related_name='comments', on_delete=models.CASCADE)# each commont is connected to a post
    author = models.CharField(max_length=200)
    text = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)

    def approve(self):
    #DESCRIPTION:
    #Class method will be used to determine a comment is approved or not.
        self.approved_comment = True
        self.save()

    def get_absolute_url(self):
    #Description:
    # When the user posted a commoned on a blog post. it will send that user
    # back to webapge that contains all the blog post.
        return reverse('post_list')

    def __str__(self):
        # DESCRIPTION:
        # Returns a comment text
        return self.text
