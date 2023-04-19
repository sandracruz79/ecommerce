# Generated by Django 4.1.2 on 2022-10-05 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('appProductos', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categoria',
            options={'verbose_name': 'categorias', 'verbose_name_plural': 'categorias de productos'},
        ),
        migrations.AddField(
            model_name='producto',
            name='imgGrande',
            field=models.ImageField(null=True, upload_to='productos'),
        ),
        migrations.AddField(
            model_name='producto',
            name='imgPeque',
            field=models.ImageField(null=True, upload_to='iconos'),
        ),
    ]