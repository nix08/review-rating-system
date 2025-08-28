from django.urls import path
from .views import ReviewView,ReviewListView

urlpatterns = [
    path('review-create/',ReviewView.as_view(),name='review'),
    path('review-list/',ReviewListView.as_view(),name='listreviews')
]
