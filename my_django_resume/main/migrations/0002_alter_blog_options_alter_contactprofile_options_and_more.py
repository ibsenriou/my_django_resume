# Generated by Django 4.0.5 on 2022-06-14 16:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='blog',
            options={'ordering': ['timestamp'], 'verbose_name': 'Blog', 'verbose_name_plural': 'Blog Profiles'},
        ),
        migrations.AlterModelOptions(
            name='contactprofile',
            options={'ordering': ['timestamp'], 'verbose_name': 'Contact Profile', 'verbose_name_plural': 'Contact Profiles'},
        ),
        migrations.AlterModelOptions(
            name='portfolio',
            options={'ordering': ['name'], 'verbose_name': 'Portfolio', 'verbose_name_plural': 'Portfolio Profiles'},
        ),
        migrations.AlterModelOptions(
            name='testimonial',
            options={'ordering': ['name'], 'verbose_name': 'Testimonial', 'verbose_name_plural': 'Testimonials'},
        ),
    ]
