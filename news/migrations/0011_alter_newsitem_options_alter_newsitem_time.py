# Generated by Django 4.2.2 on 2023-06-25 17:10

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):
    dependencies = [
        ("news", "0010_alter_newsitem_options_newsitem_id_and_more"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="newsitem",
            options={
                "ordering": ["-item_id"],
                "verbose_name": "Latest News",
                "verbose_name_plural": "Latest News",
            },
        ),
        migrations.AlterField(
            model_name="newsitem",
            name="time",
            field=models.DateTimeField(
                auto_now_add=True, default=django.utils.timezone.now
            ),
            preserve_default=False,
        ),
    ]
