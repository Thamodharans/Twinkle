# Generated by Django 5.1.5 on 2025-02-05 14:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dailytask', '0007_alter_task_estimated_time'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(blank=True, choices=[('Low', 'Low'), ('High', 'High'), ('Critical', 'Critical')], default='Low ', max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='task_status',
            field=models.CharField(blank=True, choices=[('To-Do', 'To-Do'), ('Commited', 'Commited'), ('In_Progress', 'In_Progress'), ('Completed', 'Completed'), ('Defer', 'Defer')], default='To-Do', max_length=15, null=True),
        ),
    ]
