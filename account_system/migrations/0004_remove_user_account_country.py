# Generated by Django 5.2 on 2025-07-22 04:22

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("account_system", "0003_alter_user_account_username"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="user_account",
            name="country",
        ),
    ]
