# Generated by Django 2.2.6 on 2019-11-03 18:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0020_auto_20191103_1137'),
    ]

    operations = [
        migrations.AlterField(
            model_name='items',
            name='picture',
            field=models.ImageField(default='app/static/img/default_item.jpg', upload_to='app/static/img/item/-88378545/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(default='app/static/img/default.jpg', upload_to='app/static/img/profile_pictures/-88378545/'),
        ),
        migrations.CreateModel(
            name='Encomenda',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data', models.DateField(auto_now=True)),
                ('produtos', models.ManyToManyField(to='app.Items')),
            ],
        ),
    ]
