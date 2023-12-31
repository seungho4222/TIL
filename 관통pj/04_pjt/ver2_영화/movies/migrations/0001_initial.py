# Generated by Django 4.2.6 on 2023-10-06 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('summary', models.TextField()),
                ('movie_image', models.ImageField(blank=True, upload_to='%Y%m%d/')),
            ],
        ),
    ]
