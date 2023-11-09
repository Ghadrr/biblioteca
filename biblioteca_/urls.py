from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('product-detail/<int:id>/', views.livro_detail , name='product-detail')

]