from django.urls import path, include
from . import views

urlpatterns = [ 
    path('', views.info, name='info'),
    path('home/', views.home, name='home'),
    path('add/', views.WatchableCreate.as_view(), name='watchable_create'),
    path('watchable/<int:movie_id>/fork', views.WatchableFork.as_view(), name='watchable_fork' ),
    path('mylist/', views.WatchableList.as_view(), name='watchable_index'),
    path('watchable/<int:pk>/', views.WatchableDetail.as_view(), name='watchable_detail'),
    path('watchable/<int:pk>/update/', views.WatchableUpdate.as_view(), name='watchable_update'),
    path('watchable/<int:pk>/delete/', views.WatchableDelete.as_view(), name='watchable_delete'),
    path('accounts/signup/', views.signup, name='signup'),
    path('profile/', views.profile_login, name='profile_login'),
    path('profile/<int:pk>/', views.ProfileDetail.as_view(), name='profile_detail'),
    path('profile/<int:pk>/update/', views.ProfileUpdate.as_view(), name='profile_update'),
    path('profile/<int:profile_id>/follow/', views.follow, name='follow'),
    path('profile/<int:pk>/following/', views.FollowingList.as_view(), name='following'),
    path('settings/', views.settings, name='settings'),
    path('settings/profilephoto/add', views.profile_photo_add, name='profile_photo_add'),
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