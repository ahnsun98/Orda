# Generated by Django 3.2.5 on 2022-01-27 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review', '0009_alter_post_author'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID'),
        ),
    ]
