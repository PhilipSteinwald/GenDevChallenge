# Generated by Django 4.1.1 on 2023-05-20 13:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0003_alter_first_roomtype_alter_second_roomtype'),
    ]

    operations = [
        migrations.AlterField(
            model_name='first',
            name='roomtype',
            field=models.DecimalField(decimal_places=0, max_digits=3),
        ),
    ]
