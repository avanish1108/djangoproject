# Generated by Django 2.2.2 on 2019-08-13 16:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('register', '0002_auto_20190813_2145'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userprofileinfo',
            name='profile_pic',
            field=models.ImageField(blank=True, upload_to='media/'),
        ),
    ]
