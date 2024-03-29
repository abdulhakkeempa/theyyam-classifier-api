from api.serializers import ImageSerializer
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
import os
import numpy as np
import cv2
from api.predict import predict

class ImageUploadAPI(APIView):
    def post(self, request, format=None):
        serializer = ImageSerializer(data=request.data)
        if serializer.is_valid():
            image_file = request.FILES['theyyam_image']
            image_specs = []
            output = None
            try:
                # Decode image data to OpenCV object
                img = cv2.imdecode(np.fromstring(image_file.read(), np.uint8), cv2.IMREAD_COLOR)
                image_specs = {
                    "width":img.shape[1],
                    "height":img.shape[0],
                    "channels":img.shape[2],
                }
                output = predict(img)
            except Exception as error:
                print(error)

            return Response({"status":"Success","image":image_specs,"classification":output})
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
