# Generated by Django 4.0.4 on 2022-08-27 05:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vender', '0002_regdetail_conformpassword'),
    ]

    operations = [
        migrations.CreateModel(
            name='coupledetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='')),
                ('couplename', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.IntegerField()),
                ('description', models.TextField()),
            ],
        ),
    ]
