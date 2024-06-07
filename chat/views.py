from django.contrib.auth import get_user_model
from rest_framework import generics
from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .models import Message, Thread
from .serializers import MessageSerializer, ThreadSerializer

User = get_user_model()


class ThreadCreateView(generics.CreateAPIView):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        instance = serializer.save()

        if instance.participants.count() > 2:
            raise ValidationError("A thread cannot have more than two participants.")

        participants = self.request.data.get('participants')
        if participants:
            participants = [int(p) for p in participants]
            existing_thread = Thread.objects.filter(participants__id__in=participants).distinct()
            if existing_thread.exists():
                return Response(ThreadSerializer(existing_thread.first()).data)
        serializer.save()


class ThreadDeleteView(generics.DestroyAPIView):
    queryset = Thread.objects.all()
    serializer_class = ThreadSerializer
    permission_classes = [IsAuthenticated]


class UserThreadsListView(generics.ListAPIView):
    serializer_class = ThreadSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Thread.objects.filter(participants=self.request.user)


class MessageCreateView(generics.CreateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]


class ThreadMessagesListView(generics.ListAPIView):
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        thread_id = self.kwargs.get('thread_id')
        return Message.objects.filter(thread_id=thread_id)


class MarkMessageAsReadView(generics.UpdateAPIView):
    queryset = Message.objects.all()
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def perform_update(self, serializer):
        serializer.instance.is_read = True
        serializer.save()


class UnreadMessagesCountView(generics.ListAPIView):
    serializer_class = MessageSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        return Message.objects.filter(thread__participants=self.request.user, is_read=False)
