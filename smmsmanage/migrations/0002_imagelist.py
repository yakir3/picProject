# Generated by Django 3.2.9 on 2022-01-02 14:47

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('userprofile', '0005_alter_userprofile_usage_percent'),
        ('smmsmanage', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ImageList',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('filename', models.CharField(max_length=100)),
                ('imgurl', models.URLField(blank=True)),
                ('size', models.IntegerField()),
                ('width', models.IntegerField()),
                ('height', models.IntegerField()),
                ('imghash', models.CharField(max_length=50)),
                ('deleteurl', models.URLField(blank=True)),
                ('last_requestid', models.CharField(blank=True, max_length=50)),
                ('uploaddate', models.DateTimeField(default=django.utils.timezone.now)),
                ('belong_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='userprofile.userprofile')),
            ],
            options={
                'ordering': ('-uploaddate',),
            },
        ),
    ]
