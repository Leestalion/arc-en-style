# Generated by Django 3.0.5 on 2020-04-05 18:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20200405_1940'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, upload_to='images/'),
        ),
    ]
