# Generated by Django 2.2.2 on 2019-06-23 21:20

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.CharField(max_length=144)),
                ('title', models.CharField(max_length=144)),
                ('content', models.TextField()),
                ('created_at', models.CharField(max_length=144)),
            ],
        ),
    ]