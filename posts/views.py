from rest_framework.response import Response
from rest_framework import viewsets
from django.shortcuts import get_object_or_404
from django.contrib.auth.models import User
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics
from posts.serializers import *
from posts.models import *


# input parameters for the articles endpoint
CATEGORY = openapi.Parameter(
    'category',
    in_=openapi.IN_QUERY,                   
    type=openapi.TYPE_STRING
)
SEARCH = openapi.Parameter(
    'search',
    in_=openapi.IN_QUERY,
    type=openapi.TYPE_STRING
)


class AricleList(viewsets.ModelViewSet):
    serializer_class = ArticleListSerializer

    def get_queryset(self):
        filters = {
            "published": True, # list only published articles
        }

        category = self.request.GET.get('category')
        search = self.request.GET.get('search')

        # get articles by category
        if category:
            filters['category__title'] = category

        # search title contains
        if search:
            filters['title__icontains'] = search
       
        return Article.objects.filter(**filters)

    @swagger_auto_schema(
        manual_parameters=[CATEGORY, SEARCH],
    )
    def list(self, *args, **kwargs):
        """
        Override the list method so we can add the category and search
        parameters to the OpenAPI spec
        """

        queryset = self.filter_queryset(self.get_queryset())

        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        response_list = serializer.data

        return Response(response_list)

class ArticleDetail(generics.RetrieveAPIView):
    queryset = Article.objects.all()
    serializer_class = ArticleDetailSerializer

    def get(self, *args, **kwargs):
        """
        Override the get method so we only return published articles
        """

        article = get_object_or_404(self.queryset, pk=kwargs['pk'], published=True)

        serializer = self.serializer_class(article, many=False)
        return Response(serializer.data)

class AuthorsList(generics.ListAPIView):
    serializer_class = AuthorSerializer
    queryset = User.objects.all()

class AuthorDetail(generics.RetrieveAPIView):
    serializer_class = AuthorSerializer
    queryset = User.objects.all()

class AuthorArticles(generics.ListAPIView):
    serializer_class = ArticleListSerializer

    def get_queryset(self):
        return Article.objects.filter(author__id=self.kwargs['pk'])

class CategoriesList(generics.ListAPIView):
    serializer_class = CategorySerializer
    queryset = Category.objects.all()