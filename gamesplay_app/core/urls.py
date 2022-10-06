from django.urls import path

from gamesplay_app.core.views import show_index, create_profile, show_dashboard, create_game, show_game, edit_game, \
    delete_game, show_profile, edit_profile, delete_profile

urlpatterns = [
    path('', show_index, name='show index'),
    path('profile/create/', create_profile, name='create profile'),
    path('dashboard/', show_dashboard, name='show dashboard'),
    path('game/create/', create_game, name='create game'),
    path('game/details/<int:pk>/', show_game, name='show game'),
    path('game/edit/<int:pk>/', edit_game, name='edit game'),
    path('game/delete/<int:pk>/', delete_game, name='delete game'),
    path('profile/details/', show_profile, name='show profile'),
    path('profile/edit/', edit_profile, name='edit profile'),
    path('profile/delete/', delete_profile, name='delete profile'),
]
