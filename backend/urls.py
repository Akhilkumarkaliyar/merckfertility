from django.urls import path,include
from . import views

urlpatterns = [
    #path('',views.index, name='login admin'),
    #path('accounts/', include('django.contrib.auth.urls')),
    path('dashboard',views.dashboard, name='admindashboard'),
    path('userlist',views.userlist, name='userlist'),
    path('updatelist',views.updatelist, name='updatelist'),
    path('addupdate',views.addupdate, name='addupdate'),
    path('adduser',views.adduser, name='adduser'),
    path('Saveupdate',views.saveupdate, name='saveupdate'),
    path('Saveuser',views.saveuser, name='saveuser'),
    path('login',views.login,name="login"),
    path('mylogin',views.mylogin,name="mylogin"),
    path('Deleteupdate/<int:id>', views.Deleteupdate, name="DeleteUpdate"),
    path('Deleteuser/<int:id>', views.Deleteupdate, name="DeleteUser"),
    path('UpdateEdit/<int:id>', views.Updateedit,name="UpadetEdit"),
    #path('hospitallist',views.hospitallist,name="hospitallist"),
    path('hospital',views.hospitallist, name='hospitallist'),
    path('hospitaledit/<int:id>', views.hospitaledit,name="hospitaledit"),
    path('addhospital',views.addhospital, name='addhospital'),
    path('Savehospital',views.Savehospital, name='Savehospital'),
    path('Deletehospital/<int:id>', views.Deletehospital, name="Deletehospital"),
    path('Specilization',views.Specilizationlist, name='Specilizationlist'),
    path('addspecilization',views.addspecilization, name='addspecilization'),
    path('Savespecilization',views.Savespecilization, name='Savespecilization'),
    path('Specilizationedit/<int:id>', views.Specilizationedit, name="Specilizationedit"),
    path('Deletespecilization/<int:id>', views.Deletespecilization, name="Deletespecilization"),
    
]