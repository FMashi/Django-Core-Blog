# Generated by Django 4.2.5 on 2023-09-16 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_comment_rating'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='approved_comment',
            field=models.BooleanField(default=True),
        ),
    ]
