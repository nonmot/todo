# Generated by Django 3.1.3 on 2020-11-27 04:43

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
            name='TodoList',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('color', models.CharField(choices=[('red', 'red'), ('orange', 'orange'), ('yellow', 'yellow'), ('pink', 'pink'), ('purple', 'purple'), ('green', 'green'), ('blue', 'blue')], default='blue', max_length=10)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='todolist_owner', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Task',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('note', models.TextField(max_length=100)),
                ('deadline', models.DateTimeField()),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('priority', models.BooleanField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='task_owner', to=settings.AUTH_USER_MODEL)),
                ('todolist', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='TODO.todolist')),
            ],
        ),
    ]