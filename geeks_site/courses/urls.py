from django.urls import path
from .views import AboutUs
from .views import CoursesList, CoursesCreate

urlpatterns = [
    # path("first_view/", first_view, name="first_view"),
    path("AboutUs/", AboutUs.as_view(), name="AboutUs"),
    path("courses-list/", CoursesList.as_view(), name="courses-list"),
    path("courses-create/", CoursesCreate.as_view() ),

]
