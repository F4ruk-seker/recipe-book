# Generated by Django 4.1.1 on 2022-09-25 20:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0005_alter_recipe_materiallist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='materialList',
            field=models.ManyToManyField(blank=True, to='recipe.material'),
        ),
    ]
