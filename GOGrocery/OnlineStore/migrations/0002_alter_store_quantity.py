# Generated by Django 4.1.7 on 2023-04-06 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("OnlineStore", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="store",
            name="quantity",
            field=models.IntegerField(max_length=20),
        ),
    ]
