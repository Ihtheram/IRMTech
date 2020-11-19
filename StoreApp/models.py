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
