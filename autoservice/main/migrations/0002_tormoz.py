# Generated by Django 4.2.3 on 2023-07-29 20:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tormoz',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('work_type', models.CharField(max_length=255, null=True)),
                ('price', models.CharField(max_length=255, null=True)),
            ],
        ),
    ]
