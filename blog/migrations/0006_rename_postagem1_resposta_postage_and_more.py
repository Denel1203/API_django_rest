# Generated by Django 4.1.3 on 2022-11-28 01:00

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_resposta_voto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resposta',
            old_name='postagem1',
            new_name='postage',
        ),
        migrations.RenameField(
            model_name='resposta',
            old_name='usuario1',
            new_name='usuario',
        ),
    ]
