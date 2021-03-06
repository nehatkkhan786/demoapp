# Generated by Django 2.2.7 on 2019-11-11 14:14

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Customer',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firm_name', models.CharField(max_length=255)),
                ('name', models.CharField(max_length=255)),
                ('address', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
                ('phone', models.IntegerField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=266)),
                ('size', models.CharField(max_length=255)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
