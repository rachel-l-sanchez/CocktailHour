# Generated by Django 4.1.5 on 2023-04-11 23:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cocktail', '0002_remove_cocktail_cocktail_uid_alter_cocktail_id_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cocktail',
            name='id',
            field=models.AutoField(editable=False, primary_key=True, serialize=False),
        ),
    ]