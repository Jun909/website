from django.shortcuts import render, redirect
from .forms import UserInfoForm

def user_form(request):
    if request.method == "POST":
        form = UserInfoForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect("success")
    
    else:
        form = UserInfoForm()

    return render(request, "user_form.html", {"form": form})

def success(request):
    return render(request, 'success.html')



