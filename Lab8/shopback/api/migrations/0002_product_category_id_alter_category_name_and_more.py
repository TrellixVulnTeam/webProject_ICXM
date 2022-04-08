# Generated by Django 4.0.3 on 2022-04-08 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='category_id',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=400),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.TextField(max_length=4000),
        ),
        migrations.AlterField(
            model_name='product',
            name='name',
            field=models.CharField(max_length=500),
        ),
    ]
