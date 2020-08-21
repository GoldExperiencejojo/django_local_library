# Generated by Django 3.1 on 2020-08-18 09:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_auto_20200818_1459'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='status',
            field=models.CharField(blank=True, choices=[('m', 'Maintenance(维护中)'), ('o', 'On loanz(已借出)'), ('a', 'Available(可用)'), ('r', 'Reserved(已预订)')], default='m', help_text='Book availability', max_length=1),
        ),
    ]