from django.urls import path
from . import views
from .views import BlogDeleteView

urlpatterns = [
    path('post', views.post_list, name='home'),
    path('post/<int:pk>', views.post_detail, name='post_detail'),
    path('post_create', views.post_create, name='post_create'),
    # path('post_delete/<int:pk>', views.post_delete, name='post_delete'),
    path('post/<int:pk>/', BlogDeleteView.as_view(), name='post_detail'),
    path('post_update/<int:pk>', views.post_update, name='post_update'),

]

