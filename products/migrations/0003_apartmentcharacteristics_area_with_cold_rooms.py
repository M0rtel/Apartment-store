# Generated by Django 4.0.3 on 2022-03-24 20:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_alter_apartmentcharacteristics_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='apartmentcharacteristics',
            name='area_with_cold_rooms',
            field=models.CharField(default='49', max_length=300),
        ),
    ]