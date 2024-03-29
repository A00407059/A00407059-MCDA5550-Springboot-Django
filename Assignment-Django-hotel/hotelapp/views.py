from django.shortcuts import render
from django.http import HttpResponse
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import HotelSerializers
from .models import Hotel

# Create your views here.

def home(request):
    return HttpResponse("<h1> HELLO WORLD </h1>")

@api_view(['GET', 'POST'])
def Hotels_list(request):
    if request.method == 'GET':
        hotels_list = Hotel.objects.all()
        hotelSerializer = HotelSerializers(hotels_list, many=True)
        return Response(hotelSerializer.data)

    if request.method == 'POST':
        hotel_request = request.data
        serialize_request_data = HotelSerializers(data=hotel_request)
        if serialize_request_data.is_valid():
            serialize_request_data.save()

        return Response({"Message": "Added Successfully"})

"""Just getting single value"""
@api_view(['GET', 'POST'])
def Hotels_detail(request,pk):
    if request.method == 'GET':
        hotels_list = Hotel.objects.get(id=pk)
        hotelSerializer = HotelSerializers(hotels_list, many=False)
        return Response(hotelSerializer.data)
