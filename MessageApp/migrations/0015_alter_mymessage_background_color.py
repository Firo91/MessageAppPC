# Generated by Django 4.2 on 2023-10-19 08:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MessageApp', '0014_mymessage_background_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymessage',
            name='background_color',
            field=models.CharField(blank=True, choices=[('green', 'Green'), ('red', 'Red'), ('yellow', 'Yellow'), ('#A91101', 'Soft Red'), ('', 'No Color')], max_length=20, null=True),
        ),
    ]
