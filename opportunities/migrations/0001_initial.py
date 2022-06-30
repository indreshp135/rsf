# Generated by Django 4.0.5 on 2022-06-18 07:24

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0069_log_entry_jsonfield'),
    ]

    operations = [
        migrations.CreateModel(
            name='OpportunitiesPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='Opp',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('name', models.CharField(max_length=255)),
                ('institute', models.CharField(max_length=255)),
                ('department', models.CharField(max_length=255)),
                ('last_date', models.DateField()),
                ('more_details', models.URLField(blank=True, max_length=255, null=True)),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='Opps', to='opportunities.opportunitiespage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]