from django.urls import path
from .views import PollCreateView, HomeView, PollDeleteView, PollDetailView, ResultView, resultDate, VoteCreate

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('create/', PollCreateView.as_view(), name='create_poll'),
    path('delete/<int:pk>/', PollDeleteView.as_view(), name='delete_poll'),
    path('vote/<slug:slug>/', PollDetailView.as_view(), name='vote'),
    path('vote/', VoteCreate.as_view(), name='add-vote'),
    path('result/<slug:slug>/', ResultView.as_view(), name='result'),
    path('resultsdate/<int:pk>/', resultDate, name='result_date'),
]