# Generated by Django 4.2 on 2025-01-29 04:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Account', '0005_comment_reply_account_biography_account_cover_image_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='qr_code',
            field=models.ImageField(blank=True, null=True, upload_to='qr_codes/'),
        ),
    ]
