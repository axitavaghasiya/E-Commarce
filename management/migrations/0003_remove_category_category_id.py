# Generated by Django 4.0.6 on 2022-09-02 11:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0002_brands_category_sub_category'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='category',
            name='category_id',
        ),
    ]
