# Generated by Django 3.2.6 on 2021-10-30 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Quiz', '0002_auto_20211030_2136'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='results',
            options={'ordering': ['id'], 'verbose_name': 'Results', 'verbose_name_plural': 'Results'},
        ),
        migrations.AddField(
            model_name='results',
            name='submitted',
            field=models.BooleanField(default=False),
        ),
    ]
