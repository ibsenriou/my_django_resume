# Generated by Django 4.0.5 on 2022-06-21 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_alter_skill_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='certificate',
            name='credentials',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='certificate',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
    ]