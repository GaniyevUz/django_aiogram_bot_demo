# Generated by Django 4.1.5 on 2023-01-25 10:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0002_remove_admin_telegram_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='admin',
            name='telegram_id',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
    ]
