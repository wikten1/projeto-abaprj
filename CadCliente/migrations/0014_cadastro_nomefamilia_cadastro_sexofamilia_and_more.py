# Generated by Django 5.0.4 on 2024-04-14 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CadCliente', '0013_alter_membrofamilia_sexo'),
    ]

    operations = [
        migrations.AddField(
            model_name='cadastro',
            name='nomeFamilia',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name='cadastro',
            name='sexoFamilia',
            field=models.CharField(choices=[('Feminino', 'Feminino'), ('Masculino', 'Masculino'), ('Outros', 'Outros')], max_length=10, null=True),
        ),
        migrations.DeleteModel(
            name='MembroFamilia',
        ),
    ]