# Generated by Django 5.0.2 on 2024-03-30 23:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MessageApp', '0023_alter_mymessage_background_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mymessage',
            name='status',
            field=models.CharField(blank=True, choices=[('Ledig', 'Ledig'), ('Møte', 'Møte'), ('Ikke på kontoret', 'Ikke på kontoret'), ('På Reise', 'På Reise'), ('På Terminalen', 'På Terminalen'), ('', 'No Status')], default='', max_length=20, null=True),
        ),
    ]
