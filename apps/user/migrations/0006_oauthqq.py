# Generated by Django 2.0.8 on 2019-03-21 10:38

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0005_auto_20190313_1619'),
    ]

    operations = [
        migrations.CreateModel(
            name='OAuthQQ',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('nickname', models.CharField(max_length=100)),
                ('qq_openid', models.CharField(max_length=100)),
                ('figureurl_qq', models.URLField()),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]