# Generated by Django 2.1.7 on 2019-03-05 03:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web_interface', '0006_beverage_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='DrinkType',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
            ],
            options={
                'verbose_name_plural': 'Drink Types',
                'ordering': ['name'],
            },
        ),
    ]
