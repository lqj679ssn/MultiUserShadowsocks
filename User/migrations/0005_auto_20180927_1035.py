# Generated by Django 2.0 on 2018-09-27 10:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('User', '0004_auto_20180927_0219'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='ss_change_time',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='ss_on',
            field=models.BooleanField(default=False, verbose_name='ss状态, 0 off, 1 on'),
        ),
    ]
