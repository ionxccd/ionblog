# Generated by Django 4.0.3 on 2022-04-03 23:28

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_alter_post_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.URLField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False),
        ),
    ]
