# Generated by Django 4.2.4 on 2023-10-31 19:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='cnh',
            field=models.CharField(blank=True, max_length=11),
        ),
    ]
