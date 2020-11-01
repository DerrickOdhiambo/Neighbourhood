# Generated by Django 3.1.2 on 2020-11-01 06:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('hood', '0004_occupant_date_created'),
    ]

    operations = [
        migrations.AddField(
            model_name='business',
            name='neighborhood',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hood.neighborhood'),
        ),
        migrations.AddField(
            model_name='occupant',
            name='neighborhood',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='hood.neighborhood'),
        ),
    ]
