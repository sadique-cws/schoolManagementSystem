# Generated by Django 4.1.3 on 2023-02-07 04:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Classes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('className', models.CharField(choices=[('LKG', 'LKG'), ('UKG', 'UKG'), ('1', '1'), ('2', '2'), ('3', '3'), ('4', '4'), ('5', '5'), ('6', '6'), ('7', '7'), ('8', '8'), ('9', '9'), ('10', '10')], max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=200)),
                ('father_name', models.CharField(max_length=200)),
                ('mother_name', models.CharField(max_length=200)),
                ('gender', models.CharField(choices=[('M', 'male'), ('F', 'Female'), ('O', 'Other')], max_length=10)),
                ('nationality', models.CharField(choices=[('Indian', 'Indian'), ('Other', 'Other')], max_length=20)),
                ('address', models.TextField()),
                ('city', models.CharField(choices=[('Purnea', 'Purnea'), ('Bhagalpur', 'Bhagalpur')], max_length=30)),
                ('state', models.CharField(max_length=200)),
                ('pin_code', models.IntegerField()),
                ('contact', models.CharField(max_length=15)),
                ('image', models.ImageField(blank=True, null=True, upload_to='students/')),
                ('dob', models.DateField()),
                ('className', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='schoolwork.classes')),
            ],
        ),
    ]