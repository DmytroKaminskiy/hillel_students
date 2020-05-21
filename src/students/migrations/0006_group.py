# Generated by Django 2.2.12 on 2020-05-21 16:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ('students', '0005_auto_20200514_1709'),
    ]

    operations = [
        migrations.CreateModel(
            name='Group',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('head', models.OneToOneField(
                    null=True,
                    on_delete=django.db.models.deletion.SET_NULL,
                    to='students.Student')),
            ],
        ),
    ]
