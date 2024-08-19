# Generated by Django 3.0.6 on 2020-05-25 19:22

import django.db.models.deletion
import wagtail.blocks
import wagtail.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('birdsong', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ExtendedContact',
            fields=[
                ('contact_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='birdsong.Contact')),
                ('first_name', models.CharField(max_length=255)),
                ('last_name', models.CharField(max_length=255)),
                ('location', models.CharField(max_length=255)),
            ],
            bases=('birdsong.contact',),
        ),
        migrations.CreateModel(
            name='SaleCampaign',
            fields=[
                ('campaign_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='birdsong.Campaign')),
                ('body', wagtail.fields.StreamField([('rich_text', wagtail.blocks.RichTextBlock(features=['h3', 'h4', 'bold', 'italic', 'link', 'ul', 'ol', 'document-link'], template='birdsong/mail/blocks/richtext.html'))])),
            ],
            bases=('birdsong.campaign',),
        ),
    ]
