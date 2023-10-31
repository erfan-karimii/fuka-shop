from django.urls import path
from . import views

app_name = 'product'


urlpatterns = [
    path('',views.show_categories,name='all-categories'),
    path('create/<str:cat>/',views.create_product,name='create-product'),
]
