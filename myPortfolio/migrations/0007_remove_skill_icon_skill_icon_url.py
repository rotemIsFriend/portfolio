# Generated by Django 4.2.16 on 2024-10-06 14:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myPortfolio', '0006_skill_icon'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='skill',
            name='icon',
        ),
        migrations.AddField(
            model_name='skill',
            name='icon_url',
            field=models.URLField(blank=True),
        ),
    ]
