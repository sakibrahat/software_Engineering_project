# Generated by Django 5.0.3 on 2024-05-04 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_petadd_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='petadd',
            name='image_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]