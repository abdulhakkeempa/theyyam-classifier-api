from api.serializers import ImageSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import os

class ImageUploadAPI(APIView):
    def post(self, request, format=None):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            image_file = request.FILES['theyyam_image']
            image_data = image_file.read()
            #do whatever with the image.
            return Response({"status":"Success"})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
