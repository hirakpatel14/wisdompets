# Generated by Django 2.2.3 on 2019-07-29 09:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adoptions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='submisson_date',
            field=models.DateTimeField(null=True),
        ),
    ]
