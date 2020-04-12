from django.urls import path, include
from . import views

urlpatterns = [ 
    path('', views.info, name='info'),
    path('home/', views.home, name='home'),
    path('add/', views.MovieCreate.as_view(), name='movie_create' ),
    path('mylist/', views.MovieList.as_view(), name='movie_index'),
    path('movie/<int:pk>/', views.MovieDetailView.as_view(), name='movie_detail'),
    path('movie/<int:pk>/update/', views.MovieUpdate.as_view(), name='movie_update'),
    path('movie/<int:pk>/delete/', views.MovieDelete.as_view(), name='movie_delete'),
    path('accounts/signup/', views.signup, name='signup'),
    path('user/<int:pk>/', views.UserDetailView.as_view(), name='user_detail'),
]




# Built in URLs for django.contrib.auth.urls
# accounts/login/ [name='login']
# accounts/logout/ [name='logout']
# accounts/password_change/ [name='password_change']
# accounts/password_change/done/ [name='password_change_done']
# accounts/password_reset/ [name='password_reset']
# accounts/password_reset/done/ [name='password_reset_done']
# accounts/reset/<uidb64>/<token>/ [name='password_reset_confirm']
# accounts/reset/done/ [name='password_reset_complete']