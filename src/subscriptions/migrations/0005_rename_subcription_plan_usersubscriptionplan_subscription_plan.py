# Generated by Django 5.0.6 on 2024-05-16 07:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("subscriptions", "0004_subscriptionplan_months"),
    ]

    operations = [
        migrations.RenameField(
            model_name="usersubscriptionplan",
            old_name="subcription_plan",
            new_name="subscription_plan",
        ),
    ]
