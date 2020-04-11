from django.urls import path, include
from main_app.views import MovieList
from . import views

urlpatterns = [ 
    path('', views.info, name='info'),
    path('home/', views.home, name='home'),
    path('accounts/', include('django.contrib.auth.urls')),
    # path('home/<int:user.id>/', views.user, name='profile'),
    path('mylist/', MovieList.as_view(), name='movie_index'),

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