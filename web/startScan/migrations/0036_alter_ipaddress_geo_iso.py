# Generated by Django 3.2.4 on 2023-06-29 12:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('startScan', '0035_vulnerability_source'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ipaddress',
            name='geo_iso',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='ips_country', to='startScan.countryiso'),
        ),
    ]
