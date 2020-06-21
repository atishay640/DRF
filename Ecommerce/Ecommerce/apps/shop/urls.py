# from django.urls import include, path
# from rest_framework import routers
# from .views import ShopUserViewSet

# router = routers.DefaultRouter()
# router.register(r'shopusers', ShopUserViewSet)

# # Wire up our API using automatic URL routing.
# # Additionally, we include login URLs for the browsable API.
# urlpatterns = [
#     path('', include(router.urls)),
#     path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
# ]


from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from .views import ShopUserView, AddToCartView, CartViewList, update_cart_view

urlpatterns = [
    path('shop/users', ShopUserView.as_view()),
    path('shop/users/add', ShopUserView.as_view()),
    path('shop/users/<int:uid>/cart', CartViewList.as_view()),
    path('shop/users/cart/add', AddToCartView.as_view()),
    path('shop/users/<int:uid>/cart/item/<int:pid>', update_cart_view),
]

urlpatterns = format_suffix_patterns(urlpatterns)