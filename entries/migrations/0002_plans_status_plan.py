# Generated by Django 2.2 on 2020-06-27 14:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('entries', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='plans',
            name='status_plan',
            field=models.CharField(choices=[(1, 'Pending'), (0, 'completed')], default=0, max_length=1),
            preserve_default=False,
        ),
    ]
