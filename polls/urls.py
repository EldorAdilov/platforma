from django.conf.urls.static import static
from django.conf import settings
from django.urls import path

from .views import index, registration, login_view, home, super_users, students, upload_video, video_list, upload_book, view_pdf, uploads
urlpatterns = [
    path("polls/", index, name="index"),
    path('', registration, name="registration"),
    path('login/', login_view, name="login"),
    path('home/', home, name="home"),
    path('super_user/', super_users, name="super_user"),
    path('students/', students, name="students"),
    path('upload/', upload_video, name="upload"),
    path('video/', video_list, name="video"),
    path('book/', upload_book, name="book"),
    path('books/', view_pdf, name="books"),
    path('uploads/', uploads, name="uploads")
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
