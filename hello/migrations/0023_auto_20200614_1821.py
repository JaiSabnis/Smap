# Generated by Django 3.0.7 on 2020-06-14 18:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hello', '0022_auto_20200614_1741'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='bio',
            field=models.CharField(blank=True, max_length=2000, null=True),
        ),
        migrations.AlterField(
            model_name='profile',
            name='name',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
