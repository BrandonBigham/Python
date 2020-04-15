# Generated by Django 2.2 on 2020-02-21 17:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('test_1_app', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='owner',
            field=models.ForeignKey(default='whoops', on_delete=django.db.models.deletion.CASCADE, related_name='posts', to='test_1_app.User'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.TextField(),
        ),
    ]
