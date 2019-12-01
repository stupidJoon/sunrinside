"""sunrinside URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
import bbs.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', bbs.views.index, name="index"),
    path('account/', include('accounts.urls')),
    path('<int:board_id>/', bbs.views.board, name='board'),
    path('addboard/', bbs.views.addBoard, name='add_board'),
    path('addarticle', bbs.views.addArticle, name='add_article'),
    path('<int:board_id>/<int:article_id>/', bbs.views.article, name='article'),
    path('addcomment', bbs.views.addComment, name='add_comment')
]
