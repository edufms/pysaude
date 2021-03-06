# Generated by Django 3.2.8 on 2021-10-17 00:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CBOS',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sigla', models.CharField(max_length=6)),
                ('descricao', models.CharField(max_length=150)),
            ],
        ),
        migrations.CreateModel(
            name='DocumentosRegistro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sigla', models.CharField(max_length=20)),
                ('nome_documento', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Especialidades',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=150)),
                ('cbo', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cadastros.cbos')),
            ],
        ),
        migrations.CreateModel(
            name='Profissionais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=150)),
                ('nome_social', models.CharField(max_length=150)),
                ('cpf', models.CharField(max_length=11)),
                ('cns', models.CharField(max_length=15)),
                ('data_nascimento', models.DateField()),
                ('nome_mae', models.CharField(max_length=150)),
                ('nome_pai', models.CharField(max_length=150)),
                ('cep', models.CharField(max_length=8)),
                ('logradouro', models.CharField(max_length=255)),
                ('num_endereco', models.IntegerField()),
                ('complemento', models.CharField(max_length=255)),
                ('bairro', models.CharField(max_length=255)),
                ('ponto_referencias', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='TiposExames',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Usuarios',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome_completo', models.CharField(max_length=150)),
                ('nome_social', models.CharField(max_length=150)),
                ('cpf', models.CharField(max_length=11)),
                ('cns', models.CharField(max_length=15)),
                ('data_nascimento', models.DateField()),
                ('nome_mae', models.CharField(max_length=150)),
                ('nome_pai', models.CharField(max_length=150)),
                ('cep', models.CharField(max_length=8)),
                ('logradouro', models.CharField(max_length=255)),
                ('num_endereco', models.IntegerField()),
                ('complemento', models.CharField(max_length=255)),
                ('bairro', models.CharField(max_length=255)),
                ('ponto_referencias', models.CharField(max_length=255)),
                ('email', models.EmailField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Telefones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('tipo_telefone', models.CharField(choices=[('c', 'Celular'), ('r', 'Recado'), ('co', 'Comercial'), ('f', 'Fixo')], max_length=10)),
                ('num_telefone', models.CharField(max_length=15)),
                ('usuario_id', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cadastros.usuarios')),
            ],
        ),
        migrations.CreateModel(
            name='Exames',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=150)),
                ('sigla', models.CharField(max_length=5)),
                ('id_tipo_exame', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cadastros.tiposexames')),
            ],
        ),
        migrations.CreateModel(
            name='EspecProfissionais',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('num_registro', models.CharField(max_length=15)),
                ('id_documento_registro', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cadastros.documentosregistro')),
                ('id_rofissional', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cadastros.profissionais')),
                ('id_specialidade', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='cadastros.especialidades')),
            ],
        ),
    ]
