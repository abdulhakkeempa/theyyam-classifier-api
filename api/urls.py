from django.urls import path,include
from api.views import ImageUploadAPI

urlpatterns = [
    path('v1/theyyam',ImageUploadAPI.as_view()),
]