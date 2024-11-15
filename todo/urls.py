from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('signup/',views.userSignup,name="signup"),
    path('login/',views.userLogin,name="login"),
    path('logout/',views.userLogout,name="logout"),
    path('list/',views.TodoListView.as_view(),name='list'),
    path('add/',views.TodoCreateView.as_view(),name='add-list'),
    path('detail/<int:pk>',views.TodoDetailView.as_view(),name='detail'),
]
