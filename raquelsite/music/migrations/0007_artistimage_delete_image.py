# Generated by Django 4.0.1 on 2022-01-30 21:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('music', '0006_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArtistImage',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='images/')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to='music.artist')),
            ],
        ),
        migrations.DeleteModel(
            name='Image',
        ),
    ]
