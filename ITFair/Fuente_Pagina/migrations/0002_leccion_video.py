# Generated by Django 2.1.2 on 2018-11-12 18:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fuente_Pagina', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='leccion',
            name='video',
            field=models.CharField(default='nulo', max_length=100),
            preserve_default=False,
        ),
    ]
