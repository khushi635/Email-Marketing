from django.shortcuts import render, redirect, HttpResponse
from django.http import FileResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from goobusinessesapp.models import AllServices
from django.http import JsonResponse
import random
import re
from email.message import EmailMessage
import ssl
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from datetime import datetime
from datetime import timedelta
# import datetime as dtpari
import threading
import markdown
import json
import os
import razorpay # pip install razorpay
from spire.pdf.common import *
from spire.pdf import *
from PyPDF2 import PdfWriter, PdfReader
import time

OurMainURL = "https://goobusines.com/"

global lastUpdatetime
lastUpdatetime = datetime.now()


############# 28th jan 2024 ################
deletExtraImagesRUNNINGstatus = True

# Create your views here.
def index(request):
    
    return render(request, 'index.html')

# def intro(request):

#     return render(request, 'intro.html')

def service(request):

    return render(request, 'service.html')
def one(request):

    return render(request, 'one.html')
def two(request):

    return render(request, 'two.html')

def three(request):

    return render(request, 'three.html')

def four(request):

    return render(request, 'four.html')
def five(request):

    return render(request, 'five.html')



