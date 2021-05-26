# Generated by Django 3.2.1 on 2021-05-21 06:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BlogCounts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('read_number', models.PositiveIntegerField(default=0)),
                ('stars_number', models.PositiveIntegerField(default=0)),
                ('blog_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.blog')),
            ],
        ),
    ]