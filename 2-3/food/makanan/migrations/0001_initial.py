# Generated by Django 3.2.3 on 2021-10-13 12:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Makan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item', models.CharField(default='', max_length=20)),
                ('jenis', models.CharField(default='', max_length=20)),
                ('harga', models.PositiveBigIntegerField(default=0)),
            ],
        ),
    ]