# Generated by Django 2.0.6 on 2018-06-23 21:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
        ('expenses', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='expense',
            options={'ordering': ['-updated'], 'verbose_name': 'запись расходов', 'verbose_name_plural': 'записи расходов'},
        ),
        migrations.RenameField(
            model_name='expense',
            old_name='product_count_in_pack',
            new_name='products_count_in_pack',
        ),
        migrations.RenameField(
            model_name='expense',
            old_name='product_number_in_pack',
            new_name='products_number_in_pack',
        ),
        migrations.RenameField(
            model_name='expense',
            old_name='product_price',
            new_name='products_total_price',
        ),
        migrations.RenameField(
            model_name='expense',
            old_name='product_weight_in_pack',
            new_name='products_weight_in_pack',
        ),
        migrations.RemoveField(
            model_name='expense',
            name='product',
        ),
        migrations.AddField(
            model_name='expense',
            name='products',
            field=models.ManyToManyField(to='products.Product', verbose_name='Продукты'),
        ),
    ]
