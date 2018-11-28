# Generated by Django 2.0.8 on 2018-11-28 20:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('capdb', '0056_casetext_tsv'),
    ]

    operations = [
        migrations.CreateModel(
            name='Snippet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contents', models.TextField(blank=True, help_text='Contents in string, JSON, etc.')),
                ('label', models.CharField(help_text='Label', max_length=24, unique=True)),
                ('format', models.CharField(choices=[('application/json', 'application/json'), ('text/tab-separated-values', 'text/tab-separated-values'), ('text/plain', 'text/plain')], help_text='Data Format', max_length=128)),
            ],
        ),
    ]
