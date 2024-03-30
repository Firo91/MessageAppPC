# Generated by Django 5.0.2 on 2024-03-30 22:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MessageApp', '0020_alter_mymessage_background_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymessage',
            name='background_image',
            field=models.CharField(blank=True, choices=[('flyingPlan.mp4', 'Reise'), ('Matrix.mp4', 'Kontoret'), ('meeting.mp4', 'Møte')], max_length=255, null=True),
        ),
    ]
