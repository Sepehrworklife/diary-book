# Generated by Django 4.1.3 on 2022-12-25 09:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="diary",
            name="content",
            field=models.TextField(default=""),
        ),
    ]