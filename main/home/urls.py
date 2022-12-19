from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='home'),
    path('vocation', views.voc, name='voc'),
    path('about', views.about_us, name='about_us'),
    path('<int:id>/', views.detail_view, name='detail'),
    path('courses', views.courses, name='courses'),
    path('courses/<int:id>/', views.detail_course_view, name='courses_detail'),
]