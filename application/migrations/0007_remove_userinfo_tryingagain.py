# Generated by Django 5.1.1 on 2024-10-31 06:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0006_userinfo_tryingagain'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userinfo',
            name='tryingagain',
        ),
    ]
