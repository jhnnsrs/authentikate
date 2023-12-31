# Generated by Django 4.2.4 on 2023-08-04 14:36

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("authentikate", "0001_initial"),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name="user",
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name="user",
            constraint=models.UniqueConstraint(
                condition=models.Q(("iss__isnull", False), ("sub__isnull", False)),
                fields=("sub", "iss"),
                name="unique_sub_iss_if_both_not_null",
            ),
        ),
    ]
