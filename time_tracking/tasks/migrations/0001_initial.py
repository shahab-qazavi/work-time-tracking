# Generated by Django 3.2.8 on 2022-08-30 19:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Tasks',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='title')),
                ('description', models.CharField(blank=True, max_length=350, null=True, verbose_name='description')),
                ('total_hours_time', models.FloatField(default=0)),
                ('state', models.CharField(choices=[('TD', 'to do'), ('PR', 'in progress'), ('PN', 'pending'), ('CL', 'cancel'), ('DN', 'done')], default='TD', max_length=2, verbose_name='state')),
                ('create_at', models.DateTimeField(auto_now_add=True, verbose_name='created at')),
                ('assignment', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='user')),
            ],
        ),
    ]
