# Generated by Django 2.1.5 on 2019-02-05 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Patient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('adhaarId', models.IntegerField()),
                ('fname', models.CharField(max_length=20)),
                ('sname', models.CharField(max_length=20)),
                ('contact_no', models.IntegerField()),
                ('address', models.CharField(max_length=70)),
            ],
        ),
    ]
