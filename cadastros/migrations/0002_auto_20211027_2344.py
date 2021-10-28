# Generated by Django 3.2.8 on 2021-10-28 02:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cadastros', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='usuarios',
            name='cidade',
            field=models.CharField(default='', max_length=255),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuarios',
            name='estado',
            field=models.CharField(default='', max_length=2),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='usuarios',
            name='sexo',
            field=models.CharField(choices=[('I', 'Indefinido'), ('M', 'Masculino'), ('F', 'Feminino'), ('NI', 'Não informado')], default='I', max_length=15),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='telefones',
            name='tipo_telefone',
            field=models.CharField(choices=[('f', 'Fixo'), ('c', 'Celular'), ('r', 'Recado'), ('co', 'Comercial')], max_length=10),
        ),
    ]