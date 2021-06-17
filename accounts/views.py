from django.shortcuts import render, redirect, HttpResponse
from django.core.mail import send_mail
from django.contrib import messages, auth
from django.contrib.auth.models import User
from django.db import transaction
from .forms import UserForm, ProfileForm
from .models import Profile


def view_profile(request):
    if request.user.is_authenticated:
        user = request.user
        current_user = {
            "id": user.id,
            "username": user.username,
            "user_permissions": user.user_permissions,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "last_login": user.last_login,
            "is_superuser": 'Superuser' if user.is_superuser else 'Regular user',
            "email": user.email,
            "photo": user.profile.photo.url if user.profile.photo else ''
        }
    else:
        return redirect('login')

    return render(request, 'accounts/profile.html', current_user)


def fixme(request):
    users = User.objects.all()
    for user in users:
        obj, created = Profile.objects.get_or_create(user=user)
        print(user.username, ' : ', created)
    return HttpResponse("It's done.")

def authors(request):
    return render(request, 'authors.html')

def handle_uploaded_file(f, filename):
    with open('photos/%Y/%m/%d/', 'wb+') as destination:
        for chunk in f.chunks():
            destination.write(chunk)


@transaction.atomic
def update_profile(request):
    if request.method == 'POST':
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=request.user.profile)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, 'Your profile was successfully updated!')
            return redirect('view_profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=request.user.profile)
    return render(request, 'accounts/edit_profile.html', {
        'user_form': user_form,
        'profile_form': profile_form
    })


def register(request):
    if request.method == 'POST':
        # Get form values
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        # Check if passwords match
        if password == password2:
            # Check username
            if User.objects.filter(username=username).exists():
                messages.error(request, 'That username is taken')
                return redirect('register')
            else:
                if User.objects.filter(email=email).exists():
                    messages.error(request, 'That email is being used')
                    return redirect('register')
                else:
                    # Looks good
                    user = User.objects.create_user(
                        username=username, password=password, email=email, first_name=first_name, last_name=last_name)
                    # Login after register
                    # auth.login(request, user)
                    # messages.success(request, 'You are now logged in')
                    # return redirect('index')
                    user.save()
                    messages.success(
                        request, 'You are now registered and can log in')

                    subject = 'Thank you for registering to our site.'
                    message = 'This is our confirmation letter about your successfull registration.'
                    email_from = 'django_blog@example.cmm'
                    recipient_list = ['reciever@example.com', ]
                    send_mail(subject, message, email_from, recipient_list)
                    
                    return redirect('login')
        else:
            messages.error(request, 'Passwords do not match')
            return redirect('register')
    else:
        return render(request, 'accounts/register.html')


def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            messages.success(request, 'You are now logged in')
            return redirect('blog')
        else:
            messages.error(request, 'Invalid credentials')
            return redirect('login')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        messages.success(request, 'You are now logged out')
        return redirect('blog')
