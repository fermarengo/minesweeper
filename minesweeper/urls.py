"""minesweeper URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path
from django.views.generic import TemplateView

from api.views import create_board, detail_board, mark_cell_as_mined

urlpatterns = [
	path('', TemplateView.as_view(template_name='index.html'), name='index'),
	path('create_board/', create_board, name='create_board'),
    path('show_board/<int:board_id>', TemplateView.as_view(template_name='show_board.html'), 
        name='show_board'),
    path('detail_board/<int:pk>', detail_board, name='detail_board'),
    path('mark_cell_as_mined/', mark_cell_as_mined, name='mark_cell_as_mined'),
    path('admin/', admin.site.urls),
]
