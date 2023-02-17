from ...models import UserBot,ItJobs
from asgiref.sync import sync_to_async
import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'rest.settings')
os.environ["DJANGO_ALLOW_ASYNC_UNSAFE"] = "true"
django.setup()

def save_user(id,language):
    users_id = UserBot.objects.values_list('user_id',flat=True)[::1]
    print(users_id)
    print(type(id))
    if str(id) not in users_id:
        #if it is new user it is going to create new user in database  
        UserBot.objects.get_or_create(user_id = id,choosen_language = language) 
    else:
        #if old user just going to change his choosen language it is going to change in database
        #without creating new folder (updates)
        jobs = UserBot.objects.filter(user_id = id).update(choosen_language = language)
        print(jobs)

def send_result(language):
    #this is going to take all jobs according to choosen language and send back as list
    return ItJobs.objects.filter(main_language = language).values()[::1]