# Generated by Django 4.1.7 on 2023-03-28 14:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0001_initial'),
        ('financial', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reception',
            name='name',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='users.user', verbose_name='از طرف'),
        ),
    ]