# Generated by Django 4.2.6 on 2023-10-22 20:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Title',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='name_title', to='apps.title')),
            ],
            options={
                'verbose_name': 'Заголовок',
                'verbose_name_plural': 'Заголовки',
            },
        ),
    ]
