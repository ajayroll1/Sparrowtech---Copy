# Generated by Django 4.2.7 on 2025-03-22 17:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_alter_item_options_remove_item_brand_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='item',
            name='item_code',
            field=models.CharField(max_length=255),
        ),
        migrations.AlterField(
            model_name='item',
            name='item_name',
            field=models.CharField(max_length=255),
        ),
    ]
