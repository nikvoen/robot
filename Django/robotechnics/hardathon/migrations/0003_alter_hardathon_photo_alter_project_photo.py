# Generated by Django 4.2.6 on 2023-12-02 21:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hardathon', '0002_rename_image_hardathon_photo_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hardathon',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d', verbose_name='изображение к мероприятию'),
        ),
        migrations.AlterField(
            model_name='project',
            name='photo',
            field=models.ImageField(blank=True, upload_to='photos/%Y/%m/%d', verbose_name='изображение к мероприятию'),
        ),
    ]