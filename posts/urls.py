from django.urls import path
from .views import AricleList, ArticleDetail, \
    CategoriesList, AuthorsList, \
    AuthorDetail, AuthorArticles


urlpatterns = [
    path("articles", AricleList.as_view({'get': 'list'})),
    path("article/<int:pk>", ArticleDetail.as_view()),

    # categories
    path("categories", CategoriesList.as_view()),

    # authors
    path("authors", AuthorsList.as_view()),
    path("author/<int:pk>", AuthorDetail.as_view()),
    path("author/<int:pk>/articles", AuthorArticles.as_view()),
]
