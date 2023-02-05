from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.forms import ModelForm
from django.utils import timezone
from posts.models import Category, User, Article

class UserAdmin(UserAdmin):
    list_display = (
        'username', 'email', 'first_name', 'last_name', 'is_staff',
        'job_description'
    )

    fieldsets = (
        (None, {
            'fields': ('username', 'password')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email', 'job_description')
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        })
    )

    add_fieldsets = (
        (None, {
            'fields': ('username', 'password1', 'password2')
        }),
        ('Personal info', {
            'fields': ('first_name', 'last_name', 'email', 'job_description')
        }),
        ('Permissions', {
            'fields': ('is_active', 'is_staff', 'is_superuser', 'groups', 'user_permissions')
        }),
        ('Important dates', {
            'fields': ('last_login', 'date_joined')
        })
    )

class AuthorForm(ModelForm):
    """
    Exclude the author field from the article form so we
    can use the logged on user instead
    """

    class Meta:
        model = Article
        exclude = ('author', 'date_published')
        

    def save(self, commit=True):
        """
        set the date published and get the author from the
        currently logged in user
        """

        instance = super().save(commit=False)
        instance.updated = timezone.now()

        # do not override the author if exists
        if not hasattr(instance, "author"):
            instance.author = self.request.user

        # set the date published to now when article is published
        if 'published' in self.changed_data:
            if instance.published:
                instance.date_published = timezone.now()

        if commit:
            instance.save()
            self.save_m2m()

        return instance

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    form = AuthorForm
    list_display = ('title', 'author', 'category', 'published', 'created', 'updated')

    def get_form(self, request, *args, **kwargs):
        """
        Pass the request object on to the save method so
        we can get the logged on user
        """

        form = super(ArticleAdmin, self).get_form(request, *args, **kwargs)
        form.request = request
        return form

admin.site.register(Category)
admin.site.register(User, UserAdmin)
