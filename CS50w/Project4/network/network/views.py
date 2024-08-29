from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
import json
from datetime import datetime
from PIL import Image

# pajinations import 

from .models import * 
from .helpers import *

# @login_required(login_url='/login')
def index(request):

    if request.method == 'GET':

        # get 20 posts each 
        allPosts = getPosts(request, Post.objects.all())

        # set none  to allLikes
        allLikes = None

        # refrence to the alluserlikesPosts
        allUserLikesPosts = []

        # if user is authenticated
        if request.user.is_authenticated :

            # check if user has Liked Posts
            if LikedPost.objects.filter(userLiked = request.user).exists():
                # get all user likes
                allLikes = LikedPost.objects.filter(userLiked = request.user) # get all user liked posts 

            # store all user liked posts in a list 
            allUserLikesPosts = getUserLikedPosts(allLikes)


        return render(request, 'network/index.html', {
            'allPosts': allPosts, 
            'allLikesPosts': allUserLikesPosts,
            'comments': Comment.objects.all().order_by('-commentTime')
        })
    

    # if request is PUT
    elif request.method == 'PUT':

        # get updatePostContent
        data = json.loads(request.body)

        if data.get('postId')is not None:
            postId = data["postId"]

        if data.get('postContent') is not None:
            postUpdatedContent = data["postContent"]

        # get post
        post = Post.objects.get(pk = postId)
        post.postContent = postUpdatedContent

        # save updated post
        post.save()

        return JsonResponse({"postId": postId, 
                                "postContent": postUpdatedContent
                            })  

    # request method POST 
    else:
        autherUsername = request.user
        # information of the user
        autherInfo = User.objects.get(username=autherUsername)
        
        # get post content
        postContent = request.POST.get('postContent')

        # creat post
        newPost = Post.objects.create(
            userPost = autherInfo, 
            postContent = postContent, 
            timePublish = datetime.now()
        )
        
        # save post in DB 
        newPost.save()

        return HttpResponseRedirect(reverse('index'))


def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        password = request.POST["password"]
        user = authenticate(request, username=username, password=password)

        # Check if authentication successful
        if user is not None:
            login(request, user)
            return HttpResponseRedirect(reverse("index"))
        else:
            return render(request, "network/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "network/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("index"))


