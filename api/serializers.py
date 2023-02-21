from rest_framework import serializers

class ImageSerializer(serializers.Serializer):
  theyyam_image = serializers.ImageField(required=True)