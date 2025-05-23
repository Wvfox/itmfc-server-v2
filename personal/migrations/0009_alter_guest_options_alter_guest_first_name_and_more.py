# Generated by Django 5.1.1 on 2025-04-09 13:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('personal', '0008_alter_guest_user_id_alter_guest_user_tag'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='guest',
            options={'ordering': ['id']},
        ),
        migrations.AlterField(
            model_name='guest',
            name='first_name',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='First name user'),
        ),
        migrations.AlterField(
            model_name='guest',
            name='last_name',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='Last name user'),
        ),
        migrations.AlterField(
            model_name='guest',
            name='user_tag',
            field=models.CharField(blank=True, max_length=128, null=True, unique=True, verbose_name='Tag user'),
        ),
    ]
