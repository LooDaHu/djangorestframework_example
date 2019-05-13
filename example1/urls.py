# Here I use django not django-rest-framework, you can use django-rest-framework to do this. learn more at api-guide
from django.urls import path

# import every classes from views.py
from . import views


urlpatterns = [

    path('model1/<int:model1_id>', views.Model1Endpoint.as_view()),
    path('model1', views.Model1Endpoint.as_view()),
    path('model1s', views.Model1sEndpoint.as_view()),

]
