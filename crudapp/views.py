from django.shortcuts import render

# Create your views here.
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render
from . models import ProfileData
from django.http import HttpResponseRedirect
from django.urls import reverse


class Home(TemplateView):
    template_name = "crudapp/home1.html"


@login_required
@csrf_exempt
def profile_create(request):
    if request.method == "POST":
        ''' getting data from user form'''
        name = request.POST['name']
        past_address = request.POST['past_address']
        current_address = request.POST['present_address']
        phone_number = request.POST['phone_number']

        ''' storing data into database'''
        profileData = ProfileData.objects.create(
            name=name,
            past_address=past_address,
            present_address=current_address,
            phone_number=phone_number,
            created_user=request.user.username
        )
        profileData.save()
        return HttpResponseRedirect(reverse("profile_data"))
    else:
        return render(request, "crudapp/profile_create.html")


@login_required
@csrf_exempt
def profile_data(request):
    created_user = request.user.username
    '''filtering data based on user_login'''
    data = ProfileData.objects.filter(created_user=created_user)
    return render(request, "crudapp/profile_view.html", {"data":data})


@login_required
@csrf_exempt
def profile_update(request,pk):
    if request.method == "POST":
        name = request.POST['username']
        past_address = request.POST['past']
        current_address = request.POST['address']
        phone_number = request.POST['phone']
        "updating profile user data"
        ProfileData.objects.filter(pk=pk).update(name=name, past_address=past_address,
                                                 present_address=current_address, phone_number=phone_number)

        return HttpResponseRedirect(reverse("profile_data"))

    else:
        "filter the data based on user selected value"
        data = ProfileData.objects.get(pk=pk)
        return render(request, "crudapp/profile_update.html", {"data":data})


@csrf_exempt
def profile_delete(request, pk):
    "deleting user record"
    data = ProfileData.objects.get(pk=pk)
    data.delete()
    return HttpResponseRedirect(reverse("profile_data"))