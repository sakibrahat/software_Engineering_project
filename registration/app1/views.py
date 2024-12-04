from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from django.http import HttpResponse


@login_required(login_url='login')
def homepage(request):
    return render(request, 'home.html')


def signuppage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')

        if pass1 != pass2:
            return HttpResponse("Your password and confirm password are not Same!!")
        else:

            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('login')

    return render(request, 'signup.html')


def loginpage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        pass1 = request.POST.get('pass')
        user = authenticate(request, username=username, password=pass1)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password is incorrect!!!")

    return render(request, 'login.html')


def logoutpage(request):
    logout(request)
    return redirect('login')




def admin_add_pet(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        species = request.POST.get('species')
        breed= request.post.get('breed')
        age = request.POST.get('age')
        description = request.POST.get('description')
        price = request.POST.get('price')
        pet = PetAdd.objects.create(name=name, species=species, breed=breed, age=age, description=description, price=price)
        return redirect('admin_panel')
    return render(request, 'pets/admin_add_pet.html')

def admin_panel(request):
    pets = PetAdd.objects.all()
    return render(request, 'pets/admin_panel.html', {'pets': pets})

def admin_remove_pet(request, pet_id):
    pet = PetAdd.objects.get(id=pet_id)
    pet.delete()
    return redirect('admin_panel')

