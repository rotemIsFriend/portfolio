# Generated by Django 4.2.16 on 2024-10-06 08:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myPortfolio', '0002_skill_project_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='image',
            field=models.ImageField(default='projects/images/default.jpg', upload_to='myPortfolio/static/images/'),
        ),
    ]
