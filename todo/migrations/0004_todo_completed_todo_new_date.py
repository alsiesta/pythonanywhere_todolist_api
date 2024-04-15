# Generated by Django 4.0.6 on 2024-04-15 21:38

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('todo', '0003_alter_todo_description'),
    ]

    operations = [
        migrations.AddField(
            model_name='todo',
            name='completed',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='todo',
            name='new_date',
            field=models.DateField(default=datetime.date.today),
        ),
    ]