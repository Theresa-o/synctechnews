# Generated by Django 4.2.2 on 2023-06-27 12:38

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0022_remove_newsitem_kids"),
    ]

    operations = [
        migrations.AddField(
            model_name="newsitem",
            name="kids",
            field=models.ManyToManyField(blank=True, to="news.newsitem"),
        ),
    ]
