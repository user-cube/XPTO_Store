# Generated by Django 2.2.6 on 2019-11-02 22:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0017_auto_20191102_2159'),
    ]

    operations = [
        migrations.DeleteModel(
            name='ImageUpload',
        ),
        migrations.AlterField(
            model_name='profile',
            name='picture',
            field=models.ImageField(default='app/static/img/default.jpg', upload_to='app/static/img/profile_pictures/-384146498/'),
        ),
    ]
