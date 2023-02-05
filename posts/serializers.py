from rest_framework import serializers
from posts.models import User, Category, Article

class ArticleListSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    author = serializers.SerializerMethodField()

    def get_category(self, post):
        print(post)
        data = post.category.title
        return data

    def get_author(self, post):
        data = {
            'name': post.author.first_name,
            'surname': post.author.last_name,
            'job_description': post.author.job_description
        }
        
        return data

    class Meta:
        model = Article
        fields = ("id", "title", "published", "date_published", "summary", "category", "author")

class ArticleDetailSerializer(serializers.ModelSerializer):
    category = serializers.SerializerMethodField()
    author = serializers.SerializerMethodField()

    def get_category(self, post):
        data = post.category.title
        return data

    def get_author(self, post):
        data = {
            'name': post.author.first_name,
            'surname': post.author.last_name,
            'job_description': post.author.job_description
        }

        return data
       
    class Meta:
        model = Article
        fields = "__all__"

class AuthorSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ("id", "first_name", "last_name", "job_description")

class CategorySerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        exclude = ("created",)