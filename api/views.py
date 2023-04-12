from api.serializers import ImageSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import os
import numpy as np
import cv2

class ImageUploadAPI(APIView):
    def post(self, request, format=None):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            image_file = request.FILES['theyyam_image']
            try:
                # Decode image data to OpenCV object
                img = cv2.imdecode(np.fromstring(image_file.read(), np.uint8), cv2.IMREAD_COLOR)
                print(img.shape)
                image_specs = {
                    "width":img.shape[1],
                    "height":img.shape[0],
                    "channels":img.shape[2],
                }
            except Exception as error:
                print(error)

            return Response({"status":"Success","image":image_specs})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
