from django.urls import path

from .import views

urlpatterns = [
    # path('', views.home_view),
    path('posts/', views.get_post_list),
]
