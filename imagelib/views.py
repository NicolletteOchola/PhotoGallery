from django.shortcuts import render,redirect,render_to_response
import datetime as dt

# Create your views here.
def index(request):
  date = dt.date.today()
  images =