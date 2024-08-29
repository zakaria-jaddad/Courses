from . import views
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"), 
    path("profile/<str:username>", views.profile_view, name="profile"), 
    path("following", views.following_view, name="following"),
    path("follow/<str:username>", views.follow, name="follow"), 
    path("unfollow/<str:username>", views.unfollow, name="unfollow"), 
    path("like/<int:post_id>", views.like, name="like"), 
    path("comment/<int:post_id>", views.comment, name="comment")
    
] + static(settings.MEDIA_URL, document_root= settings.MEDIA_ROOT) # ? this is from an article to handel uploading the videos to the database i gusse so !!!
