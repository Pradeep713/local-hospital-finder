# Generated by Django 4.0.5 on 2022-06-19 15:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0009_alter_hospital_cityname_alter_hospital_districtname_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospital',
            name='treatmentName',
            field=models.ManyToManyField(blank=True, related_name='treatmentName', to='base.treatement'),
        ),
    ]