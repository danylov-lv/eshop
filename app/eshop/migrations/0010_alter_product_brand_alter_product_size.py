# Generated by Django 4.2 on 2023-06-11 17:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('eshop', '0009_brand_product_brand'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='brand',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eshop.brand', verbose_name='Brand'),
        ),
        migrations.AlterField(
            model_name='product',
            name='size',
            field=models.CharField(choices=[('S', 'S'), ('M', 'M'), ('L', 'L'), ('XL', 'XL'), (6, 6), (6.5, 6.5), (7, 7), (7.5, 7.5), (8, 8), (8.5, 8.5), (9, 9), (9.5, 9.5), (10, 10), (10.5, 10.5), (11, 11), (11.5, 11.5)], max_length=2, verbose_name='Size'),
        ),
    ]
