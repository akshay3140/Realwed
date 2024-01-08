# Generated by Django 4.0.4 on 2022-08-13 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_cakedetail'),
    ]

    operations = [
        migrations.CreateModel(
            name='photographerdetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='media/')),
                ('photographername', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
