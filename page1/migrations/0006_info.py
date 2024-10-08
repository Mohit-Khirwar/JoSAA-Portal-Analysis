# Generated by Django 4.2.3 on 2023-07-14 19:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('page1', '0005_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='info',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('Institute', models.CharField(max_length=400)),
                ('Seat_type', models.CharField(max_length=20)),
                ('Gender', models.CharField(max_length=30)),
                ('Opening_rank', models.CharField(max_length=10)),
                ('Closing_rank', models.CharField(max_length=10)),
                ('Year', models.IntegerField()),
                ('Round', models.IntegerField()),
                ('Program_name', models.CharField(max_length=150)),
                ('Program_duration', models.IntegerField()),
                ('Program_type', models.CharField(max_length=100)),
            ],
        ),
    ]
