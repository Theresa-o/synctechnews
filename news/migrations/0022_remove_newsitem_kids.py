# Generated by Django 4.2.2 on 2023-06-27 12:34

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0021_newsitem_kids"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="newsitem",
            name="kids",
        ),
    ]