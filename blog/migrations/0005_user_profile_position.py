# Generated by Django 3.1.6 on 2021-02-18 04:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20210218_0709'),
    ]

    operations = [
        migrations.AddField(
            model_name='user_profile',
            name='position',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
