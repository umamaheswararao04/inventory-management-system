from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status

from .models import Product, StockHistory
from .serializers import ProductSerializer, StockHistorySerializer


# ----------- PRODUCTS API -----------
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_products(request):
    products = Product.objects.all()
    serializer = ProductSerializer(products, many=True)
    return Response(serializer.data)


# ----------- STOCK IN API -----------
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def api_stock_in(request):
    product_id = request.data.get('product_id')
    quantity = int(request.data.get('quantity', 0))

    product = Product.objects.get(id=product_id)
    prev_qty = product.quantity
    product.quantity += quantity
    product.save()

    StockHistory.objects.create(
        product=product,
        change_type='IN',
        quantity_changed=quantity,
        previous_quantity=prev_qty,
        new_quantity=product.quantity,
        updated_by=request.user
    )

    return Response(
        {'message': 'Stock added successfully'},
        status=status.HTTP_200_OK
    )


# ----------- STOCK OUT API -----------
@api_view(['POST'])
@permission_classes([IsAuthenticated])
def api_stock_out(request):
    product_id = request.data.get('product_id')
    quantity = int(request.data.get('quantity', 0))

    product = Product.objects.get(id=product_id)

    if quantity > product.quantity:
        return Response(
            {'error': 'Not enough stock'},
            status=status.HTTP_400_BAD_REQUEST
        )

    prev_qty = product.quantity
    product.quantity -= quantity
    product.save()

    StockHistory.objects.create(
        product=product,
        change_type='OUT',
        quantity_changed=quantity,
        previous_quantity=prev_qty,
        new_quantity=product.quantity,
        updated_by=request.user
    )

    return Response(
        {'message': 'Stock reduced successfully'},
        status=status.HTTP_200_OK
    )


# ----------- STOCK HISTORY API -----------
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def api_stock_history(request):
    history = StockHistory.objects.all().order_by('-timestamp')
    serializer = StockHistorySerializer(history, many=True)
    return Response(serializer.data)
