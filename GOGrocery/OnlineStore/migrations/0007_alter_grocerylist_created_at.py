
# Generated by Django 4.1.7 on 2023-04-16 08:36

# Generated by Django 4.1.7 on 2023-04-15 14:35


import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [

        ("OnlineStore", "0006_groceryitems_alter_grocerylist_created_at"),

        ("OnlineStore", "0006_alter_grocerylist_vegetable_name_and_more"),

    ]

    operations = [
        migrations.AlterField(
            model_name="grocerylist",
            name="created_at",
            field=models.DateField(
                default=datetime.datetime(2023, 4, 16, 11, 36, 21, 956968),
            ),
        ),
    ]
