from django.urls import path
from .views import LibraryApiView, LibraryCreateApiView, UserApiView

urlpatterns = [
    path('', LibraryCreateApiView.as_view()),
    path('detail/<pk>', LibraryApiView.as_view()),
    path('user-view/', UserApiView.as_view()),
]
