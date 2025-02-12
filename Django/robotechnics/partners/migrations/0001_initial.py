# Generated by Django 4.2.6 on 2023-10-18 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Partner',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, upload_to='images/%Y/%m/%d', verbose_name='изображение к мероприятию')),
                ('name', models.CharField(help_text='Максимум 150 символов', max_length=150, verbose_name='название')),
                ('link_to_the_site', models.URLField(verbose_name='ссылка на сайт')),
            ],
            options={
                'verbose_name': 'партнёр',
                'verbose_name_plural': 'партнёры',
            },
        ),
    ]
