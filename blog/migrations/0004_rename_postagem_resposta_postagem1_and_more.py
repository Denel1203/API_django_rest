# Generated by Django 4.1.3 on 2022-11-27 19:39

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_post_resposta_comentario'),
    ]

    operations = [
        migrations.RenameField(
            model_name='resposta',
            old_name='postagem',
            new_name='postagem1',
        ),
        migrations.RenameField(
            model_name='resposta',
            old_name='usuario',
            new_name='usuario1',
        ),
    ]