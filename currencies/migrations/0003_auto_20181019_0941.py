# Generated by Django 2.1.2 on 2018-10-19 07:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currencies', '0002_auto_20181019_0246'),
    ]

    operations = [
        migrations.AlterField(
            model_name='exchangerate',
            name='value',
            field=models.DecimalField(decimal_places=4, max_digits=12),
        ),
    ]