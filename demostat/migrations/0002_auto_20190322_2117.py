# Generated by Django 2.1.7 on 2019-03-22 20:17

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('demostat', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Region',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField()),
                ('name', models.CharField(max_length=200)),
                ('group', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='demostat.Region')),
            ],
        ),
        migrations.AddField(
            model_name='demo',
            name='group',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='demostat.Demo'),
        ),
        migrations.RemoveField(
            model_name='demo',
            name='organisation',
        ),
        migrations.AddField(
            model_name='demo',
            name='organisation',
            field=models.ManyToManyField(to='demostat.Organisation'),
        ),
        migrations.AlterField(
            model_name='demo',
            name='tags',
            field=models.ManyToManyField(blank=True, to='demostat.Tag'),
        ),
        migrations.AddField(
            model_name='location',
            name='region',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, to='demostat.Region'),
        ),
    ]
