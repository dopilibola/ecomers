# Generated by Django 5.1.2 on 2024-11-01 14:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('store', '0003_product_is_sale_product_sale_price_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='costomer',
            new_name='costumer',
        ),
    ]
