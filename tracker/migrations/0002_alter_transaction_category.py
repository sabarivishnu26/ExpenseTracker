# Generated by Django 5.2 on 2025-05-07 14:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tracker', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='transaction',
            name='category',
            field=models.CharField(choices=[('food', 'Food'), ('rent', 'Rent'), ('travel', 'Travel'), ('others', 'Others')], max_length=100),
        ),
    ]
