from django.urls import path
from .views import (
    ThreadCreateView, ThreadDeleteView, UserThreadsListView,
    MessageCreateView, ThreadMessagesListView, MarkMessageAsReadView,
    UnreadMessagesCountView
)

urlpatterns = [
    path('threads/', ThreadCreateView.as_view(), name='thread-create'),
    path('threads/<int:pk>/', ThreadDeleteView.as_view(), name='thread-delete'),
    path('threads/user/', UserThreadsListView.as_view(), name='user-threads'),
    path('messages/', MessageCreateView.as_view(), name='message-create'),
    path('messages/thread/<int:thread_id>/', ThreadMessagesListView.as_view(), name='thread-messages'),
    path('messages/<int:pk>/read/', MarkMessageAsReadView.as_view(), name='mark-message-as-read'),
    path('messages/unread/', UnreadMessagesCountView.as_view(), name='unread-messages-count'),
]
