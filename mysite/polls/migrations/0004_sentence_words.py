# Generated by Django 4.2.10 on 2024-02-26 14:54

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0003_alter_qiangdaitem_pub_date'),
    ]

    operations = [
        migrations.CreateModel(
            name='Sentence',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sentence', models.CharField(max_length=200)),
                ('translation', models.CharField(max_length=200)),
                ('learned', models.BooleanField(default=False)),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='date added')),
            ],
        ),
        migrations.CreateModel(
            name='Words',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('word', models.CharField(max_length=200)),
                ('pronunciation', models.CharField(max_length=200)),
                ('type', models.CharField(max_length=200)),
                ('mean', models.CharField(max_length=200)),
                ('add_date', models.DateTimeField(auto_now_add=True, verbose_name='date added')),
                ('sentence', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='words', to='polls.sentence')),
            ],
        ),
    ]
