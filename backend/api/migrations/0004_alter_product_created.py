# Generated by Django 5.0.4 on 2024-04-20 21:25

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0003_alter_priceupdate_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='created',
            field=models.DateField(default=datetime.datetime.now),
        ),
    ]
