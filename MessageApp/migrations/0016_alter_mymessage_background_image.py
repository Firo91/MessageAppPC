# Generated by Django 4.2 on 2023-10-19 09:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MessageApp', '0015_alter_mymessage_background_color'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymessage',
            name='background_image',
            field=models.CharField(blank=True, choices=[('flyingPlan.mp4', 'Reise'), ('Matrix.mp4', 'Kontoret')], max_length=255, null=True),
        ),
    ]
