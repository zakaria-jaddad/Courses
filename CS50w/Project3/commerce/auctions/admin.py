from django.contrib import admin
from .models import User, Listing, Watchlist, UserBid, Winner, Comments, Categories

# Register your models here.
admin.site.register(User)
admin.site.register(Listing)
admin.site.register(Watchlist)
admin.site.register(UserBid)
admin.site.register(Winner)
admin.site.register(Comments)
admin.site.register(Categories)
