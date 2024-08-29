from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    userProfileImage = models.ImageField( upload_to='network/media/profile_images/', null=True,)
    userCoverImage = models.ImageField(upload_to='network/media/covers_images/', null=True)
    userBio = models.TextField(max_length=300, blank=True)


    # def saveImage(self):


class Post(models.Model):        
    """
    TODO : every post has : 
    -> post id 
    -> user id the id of the poster 
    -> post content
    """

    userPost = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_post")
    postContent = models.TextField(max_length=10000, null=False)
    timePublish = models.DateTimeField(auto_now=False)
    likeCount = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.userPost} made {self.postContent} in {self.timePublish}"


class Comment(models.Model):
    """
    TODO : every Comment has : 
    -> comment id 
    -> post id 
    -> user id 
    -> content of the comment       

    | 1 <- comment id | 5 <- post id  | 1 -> zakaria | holla | aug/4/2023 | 
    """

    postId = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="post_id")
    commenterId = models.ForeignKey(User, on_delete=models.CASCADE, related_name="commenter_id")
    comment = models.TextField(max_length=500, null=False)
    commentTime = models.DateTimeField(auto_now=True)


class LikedPost(models.Model):
    """
    TODO : every liked post has : 
    -> post id 
    -> user id who liked the post 
            |post number : 5 | zakaria |
            |post number : 5 | Youness |
        and wth that you can count the number 
    """
    
    likedPost = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="liked_post_id")
    userLiked = models.ForeignKey(User, on_delete=models.CASCADE, related_name="happey_user")


    class Meta:
        unique_together = ('likedPost', 'userLiked')


class Following(models.Model):
    """
    TODO : every follower has : 
    -> user id
    -> follower id 
    """

    follower = models.ForeignKey(User, on_delete=models.CASCADE, related_name="follower")
    followedUser = models.ForeignKey(User, on_delete=models.CASCADE, related_name="followed")