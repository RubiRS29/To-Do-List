# Generated by Django 3.2.4 on 2021-06-27 06:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('toDoTasks', '0002_alter_task_listadd'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='listAdd',
            field=models.CharField(blank=True, default=None, max_length=100, null=True),
        ),
    ]
