# Generated by Django 3.2.6 on 2021-10-31 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0004_alter_results_score'),
    ]

    operations = [
        migrations.AddField(
            model_name='results',
            name='date_taken',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
