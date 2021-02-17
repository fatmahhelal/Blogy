# Generated by Django 3.1.6 on 2021-02-17 13:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('blog', '0012_categorys'),
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', models.TextField()),
                ('post_img', models.ImageField(null=True, upload_to='')),
                ('date_post', models.DateTimeField(default=django.utils.timezone.now)),
                ('isPublish', models.BooleanField(default=False)),
                ('likes_count', models.IntegerField()),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('category_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.categorys')),
            ],
        ),
    ]
