# Generated by Django 4.1.2 on 2022-10-23 10:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('barang', '0002_merek_produk_merek'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Merek',
            new_name='Kategori',
        ),
        migrations.RemoveField(
            model_name='produk',
            name='merek',
        ),
        migrations.AddField(
            model_name='produk',
            name='kategori',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='barang.kategori'),
        ),
    ]
