# Generated by Django 2.2.2 on 2019-07-19 16:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('survey', '0002_auto_20190716_2325'),
    ]

    operations = [
        migrations.AlterField(
            model_name='surveyform',
            name='Hobbies',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='surveyform',
            name='Qualities',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='surveyform',
            name='interest',
            field=models.CharField(max_length=200),
        ),
    ]
