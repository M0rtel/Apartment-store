# Generated by Django 4.0.3 on 2022-03-25 07:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0004_apartmentcharacteristicskv1_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApartmentCharacteristicsR',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image1', models.ImageField(upload_to='projects/img/')),
                ('image2', models.ImageField(upload_to='projects/img/')),
                ('image3', models.ImageField(upload_to='projects/img/')),
                ('image4', models.ImageField(upload_to='projects/img/')),
                ('image5', models.ImageField(upload_to='projects/img/')),
                ('image6', models.ImageField(upload_to='projects/img/')),
                ('image7', models.ImageField(upload_to='projects/img/')),
                ('image8', models.ImageField(upload_to='projects/img/')),
                ('image9', models.ImageField(upload_to='projects/img/')),
                ('image10', models.ImageField(upload_to='projects/img/')),
                ('what_apartment', models.CharField(default='1-ая квартира', max_length=300)),
                ('price', models.CharField(max_length=300)),
                ('district', models.CharField(max_length=300)),
                ('name_object', models.CharField(max_length=300)),
                ('total_area', models.CharField(max_length=300)),
                ('living_area', models.CharField(max_length=300)),
                ('kitchen', models.CharField(max_length=300)),
                ('floor', models.CharField(max_length=300)),
                ('total_floors', models.CharField(max_length=300)),
                ('material', models.CharField(max_length=300)),
                ('condition', models.CharField(max_length=300)),
                ('fund', models.CharField(max_length=300)),
                ('certificate', models.CharField(max_length=300)),
                ('windows', models.CharField(max_length=300)),
                ('balcony', models.CharField(max_length=300)),
                ('bathroom', models.CharField(max_length=300)),
                ('hot_water', models.CharField(max_length=300)),
                ('heating', models.CharField(max_length=300)),
                ('rooms', models.CharField(max_length=300)),
                ('elevator', models.CharField(max_length=300)),
                ('area_with_cold_rooms', models.CharField(default='49', max_length=300)),
                ('comments', models.TextField()),
            ],
            options={
                'verbose_name': 'Характеристику рекомендованной квартиры',
                'verbose_name_plural': 'Характеристики рекомендованных квартир',
            },
        ),
    ]
