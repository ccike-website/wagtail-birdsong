# Generated by Django 3.0.6 on 2020-05-07 23:43

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Campaign',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='The name of the campaign', max_length=255)),
                ('subject', models.TextField()),
                ('sent_date', models.DateTimeField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Receipt',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sent_date', models.DateTimeField(auto_now=True)),
                ('success', models.BooleanField(default=False)),
                ('campaign', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='birdsong.Campaign')),
                ('contact', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='birdsong.Contact')),
            ],
        ),
        migrations.AddField(
            model_name='campaign',
            name='receipts',
            field=models.ManyToManyField(through='birdsong.Receipt', to='birdsong.Contact'),
        ),
    ]
