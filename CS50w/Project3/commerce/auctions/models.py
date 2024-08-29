from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    pass


# ! listing class 
class Listing(models.Model):


    # ! so here IDK why i keep getting a null value i need to get the is of the user though !
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="userlisting", null=True)


    # ! here the active would be always active but when the bider can turn it to False wich goona stope it 
    active = models.CharField(max_length=5, default=True)

    title = models.CharField(max_length=64)
    bid = models.IntegerField()
    description = models.CharField(max_length=10000)

    image = models.TextField(blank=True)
    category = models.CharField(max_length = 50 ,blank=True)
    

    def __str__(self):
        return f" {self.title} : {self.bid}, {self.description}, {self.category}"


class Categories(models.Model): 

    category_name = models.CharField(max_length=500, blank=True)
    listing_id = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="listing_id_in_category")

class Watchlist(models.Model):

    listing_id = models.IntegerField(null=True)
    user_id = models.IntegerField(null=True)



    def __str__(self):
        return f"{self.listing_id} : {self.user_id}"
    # get the user id and with that id get all user's lisitng that's all.


class UserBid(models.Model):

    user_new_bid = models.PositiveIntegerField(blank=True, default=0)

    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_id", null=False)

    listing_id = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="listing_id", null=False)



# make winner the has id of the winner, id of the listing and price of the winning auction (bid)

class Winner(models.Model):

    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="winner_id")

    listing_id = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="winner_listing")

    winning_price = models.PositiveIntegerField()



class Comments(models.Model):

    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name="user_comment_id")

    listing_id = models.ForeignKey(Listing, on_delete=models.CASCADE, related_name="listing_comment_id")

    comment = models.TextField(blank=False)