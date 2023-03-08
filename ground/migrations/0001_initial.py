# Generated by Django 4.1.5 on 2023-03-08 19:02

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Ground',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=100)),
                ('area', models.CharField(max_length=100)),
                ('city', models.CharField(max_length=100)),
                ('description', models.TextField(blank=True)),
                ('num_of_courts', models.IntegerField(default=1)),
                ('sports_type', models.CharField(max_length=100)),
                ('owner_contact', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
                ('image', models.ImageField(upload_to='gallery')),
                ('has_lights', models.BooleanField(default=False)),
                ('has_drinks', models.BooleanField(default=False)),
                ('map_link', models.CharField(max_length=100)),
                ('should_also_be_shown_in', models.CharField(max_length=150)),
                ('slug', models.SlugField(blank=True, null=True)),
            ],
            options={
                'ordering': ['-name'],
            },
        ),
    ]