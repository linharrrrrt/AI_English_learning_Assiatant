# Generated by Django 4.2.10 on 2024-02-27 02:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0004_sentence_words'),
    ]

    operations = [
        migrations.AddField(
            model_name='sentence',
            name='syntactic_analysis',
            field=models.CharField(default=None, max_length=200),
            preserve_default=False,
        ),
    ]
