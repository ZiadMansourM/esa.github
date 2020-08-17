from django.shortcuts import render
from .models import CustomUser
from django.template.loader import render_to_string
from esa.settings import BASE_DIR
from django.http import HttpResponse, HttpResponseNotFound

import json

def load(request):
    try:
        with open('sheets.json') as data:
            esas = json.load(data)
    except:
        return HttpResponseNotFound('<h1>Could not load the file</h1>')
    
    for esa in esas:
        first_name, second_name, third_name, *last = esa['Name'].split(" ")
        try:
            obj = CustomUser.objects.get(first_name=first_name, second_name=second_name, third_name=third_name)
            obj.num_posts = esa['Posts']
            obj.num_reactions = esa['Reactions']
            obj.num_shares = esa['Shares']
            obj.num_posts_month = esa['Posts per Month']
            obj.num_reactions_post = esa['Reactions per Post']
            obj.num_shares_post = esa['Shares per Post']
            obj.missed = esa['Missed']
            obj.met = esa['Met']
            obj.save()
        except:
            if last:
                username = f'{ first_name }{ second_name }{ third_name }{last}'
            else:
                username = f'{ first_name }{ second_name }{ third_name }'
            obj = CustomUser(username=username)
            password = 'testing321'
            obj.set_password(password)
            
            obj.first_name = first_name
            obj.second_name = second_name
            obj.third_name = third_name

            obj.num_posts = esa['Posts']
            obj.num_reactions = esa['Reactions']
            obj.num_shares = esa['Shares']
            obj.num_posts_month = esa['Posts per Month']
            obj.num_reactions_post = esa['Reactions per Post']
            obj.num_shares_post = esa['Shares per Post']
            obj.missed = esa['Missed']
            obj.met = esa['Met']
            obj.save()

    esas =  CustomUser.objects.all()
    context = {
        "esas": esas
    }
    print('json file loaded successfully !!')
    print('Directory:' + BASE_DIR + '/base.html')
    return render(request, 'users/home.html', context)

    
# Create your views here.
def home(request):
    esas =  CustomUser.objects.all()
    context = {
        "esas": esas
    }

    content = render_to_string('users/home.html', context)                
    with open(BASE_DIR+'/index.html', 'w', encoding="UTF-8") as static_file:
        static_file.write(content)
    
    print('Html file created successfully !!')
    print('Directory:' + BASE_DIR + '/base.html')
    return render(request, 'users/home.html', context)
