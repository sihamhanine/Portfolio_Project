# Generated by Django 5.1.1 on 2024-10-17 19:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0006_remove_devis_client_remove_devis_client_address_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='sender_email',
            new_name='email',
        ),
        migrations.RenameField(
            model_name='contact',
            old_name='sender_name',
            new_name='nom',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='sender_phone',
        ),
        migrations.AddField(
            model_name='contact',
            name='objet',
            field=models.CharField(default='Inconnu', max_length=50),
        ),
    ]
