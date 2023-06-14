# Generated by Django 4.2.2 on 2023-06-14 06:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('gryb_app', '0002_order_address_order_recipient_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='carouselimage',
            name='active',
            field=models.BooleanField(default=False, verbose_name='Активность'),
        ),
        migrations.AddField(
            model_name='carouselimage',
            name='link',
            field=models.URLField(blank=True, verbose_name='Ссылка'),
        ),
    ]