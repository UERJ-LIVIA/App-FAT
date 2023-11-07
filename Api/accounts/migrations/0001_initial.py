# Generated by Django 4.2.4 on 2023-11-01 20:06

import accounts.models
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=20)),
                ('ativo', models.BooleanField(default=True)),
                ('email', models.EmailField(max_length=50)),
                ('placa_carro', models.CharField(blank=True, max_length=8, null=True)),
                ('cnh', models.CharField(blank=True, max_length=11, null=True)),
                ('diretorio', models.ImageField(upload_to=accounts.models.upload_path)),
                ('senha', models.CharField(default='*********', max_length=50)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
