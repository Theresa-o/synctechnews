# Generated by Django 4.2.2 on 2023-06-21 15:57

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0002_allnews"),
    ]

    operations = [
        migrations.AlterField(
            model_name="hackernews",
            name="news_id",
            field=models.BigIntegerField(primary_key=True, serialize=False),
        ),
    ]
