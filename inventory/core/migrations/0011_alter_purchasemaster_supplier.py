# Generated by Django 4.2.7 on 2025-02-24 12:39

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_alter_purchasemaster_supplier'),
    ]

    operations = [
        migrations.AlterField(
            model_name='purchasemaster',
            name='supplier',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.suppliermaster'),
        ),
    ]
