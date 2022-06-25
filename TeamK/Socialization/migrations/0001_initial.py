# Generated by Django 3.2.5 on 2022-06-25 04:03

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Username', models.CharField(max_length=10, unique=True)),
                ('Password', models.CharField(max_length=50)),
                ('Name', models.CharField(max_length=20)),
                ('Year', models.IntegerField()),
                ('Major', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='ChatMessage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ChatRoomName', models.CharField(max_length=100)),
                ('receiver', models.CharField(max_length=10000)),
                ('message', models.CharField(max_length=1000)),
                ('date', models.DateField()),
                ('sender', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Socialization.user', to_field='Username')),
            ],
        ),
    ]