from .models import ShopUser, Cart
from .serializers import ShopUserSerializer, ViewCartSerializer, AddToCartSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, generics
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import IsAuthenticated, IsAdminUser

class ShopUserView(APIView):
    """
    List all Shop users, or create a new shop user.
    """
    def get(self, request, format=None):
        sUsers = ShopUser.objects.all()
        serializer = ShopUserSerializer(sUsers, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = ShopUserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class AddToCartView(generics.GenericAPIView):
    serializer_class = AddToCartSerializer
    def post(self, request, format=None):
        try:
            serializer = AddToCartSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            if status.HTTP_400_BAD_REQUEST:
                if serializer.errors["non_field_errors"][0].code == 'unique':
                    raise Exception("Cann't add same product more than once. Add new product.")
                else:
                    Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as exp:
            # import pdb; pdb.set_trace()
            return Response({"error" :{"message": str(exp)}}, status=status.HTTP_400_BAD_REQUEST)


class CartViewList(generics.ListAPIView):
    serializer_class = ViewCartSerializer

    def get_queryset(self):
        uid = self.kwargs['uid']
        return Cart.objects.filter(user=uid)

@api_view(['DELETE','PUT'])
@permission_classes([IsAdminUser])
def update_cart_view(request, uid, pid):

    if request.method == 'DELETE':
        item_list =  list(Cart.objects.filter(user=uid, product=pid))
        if item_list:
            item_list[0].delete()
            content = {'message': 'Item removed from cart successfully.'}
        else:
            content = {'message': 'Item does not exist in cart.'}
        return Response(content, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        if "quantity" in request.data:
            item_list =  list(Cart.objects.filter(user=uid, product=pid))
            if item_list:
                item = item_list[0]
                item.quantity = request.data["quantity"]
                item.save()
                content = {'message': 'Item updated from cart successfully.'}
            else:
                content = {'message': 'Item does not exist in cart.'}
            return Response(content, status=status.HTTP_200_OK)
        else:
            return Response({"error":{'message':"'quantity' is missing."}}, status=status.HTTP_400_BAD_REQUEST)
