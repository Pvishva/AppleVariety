# Generated by Django 5.0.1 on 2024-07-05 16:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pommelogy', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='AppleVariety',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('image', models.ImageField(upload_to='apple_images/')),
                ('description', models.TextField()),
                ('visual_characteristics', models.TextField()),
                ('taste_profile', models.TextField()),
                ('culinary_uses', models.TextField()),
            ],
        ),
    ]
