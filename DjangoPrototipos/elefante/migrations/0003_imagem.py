# Generated by Django 4.1 on 2022-09-22 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('elefante', '0002_dados_paperquestion_rename_id_prova_paper_id_paper_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Imagem',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('descricao', models.CharField(max_length=30)),
                ('foto', models.ImageField(blank=True, upload_to='imagem_site')),
            ],
        ),
    ]