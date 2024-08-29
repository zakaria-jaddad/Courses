from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("login", views.login_view, name="login"),
    path("logout", views.logout_view, name="logout"),
    path("register", views.register, name="register"), 
    path("create", views.createListing, name="create"), 
    path("listings/<int:listing_id>", views.bid, name="bid"), 
    path('watchlist', views.watchlist, name="watchlist"), 
    path('categories', views.categories, name="categories"), 
    path('category/<str:category_name>', views.category, name="category")
]
