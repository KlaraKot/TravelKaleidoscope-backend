from django.urls import path
from . import views
from myapp.views import *
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('GAPlaces', views.getAllPlaces),
    path('PlaceDetails', views.placeDetails),
    path('GAUsers', views.getAllUsers),
    path('UserDetails', views.userDetails),
    path('survey', views.surveyDetails),
    path('city', views.cityDetails),
    #path('rate', views.cityRate),
    #path('tenBest', views.tenBest),
    path('refreshToken', RefreshToken.as_view()),
    path('register', RegisterView.as_view()),
    path('login', LoginView.as_view()),
    path('user', UserView.as_view()),
    path('logout', LogoutView.as_view()),
    path('tenBest', TenBestView.as_view()),
    path('rate', RateCityView.as_view()),
    path('changePassword', ChangePasswordView.as_view()),
    path('fillSurvey', FillSurveyView.as_view())

]
