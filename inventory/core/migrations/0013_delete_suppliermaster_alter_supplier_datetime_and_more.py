# Generated by Django 4.2.7 on 2025-02-26 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0012_alter_purchasemaster_supplier'),
    ]

    operations = [
        migrations.DeleteModel(
            name='SupplierMaster',
        ),
        migrations.AlterField(
            model_name='supplier',
            name='datetime',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='supplier',
            name='mobile_no',
            field=models.CharField(max_length=10),
        ),
    ]
