# Generated by Django 5.1.2 on 2024-10-09 18:40

import django.db.models.deletion
import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_muatation'),
    ]

    operations = [
        migrations.CreateModel(
            name='Mutation',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('description', models.CharField(max_length=256)),
                ('otherParty', models.CharField(max_length=64)),
                ('otherPartyAccountNumber', models.CharField(max_length=64)),
                ('dateTime', models.DateTimeField()),
            ],
        ),
        migrations.DeleteModel(
            name='Muatation',
        ),
        migrations.AlterField(
            model_name='account',
            name='creationDate',
            field=models.DateField(auto_now=True),
        ),
        migrations.AddField(
            model_name='mutation',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.account'),
        ),
    ]