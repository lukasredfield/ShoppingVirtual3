# Generated by Django 4.1 on 2022-10-12 00:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('tienda', '0005_rename_categoria_categoriaprod'),
    ]

    operations = [
        migrations.AddField(
            model_name='productos',
            name='categorias',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='tienda.categoriaprod'),
            preserve_default=False,
        ),
    ]