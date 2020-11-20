from django.db import models
from django.contrib.auth.models import User, Group

# Create models.

# An admin, or seller or customer
class PERSON(models.Model):
    user = models.OneToOneField(User, null=True, blank=True, on_delete=models.CASCADE)
    group = models.OneToOneField(Group, null=True, blank=True, on_delete=models.CASCADE, default=3)
    name = models.CharField(max_length=200, null=True)
    email = models.EmailField(max_length=200)
    image = models.ImageField(null=True, blank=True)   

    def __str__(self):
        return self.name
	
    # User profile picture
    @property
    def imageURL(self):
        try:
            url = self.image.url
        except:
            url = 'https://ssl.gstatic.com/images/branding/product/2x/avatar_square_grey_512dp.png'
        return url

# A tech item either digital or physical 
class TECH(models.Model):
	seller = models.ForeignKey(PERSON, on_delete=models.SET_NULL, null=True, blank=True)
	name = models.CharField(max_length=200)
	price = models.FloatField()

    # True for digital, false for physical 
	digital = models.BooleanField(default=False,null=True, blank=True)
	picture = models.ImageField(null=True, blank=True)

	def __str__(self):
		return self.name

	@property
	def pictureURL(self):
		try:
			url = self.picture.url
		except:
			url = 'static/media/placeholder.png'
		return url

#Each order given by a particular user(customer)
class OrderInfo(models.Model):
	customer = models.ForeignKey(PERSON, on_delete=models.SET_NULL, null=True, blank=True)
	date_ordered = models.DateTimeField(auto_now_add=True)
	complete = models.BooleanField(default=False)
	transaction_id = models.CharField(max_length=100, null=True)

	def __str__(self):
		return str(self.id)

	@property
	def shipping(self):#get if the item is digital or physical
		shipping = False
		orderedtech = self.orderedtech_set.all()
		for i in orderedtech:
			if i.tech.digital == False:
				shipping = True
		return shipping

	@property
	def get_cart_total(self):#get price total for items in cart
		orderedtechs = self.orderedtech_set.all()
		total=sum([item.get_total for item in orderedtechs])
		return total

	@property
	def get_cart_items(self):#get number of items in cart
		orderedtechs = self.orderedtech_set.all()
		total=sum([item.quantity for item in orderedtechs])
		return total

#Each items in cart
class OrderedTech(models.Model):
	tech = models.ForeignKey(TECH, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(OrderInfo, on_delete=models.SET_NULL, null=True)
	quantity = models.IntegerField(default=0, null=True, blank=True)
	date_added = models.DateTimeField(auto_now_add=True)

	@property
	def get_total(self):
		total=self.tech.price*self.quantity
		return total


class DeliveryLocation(models.Model):
	customer = models.ForeignKey(PERSON, on_delete=models.SET_NULL, null=True)
	order = models.ForeignKey(OrderInfo, on_delete=models.SET_NULL, null=True)
	address = models.CharField(max_length=200, null=False)
	city = models.CharField(max_length=200, null=False)
	state = models.CharField(max_length=200, null=False)
	zipcode = models.CharField(max_length=200, null=False)
	date_added = models.DateTimeField(auto_now_add=True)

	def __str__(self):
		return self.address
