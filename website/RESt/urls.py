from django.urls import path,include
from .import views
from rest_framework.urlpatterns import format_suffix_patterns
urlpatterns = [

    path('',views.Person.as_view()),
    path('product/',views.Product_list),
    path('product/<int:pk>/',views.Product_detail)
]
