from io import StringIO
from .models import *
from django.core.paginator import Paginator
from PIL import Image
from django.core.files.base import ContentFile

# get user all posts 
def userAllPosts(username):
    userInformations = User.objects.get(username = username)
    userPosts = Post.objects.filter(userPost = userInformations.pk)

    return userPosts, userInformations


# formate the date 
def formatDateJoined(date):
    return date.strftime("%d %B %Y")

def getUser(username):
    return User.objects.get(username = username)

# if the two users in a db...
def isFollow(user, followedUser):
        return Following.objects.filter(follower = user, followedUser = followedUser).exists()

def followerCount(follower):
    return Following.objects.filter(followedUser = follower).count()


def followingCount(following):
    return Following.objects.filter(follower = following).count()


def getUserLikedPosts(allLikes):

    # set all userliked posts in a list 
    allUserLikesPosts = []
    
    # if the list is empty --> the user liked no posts yet
    if not allLikes:
        return []
    
    for like in allLikes:
        allUserLikesPosts.append(like.likedPost)

    return allUserLikesPosts


def getPosts(request, posts):

    Posts = Paginator(posts.order_by('-timePublish'), 10)

    # set up paginations
    page = request.GET.get('page')

    # return all 20 posts
    return Posts.get_page(page)


def checkComment(comment):

    # check comment
    if comment == '' or comment.replace(' ', '') == '':
        return False
    return True


def cropProfileImage(profileImage) :
    image = Image.open(profileImage)


    # if the image has the same width and heihgt 1:1
    if image.height == image.width :
        return profileImage

    # get long and short part
    longEdge, shortEdge  = getEadges(image)

    longEdgeMiddle = round(longEdge / 2)

    shortEdgeMiddle = round(shortEdge / 2)

    cropPart = longEdgeMiddle - shortEdgeMiddle

    # Correct the cropping coordinates
    croppedProfileImage = image.crop((cropPart, 0, longEdge - cropPart, shortEdge))

    croppedProfileImage.save(profileImage)

""" getEadges function get the longedge and the shortedge of the image """
def getEadges(image):
    # check to get the lobges part 
    if image.height < image.width:  #if this True 
        longEdge = image.width
        shortEdge = image.height
    else:   # if False 
        longEdge = image.height
        shortEdge = image.width

    return longEdge, shortEdge

