# Generated by Django 2.2.7 on 2019-11-11 14:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gnb', '0003_auto_20191111_1452'),
    ]

    operations = [
        migrations.AlterField(
            model_name='damage',
            name='name',
            field=models.ForeignKey(on_delete=None, related_name='damage_customer_name', to='gnb.Product'),
        ),
    ]
