# Generated by Django 2.1.7 on 2019-03-04 07:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_interface', '0003_auto_20190303_2138'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='pin',
            field=models.IntegerField(default=0, unique=True),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='beverage',
            name='capacity',
            field=models.IntegerField(default=1000),
        ),
        migrations.AlterField(
            model_name='beverage',
            name='cost_per_unit',
            field=models.DecimalField(decimal_places=4, default=0.59, max_digits=10),
        ),
        migrations.AlterField(
            model_name='beverage',
            name='remaining',
            field=models.IntegerField(default=500),
        ),
        migrations.AlterField(
            model_name='drink',
            name='cost',
            field=models.DecimalField(decimal_places=2, max_digits=10),
        ),
        migrations.AlterField(
            model_name='pour',
            name='volume',
            field=models.IntegerField(default=20),
        ),
    ]
