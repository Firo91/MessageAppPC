# Generated by Django 4.2 on 2023-10-19 08:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MessageApp', '0013_alter_mymessage_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='mymessage',
            name='background_image',
            field=models.CharField(blank=True, choices=[('flyingPlan.mp4', 'Reise')], max_length=255, null=True),
        ),
    ]
