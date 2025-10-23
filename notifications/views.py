from django.shortcuts import render
from .models import Notification
from .serializers import NotificationSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django_q.tasks import async_task


# Create your views here.
@api_view(['POST'])
def notificationsView(request):
    serializer = NotificationSerializer(data=request.data)
    if serializer.is_valid():
        notification = serializer.save()
        async_task('notifications.tasks.send_notification', notification.id)
        return Response({"message": "Notification created successfully", "data": serializer.data}, status=201)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def notificationStatusView(request, id):
    try:
        get_notification = Notification.objects.get(id=id)
    except Notification.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = NotificationSerializer(get_notification)
        return Response(serializer.data, status=status.HTTP_200_OK)



