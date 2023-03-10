# Generated by Django 4.0.4 on 2022-11-20 10:44

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Stocks',
            fields=[
                ('uid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('crerated_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
                ('stock_name', models.CharField(max_length=100)),
                ('stock_url', models.URLField()),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
