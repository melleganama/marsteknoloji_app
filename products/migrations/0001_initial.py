# Generated by Django 4.2.1 on 2023-06-18 10:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AddProducts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_name', models.CharField(max_length=100)),
                ('product_price', models.IntegerField()),
                ('product_discount_price', models.IntegerField(blank=True)),
                ('stock_quantity', models.IntegerField()),
                ('product_desc', models.TextField()),
                ('product_specif', models.TextField()),
                ('product_color', models.CharField(choices=[('Black', 'Black'), ('Blue', 'Blue'), ('Pink', 'Pink'), ('Silver', 'Silver'), ('white', 'white'), ('Green', 'Green'), ('Yellow', 'Yellow'), ('transparent', 'transparent')], max_length=20)),
                ('product_category', models.CharField(choices=[('computer', 'computer'), ('phone', 'phone'), ('keyboard', 'keyboard'), ('mouse', 'mouse'), ('earphones', 'earphones'), ('phone cover', 'phone cover'), ('computer components', 'computer components')], max_length=20)),
            ],
        ),
    ]