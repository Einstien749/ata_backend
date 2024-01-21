from django.shortcuts import render

# Create your views here.

from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Portfolio
from .serializers import *

@api_view(['GET'])
def portfolioview(request):

    items = Portfolio.objects.all()
    serializer = PortfolioSerializer(items, many=True)
    return Response(serializer.data)
    
