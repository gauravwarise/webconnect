from django.urls import re_path

from .import consumers


websocket_urlpatterns = [
    re_path(r'ws/demo/$', consumers.MyConsumer.as_asgi()),
    # Add more URL patterns for different consumers as needed
]