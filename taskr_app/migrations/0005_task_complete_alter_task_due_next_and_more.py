# Generated by Django 5.0.2 on 2024-04-04 22:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskr_app', '0004_alter_task_repeat_days'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='complete',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='task',
            name='due_next',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='task',
            name='repeat_days',
            field=models.SmallIntegerField(default=1, validators=[django.core.validators.MinValueValidator(1)], verbose_name='Repeat every _ days'),
        ),
    ]
