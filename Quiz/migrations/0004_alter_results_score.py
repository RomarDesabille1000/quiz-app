# Generated by Django 3.2.6 on 2021-10-30 17:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0003_auto_20211031_0010'),
    ]

    operations = [
        migrations.AlterField(
            model_name='results',
            name='score',
            field=models.IntegerField(blank=True, null=True),
        ),
    ]
