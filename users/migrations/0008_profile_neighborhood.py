# Generated by Django 3.1.2 on 2020-11-01 14:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0011_delete_occupant'),
        ('users', '0007_auto_20201031_1438'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='neighborhood',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='hood.neighborhood'),
        ),
    ]
