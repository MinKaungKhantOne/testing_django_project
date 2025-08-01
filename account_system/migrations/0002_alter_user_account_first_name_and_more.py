# Generated by Django 5.2 on 2025-07-10 01:52

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("account_system", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user_account",
            name="first_name",
            field=models.CharField(
                blank=True, max_length=150, verbose_name="first name"
            ),
        ),
        migrations.AlterField(
            model_name="user_account",
            name="last_name",
            field=models.CharField(
                blank=True, max_length=150, verbose_name="last name"
            ),
        ),
    ]
