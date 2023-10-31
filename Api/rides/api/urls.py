from django.urls import path, include
from .views import (RidesAPIView,
                    RideDetailAPIView,
                    ProfileDetailAPIView,
                    ProfilesAPIView,
                    UserDetailAPIView,
                    )
                 
# create your routes here !

urlpatterns = [
    path('rides/', RidesAPIView.as_view(), name='rides'),
    path('rides/<int:pk>/', RideDetailAPIView.as_view(), name='ride'),
    path('profiles/', ProfilesAPIView.as_view(), name='profiles'),
    path('profiles/<int:pk>', ProfileDetailAPIView.as_view(), name='profile'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.jwt')),
    path('auth/', include('djoser.urls.authtoken')),
]
