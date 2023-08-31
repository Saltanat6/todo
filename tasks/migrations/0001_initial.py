# Generated by Django 4.2.4 on 2023-08-29 12:41

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_created=True)),
                ('title', models.CharField(max_length=150)),
                ('description', models.TextField()),
                ('type', models.CharField(choices=[('work', 'Work'), ('home', 'Home'), ('edu', 'Edu')], max_length=25)),
            ],
        ),
    ]
