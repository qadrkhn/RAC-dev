# Generated by Django 4.1.5 on 2023-01-25 11:35

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('partner_name', models.CharField(max_length=50)),
                ('website_url', models.CharField(max_length=100)),
                ('checkout_url', models.CharField(max_length=100)),
            ],
        ),
    ]
