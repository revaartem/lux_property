# Generated by Django 4.1.6 on 2023-02-14 12:28

from django.db import migrations, models
import main_page.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0008_remove_ourbenefits_agents_point_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='CustomerSays',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('photo', models.ImageField(upload_to='', verbose_name=main_page.models.CustomerSays.get_file_name)),
                ('name', models.CharField(max_length=200)),
                ('comment', models.TextField(max_length=1000)),
                ('customer_position', models.CharField(max_length=200)),
                ('is_visible', models.BooleanField(default=True, help_text='Is comment visible on site.')),
            ],
        ),
        migrations.AlterField(
            model_name='propertyphoto',
            name='photo',
            field=models.ImageField(upload_to=main_page.models.PropertyPhoto.get_file_name),
        ),
    ]
