# Generated by Django 4.1.3 on 2022-11-18 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Crutch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('datePublished', models.DateField()),
                ('description', models.TextField()),
                ('price', models.IntegerField()),
                ('imageField', models.ImageField(upload_to='')),
            ],
        ),
    ]