def register(request):
    if request.method == "POST":
        username = request.POST["username"]
        email = request.POST["email"]

        # Ensure password matches confirmation
        password = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password != confirmation:
            return render(request, "network/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            user = User.objects.create_user(username, email, password)
            user.save()
        except IntegrityError:
            return render(request, "network/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("index"))
    else:
        return render(request, "network/register.html")


def profile_view(request, username):

    # ! if request is POST ----> it means that the user have edit their profile
    if request.method == 'POST':

        # * START GETTING DATA FROM THE POST FORM
            # get user cover image 
        userCoverImage = request.FILES.get('coverImage', None)

            # get user profile image 
        userProfileImage = request.FILES.get('profileImage', None)

            # get user fist name 
        userFirstName = request.POST.get('firstName', '')

            # get user last name 
        userLastName = request.POST.get('lastName', '')

            # get user bio
        userBio = request.POST.get('userBio', '')

            # get user 
        user = getUser(username)

            # update user
        if userCoverImage:  # ? if the user provide a cover image 
            user.userCoverImage = userCoverImage
            
        if userProfileImage: # ? if ther user provide a profile image
            user.userProfileImage = cropProfileImage(userProfileImage) 
            # return HttpResponse(cropProfileImage(userProfileImage))

        user.first_name = userFirstName
        user.last_name = userLastName
        user.userBio = userBio

            # save update
        user.save()

        return HttpResponseRedirect(reverse('profile', kwargs={"username": username}))
    
    #if request is GET

    # get user all 20p posts and user informations 

    userPosts, userInformations = userAllPosts(username)

    userPosts = getPosts(request, userPosts)

    # formt the date_joind 
    userInformations.date_joined = formatDateJoined(userInformations.date_joined)


    # set none  to allLikes
    allLikes = None

    # refrence for allUserLiedPosts
    allUserLikesPosts = []

    # if user is authentivcated
    if request.user.is_authenticated :

        # check if user has Liked Posts
        if LikedPost.objects.filter(userLiked = request.user).exists():
            # get all user likes
            allLikes = LikedPost.objects.filter(userLiked = request.user) # get all user liked posts 

        # store all user liked posts in a list 
        allUserLikesPosts = getUserLikedPosts(allLikes)

    # render template
    return render(request, 'network/profile.html', {
        "userInformations": userInformations, 
        "userPosts": userPosts,
        "isFollow": isFollow(request.user.pk, userInformations.pk), 
        "followerCount": followerCount(userInformations), 
        "followingCount": followingCount(userInformations), 
        "allLikesPosts": allUserLikesPosts, 
        'comments': Comment.objects.all().order_by('-commentTime')
    })


@login_required(login_url='/login')
def follow(request, username):
    if request.method == 'POST':

        # ! A USER FOLLOWS THE FOLLOWED PERSONE (influencer)
        # get user informations
        user = request.user 

        # get followed user 
        followedUser = getUser(username)

        # add them to database 
        Following.objects.create(
                                follower = user, 
                                followedUser = followedUser
                            ).save()

        return HttpResponseRedirect(reverse('profile', kwargs={'username': username}))
    else:
        return HttpResponseRedirect(reverse('profile', kwargs={'username': username}))


@login_required(login_url='/login')
def unfollow(request, username):
    if request.method == 'POST':

        # ! A USER FOLLOWS THE FOLLOWED PERSONE (influencer)
        # get user informations
        user = request.user 

        # get followed user 
        followedUser = getUser(username)

        # remove the user and followed from the database 
        Following.objects.filter(follower = user, followedUser = followedUser).delete()

        return HttpResponseRedirect(reverse('profile', kwargs={'username': username}))
    else:
        return HttpResponseRedirect(reverse('profile', kwargs={'username': username}))


@login_required(login_url='/login')
def following_view(request):
    if request.method == 'POST':
        return HttpResponseRedirect(reverse('following'))

    else: # GET
        # if the user has no following
        if not Following.objects.filter(follower = request.user).exists():
            return render(request, 'network/following.html', {
                "noFollowing": True
            })        

        # get all user following    
        Followings = Following.objects.filter(follower = request.user)

        following_users = [following.followedUser for following in Followings]

        allPosts = getPosts(request, Post.objects.filter(userPost__in=following_users))

        # set none  to allLikes
        allLikes = None

        # check if user has Liked Posts
        if LikedPost.objects.filter(userLiked = request.user).exists():
            # get all user likes
            allLikes = LikedPost.objects.filter(userLiked = request.user) # get all user liked posts 

        # store all user liked posts in a list 
        allUserLikesPosts = getUserLikedPosts(allLikes)

        return render(request, 'network/following.html',{
            "allPosts": allPosts,
            "allLikesPosts": allUserLikesPosts, 
            'comments': Comment.objects.all().order_by('-commentTime')
            
        })


def like(request, post_id):

    # check if the request was manula 
    if 'HTTP_X_REQUESTED_WITH' not in request.META :

        if request.method != 'PUT':
            return HttpResponseRedirect(reverse('index'))
        else:
            # get data 
            data = json.loads(request.body)

            # get the following counter
            if data.get("likeCount") is not None:
                likeCounter = data["likeCount"]

            # get user from user id 
            post = Post.objects.get(pk = post_id)

            # update post like Counter
            post.likeCount = int(likeCounter)

            # save 
            post.save()

            # for this you need every time eather remove or add the user 
                # if the user allready exist in the database ===> remove it 
                # else add it 
            
            # if user exist in the database
            if LikedPost.objects.filter(likedPost = post, userLiked = request.user).exists():
                # remove the user
                LikedPost.objects.filter(likedPost = post, userLiked = request.user).delete()

            # if the user is not in the databse 
            else:
                # create the user 
                LikedPost.objects.create(likedPost = post, userLiked = request.user)

            return HttpResponse(status=200)

    # if request using javascript
    else:   
        # get like coounter
        likeCounter = Post.objects.get(pk = post_id).likeCount

        return JsonResponse({"likeCounter" : likeCounter})
    

def comment(request, post_id):
    if request.method == 'POST':
        # get comment information
        commenter = request.user 

        # get post  
        post = Post.objects.get(pk = post_id)

        # if the user comment is valid  
        if checkComment(request.POST["comment"]):
            comment = request.POST["comment"]

        else: # comment isn't valid
            return HttpResponse('comment is not valid.')

        # create comment 
        Comment.objects.create(
                            postId = post, 
                            commenterId = commenter, 
                            comment = comment,
                    )
            

    return HttpResponseRedirect(reverse('index'))