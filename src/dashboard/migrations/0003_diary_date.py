# Generated by Django 4.1.3 on 2022-12-25 11:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("dashboard", "0002_diary_content"),
    ]

    operations = [
        migrations.AddField(
            model_name="diary",
            name="date",
            field=models.DateTimeField(null=True),
        ),
    ]