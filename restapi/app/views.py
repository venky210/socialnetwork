from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.decorators import api_view, permission_classes
from django.contrib.auth import authenticate
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework_simplejwt.tokens import RefreshToken
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import Group
from app.models import *  
from app.serializers import * 


@api_view(['POST'])
def register(request):
    if request.method == 'POST':
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response (serializer.data,status=status.HTTP_201_CREATED)
        return Response (serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
def login(request):
    if request.method == 'POST':
        username = request.data.get('username')
        password = request.data.get('password')
        user = None
        if '@' in username:
            try:
                user = CustomUser.objects.get(email=username)
            except ObjectDoesNotExist:
                pass


        if not user:
            user = authenticate(username=username, password=password)


        if user:
            refresh = RefreshToken.for_user(user)
            return Response({'refresh': str(refresh), 'access': str(refresh.access_token)}, status=status.HTTP_200_OK)


        return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_product(request):
    if request.user.role == CustomUser.Role.DEALER:
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(dealer=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({'"Token Type": "Given token not valid for any token type"'}, status=status.HTTP_403_FORBIDDEN)    
    
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def product_list(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    elif request.method == 'POST':
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_product(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.user == product.dealer:
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    else:
        return Response({"error": "You are not authorized to update this product"}, status=status.HTTP_403_FORBIDDEN)
    

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_product(request, pk):
    try:
        product = Product.objects.get(pk=pk)
    except Product.DoesNotExist:
        return Response({"error": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
    
    if request.user == product.dealer:
        product.delete()
        return Response({"message": "Product deleted successfully"}, status=status.HTTP_204_NO_CONTENT)
    else:
        return Response({"error": "You are not authorized to delete this product"}, status=status.HTTP_403_FORBIDDEN)
    
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_product_to_wishlist(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    if WishlistItem.objects.filter(user=request.user, product=product).exists():
        return Response({"error": "Product already exists in the wishlist."}, status=status.HTTP_400_BAD_REQUEST)
    wishlist_item = WishlistItem.objects.create(user=request.user, product=product)
    serializer = WishlistItemSerializer(wishlist_item)

    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def view_wishlist(request):
    wishlist_items = WishlistItem.objects.filter(user=request.user)
    serializer = WishlistItemSerializer(wishlist_items, many=True)
    
    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def remove_from_wishlist(request, wishlist_item_id):
    try:
        wishlist_item = WishlistItem.objects.get(pk=wishlist_item_id, user=request.user)
    except WishlistItem.DoesNotExist:
        return Response({"error": "Wishlist item not found."}, status=status.HTTP_404_NOT_FOUND)
    wishlist_item.delete()
    
    return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def add_product_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart_item = Cart.objects.create(user=request.user, product=product)
    serializer = CartSerializer(cart_item)

    return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def cart_list(request):
    cart_items = Cart.objects.filter(user=request.user)
    serializer = CartSerializer(cart_items, many=True) 
    return Response(serializer.data)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def remove_from_cart(request, cart_item_id):
    cart_item = get_object_or_404(Cart, pk=cart_item_id, user=request.user)
    cart_item.delete()
    return Response({"message": "Cart item removed successfully."}, status=status.HTTP_204_NO_CONTENT)
