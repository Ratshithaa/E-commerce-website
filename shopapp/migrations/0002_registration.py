# Generated by Django 5.0.6 on 2024-06-26 14:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('shopapp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='registration',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=150)),
                ('password', models.CharField(max_length=150)),
                ('email', models.CharField(max_length=150)),
                ('phone', models.IntegerField()),
            ],
        ),
    ]
