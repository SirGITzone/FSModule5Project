# Generated by Django 2.2.6 on 2020-02-04 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('p_library', '0004_auto_20200105_1942'),
    ]

    operations = [
        migrations.CreateModel(
            name='PublishingHouse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('apellation', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='book',
            name='publishing_house',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='p_library.PublishingHouse'),
        ),
    ]