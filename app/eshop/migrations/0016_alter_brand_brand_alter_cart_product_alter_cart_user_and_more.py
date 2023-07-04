# Generated by Django 4.2 on 2023-06-26 17:33

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('eshop', '0015_favourite'),
    ]

    operations = [
        migrations.AlterField(
            model_name='brand',
            name='brand',
            field=models.CharField(max_length=50, unique=True, verbose_name='Brand Name'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eshop.size', verbose_name='Product'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='category',
            name='category_name',
            field=models.CharField(max_length=25, unique=True, verbose_name='Category Name'),
        ),
        migrations.AlterField(
            model_name='favourite',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='eshop.product', verbose_name='Product'),
        ),
        migrations.AlterField(
            model_name='favourite',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AlterField(
            model_name='shippinginfo',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User'),
        ),
        migrations.AlterUniqueTogether(
            name='cart',
            unique_together={('user', 'product')},
        ),
        migrations.AlterUniqueTogether(
            name='favourite',
            unique_together={('user', 'product')},
        ),
        migrations.AlterUniqueTogether(
            name='size',
            unique_together={('product', 'size')},
        ),
        migrations.AlterUniqueTogether(
            name='subcategory',
            unique_together={('category', 'subcategory_name')},
        ),
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.CharField(choices=[('New', 'New'), ('Confirmed', 'Confirmed'), ('Paid', 'Paid'), ('Sent', 'Sent'), ('Completed', 'Completed')], max_length=15, verbose_name='Status')),
                ('ship_to', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='eshop.shippinginfo', verbose_name='Ship to')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='User')),
            ],
        ),
        migrations.AddField(
            model_name='cart',
            name='order',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='eshop.order', verbose_name='Order'),
        ),
    ]
