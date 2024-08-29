from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.db.models import Max
    # ! for handeling error of getting something doesn't exist in DB    
from django.core.exceptions import ObjectDoesNotExist


# * inporting helpers file 
from .helpers.helpers import is_valid

#TODO [ ] : Models The Application Should Have At Least Three Models 
#TODO [X] : User Should Be Able To Visit A Page To Create A New Listing 
#TODO [X] : After Creating A New Listing The User Will Be Redirected To Index Page And See An Alert, All The Listing 

# ! importing models that has classes for DB
from .models import User, Listing, Watchlist, UserBid, Winner, Comments, Categories


def index(request):

    listing_success = request.session.get('listing_success', False)
    if listing_success:
        del request.session['listing_success']

    return render(request, "auctions/index.html", {
        "listing_successfull": listing_success, 
        "listings": Listing.objects.all()
    })



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
            return render(request, "auctions/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "auctions/login.html")


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
            return render(request, "auctions/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            # ! with this line you are creating a user in the database 
            user = User.objects.create_user(username, email, password)
            # * saving the user using .save() method
            user.save()

            # * if the username is already in the database the code will send and error
                # regestartion HTML page 
        except IntegrityError:
            return render(request, "auctions/register.html", {
                "message": "Username already taken."
            })
        
        # ! if there isn't any error login the user 
            # and redirect them to the index rout and the procces is over with a logged in user 
        login(request, user)
        return HttpResponseRedirect(reverse("index"))

        # ! if a user tries to acces the page using the get methode redirect them to registartion page 
    else:
        return render(request, "auctions/register.html")
    

def createListing(request):

    # * if the user submit the form to create a listing  

    if request.method == "POST":

        # ! getting the user info's, i have spend all of yeasterdy trying to make it and it's just was this line that i have forgotten about damn
        user = request.user

        # * getting the infromation fro for the listing 

        title = request.POST["title"]
        description = request.POST["description"]

        # ! if the user hadn't an image and category 
        try : 
            image = request.POST["image"]
            category = request.POST["category"]
        except ValueError:
            # if no image and category assigne None to them
            image = ""
            category = ""
        bid = request.POST["bid"]

        # TODO : verification for data that is provided by the user title, bid, description.
        if is_valid(title, bid, description) == False:
            return render(request, "auctions/create.html", {
                "missing_data": "fill all required input fiels"
            })

        # needs a verifiction for the bid 
        bid = int(request.POST["bid"])

        if bid < 1:
            return render(request, "auctions/create.html", {
                "bid": "The Bid Shoud Be Greater than 0"
            })
        
        bidListing = Listing(user = user, title = title, bid = bid, description = description, image = image, category = category)
        bidListing.save()

        # * adding listingCAtegory to the Categories Model
        Categories(category_name = category.capitalize(), 
                    # !!!!!! GETTING THE SUBMITED LISTING ID BY CALLING IT  
                    listing_id = Listing.objects.get(user = user, 
                                                        title = title,
                                                        bid = bid,
                                                        description = description, 
                                                        image = image, 
                                                        category = category
                                                    )
                ).save()

        # ? return redirect(reverse("index"), hello="hello"), surved but the other is better 
        request.session['listing_success'] = True
        return HttpResponseRedirect(reverse('index'))

    else:
        # ! is the user is not authenticated so he has no access to this page 
        if not request.user.is_authenticated:
            return HttpResponseRedirect(reverse("register"))

        # * redering the page
        return render(request, "auctions/create.html")
    
@login_required(login_url="register")
def bid(request, listing_id):
    if request.method == "POST":
        listing = Listing.objects.get(pk = listing_id)

        # * if the user add the listing to their watch list 

        if 'add_listing' in request.POST:

            # TODO : ADD LISTING TO DB
            # * inserting new list to watchlist 
            watchlist = Watchlist(listing_id = listing_id, user_id = request.user.id)
            watchlist.save()

            request.session["new_price_error"] = [True, 'Listing Has Been Added To Watch List', 'Click Here To Remove', 'primary', 'error']
            return HttpResponseRedirect(reverse("bid", kwargs = {"listing_id": listing_id}))

        # * if the user want to remove the listing from their watch list 

        if 'remove_listing' in request.POST:

            # TODO : REMOVE LISTING FROM DB 

            # *removing the listing from the Watchlist DB
            watchlist = Watchlist.objects.get(listing_id = listing_id, user_id = request.user.id)
            watchlist.delete()
            request.session["new_price_error"] = [True, 'Listing Has Been Removed From Watch List', 'Click Here To Remove', 'primary', 'error']
            return HttpResponseRedirect(reverse("bid", kwargs = {"listing_id": listing_id}))



#  ! MAKING THE LISTING UNACITVE 


        if 'active' in request.POST:
            listing.active = False
            listing.save()

            # * for showing the user they won or not

            return HttpResponseRedirect(reverse('bid', kwargs = {'listing_id': listing_id}))


#  ! ADDING NEW PRICE TO THE LISTING 

        # TODO: THERE IS SOMETHING I NEED TO FIX 

        if 'submit_new_bid' in request.POST:

            # * getting the new bid 
            new_bid_price = request.POST["new-bid"]

            # * getting the listign to user it's previus bid value 
            current_listing = Listing.objects.get(pk = listing_id)

            # * if the listing is not active 

            if current_listing.active == "False":
                request.session["new_price_error"] = [True, "This Listing Is Inactive", "Click Here To Remove", "danger", 'error']
                return HttpResponseRedirect(reverse("bid", kwargs = {"listing_id": listing_id}))
            
            # !!!!!!! IF THERE ARE BIDS OR JUST A BID IN USERBID 
            if UserBid.objects.filter(listing_id = listing_id).exists():

                listing_previous_bid = UserBid.objects.filter(listing_id = listing_id).aggregate(max_price = Max('user_new_bid'))

                # * checking if the user has inserted and int
                try: 
                    new_bid_price = int(new_bid_price)
                except ValueError:
                    request.session["new_price_error"] = [True, "Make Sure To Write Number Values In The Price Field", "Click Here To Remove", "warning", 'error']
                    return HttpResponseRedirect(reverse("bid", kwargs = {"listing_id": listing_id}))

                # ! verifing the bid, it should be greatter than prevuis bid 
                if int(new_bid_price) <= int(listing_previous_bid['max_price']):
                    request.session["new_price_error"] = [True, "price is lower or equal to the original price, ", "Provide A better Price", "danger", 'error']
                    # * passing listing_id to reverse 
                    return HttpResponseRedirect(reverse("bid", kwargs = {"listing_id": listing_id}))

                # new price bid to the user bid db 
                usersnewbid = UserBid.objects.get(user_id = request.user.id, listing_id = listing_id)
                usersnewbid.user_new_bid = new_bid_price
                usersnewbid.save()


            else:
                try: 
                    new_bid_price = int(new_bid_price)
                except ValueError:
                    request.session["new_price_error"] = [True, "Make Sure To Write Number Values In The Price Field", "Click Here To Remove", "warning", 'error']
                    return HttpResponseRedirect(reverse("bid", kwargs = {"listing_id": listing_id}))

                # !CHECKING TO SEE IF NEW PRICE IS BIGGER THAT PREVOIUS PRICE

                if new_bid_price <= Listing.objects.get(pk = listing_id).bid:
                    request.session["new_price_error"] = [True, "price is lower or equal to the original price, ", "Provide A better Price", "danger", 'error']
                    return HttpResponseRedirect(reverse("bid", kwargs = {"listing_id": listing_id}))

                else :
                    try:
                        # * Getting the userbid from the DB 
                        newprice = UserBid.objects.get(user_id = request.user.id, listing_id = listing_id)

                        # * here the user_new_bid is = 0 but i'm gonna asign it to new_bid_price
                        newprice.user_new_bid = new_bid_price 
                        newprice.save()
                        

                # TODO : ELSE CREATE IT 
                    except ObjectDoesNotExist:
                        newprice = UserBid(user_new_bid = new_bid_price , user_id = User.objects.get(pk = request.user.id), 
                                                listing_id = Listing.objects.get(pk = listing_id))
                        newprice.save()

            # * if the user has insert a succesfull price || # * notifying the user when new bid successful
            request.session["new_price_success"] = True
            listing.bid = new_bid_price
            listing.save()
            return HttpResponseRedirect(reverse("bid", kwargs = {"listing_id": listing_id}))





            # * giving the same value of new_bid_price to user_bid
        # TODO IF THE USER BID IN THE DB 

    #  ! ADDING COMMENT TO LISTING 
    if 'add-comment' in request.POST:
        
        # * GETTING THE COMMENT 
        comment = request.POST['comment']

        # * adding comment to DB    
        new_comment = Comments(user_id = User.objects.get(pk = request.user.id), 
                               listing_id = Listing.objects.get(pk = listing_id), 
                               comment = comment)

        new_comment.save()
        return HttpResponseRedirect(reverse('bid', kwargs = {'listing_id': listing_id}))


    # ! IF THE METHOD IS GET
    else:

        # * getting the listing to check if it's active if not show to the user who has the big price that he won 
        inactive_listing = Listing.objects.get(pk = listing_id)

        # seeing if the user bid exist in the DB if True do the folowing
        userbid = UserBid.objects.filter(user_new_bid = inactive_listing.bid, listing_id = listing_id).exists()

        # YES IF TRUE   
        if userbid :

            # * update the value of userbid to get the winner bid 
            userbid = UserBid.objects.get(user_new_bid = inactive_listing.bid, listing_id = listing_id)

            # checking if listing is not active  and the user id is the same as the user id 
            if inactive_listing.active == "False" and userbid.user_id.pk == request.user.id :
                request.session["new_price_error"] = [True, 'Congrats You Won The Auction', f'With a bid price = ${userbid.user_new_bid}', 'success', 'not-error']


                # ! adding the information about the winner of the auctino and id of listing, id of the user (winner)
                if not Winner.objects.filter(user_id = request.user.id, listing_id = listing_id, winning_price = userbid.user_new_bid).exists(): 

                    Winner(user_id = User.objects.get(pk = request.user.id),
                                listing_id = Listing.objects.get(pk = listing_id), 
                                winning_price = userbid.user_new_bid
                            ).save()

        # * end of showing the winner 

        # * GETTING THE WATCHLIST ATTRIBUTE TO SEE IF THE LISTING IN THE WATCHLIST 
        watchlist = False
        try:
            watchlist = Watchlist.objects.get(listing_id = listing_id, user_id = request.user.id)
            watchlist = True
        # * IF THE OBJECT DOSN'T EXIST IN THE DB
        except Watchlist.DoesNotExist:
            pass
            



        listing = Listing.objects.get(id=listing_id)

        user = User.objects.get(pk = listing.user.pk)

        # ? so here i used a method provided by gpt 
            # ! so if the bid-price is less or equal to the original price the session would have True Value 
                # ! with it the user will be redirected to the page if it's True the user will see the erro if not the user wont

        new_price_error = request.session.get('new_price_error', False)
        new_price_success = request.session.get('new_price_success', False)

        # Delete the session to make sure it will be false next time 
        if isinstance(new_price_error, list) and len(new_price_error) == 5:
            del request.session["new_price_error"]
        else: 
            new_price_error = [False, '', '', '', '']

        if new_price_success == True:
            del request.session["new_price_success"]

        # * checking for comments if any?  
        comments = None
        if Comments.objects.filter(listing_id = listing_id).exists():
            comments = Comments.objects.filter(listing_id = listing_id)

        # checking for bids if any 
        newprice = {"max_price": None}
        if UserBid.objects.filter(listing_id = listing_id).exists():    
            # getting new bid price after updated  
            newprice  = UserBid.objects.filter(listing_id = listing_id).aggregate(max_price = Max('user_new_bid'))


        return render(request, "auctions/listing.html", {
            "new_price_error": new_price_error, 
            "new_price_success": new_price_success, 
            "username": user, 
            "listing": listing, 
            "watchlist": watchlist, 
            "comments": comments, 
            "bid_price": newprice['max_price']
        })
    
@login_required(login_url="register")
def watchlist(request):
    # ! there is only one method which is GET so there is no condition for doing that 


    # * checking if the user has a listings in their watchlist 
    if not Watchlist.objects.filter(user_id = request.user.id).exists():
        return render(request, 'auctions/watch.html', {
            "listings": watchlist_litstings,
            })
    

    # getting the user ids and listing ids that are in the user watchlist 
    users_watchlist = Watchlist.objects.filter(user_id = request.user.id)

    watchlist_litstings = Listing.objects.filter(id__in =  users_watchlist.values('listing_id'))

    # the highlighted thing is a way in django to tell give me all the ids that are in somethign like id in 

    return render(request, 'auctions/watch.html', {
        "listings": watchlist_litstings, 
    })


@login_required(login_url="register")
def categories(request): 

    # * with this you get just one category name if there are a lot with the same name in the table 
    categories_listing = Categories.objects.order_by().values('category_name').distinct()

    category_out_of_range = request.session.get('category_out_of_range', [False, ''])

    if category_out_of_range[0]: 
        del request.session["category_out_of_range"]

    return render(request, 'auctions/categories.html', {
        "categories": categories_listing, 
        "category_out_of_range": category_out_of_range, 
    })


@login_required(login_url="register")
def category(request, category_name : str):

    # if no category assign "" to the category_name
    if category_name == "no-category":
        category_name = ""        


    # * if the category doesn't exist in the DB send this error 
    if not Categories.objects.filter(category_name = category_name).exists():
        request.session['category_out_of_range'] = [True, category_name]
        return HttpResponseRedirect(reverse('categories'))

    # * getting all listing ids that have the same category 
    listing_ids = Categories.objects.filter(category_name = category_name)

    listings = Listing.objects.filter(id__in = listing_ids.values('listing_id'))


    return render(request, 'auctions/category.html', {
        "listings": listings, 
        "category_name": category_name
    })







