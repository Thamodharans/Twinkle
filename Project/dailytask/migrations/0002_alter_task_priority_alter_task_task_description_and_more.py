# Generated by Django 5.1.5 on 2025-02-04 11:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dailytask', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(blank=True, choices=[('Low', 'Low'), ('High', 'High'), ('Critical', 'Critical')], default='Low', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_status',
            field=models.CharField(blank=True, choices=[('To-Do', 'To-Do'), ('Commited', 'Commited'), ('In Progress', 'In Progress'), ('Completed', 'Completed'), ('Defer', 'Defer')], default='To-Do', max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_type',
            field=models.CharField(blank=True, choices=[('Task', 'Task'), ('Bug', 'Bug')], default='Task', max_length=255, null=True),
        ),
    ]
