# Generated by Django 4.2.6 on 2023-12-03 10:13

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('hardathon', '0003_alter_hardathon_photo_alter_project_photo'),
    ]

    operations = [
        migrations.RenameField(
            model_name='hardathon',
            old_name='application_end_date',
            new_name='closing_date_for_applications',
        ),
        migrations.RenameField(
            model_name='hardathon',
            old_name='link_to_competition_task',
            new_name='competition_task',
        ),
        migrations.RenameField(
            model_name='hardathon',
            old_name='application_start_date',
            new_name='date_for_accepting_applications',
        ),
        migrations.RenameField(
            model_name='hardathon',
            old_name='organizers_photo',
            new_name='main_organizer_photo',
        ),
        migrations.RenameField(
            model_name='hardathon',
            old_name='organizers_word',
            new_name='main_organizer_word',
        ),
        migrations.RenameField(
            model_name='hardathon',
            old_name='date_of_summing_up',
            new_name='summing_up_date',
        ),
    ]