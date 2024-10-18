# Generated by Django 5.1.1 on 2024-10-18 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('category', '0002_remove_categorymodel_task'),
        ('task', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='taskmodel',
            name='category',
            field=models.ManyToManyField(related_name='categories', to='category.categorymodel'),
        ),
    ]
