# Here are general import
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

# import all models in the application
from .models import *

# import all serializers of models
from .serializers import *

# Create your views here.
'''
In APIView class, there are get(), post(), put(), patch() and delete().
The APIView class can figure out the METHOD of incoming request and choose 
the corresponding function to handle the request. 
'''


class Model1Endpoint(APIView):

    # override get method
    def get(self, request, model1_id):
        try:
            # try to get the queried model1 in the database
            query = Model1.objects.get(model1_id=model1_id)
            # use serializer to transform the queried model1 from a model1 object to JSON data
            serializer = Model1Serializer(query)
            # Return the JSON data
            return Response(serializer.data)
        # If it is not found
        except Model1.DoesNotExist:
            # return the error message
            return Response({"error": "Model1 does not exist"}, status=status.HTTP_404_NOT_FOUND)

    # override post method
    def post(self, request):
        # transform the incoming JSON data into a model1 object.
        serializer = Model1Serializer(data=request.data)
        # test transformed data is valid or not.
        if serializer.is_valid():
            # if it is valid, just save it.
            new_model1 = serializer.save()
            # and return the success message.
            return Response({"model1_id": new_model1.model1_id}, status=status.HTTP_200_OK)
        # if it is not be saved successfully, return error message.
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    # override put method
    def put(self, request, model1_id):
        # try to find the object to be updated
        try:
            update_model1 = Model1.objects.get(model1_id=model1_id)
        except update_model1.DoesNotExist:
            return Response({"error": "Model1 does not exist"}, status=status.HTTP_404_NOT_FOUND)

        # transform the incoming JSON data into a model1 object.
        # And partial=False means all required fields should show up in the data
        # or it can not pass serializer validation check.
        serializer = Model1Serializer(update_model1, data=request.data, partial=False)
        # make sure the data is correct.
        if serializer.is_valid():
            # save it, if it is correct.
            update_model1 = serializer.save()
            # return success message.
            return Response({"model1_id": update_model1.model1_id}, status=status.HTTP_200_OK)
        # return error message,  serializer.errors can give more details about why the operation is fail.
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    # override put method, almost the same with put method.
    def patch(self, request, model1_id):
        try:
            update_model1 = Model1.objects.get(model1_id=model1_id)
        except update_model1.DoesNotExist:
            return Response({"error": "Model1 does not exist"}, status=status.HTTP_404_NOT_FOUND)

        # partial=True means any missing of required fields is acceptable.
        serializer = Model1Serializer(update_model1, data=request.data, partial=True)
        if serializer.is_valid():
            update_model1 = serializer.save()
            return Response({"model1_id": update_model1.model1_id}, status=status.HTTP_200_OK)
        return Response({"error": serializer.errors}, status=status.HTTP_400_BAD_REQUEST)

    # override delete method.
    def delete(self, request, model1_id):
        # try to find the object first, then delete it, or return NOT_FOUND.
        try:
            delete_model1 = Model1.objects.get(model1_id=model1_id)
            delete_model1.delete()
            return Response({}, status=status.HTTP_200_OK)
        except Model1.DoesNotExist:
            return Response({"error": "Model1 does not exist"}, status=status.HTTP_404_NOT_FOUND)


# This class is for getting all objects in the database.
class Model1sEndpoint(APIView):
    def get(self, request):
        try:
            # Model1.objects.all() here. Not .get() to get all objects.
            queryset = Model1.objects.all()
            # many=True, due to one more object to handle
            serializer = Model1Serializer(queryset, many=True)
            # return the query in JSON
            return Response(serializer.data)
        except Model1.DoesNotExist:
            # return error message if there is no object here.
            return Model1({"error": "Model1 does not exist"}, status=status.HTTP_404_NOT_FOUND)