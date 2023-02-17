# Generated by Django 4.0.5 on 2023-02-09 09:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BotUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=30)),
                ('choosen_language', models.CharField(max_length=10)),
                ('latest_id', models.CharField(max_length=30)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='ItJobs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company_name', models.CharField(max_length=20)),
                ('what_we_do', models.TextField()),
                ('requirement', models.TextField()),
                ('scope', models.CharField(choices=[('Android', 'Android'), ('Backend', 'Backend'), ('Blockchain', 'Blockchain'), ('Data Science', 'Data Science'), ('DevOps', 'DevOps'), ('Frontend', 'Frontend'), ('Mobile', 'Mobile'), ('QA', 'QA'), ('Security Engineer', 'Security Enginerr'), ('IOS', 'IOS')], default='Android', max_length=20)),
                ('main_language', models.CharField(choices=[('Python', 'Python'), ('JavaScript', 'JavaScript'), ('Java', 'Java'), ('HTML', 'HTML'), ('CSS', 'CSS'), ('SQL', 'SQL'), ('C#', 'C#'), ('C', 'C'), ('C++', 'C++'), ('TypeScript', 'TypeScript'), ('PHP', 'PHP'), ('R', 'R'), ('Bash/Shell', 'Bash/Shell'), ('Go', 'Go'), ('Swift', 'Swift')], default='Python', max_length=15)),
                ('experience', models.CharField(choices=[('Intern', 'Intern'), ('Junior', 'Junior'), ('Middle', 'Middle'), ('Senior', 'Senior'), ('CTO', 'CTO')], max_length=10)),
                ('base_salary', models.PositiveIntegerField()),
                ('tg_username', models.CharField(max_length=15)),
                ('location', models.CharField(max_length=25)),
                ('remote', models.BooleanField(default=False)),
                ('created', models.DateTimeField(auto_now_add=True)),
            ],
        ),
        migrations.CreateModel(
            name='UserBot',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=30)),
                ('choosen_language', models.CharField(max_length=20)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]