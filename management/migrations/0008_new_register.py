# Generated by Django 4.0.6 on 2022-09-07 06:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('management', '0007_product_master'),
    ]

    operations = [
        migrations.CreateModel(
            name='new_register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Firstname', models.CharField(max_length=100)),
                ('Lastname', models.CharField(max_length=100)),
                ('Emailaddress', models.CharField(max_length=100)),
                ('Password', models.CharField(max_length=100)),
            ],
        ),
    ]
