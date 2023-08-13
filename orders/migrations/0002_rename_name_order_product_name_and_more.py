# Generated by Django 4.2.4 on 2023-08-13 08:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('payment', '0002_remove_payment_orders_remove_payment_receipt_and_more'),
        ('inventory', '0002_alter_product_image'),
        ('customer', '0003_remove_customer_orders'),
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='name',
            new_name='product_name',
        ),
        migrations.RenameField(
            model_name='order',
            old_name='products',
            new_name='quantity',
        ),
        migrations.RemoveField(
            model_name='order',
            name='delivery',
        ),
        migrations.RemoveField(
            model_name='order',
            name='locations',
        ),
        migrations.AddField(
            model_name='order',
            name='customer',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='customer.customer'),
        ),
    
    
        migrations.AddField(
            model_name='order',
            name='payment',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='payment.payment'),
        ),
        migrations.AddField(
            model_name='order',
            name='product',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='inventory.product'),
        ),
        migrations.AddField(
            model_name='order',
            name='total_price',
            field=models.DecimalField(decimal_places=2, default=1, max_digits=8),
            preserve_default=False,
        ),
    ]
