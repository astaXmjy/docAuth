from django.shortcuts import render
from .form import AadharForm
from .models import Aadhar
from django.contrib import messages


# Create your views here.


def extract(request):
    if request.method == "POST":
        form = AadharForm(request.POST)

        if form.is_valid():
            form.save()
            # print(messages.success(request, ("Maa chuda bsdk!")))
            return messages.success(request, ("congrats"))
        else:
            messages.error(request, ("Try again"))

    else:
        form = AadharForm()

    return render(request, "form.html", {"form": form})
