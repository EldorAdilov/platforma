from django.conf.urls.static import static
from django.conf import settings
from django.urls import path

from polls.views import (index, registration, login_view, home, super_users, students, upload, video, book, view_pdf,
                         uploads, add_question, quiz, result, superuser_results)

urlpatterns = [
    path("polls/", index, name="index"),
    path('', registration, name="registration"),
    path('login/', login_view, name="login"),
    path('home/', home, name="home"),
    path('super_user/', super_users, name="super_user"),
    path('students/', students, name="students"),
    path('upload/', upload, name="upload"),
    path('video/', video, name="video"),
    path('book/', book, name="book"),
    path('view_pdf/', view_pdf, name="view_pdf"),
    path('uploads/', uploads, name="uploads"),
    path('add_question/', add_question, name="add_question"),
    path('quiz/', quiz, name="quiz"),
    path('result/', result, name='result'),
    path('superuser_results/', superuser_results, name='superuser_results'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
