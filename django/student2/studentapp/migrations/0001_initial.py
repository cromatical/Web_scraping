# Generated by Django 3.1 on 2020-09-01 14:53

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
            name='AiClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('class_num', models.IntegerField()),
                ('teacher', models.CharField(max_length=30)),
                ('class_room', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='AiStudents',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('phone_num', models.CharField(max_length=30)),
                ('participate_class', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='student_object', to='studentapp.aiclass')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='student_object', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='StudentPost',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('intro', models.TextField()),
                ('writer', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='post', to='studentapp.aistudents')),
            ],
        ),
    ]