# Generated by Django 4.0 on 2022-01-07 09:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_user_provider_accounts_id_user_provider_type_code'),
        ('products', '0001_initial'),
        ('cart', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='CartItem',
            new_name='ProductCratItem',
        ),
    ]
