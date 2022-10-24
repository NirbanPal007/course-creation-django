from django.contrib import admin
from django.urls import path,include
from courseformapp import views
from django.conf import settings
from django.conf.urls.static import static

app_name = "courseformapp"

urlpatterns = [
   
    path('',views.index,name="index"),
    path('course_creation_script',views.course_creation_script,name="course_creation_script"),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)