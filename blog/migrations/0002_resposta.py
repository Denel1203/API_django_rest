# Generated by Django 4.1.3 on 2022-11-27 13:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Resposta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descriçao', models.CharField(max_length=30)),
                ('post', models.TextField(max_length=500)),
                ('postagem', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.postagem')),
                ('usuario', models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.usuario')),
            ],
        ),
    ]
