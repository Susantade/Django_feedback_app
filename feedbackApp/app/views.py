from uuid import RESERVED_FUTURE
from django.shortcuts import redirect, render
from .models import *
from django.contrib.auth.models import auth
from django.contrib import messages
from django.contrib import auth

# Create your views here.

login =[]  # Keep track of loggedin users

lists=[]  # Stores all users for displaying comments in comment page

def index(request):
    return render(request, 'app/index.html')

def signin(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        lists.clear()
        if User.objects.filter(email = email).exists():
            user = User.objects.get(email = email)
            if user.password == password:
                request.session['id']=user.id
                request.session['email']=user.email
                comments=User.objects.values_list('comment')
                
                for i in comments:
                    if i[0]!='':
                        lists.append(User.objects.get(comment=i[0]))
                        
                login.append(user)
                
                return redirect('comment')
            else:
                #warning = "Password not matched"
                messages.info(request, "Password not matched")
                return redirect('signin')
        else:
            messages.warning(request,message='User does not exist. Sign Up')
            return redirect('signin')
    else:
        return render(request, "app/signin.html")


def signup(request):
    if request.method == 'POST':

        email = request.POST['email']
        password = request.POST['password']
        secret = request.POST['secret']
        user = User.objects.filter(email = email)
        if user:
            messages.warning(request, "Email already exist. Sign In")
            return redirect('signup')
        else:
            user = User.objects.create(email = email, password = password, secret = secret)
            messages.info(request, "Successfully registered")
            return redirect('signup')
    else:
        return render(request, "app/signup.html")


def forgot_password(request):
    if request.method == "POST":
        email = request.POST['email']
        secret = request.POST['secret']
       
        if User.objects.filter(email = email).exists():
            user = User.objects.get(email = email)
            if user.secret == secret:
                password = user.password
                return render(request, 'app/forgotpassword.html', {'password':password})
            else:
                messages.info(request, "Secret code not matched")
                return redirect('forgotpassword')
        else:
            messages.warning(request, "User not found")
            return redirect('forgotpassword')
    else:
        return render(request, "app/forgotpassword.html")
    

def comment_page(request):
    user = User.objects.all()
    return render(request, "app/comment.html", {'lists':lists})

def comment_save(request, pk):
    if request.method == 'POST':
        comment = request.POST['comment']
        user = User.objects.get(id=pk)
        if user:
            user.comment = comment
            user.save()
            comments=User.objects.values_list('comment')
            lists=[]
            for i in comments:
                if i[0]!='':
                    lists.append(User.objects.get(comment=i[0]))
            messages.info(request,"Comment has been saved")
            return render(request, 'app/comment.html', {'lists':lists})


# Page not found error
def error_404(request, exceptions):
    return render(request, "app/404.html")

# Internal server error
def error_500(request):
    return render(request, 'app/500.html')


def comment_filter(request):
    return render(request, "app/comment.html",{'lists':login})


def logout(request):
    email = request.session['email']
    idd = User.objects.get(email=email).id
    del request.session['email']

    for i in range(len(login)):
        if idd == login[i].id:
            login.pop(i)
    auth.logout(request)
    return redirect('index')

    
