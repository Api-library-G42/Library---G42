# Generated by Django 4.1.7 on 2023-03-07 12:32

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("user", "0002_remove_user_name_user_is_colaborator_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="password",
            field=models.CharField(max_length=127),
        ),
        migrations.AlterField(
            model_name="user",
            name="username",
            field=models.CharField(max_length=127, unique=True),
        ),
    ]