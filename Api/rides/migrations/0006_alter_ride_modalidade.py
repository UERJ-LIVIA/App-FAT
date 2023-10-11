# Generated by Django 4.2.5 on 2023-10-04 19:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rides', '0005_rename_passageiro_ride_passageiros'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ride',
            name='modalidade',
            field=models.CharField(choices=[('CARONA', 'CARONA'), ('UBER', 'Uber')], default='Modalidade.CARONA', max_length=12),
        ),
    ]
