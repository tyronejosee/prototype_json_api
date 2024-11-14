# Generated by Django 5.1 on 2024-11-14 16:27

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_available', models.BooleanField(db_index=True, default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=255)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('postal_code', models.CharField(max_length=20)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Make',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_available', models.BooleanField(db_index=True, default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=50)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Automobile',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_available', models.BooleanField(db_index=True, default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('model', models.CharField(max_length=50)),
                ('year', models.IntegerField()),
                ('serial_number', models.CharField(max_length=100, unique=True)),
                ('role', models.CharField(choices=[('available', 'Available'), ('rented', 'Rented'), ('maintenance', 'Maintenance')], default='available', max_length=20)),
                ('daily_rate', models.DecimalField(decimal_places=2, max_digits=6)),
                ('location', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='automobiles', to='vehicles.location')),
                ('make_id', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='makes', to='vehicles.make')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='MaintenanceRecord',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('is_available', models.BooleanField(db_index=True, default=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('description', models.TextField()),
                ('date', models.DateField()),
                ('cost', models.DecimalField(decimal_places=2, max_digits=7)),
                ('completed', models.BooleanField(default=False)),
                ('automobile', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='maintenance_records', to='vehicles.automobile')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
