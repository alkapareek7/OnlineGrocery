
import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [

        ("OnlineStore", "0004_merge_20230402_1155"),

        ("OnlineStore", "0004_merge_20230415_1325"),

    ]

    operations = [
        migrations.AlterField(
            model_name="grocerylist",
            name="created_at",
            field=models.DateField(

                default=datetime.datetime(2023, 4, 2, 11, 58, 43, 264385),

                

            ),
        ),
    ]
