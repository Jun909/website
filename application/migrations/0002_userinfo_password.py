# Generated by Django 5.1.1 on 2024-10-31 06:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='password',
            field=models.CharField(default=123, max_length=50),
        ),
    ]
