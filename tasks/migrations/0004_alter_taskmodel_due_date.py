# Generated by Django 4.2.5 on 2023-09-19 18:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tasks', '0003_alter_taskmodel_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='taskmodel',
            name='due_date',
            field=models.DateField(),
        ),
    ]
