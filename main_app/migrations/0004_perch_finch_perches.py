# Generated by Django 4.0.1 on 2022-01-26 23:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0003_alter_feeding_options_rename_funch_feeding_finch_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Perch',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('location', models.TextField(max_length=250)),
                ('num_perches', models.IntegerField(verbose_name='Number of Perches')),
            ],
        ),
        migrations.AddField(
            model_name='finch',
            name='perches',
            field=models.ManyToManyField(to='main_app.Perch'),
        ),
    ]