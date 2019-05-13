# Use build-in serializer class form rest framework
from rest_framework import serializers

# Import our models
from . import models

''' 
    fields  = '__all__' means serializer will take all fields in the model to handle.
    For example,
    If we send a GET request, serializer will give the data of all fields in the model in JSON format.
    IF we send a POST/PUT/PATCH request. serializer will make sure everything is correct, including the correctness of 
    JSON data, existence of the value of foreign keys and so on. So, the incoming data won't break the integrity of the
    database.
    
    I recommend you use fields = '__all__', if you don't have some special requirement. There are two reasons:
    1) It is easy to use.
    2) It may reduce the risk of the data leak. 

'''


# Extend the built-in serializer
class Model1Serializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Model1


# equivalence expression
# class Model1Serializer(serializers.ModelSerializer):
#     class Meta:
#         fields = (
#                   'model1_id',
#                   'model1_int',
#                   'model1_datetime',
#                   'model1_text',
#                   'model2_id',
#                   )
#         models = models.Model1


class Model2Serializer(serializers.ModelSerializer):
    class Meta:
        fields = '__all__'
        model = models.Model2
