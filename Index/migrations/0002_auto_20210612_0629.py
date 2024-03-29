# Generated by Django 3.1.5 on 2021-06-12 00:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Index', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='slider_display',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=90)),
                ('description', models.TextField(max_length=1000)),
                ('image', models.ImageField(upload_to='slider_images/')),
            ],
        ),
        migrations.AlterField(
            model_name='about',
            name='description',
            field=models.TextField(max_length=1000),
        ),
        migrations.AlterField(
            model_name='about',
            name='image',
            field=models.ImageField(upload_to='about_Image/'),
        ),
        migrations.AlterField(
            model_name='about',
            name='title',
            field=models.CharField(max_length=90),
        ),
    ]
