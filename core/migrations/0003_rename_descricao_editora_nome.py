# Generated by Django 4.1 on 2022-10-20 18:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0002_remove_categoria_descricao"),
    ]

    operations = [
        migrations.RenameField(
            model_name="editora",
            old_name="descricao",
            new_name="nome",
        ),
    ]