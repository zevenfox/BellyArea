# Generated by Django 4.1.3 on 2022-11-28 21:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('belly', '0004_toppick'),
    ]

    operations = [
        migrations.CreateModel(
            name='Graph',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('age', models.CharField(max_length=255)),
                ('point', models.CharField(max_length=255)),
                ('sex', models.CharField(max_length=255)),
            ],
            options={
                'db_table': 'Graph',
            },
        ),
    ]
