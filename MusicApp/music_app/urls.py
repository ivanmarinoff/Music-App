from django.urls import path, include

from MusicApp.music_app.views import index, add_album, album_details, delete_album, profile_details, \
    profile_delete, edit_album
urlpatterns = [
    path('', index, name='index'),
    path('album/', include([
        path('add/', add_album, name='album add'),
        path('details/<int:pk>/', album_details, name='album details'),
        path('edit/<int:pk>/', edit_album, name='album edit'),
        path('delete/<int:pk>/', delete_album, name='album delete'),
    ]),
         ),
    path('profile/', include([
        path('details/', profile_details, name='profile details'),
        path('delete/', profile_delete, name='profile delete'),
    ]))
]