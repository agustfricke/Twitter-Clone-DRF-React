# Generated by Django 4.2 on 2023-04-16 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0002_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='image',
            field=models.ImageField(blank=True, upload_to=''),
        ),
    ]
