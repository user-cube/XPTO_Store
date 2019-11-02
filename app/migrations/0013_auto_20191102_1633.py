# Generated by Django 2.2.6 on 2019-11-02 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_auto_20191101_1125'),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nome', models.CharField(max_length=50)),
                ('picture', models.ImageField(upload_to='profile_pictures')),
                ('morada', models.CharField(max_length=100)),
                ('zipcode', models.CharField(max_length=20)),
                ('pais', models.CharField(max_length=25)),
            ],
        ),
        migrations.DeleteModel(
            name='Carrinho',
        ),
    ]