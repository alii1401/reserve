from django.shortcuts import render 
import json
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from requests import delete

from .models import *
from .serializers import *
from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import date
from datetime import datetime

# Create your views here.

def index(request):
    today = date.today()
    information = Doctors.objects.all()
    return render(request, "reserve/index.html",{ 
        'today':today,
        'information':information
    })

@csrf_exempt 
def reserve(request):

    if request.method == 'POST':
        data = json.loads(request.body)
        doctor_id = data.get("doctorId")
        date0 = data.get("dateNobat")
        print(date0)

        try:
            doctor = Doctors.objects.get(id = doctor_id, date=date0)
            print(doctor)

            if int(doctor.mandeh) == 0:
                doctor.is_end = True
                doctor.save(update_fields=['is_end'])

                return JsonResponse({
                "error": "capasity is full!"},
                status=404)

            else:
                flag = 0
                user_inf = UserInf.objects.get(username = request.user)
   
                user_check = Reserve.objects.get(username = user_inf)
                if user_check.inf_turn:
                    for dr in user_check.inf_turn:
                        if dr == doctor and dr.date == date0:
                            flag = 1

                            return JsonResponse({
                                "error":"You have already booked this doctor's appointment!"
                            },status=404) 

                if user_check and flag == 0 :
                    user_check.inf_turn.add(doctor)
                    flag = 1

                    doctor.mandeh -= 1 
                    doctor.nobat += 1
                    doctor.save(update_fields=['mandeh','nobat'])

                elif flag != 1 :
                    res = Reserve() 
                    res.username = user_inf
                    res.save()

                    res.inf_turn.add(doctor)

                    doctor.mandeh -= 1 
                    doctor.nobat += 1
                    doctor.save(update_fields=['mandeh','nobat'])


                return HttpResponse(status = 204)

        except Doctors.DoesNotExist:
            return JsonResponse({
                "error": "dar in tarikh, doctor morednazar yaft nshod!"},
                status=404)
            

@api_view(['GET'])
def my_appointment(request):
    if request.method == 'GET':
        user_inf = UserInf.objects.get(username = request.user)
        reserves = Reserve.objects.get(username = user_inf)
        serializer = ReserveSerializer(reserves, many=False)

        return Response(serializer.data)


@csrf_exempt 
def schedule(request):
    
    if request.method == 'POST':
        data = json.loads(request.body)
        date0 = data.get("date")
        print(date0)

        doctors0 = Doctors.objects.all()
        for dr0 in doctors0:
            dr0.is_active = False
            dr0.save(update_fields=['is_active'])

        doctors = Doctors.objects.filter(date = date0)

        for dr in doctors:
            dr.is_active = True
            dr.save(update_fields=['is_active'])

        return HttpResponse(status = 204)


@api_view(['GET'])
def get_schedule(request):
    if request.method == 'GET':
        doctors = Doctors.objects.filter(is_active = True)
        
        return JsonResponse([doctor.serialize() for doctor in doctors], safe=False)


@csrf_exempt
def initialstate(request):
    if request.method == 'POST':
        doctors0 = Doctors.objects.all()

        for dr0 in doctors0:
            dr0.is_active = False
            dr0.save(update_fields=['is_active'])
            print("ok")
        
        return HttpResponse(status=204)



        
 




@csrf_exempt
def login_view(request):
    if request.method == "POST":

        # Attempt to sign user in
        username = request.POST["username"]
        # print(username)
        password = request.POST["password"]
        u = User.objects.get(username = username, password=password)
        print(u)
   
        # user = authenticate(request, username=username, password=password)
        # print(user)

        # Check if authentication successful
        if u is not None:
            login(request, u)
            return HttpResponseRedirect(reverse("reserve:index"))
        else:
            return render(request, "reserve/login.html", {
                "message": "Invalid username and/or password."
            })
    else:
        return render(request, "reserve/login.html")


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("reserve:index"))


def register(request):
    if request.method == "POST":

        user0 = request.POST["username"]
        first = request.POST["first-name"]
        last  = request.POST["last-name"]
        
        email0 = request.POST["email"]
        nationalCode = request.POST["national-code"]
        fatherName = request.POST["father-name"]
        phoneNumber = request.POST["phone-number"]

        if request.POST["address"] != '':
            adres = request.POST["address"]


        # Ensure password matches confirmation
        password0 = request.POST["password"]
        confirmation = request.POST["confirmation"]
        if password0 != confirmation:
            return render(request, "reserve/register.html", {
                "message": "Passwords must match."
            })

        # Attempt to create new user
        try:
            # user = User.objects.create_user(user0, email0, password0,first,last)
            user = User(
                username = user0,
                email = email0,
                password = password0,
                first_name = first,
                last_name = last
            )
            user.save()

            user = User.objects.get(username = user0)

            if request.POST["address"] != '':
                print('amadim')
                user_inf = UserInf(
                    username = user,
                    father_name = fatherName,
                    national_code = nationalCode,
                    phone_number = phoneNumber,
                    address = adres
                )
                user_inf.save()

            else:
                user_inf = UserInf(
                    username = user,
                    father_name = fatherName,
                    national_code = nationalCode,
                    phone_number = phoneNumber
                )
                user_inf.save()


        except IntegrityError:
            return render(request, "reserve/register.html", {
                "message": "Username already taken."
            })
        login(request, user)
        return HttpResponseRedirect(reverse("reserve:index"))
    else:
        return render(request, "reserve/register.html")