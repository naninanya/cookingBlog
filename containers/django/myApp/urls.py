from django.urls import path
from . import views

app_name = 'myApp'
urlpatterns = [
    path('', views.diarylistview, name="diary_list"),
    path('diary_detail/<int:pk>/', views.diarydetailview, name="diary_detail"),
    path('test', views.testRESTView.as_view(), name="test"),
]
