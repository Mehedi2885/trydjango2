from django.urls import path
from .views import my_fbv, CourseView

app_name = 'courses'
urlpatterns = [
    path('', CourseView.as_view(template_name='contact.html'), name='course-list'),
    path('<int:id>/', CourseView.as_view(), name='course-detail')
    #path('', my_fbv, name='course-list'),


]
