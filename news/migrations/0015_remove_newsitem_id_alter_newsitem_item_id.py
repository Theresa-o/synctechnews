# Generated by Django 4.2.2 on 2023-06-26 08:16

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0014_allhackernews_api_created_newsitem_api_created"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="newsitem",
            name="id",
        ),
        migrations.AlterField(
            model_name="newsitem",
            name="item_id",
            field=models.IntegerField(primary_key=True, serialize=False, unique=True),
        ),
    ]
