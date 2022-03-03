from django.shortcuts import render
from django.shortcuts import render,redirect
from django.http.response import HttpResponse
#for database importing user
from django.contrib.auth.models import User
#for sendin user meassages
from django.contrib import messages
#importing authentication inbuilt function
from django.contrib.auth import authenticate,login,logout
from TYTY import settings
from django.core.mail import send_mail
from .models import Contact, Download ,Playgame


# Create your views here.

def home(request):
    return render(request ,'index.html')

def contact(request):
    if request.method=='POST':
        name=request.POST['name']
        phone=request.POST['phone']
        email=request.POST['email']
        query=request.POST['query']
        con_obj = Contact(name=name, phone=phone, email=email, query=query)
        con_obj.save()
        return redirect('contact')

    return render(request,'contact.html')

    
def signup(request):
    if(request.method == 'POST'):
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        pass1 = request.POST['pass1']
        pass2 = request.POST['pass2']

        if (User.objects.filter(username=username)):
            messages.error(request, 'This Username is already taken!')
            return redirect('signup')
        
        if (User.objects.filter(email=email)):
            messages.error(request, 'E-mail is already registered!')
            return redirect('signup')
        
        if (len(username)>15):
            messages.error(request, 'Username must be under 15 characters!')
            return redirect('signup')
        
        if (pass1!=pass2):
            messages.error(request, 'Passwords did not match!')
            return redirect('signup')

        if(not username.isalnum()):
            messages.error(request, 'Username must be alpha-numeric')
            return redirect('signup')

        #Creating new user in database
        myuser = User.objects.create_user(username, email, pass1)
        myuser.first_name = fname
        myuser.last_name = lname
        
        #Saving user in database
        myuser.save()        
        messages.success(request, 'Your accout has been successfully created. We have sent you confirmation email, please confirm your email')

        #Welcome e-mail
        subject = 'Welcome to TechGames.com'
        msg = 'Hello '+myuser.first_name+'!\nWelcome to TechGames.com you can enjoy variety of games here.\nThank you for visiting.\n Happy Gaming !'
        from_email = settings.EMAIL_HOST_USER
        to_list = [myuser.email]
        send_mail(subject, msg, from_email, to_list, fail_silently=True)
        return redirect('signin')
    else:
        return render(request, 'signup.html')


def signin(request):

    if(request.method == 'POST'):
        username = request.POST['username']
        pass1 = request.POST['pass1']

        user = authenticate(username=username, password=pass1)

        if(user is not None):
            login(request, user)
            fname = {'name': user.first_name}
            return render(request, 'index.html',fname)
        else:
            messages.error(request, 'Wrong credentials !')
            return redirect('signin')
    return render(request, 'signin.html')


def signout(request):
    logout(request)
    messages.success(request, 'Logged out successfully!')
    return redirect('home')

def searchDownloads(request):
    query = request.GET['search']
    allGames = Download.objects.filter(name__icontains=query)
    result = {'file' : allGames}
    return render(request,'searchDownloads.html',result)

def searchGames(request):
    query = request.GET['search']
    allGames = Playgame.objects.filter(name__icontains=query)
    result = {'file' : allGames}
    return render(request,'search.html',result)

def playgame(request):
    games = {'file' :Playgame.objects.all()}
    return render(request,'playgames.html',games)

def car(request):
    return render(request,'car.html')

def aboutUs(request):
     return render(request,'aboutUs.html')

def flappybird(request):
    return render(request,'Flappy_Bird.html')

def download(request):
    games = {'file' :Download.objects.all()}
    return render(request,'download.html',games)

def TicTacToe(request):
    return render(request,'TicTacToe.html')

def TicTacToe(request):
    return render(request,'TicTacToe.html')

def CPU(request):
    return render(request,'CPU.html')

def snake(request):
    return render(request,'snake.html')

def wordscramble(request):
    return render(request,'WorldScramble.html')

def dino(request):
    return render(request,'dino.html')




