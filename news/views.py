from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from django.db.models import Q
from .serializers import  NewsItemSerializer
from .models import NewsItem
from rest_framework.pagination import PageNumberPagination

class NewsIdView(GenericAPIView):
    serializer_class = NewsItemSerializer
    pagination_class = PageNumberPagination

    def get(self, request, format=None):
        queryset = self.get_queryset()
        page = self.paginate_queryset(queryset)
        serializer = self.get_serializer(page, many=True)
        return self.get_paginated_response(serializer.data)

    def get_queryset(self):
        queryset = NewsItem.objects.all()
        search_param = self.request.query_params.get('search')
        type_param = self.request.query_params.get('type')

        #search for item
        if search_param:
            queryset = queryset.filter(
                Q(by__icontains=search_param) |
                Q(title__icontains=search_param) |
                Q(item_type__icontains=search_param)
            )
        
        #filter by type
        if type_param:
            queryset = queryset.filter(item_type=type_param)

        return queryset
    

    def post(self, request, *args, **kwargs):
        serializer = NewsItemSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        instance = serializer.save(api_created=True)
        return_serializer = NewsItemSerializer(instance)
        return Response(return_serializer.data, status=status.HTTP_201_CREATED)

#TODO Adding the child comments as seen in the doc bonus  
class NewsDetailsView(GenericAPIView):
    queryset = NewsItem.objects.all()
    lookup_field = 'item_id'
    serializer_class = NewsItemSerializer

    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        # serializer = NewsItemSerializer(instance)
        serializer = NewsItemSerializer(instance, context={'request': request})
        return Response(serializer.data, status=status.HTTP_200_OK)

    def patch(self, request, *args, **kwargs):
        instance = self.get_object()

        # Check if the item was created in the API
        if instance.api_created:
            serializer = self.get_serializer(instance, data=request.data, partial=True)
            serializer.is_valid(raise_exception=True)
            instance = serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response({"error": "Updating items not created in the API is not allowed."}, status=status.HTTP_403_FORBIDDEN)

    def delete(self, request, *args, **kwargs):
        instance = self.get_object()

        # Check if the item was created in the API
        if instance.api_created:
            instance.delete()
            return Response({}, status=status.HTTP_204_NO_CONTENT)
        else:
            return Response({"error": "Deleting items not created in the API is not allowed."}, status=status.HTTP_403_FORBIDDEN)

