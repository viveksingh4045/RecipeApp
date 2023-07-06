from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User, auth
from core.models import Profile, Recipe
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.db.models import Q
# Create your views here.

def signup(request):
    '''
    This view function is used to validate the data sent by user.
    And creates new user if validation is successful else it will reject the request.
    '''
    if request.method == "POST":
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        password2 = request.POST['password2']

        if password == password2:
            if User.objects.filter(email = email).exists():
                messages.info(request, 'Email already exists')
                return redirect('signup')
            
            elif User.objects.filter(username = username).exists():
                messages.info(request, 'Username already exists')
                return redirect('signup')
            else:
                user = User.objects.create_user(username = username, email=email, password=password)
                user.save()

                user_login  = auth.authenticate(username=username, password = password)
                auth.login(request, user_login)

                user_model = User.objects.get(username = username)
                new_profile = Profile.objects.create(user=user_model)
                new_profile.save()
                return redirect('settings')
        else:
            messages.info(request, "Password not matching")
            return redirect('signup')
    else:
        return render(request, 'index.html',{'mode':'sign-up-mode'})

def signin(request):
    """
    This view function will be used throughout to authenticate user
    based on basic auth using username & password
    """
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user  = auth.authenticate(username=username, password = password)

        if user is not None:
            #User is authenticated
            auth.login(request, user)
            #return redirect('/')
            return redirect('home')
        else:
            print('User Authentication failed')
            messages.info(request, 'Username and/or Password is invalid')
            return redirect('signin')
    else:
        #redirect user to login page
        print("Validation Failed")
        return render(request, 'index.html')


@login_required(login_url='signin')
def settings(request):
    '''
    If request method is get it will render setting page.
    If request method is post this function will update data in tables and render page
    '''
    user_object = User.objects.get(username = request.user.username)
    user_profile = Profile.objects.get(user = user_object)
    if request.method == 'POST':
        if request.FILES.get('profileimg') == None:
            print('Here')
            img = user_profile.profileimg
        else:
            img = request.FILES.get('profileimg')

        bio = request.POST['bio']
        location = request.POST['location']
        firstName = request.POST['firstName']
        lastName = request.POST['lastName']

        user_profile.profileimg = img
        user_profile.bio = bio
        user_profile.location = location
        user_profile.save()

        user_object.first_name =firstName
        user_object.last_name = lastName
        user_object.save()
        messages.info(request,'Profile has been updated click on Home to visit homepage')
        return redirect('settings')
    recipes = Recipe.objects.filter(user = user_object).order_by('created_at')
    return render(request,'profilepage.html', {'user_profile':user_profile,'user_object':user_object,
                                               'recipes':recipes,
                                               'post_len':len(recipes)})

@login_required(login_url='signin')
def logout(request):
    '''
    This view will be used to logout user throughout the app
    '''
    auth.logout(request)
    return redirect('signin')

@login_required(login_url='signin')
def recipe(request):
    user_object = User.objects.get(username = request.user.username)
    user_profile = Profile.objects.get(user = user_object)
    flag = -1
    if request.method == "POST":
        recipename = request.POST['recipename']
        recipedescription = request.POST['recipedescription']
        recipeimg =request.FILES.get('recipeimg')
        newRecipe = Recipe.objects.create(user=user_object, recipename=recipename,
                                        recipeimg = recipeimg,
                                        description = recipedescription)
        newRecipe.save()
        messages.info(request, 'Recipe Uploaded successfully')
    else:
        query = request.GET.get('query', '')
        if query != '':
            recipes = recipes = Recipe.objects.filter(Q(recipename__contains = query)
                                                      | Q(description__contains = query)
                                                      ).order_by('created_at')
            flag = 0
    if flag == -1:
        recipes = Recipe.objects.all().order_by('created_at')
    #print(len(recipes))
    return render(request, 'feed.html', {'user_profile':user_profile,
                                         'user_object':user_object,
                                         'recipes':recipes})