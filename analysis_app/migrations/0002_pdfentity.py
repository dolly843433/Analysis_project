# Generated by Django 4.2.1 on 2024-11-11 15:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analysis_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PdfEntity',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('country', models.CharField(blank=True, max_length=100, null=True)),
                ('entity', models.TextField()),
            ],
        ),
    ]
