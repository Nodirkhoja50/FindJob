from django.shortcuts import render,redirect
from django.views.generic.detail import DetailView
from .models import ItJobs
from .models import UserBot
from django.views import View
import requests
from django.contrib import messages
from .forms import JobForm
import json
# Create your views here.
'''class ViewForms(CreateView):
    model = ItJobs
    template_name = 'forms.html'
    fields = '__all__'''
    
def ViewForms(request):
    id = 0
    form = JobForm()
    if request.method == 'POST':
        form =  JobForm(request.POST)
        if form.is_valid():
            id = int(ItJobs.objects.latest('id').id)+1
            form.save()
            messages.success(request,'Qabul qilindi!')    
    context = {     
        'form': form
    }
    #api telegram token
    token = '5986096208:AAE_UIcHt9m1gFhFvUtBKpvcRTRxwZzgxRI'
    #dict of sending url , take id from last submited form
    dict_of_inline = {"inline_keyboard": [[{"text": "Watch👀","url": f"http://127.0.0.1:8000/detail/{id}"}]]}
    #converts dict_of_inline to json
    json_inline = json.dumps(dict_of_inline)
    #text of sending job 
    text = f"<b>{str(request.POST.get('scope'))}</b>"+"\nCompany:"+str(request.POST.get('company_name'))+"\nSteck:"+f"<b>{str(request.POST.get('main_language'))}</b>"+"\nBase money:$"+str(request.POST.get('base_salary'))+"\nLocation:"+str(request.POST.get('location')) 
    #via url of telegram
    url = 'https://api.telegram.org/bot'+token+'/sendMessage'
    #take of all web languages at database
    web_language = request.POST.get('main_language')
    #filter according to chosen language from form
    users = UserBot.objects.filter(choosen_language=web_language).values_list('user_id',flat = True)
    if users != None:
        for i in range(len(users)):
            #form of job,sending to bot
                data = {
                    "chat_id": str(users[i]),
                    "text": text,
                    "parse_mode":"HTML",
                    "reply_markup": json_inline
                }
                requests.post(url,data=data)
    return render(request,'forms.html',context)

class ViewSubmited(View):
    def get(self,request):
        return render(request,'submited_job.html')

class viewDetailJobs(DetailView):
    model = ItJobs
    template_name = 'show_details.html'
    context_object_name = 'jobs'