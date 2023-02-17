from django.db import models
from django.urls import reverse
# Create your models here.


class ItJobs(models.Model):

     #begging of choices scroll down 

    #OPTIONS OF MAIN LANGUAE PLACE
    Csharp = 'C#'
    Cplus = 'C++'
    Python = 'Python'
    JavaScript = 'JavaScript'
    Java = 'Java'
    HTML = 'HTML'
    CSS  = 'CSS'
    SQL  = 'SQL'
    C   = 'C'
    TypeScript = 'TypeScript'
    PHP = 'PHP'
    R  = 'R'
    BashShell = 'Bash/Shell'
    Go = 'Go'
    Swift = 'Swift'
    CHOICES_IN_LANGUAGES = [
         ('Python',Python),
         ('JavaScript',JavaScript),
         ('Java',Java),
         ('HTML',HTML),
         ('CSS',CSS),
         ('SQL',SQL),
         ('C#',Csharp),
         ('C',C),
         ('C++',Cplus),
         ('TypeScript',TypeScript),
         ('PHP',PHP),
         ('R',R),
         ('Bash/Shell',BashShell),
         ('Go',Go),
         ('Swift',Swift),
    ]

    #OPTIONS OF SCOPE PLACE
    Android="Android"
    Backend="Backend"
    Blockchain="Blockchain"
    DataScience = "Data Science"
    DevOps = "DevOps"
    Frontend = 'Frontend'
    Fullstack = 'Fullstack'
    Mobile = 'Mobile'
    QA ='QA'
    SecurityEngineer = "Security Enginerr"
    IOS = "IOS"
    CHOICE_OF_SCOPE=[
        ("Android",Android),
        ("Backend",Backend),
        ("Blockchain",Blockchain),
        ("Data Science",DataScience),
        ("DevOps",DevOps),
        ('Frontend',Frontend),
        ('Mobile',Mobile),
        ('QA',QA),
        ('Security Engineer',SecurityEngineer),
        ('IOS',IOS),
     ]

    #OPTIONS OF EXPERIENCE PLACE
    Intern = "Intern"
    Junior = "Junior"
    Middle = "Middle"
    Senior = "Senior"
    CTO = "CTO"
    EXPERIENCED = [
    ('Intern',Intern),
    ("Junior",Junior),
    ("Middle",Middle),
    ("Senior",Senior),
    ("CTO",CTO),
    ]
    #end of choices scroll down 

    #attributes of the Job model here

    company_name = models.CharField(max_length=20)
    what_we_do = models.TextField()
    requirement = models.TextField(blank=False,null=False)
    location=models.CharField(max_length=25)
    #choices of scope here
    scope=models.CharField(max_length=20,choices=CHOICE_OF_SCOPE,default=Android) 
    #choices of main language here
    main_language = models.CharField(max_length=15,choices=CHOICES_IN_LANGUAGES,default=Python) 
    remote=models.BooleanField(default=False)
    #choices of experience here
    experience = models.CharField(max_length=10,choices=EXPERIENCED) 
    base_salary = models.PositiveIntegerField(null = False,blank=False)
    tg_username = models.CharField(max_length=15,blank=False,null=False)
    location=models.CharField(max_length=25)
    remote=models.BooleanField(default=False)
    created = models.DateTimeField(auto_now_add=True)

    #reverse to url http with job id
    def get_absolute_url(self):
        return reverse('url',args = [str(self.id)])

    #show company name in db
    def __str__(self) -> str:
        return self.company_name
        
class BotUser(models.Model):
    user_id =  models.CharField(max_length=30)
    choosen_language = models.CharField(max_length=10)
    latest_id = models.CharField(max_length=30)
    created_at = models.DateTimeField(auto_now_add=True)

class UserBot(models.Model):
    user_id = models.CharField(max_length=30)
    choosen_language = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)  
    