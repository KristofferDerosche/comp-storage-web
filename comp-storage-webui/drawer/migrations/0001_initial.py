# Generated by Django 5.1.7 on 2025-03-21 21:23

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('category', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Drawer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(blank=True, max_length=10, null=True, unique=True)),
                ('size', models.CharField(choices=[('wide1', 'Wide 1'), ('wide2', 'Wide 2'), ('narrow', 'Narrow'), ('large', 'Large'), ('largest', 'Largest')], default='wide1', max_length=10)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('category', models.ManyToManyField(blank=True, null=True, related_name='drawers', to='category.category')),
            ],
        ),
    ]
