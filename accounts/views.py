from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm

# Create your views here.
def signup_views(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            # log user in
            return redirect("articles:list_article")
    else:
        form = UserCreationForm()
    context = {'form': form}
    return render (request, 'accounts/signup.html', context)