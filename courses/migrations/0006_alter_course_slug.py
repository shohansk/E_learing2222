# Generated by Django 4.0.2 on 2022-02-03 19:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('courses', '0005_course_slug_alter_course_description_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='slug',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
