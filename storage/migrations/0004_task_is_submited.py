# Generated by Django 3.1.4 on 2020-12-30 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('storage', '0003_auto_20201230_0957'),
    ]

    operations = [
        migrations.AddField(
            model_name='task',
            name='is_submited',
            field=models.BooleanField(default=False),
        ),
    ]