# Generated by Django 5.0.4 on 2024-05-04 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0002_remove_menu_inventory_menu_description_alter_menu_id'),
    ]

    operations = [
        migrations.RenameField(
            model_name='menu',
            old_name='ID',
            new_name='id',
        ),
    ]