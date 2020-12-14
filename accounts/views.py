from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth import login


def signup_views(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # log user in
            login(request, user)
            return redirect("articles:list_article")
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render(request, 'accounts/signup.html', context)


def login_views(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            # login user
            user = form.get_user()
            login(request, user)
            return redirect("articles:list_article")
    else:
        form = AuthenticationForm()
    return render(request, 'accounts/login.html', {'form': form})
