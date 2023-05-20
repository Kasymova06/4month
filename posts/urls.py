from django.urls import path
from posts import views

urlpatterns = [
    path("", views.get_index, name='view-get_index'),
    path("contacts/", views.get_contacts, name='view-get_contacts'),
    path("about/", views.get_about, name='view-get_about'),
    path("posts/<int:pk>", views.get_post, name='post-detail'),
    path("update_post/", views.update_post, name="post-update"),
    path("create_post/", views.create_post, name="post-create"),
]