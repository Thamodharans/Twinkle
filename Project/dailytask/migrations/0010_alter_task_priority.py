# Generated by Django 5.1.5 on 2025-02-06 07:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dailytask', '0009_alter_task_task_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='priority',
            field=models.CharField(blank=True, choices=[('Low', 'Low'), ('High', 'High'), ('Critical', 'Critical')], default='Low ', max_length=255, null=True),
        ),
    ]
