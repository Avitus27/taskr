# Generated by Django 5.0.2 on 2024-04-04 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('taskr_app', '0003_task_repeat_days_task_repeats'),
    ]

    operations = [
        migrations.AlterField(
            model_name='task',
            name='repeat_days',
            field=models.SmallIntegerField(default=1, verbose_name='Repeat every _ days'),
        ),
    ]