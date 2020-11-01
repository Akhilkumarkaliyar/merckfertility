#from api.views import RegisterAPI,LoginAPI

from django.urls import path
from knox import views as knox_views

from.views import*

urlpatterns = [
    path('registered_nurse/', RegisterAPI.as_view({'post':'create'})),
    path('register_get/', List.as_view({'get':'list'})),
    path('login/', LoginView.as_view({'post':'create'})),
    path('country/', country.as_view({'get':'country'})),
    path('hospital/', hospital.as_view({'get':'hospital'})),
    path('specilization/', specilization.as_view({'get':'specilization'})),
    path('state/', state.as_view({'post':'state'})),
    path('city/', city.as_view({'post':'city'})),

    #path('login/', LoginAPI.as_view(), name='login'),
    #path('logout/', knox_views.LogoutView.as_view(), name='logout'),
    #path('logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
]
