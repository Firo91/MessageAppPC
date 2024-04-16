# Generated by Django 4.2.5 on 2024-04-16 04:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MessageApp', '0024_alter_mymessage_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymessage',
            name='background_image',
            field=models.CharField(blank=True, choices=[('flyingPlan.mp4', 'Reise'), ('Matrix.mp4', 'Kontoret'), ('meeting.mp4', 'Møte'), ('terminal.mp4', 'Terminal'), ('home.mp4', 'Hjem')], max_length=255, null=True),
        ),
    ]