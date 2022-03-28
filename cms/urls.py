from unicodedata import name
from django.urls import path
from django.conf.urls import include
from .views import  BlogDetailView
from cms import views
from django.contrib.auth import views as auth
app_name = 'cms'
urlpatterns = [
    path('',views.index,name='home'),
    path('<slug:foo>/search/', views.search, name='search'),
    path('search-notes/', views.search_notes, name='search-notes'),
    path('note/<id>', views.note_details),
    path('add-note/', views.add_note,name="add-note"),
    # path('login/', views.Login, name='login'),
    # path('logout/', auth.LogoutView.as_view(template_name ='home.html'), name ='logout'),
    path('register/', views.register, name='register'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('delete/<id>', views.delete),
    path('update_note/', views.update_note),
    path("create-resume/", views.create_resume, name="create-resume"),
    path("manual-resume/", views.manual_resume, name="manual-resume"),
    path("resume/", views.resume, name="resume"),
    path('profile/',views.profile,name='profile'),
    path('course/<slug:foo>', views.course_list, name='course_list'),
    path('<slug:foo>/<slug:slug>/', BlogDetailView.as_view(), name='cms_detail'),
   
    
   
   
    
    
]
