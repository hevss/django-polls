# Generated by Django 4.2.4 on 2023-11-07 13:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('polls', '0003_alter_question_pub_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='question',
            name='author',
            field=models.ForeignKey(editable=False, null=True, on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL),
        ),
    ]
