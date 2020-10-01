# Generated by Django 3.0.8 on 2020-10-01 19:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('forumApp', '0004_auto_20201001_1625'),
    ]

    operations = [
        migrations.CreateModel(
            name='Answers',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('answer', models.TextField()),
                ('block_obj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forumApp.Blocks')),
                ('question_obj', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forumApp.Questions')),
                ('user_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='forumApp.ForumUser')),
            ],
        ),
    ]