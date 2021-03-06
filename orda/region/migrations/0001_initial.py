# Generated by Django 4.0.1 on 2022-01-24 06:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Mountain',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('loc', models.CharField(max_length=20)),
                ('height', models.CharField(max_length=20)),
                ('overview', models.CharField(max_length=20)),
                ('routeimglink', models.CharField(max_length=20)),
                ('detail', models.CharField(max_length=20)),
                ('tourism', models.CharField(max_length=20)),
                ('tourismimglink', models.CharField(max_length=20)),
                ('lat', models.DecimalField(decimal_places=15, max_digits=30)),
                ('lng', models.DecimalField(decimal_places=15, max_digits=30)),
            ],
            options={
                'db_table': 'mountain',
                'managed': False,
            },
        ),
    ]
