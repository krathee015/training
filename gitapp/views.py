from django.shortcuts import render
import requests

def github(request):
    user = {}
    if 'username' in request.GET:
        username = request.GET['username']
        url = 'https://api.github.com/users/%s' % username
        response = requests.get(url)
        user = response.json()
    context = {'user':user}
    return render(request,'gitapp/github.html',context)


# Create your views here.
