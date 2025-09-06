from django.http import request
from django.shortcuts import render, redirect
from django.db import IntegrityError
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

import cv2
from docInterface.settings import Model_ROOT, MEDIA_ROOT
from .models import SkinCancer
import tensorflow_hub as hub
from PIL import Image
import os
import numpy as np

import tensorflow as tf

def home(request):
    return render(request, 'home.html')

@login_required
def check(request):

    if request.method == 'GET':
        return render(request, 'check.html')
    else:
        skinModel = tf.keras.models.load_model(
            Model_ROOT + '/mymodel.h5', custom_objects={'KerasLayer': hub.KerasLayer})

        image = request.FILES['image'].name
        np.set_printoptions(suppress=True)
        img = Image.open(request.FILES['image']).resize((224, 224))
        img.save(os.path.join(MEDIA_ROOT, image), 'jpeg')
        img = np.asarray(img, dtype=np.float32)
        img = img.reshape(1, 224, 224, 3)

        prediction = skinModel.predict(img)
        nv = int(float(prediction[0][0])*100)
        mel = int(float(prediction[0][1])*100)
        bkl = int(float(prediction[0][2])*100)
        bcc = int(float(prediction[0][3])*100)
        akiec = int(float(prediction[0][4])*100)
        vasc = int(float(prediction[0][5])*100)
        df = int(float(prediction[0][6])*100)
        new = SkinCancer(
            image=image, nv=nv, mel=mel, bkl=bkl, bcc=bcc, akiec=akiec, vasc=vasc, df=df)
        new.save()
        print('data saved')
        return render(request, 'result.html', {'result': new})



#---------------AUTHENTIFICATION-------------------#

def signupuser(request):
    if request.method == 'GET':
        return render(request, 'signupuser.html', {'form': UserCreationForm()})
    else:

        # create a new user
        if request.POST['password1'] == request.POST['password2']:

            try:
                # If passwords match, create user
                user = User.objects.create_user(
                    request.POST['username'], password=request.POST['password1'])
                user.save()
                login(request, user)
                # send them to "current" page
                return redirect(check)

            except IntegrityError:
                # username already in db
                return render(request, 'signupuser.html', {'form': UserCreationForm(), 'error': 'That username has already been taken. Please choose a new username.'})

        else:
            # passwords don't match
            print('wrong password')
            # send them back to signupuser.html
            return render(request, 'signupuser.html', {'form': UserCreationForm(), 'error': 'Passwords did not match'})

def loginuser(request):
    if request.method == 'GET':
        return render(request, 'loginuser.html', {'form': AuthenticationForm()})
    else:
        user = authenticate(
            request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return render(request, 'loginuser.html', {'form': AuthenticationForm(), 'error': 'Username and password did not match'})
        else:
            login(request, user)
            return redirect(check)


@ login_required
def logoutuser(request):
    if request.method == 'POST':
        logout(request)
        return redirect(home)

