# Generated by Django 3.0.3 on 2021-08-30 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Technology',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.CharField(max_length=50)),
                ('tachnology', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=100)),
            ],
        ),
    ]
