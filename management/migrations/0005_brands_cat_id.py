# Generated by Django 4.0.6 on 2022-09-05 07:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0004_remove_sub_category_sub_category_id_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='brands',
            name='cat_id',
            field=models.ForeignKey(default='', on_delete=django.db.models.deletion.CASCADE, to='management.category'),
        ),
    ]
