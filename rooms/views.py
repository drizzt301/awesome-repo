
#from rest_framework.generics import RetrieveAPIView
from rest_framework.views import APIView
#from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Room
from .serializers import ReadRoomSerializer, WriteRoomSerializer, BigRoomSerializer


# class ListRoomsview(ListAPIView):
#     queryset = Room.objects.all()
#     serializer_class = RoomSerializer


class RoomsView(APIView):
    def get(self, request):
        rooms = Room.objects.all()[:5]
        serializer = ReadRoomSerializer(rooms, many=True).data
        return Response(serializer)
    def post(self, request):
        if not request.user.is_authenticated:
            return Response(status=status.HTTP_401_UNAUTHORIZED)
        serializer = WriteRoomSerializer(data=request.data)
        if serializer.is_valid():
            room = serializer.save(user=request.user) 
            room_serializer = ReadRoomSerializer(room).data             
            return Response(data = room_serializer, status=status.HTTP_200_OK)
        else:
            return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class RoomView(APIView):
    def get(self, request, pk):
        #print(pk)
        try:
            room = Room.objects.get(pk=pk)
            serializer = ReadRoomSerializer(room)
            return Response(serializer)
        except Room.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

    def put(self, request):
        pass
    def delete(self, request):
        pass
    
# class SeeRoomView(RetrieveAPIView):
#     queryset = Room.objects.all()
#     serializer_class = BigRoomSerializer
#     lookup_url_kwarg = "pk"







#APIView
    #from rest_framework.views import APIView
    # class ListRoomsview(APIView):
    #     def get(self, request):
    #         rooms = Room.objects.all()
    #         serializer = RoomSerializer(rooms, many=True)
    #         return Response(serializer.data)

# 함수형 뷰
    #from rest_framework.decorators import api_view
    # @api_view(["GET", "DELETE"])
    # def list_rooms(request):
    #     rooms = Room.objects.all()
    #     serialized_rooms = RoomSerializer(rooms, many=True)
    #     return Response(data=serialized_rooms.data)

# @api_view(["GET", "POST"])
    # def rooms_view(request):
    #     if request.method == "GET":
    #         rooms = Room.objects.all()[:5]
    #         serializer = ReadRoomSerializer(rooms, many=True).data
    #         return Response(serializer)
    #     elif request.method == "POST":
    #         if not request.user.is_authenticated:
    #             return Response(status=status.HTTP_401_UNAUTHORIZED)
    #         serializer = WriteRoomSerializer(data=request.data)
    #         #print(dir(serializer))
    #         if serializer.is_valid():
    #             room = serializer.save(user=request.user) 
    #             #save 가 create or update 를 감지한다. - you never direct call create, update
    #             room_serializer = ReadRoomSerializer(room).data             
    #             return Response(data = room_serializer, status=status.HTTP_200_OK)
    #         else:
    #             #print(serializer.errors)
    #             return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)
