"""
URL configuration for blog_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from blog.views import home, post_detail, like_post, search
from blog.views import category_posts
from blog.views import PostEditView, PostDeleteView
from blog.views import create_post


urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('', home, name="home"),
    path('post/<int:post_id>/', post_detail, name="post_detail"),
    path('post/<int:post_id>/like/', like_post, name="like_post"),
    path('search/', search, name="search"),
    path('accounts/', include("accounts.urls")),
    path('category/<int:category_id>/', category_posts, name="category_posts"),
    path("post/<int:pk>/edit/", PostEditView.as_view(), name="post_edit"),
    path("post/<int:pk>/delete/", PostDeleteView.as_view(), name="post_delete"),
    path("post/create/", create_post, name="create_post"),

]

