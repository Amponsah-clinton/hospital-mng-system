# Generated by Django 4.1.4 on 2023-03-20 21:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0002_addrecord_gender'),
        ('members', '0003_antenatal_care'),
    ]

    operations = [
        migrations.CreateModel(
            name='Notes',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Findings', models.TextField()),
                ('Drug_Prescriptions', models.TextField()),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.addrecord')),
            ],
        ),
    ]
