from django.db import models
from django.contrib.auth.models import AbstractUser
from django.conf import settings
from rest_framework.authtoken.models import Token
from django.db.models.signals import post_save
from django.dispatch import receiver



UNIT_CHOICES =(
	('INR', ("INR")),
	('USD', ("USD"))
)

CATEGORY_CHOICES =(
	('WATCHES', ("WATCHES")),
	('BAGS', ("BAGS")),
	('SUNGLASSES', ("SUNGLASSES")),
	('JEWELLERY', ("JEWELLERY")),
	('WALLETS', ("WALLETS")),
	('OTHERS', ("OTHERS")),
)

class ShopUser(AbstractUser, models.Model):
	name = models.CharField(max_length=30, null=False, blank=False,)
	email = models.EmailField(max_length=50, null=False, blank=False, unique = True)
	contact_number = models.CharField(max_length=13,)
	username = models.CharField(max_length=30, null=False, blank=False, unique = True)

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email']

	def __str__(self):
		return str(self.email or self.username)


class Product(models.Model):
	name = models.CharField(max_length=30, null=False, blank=False,)
	description = models.CharField(max_length=500,)
	price = models.IntegerField(null=False, blank=False,)
	unit = models.CharField(max_length=10, null=False, blank=True, choices=UNIT_CHOICES)
	category = models.CharField(max_length=10, null=False, default='OTHER', choices=CATEGORY_CHOICES)

	def __str__(self):
		return self.name


class Cart(models.Model):
	user = models.ForeignKey( ShopUser, on_delete=models.CASCADE)
	product = models.ForeignKey( Product, on_delete=models.CASCADE,)
	quantity = models.IntegerField(null=False, blank=False,)

	class Meta:
		unique_together = ('user', 'product',)

	def __str__(self):
		return self.user.name

@receiver(post_save, sender=settings.AUTH_USER_MODEL)
def create_auth_token(sender, instance=None, created=False, **kwargs):
    if created:
        Token.objects.create(user=instance)