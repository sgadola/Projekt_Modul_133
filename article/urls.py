from django.urls import path, include

from article import views


# URLs for the article section / app(?)
urlpatterns = [
    # Site for managing articles like create, delete edit, etc
    path('createArticle/', views.create_article, name='create_article'),
    path('deleteArticle/', views.delete_article, name='delete_article'),
    path('editArticle/', views.edit_article, name='edit_article'),
    path('viewArticle/', views.view_article, name='view_article'),
    path('searchArticle/', views.search_article, name='search_article')
]