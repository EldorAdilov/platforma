from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from polls.models import Video, Book
from users.models import MyUser


# Create your views here.


def index(request):
    return render(request, "home.html")


def registration(request):
    if request.method == 'POST':
        new_user = MyUser.objects.create(
            username=request.POST.get('usr'),
            phone_number=request.POST.get('phn')
        )
        new_user.set_password(request.POST.get('psw'))
        new_user.save()
        return redirect('login')
    return render(request, "registration.html")


def login_view(request):
    if request.method == 'POST':
        username = request.POST['usr']
        password = request.POST['psw']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            request.session['usr'] = user.username
            request.session.save()
            return redirect('home')
        else:
            return render(request, 'login.html', {'error_message': 'Natogri login yoki parol'})
    else:
        return render(request, 'login.html')


@login_required
def home(request):
    if request.user.is_superuser:
        return redirect('super_user')
    else:
        return render(request, 'home.html')


def students(request):
    users = MyUser.objects.filter(is_admin=0).values('id', 'username', 'phone_number')

    return render(request, 'students.html', {'users': users})


def upload(request):
    if request.method == 'POST' and request.FILES['video']:
        video_file = request.FILES['video']
        video_name = request.POST.get('video_name')
        Video.objects.create(video=video_file, name=video_name)
        return render(request, 'uploads.html')
    return render(request, 'upload.html')


def book(request):
    if request.method == 'POST' and request.FILES['book_pdf']:
        book_pdf = request.FILES['book_pdf']
        book_name = request.POST.get('book_name')
        Book.objects.create(book_file=book_pdf, book_name=book_name)
        return render(request, 'uploads.html')
    return render(request, 'book.html')


def view_pdf(request):
    books = Book.objects.all()
    return render(request, 'view_pdf.html', {'books': books})


def video(request):
    videos = Video.objects.all()
    return render(request, 'video.html', {'videos': videos})


def super_users(request):
    return render(request, 'super_user.html')


def logout_view(request):
    logout(request)
    return redirect('login')


def uploads(request):
    return render(request, 'uploads.html')

