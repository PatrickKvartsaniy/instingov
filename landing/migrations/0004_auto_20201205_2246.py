# Generated by Django 3.1.4 on 2020-12-05 22:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('landing', '0003_sitecontent_lang'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sitecontent',
            name='lang',
            field=models.CharField(choices=[('English', 'English'), ('Ukrainian', 'Ukrainian')], max_length=10),
        ),
    ]