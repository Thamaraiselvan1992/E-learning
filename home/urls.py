
from django.urls import path

from home import views
app_name = 'home'
urlpatterns = [
    path('',views.index,name='welcome'),  
    path('search-course',views.search_courses,name='search-course'), 
    path('course',views.courses,name='course'),  
    
       
]