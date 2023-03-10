# Generated by Django 3.2.9 on 2023-01-05 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('heyurl', '0001_initial'),
    ]

    operations = [
        migrations.DeleteModel(
            name='User',
        ),
        migrations.AlterField(
            model_name='click',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='click',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='url',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='url',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
