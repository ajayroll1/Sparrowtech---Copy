# Generated by Django 4.2.7 on 2025-02-27 11:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0013_delete_suppliermaster_alter_supplier_datetime_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemmaster',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.brandmaster'),
        ),
        migrations.AlterField(
            model_name='itemmaster',
            name='datetime',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterModelTable(
            name='itemmaster',
            table='core_item_master',
        ),
    ]
