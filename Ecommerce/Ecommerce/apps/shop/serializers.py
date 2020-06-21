from rest_framework import serializers
from .models import ShopUser, Cart, Product


class ShopUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ShopUser
        fields = ('name', 'username', 'email', 'contact_number', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = ShopUser(
            email=validated_data['email'],
            username=validated_data['username'],
            name=validated_data['name'],
            contact_number=validated_data['contact_number'],
        )
        user.set_password(validated_data['password'])
        user.save()
        return user

class ProductSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Product
        fields = ('name', 'description', 'price', 'unit', 'category')

class ViewCartSerializer(serializers.HyperlinkedModelSerializer):
	product = ProductSerializer()

	class Meta:
		model = Cart
		fields = ('product', 'quantity')

class AddToCartSerializer(serializers.ModelSerializer):

	class Meta:
		model = Cart
		fields = ('user', 'product', 'quantity')