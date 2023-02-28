# Generated by Django 4.1.7 on 2023-02-28 08:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ItemId', models.IntegerField()),
                ('ItemName', models.CharField(max_length=255)),
                ('Price', models.FloatField()),
                ('Quantity', models.IntegerField()),
                ('Category', models.CharField(max_length=255)),
            ],
        ),
    ]