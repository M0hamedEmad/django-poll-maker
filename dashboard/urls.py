from django.urls import path
from .views import ProfileView, PollListView

urlpatterns = [
    path('', PollListView.as_view(), name='polls'),
    path('profile/', ProfileView.as_view(), name='profile'),
]