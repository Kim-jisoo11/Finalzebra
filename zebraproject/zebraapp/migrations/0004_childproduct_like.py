# Generated by Django 3.1.3 on 2020-11-18 22:56

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('zebraapp', '0003_myitem'),
    ]

    operations = [
        migrations.AddField(
            model_name='childproduct',
            name='like',
            field=models.ManyToManyField(blank=True, related_name='like_product', to=settings.AUTH_USER_MODEL),
        ),
    ]
