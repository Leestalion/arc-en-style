# Generated by Django 3.0.5 on 2020-04-06 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20200406_1449'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='type_image',
            field=models.CharField(choices=[('OP', 'Portes et Fenêtres'), ('BS', 'Bibliothèques'), ('DR', 'Dressings'), ('OT', 'Autres')], default='OP', max_length=2),
        ),
    ]
