# Generated by Django 4.0 on 2021-12-11 07:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Poll',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField()),
                ('option_1', models.CharField(help_text='option 1', max_length=100)),
                ('option_2', models.CharField(help_text='option 2', max_length=100)),
                ('option_3', models.CharField(help_text='option 3', max_length=100)),
                ('option_1_counter', models.IntegerField(default=0, help_text='counter for option 1')),
                ('option_2_counter', models.IntegerField(default=0, help_text='counter for option 2')),
                ('option_3_counter', models.IntegerField(default=0, help_text='counter for option 3')),
            ],
        ),
    ]
