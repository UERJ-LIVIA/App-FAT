from django.urls import path
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
    path('token/user-detail/',UserDetailAPIView.as_view(),name='user-detail')

]
