# Generated by Django 3.1.7 on 2021-03-17 19:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backh', '0004_auto_20210317_2252'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to=''),
        ),
    ]