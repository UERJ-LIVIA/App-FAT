# Generated by Django 4.2.5 on 2023-10-04 19:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cnh',
            field=models.IntegerField(null=True),
        ),
    ]
