# Generated by Django 2.2.6 on 2019-11-03 18:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0022_auto_20191103_1837'),
    ]

    operations = [
        migrations.AddField(
            model_name='encomenda',
            name='preco',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=11),
        ),
        migrations.AddField(
            model_name='encomenda',
            name='quantidade',
            field=models.IntegerField(default=1, max_length=10),
        ),
        migrations.AddField(
            model_name='encomenda',
            name='total',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=11),
        ),
        migrations.AlterField(
            model_name='items',
            name='picture',
            field=models.ImageField(default='app/static/img/default_item.jpg', upload_to='app/static/img/item/1066483206/'),
        ),
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(default='app/static/img/default.jpg', upload_to='app/static/img/profile_pictures/1066483206/'),
        ),
    ]