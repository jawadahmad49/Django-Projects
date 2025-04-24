from rest_framework.response import Response # type: ignore
from rest_framework.decorators import api_view # type: ignore
from base.models import Item
from .serializers import ItemSerializer
@api_view(['GET'])
def getData(request):
    items = Item.objects.all()
    serializer = ItemSerializer(items,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addItem(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)