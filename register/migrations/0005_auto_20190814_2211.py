# Generated by Django 2.2.2 on 2019-08-14 16:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0004_auto_20190814_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='profile_pic',
            field=models.ImageField(upload_to='profilepic'),
        ),
    ]
