<<<<<<< HEAD
# Generated by Django 4.1.7 on 2023-04-02 08:58
=======
# Generated by Django 4.1.7 on 2023-04-15 10:29
>>>>>>> c15f5164e3ebff596aadd9ec4df778d378b10fb9

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
<<<<<<< HEAD
        ("OnlineStore", "0004_merge_20230402_1155"),
=======
        ("OnlineStore", "0004_merge_20230415_1325"),
>>>>>>> c15f5164e3ebff596aadd9ec4df778d378b10fb9
    ]

    operations = [
        migrations.AlterField(
            model_name="grocerylist",
            name="created_at",
            field=models.DateField(
<<<<<<< HEAD
                default=datetime.datetime(2023, 4, 2, 11, 58, 43, 264385)
=======
                default=datetime.datetime(2023, 4, 15, 13, 29, 17, 979449)
>>>>>>> c15f5164e3ebff596aadd9ec4df778d378b10fb9
            ),
        ),
    ]
