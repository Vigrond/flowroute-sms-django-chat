# Generated by Django 2.1 on 2018-08-23 11:48

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64)),
                ('user', models.BooleanField()),
            ],
        ),
        migrations.CreateModel(
            name='Media',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=32)),
                ('file_name', models.CharField(max_length=256)),
                ('mime_type', models.CharField(max_length=64)),
                ('url', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flowId', models.CharField(db_index=True, max_length=64)),
                ('type', models.CharField(max_length=32)),
                ('amount_display', models.DecimalField(decimal_places=6, max_digits=8)),
                ('amount_nanodollars', models.PositiveIntegerField()),
                ('body', models.TextField()),
                ('direction', models.CharField(max_length=32)),
                ('is_mms', models.BooleanField()),
                ('message_callback_url', models.CharField(max_length=256)),
                ('message_encoding', models.IntegerField()),
                ('message_type', models.CharField(max_length=32)),
                ('status', models.CharField(max_length=32)),
                ('timestamp', models.DateTimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Number',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=16)),
                ('contact', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='flowchat.Contact')),
            ],
        ),
        migrations.AddField(
            model_name='message',
            name='recipient',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='recipients', to='flowchat.Number'),
        ),
        migrations.AddField(
            model_name='message',
            name='sender',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='senders', to='flowchat.Number'),
        ),
        migrations.AddField(
            model_name='media',
            name='message',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='flowchat.Message'),
        ),
    ]
