# Generated by Django 5.1.1 on 2024-10-15 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('services', '0005_service_subservice1_description_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='devis',
            name='client',
        ),
        migrations.RemoveField(
            model_name='devis',
            name='client_address',
        ),
        migrations.RemoveField(
            model_name='devis',
            name='devis_status',
        ),
        migrations.RemoveField(
            model_name='devis',
            name='estimated_price',
        ),
        migrations.RemoveField(
            model_name='devis',
            name='service_description',
        ),
        migrations.AddField(
            model_name='devis',
            name='additional_details',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='devis',
            name='client_email',
            field=models.EmailField(default='unknown@example.com', max_length=254),
        ),
        migrations.AddField(
            model_name='devis',
            name='client_name',
            field=models.CharField(default='Inconnu', max_length=100),
        ),
        migrations.AddField(
            model_name='devis',
            name='desired_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='devis',
            name='estimated_budget',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='devis',
            name='phone',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AlterField(
            model_name='devis',
            name='created_at',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='devis',
            name='service',
            field=models.CharField(max_length=100),
        ),
    ]
