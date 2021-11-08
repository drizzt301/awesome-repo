from rest_framework.routers import DefaultRouter
from django.urls import path
from . import views

app_name = "rooms"

urlpatterns =  [
    path("", views.RoomsView.as_view()),
    path("<int:pk>/", views.RoomView.as_view()),
]



# 클래스형
    # from . import views
    # path("list/", views.ListRoomsview.as_view()),
    # path("<int:pk>/", views.SeeRoomView.as_view()),

# 함수형
    # path("list/", views.list_rooms),  
