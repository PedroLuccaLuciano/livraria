# Generated by Django 4.1 on 2022-12-14 11:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0003_autor_email_alter_autor_dtnasc"),
    ]

    operations = [
        migrations.RenameField(
            model_name="categoria",
            old_name="nome",
            new_name="descricao",
        ),
    ]
