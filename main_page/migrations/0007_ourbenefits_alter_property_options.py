# Generated by Django 4.1.6 on 2023-02-14 11:33

from django.db import migrations, models
import main_page.models
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('main_page', '0006_alter_property_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='OurBenefits',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('header', models.TextField(max_length=200)),
                ('heading_text', models.TextField(max_length=300)),
                ('house_point', tinymce.models.HTMLField(max_length=100)),
                ('agents_point', tinymce.models.HTMLField(max_length=100)),
                ('safety_point', tinymce.models.HTMLField(max_length=100)),
                ('image', models.ImageField(upload_to=main_page.models.OurBenefits.get_file_name)),
                ('block_1_header_number', models.CharField(max_length=10)),
                ('block_1_heading_text', models.CharField(max_length=40)),
                ('block_2_header_number', models.CharField(max_length=10)),
                ('block_2_heading_text', models.CharField(max_length=40)),
                ('block_3_header_number', models.CharField(max_length=10)),
                ('block_3_heading_text', models.CharField(max_length=40)),
                ('block_4_header_number', models.CharField(max_length=10)),
                ('block_4_heading_text', models.CharField(max_length=40)),
            ],
        ),
        migrations.AlterModelOptions(
            name='property',
            options={'ordering': ('is_visible', 'recommended_offer', 'realtor', 'price', 'country')},
        ),
    ]
