# Generated by Django 2.0.6 on 2018-06-23 16:20

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('products', '0001_initial'),
        ('contractors', '0002_auto_20180623_1619'),
    ]

    operations = [
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('event_date', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Дата')),
                ('product_number', models.IntegerField(default=1)),
                ('product_price', models.FloatField(default=0)),
                ('total_sum', models.FloatField(default=0)),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Создано')),
                ('updated', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Обновлено')),
                ('contractor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='contractors.Contractor', verbose_name='Контрагент')),
            ],
            options={
                'verbose_name': 'запись доходов',
                'verbose_name_plural': 'записи доходов',
            },
        ),
        migrations.CreateModel(
            name='IncomeItem',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Нименование')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Создано')),
                ('updated', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Обновлено')),
            ],
            options={
                'verbose_name': 'статья доходов',
                'verbose_name_plural': 'статьи доходов',
            },
        ),
        migrations.CreateModel(
            name='IncomeItemGroup',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=300, verbose_name='Нименование')),
                ('created', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Создано')),
                ('updated', models.DateTimeField(default=django.utils.timezone.now, verbose_name='Обновлено')),
            ],
            options={
                'verbose_name': 'группа статьи доходов',
                'verbose_name_plural': 'группы статьи доходов',
            },
        ),
        migrations.AddField(
            model_name='incomeitem',
            name='group',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='incomes.IncomeItemGroup', verbose_name='Группа'),
        ),
        migrations.AddField(
            model_name='income',
            name='item',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='incomes.IncomeItem', verbose_name='Статья доходов'),
        ),
        migrations.AddField(
            model_name='income',
            name='product',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='products.Product', verbose_name='Продукт'),
        ),
    ]