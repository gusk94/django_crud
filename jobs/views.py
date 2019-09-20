from django.shortcuts import render, redirect, get_object_or_404
from .models import Job
from faker import Faker
from pprint import pprint
from decouple import config
import requests


def new(request):
    if request.method == 'GET':
        return render(request, 'jobs/new.html')
    else:
        name = request.POST.get('name')
        if not Job.objects.filter(name=name):
            job = Job()
            job.name = name
            fake = Faker()
            past_job = fake.job()
            job.past_job = past_job
            job.save()
        job = Job.objects.filter(name=name).first()
        KEY = config('KEY')
        url = 'http://api.giphy.com/v1/gifs/search?api_key=' + KEY + '&q=' + job.past_job +'&limit=1&lang=ko'
        datas = requests.get(url).json()
        data = datas.get("data")
        gif_url = ''
        if data:
            gif_url = data[0].get("images").get("original").get("url")
            print(gif_url)
        context = {'job': job, 'gif_url' : gif_url}
        return render(request, 'jobs/result.html', context)
