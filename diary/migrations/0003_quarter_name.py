# Generated by Django 4.1 on 2022-09-30 15:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0002_alter_evaluation_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='quarter',
            name='name',
            field=models.CharField(default='some', max_length=30),
            preserve_default=False,
        ),
    ]
