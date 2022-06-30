# Generated by Django 4.0.4 on 2022-05-24 05:49

from django.db import migrations, models
import django.db.models.deletion
import modelcluster.fields
import wagtail.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0069_log_entry_jsonfield'),
        ('wagtailimages', '0024_index_image_file_hash'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResearchesPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='ResearcherPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.page')),
                ('bio', wagtail.fields.RichTextField(null=True)),
                ('intrests', wagtail.fields.RichTextField(null=True)),
                ('department', models.CharField(choices=[('', ''), ('Architecture', 'Architecture'), ('Chemical Engineering', 'Chemical Engineering'), ('Civil Engineering', 'Civil Engineering'), ('Computer Science', 'Computer Science'), ('Electrical Engineering', 'Electrical Engineering'), ('Environmental Engineering', 'Environmental Engineering'), ('Industrial Engineering', 'Industrial Engineering'), ('Materials Science', 'Materials Science'), ('Mechanical Engineering', 'Mechanical Engineering'), ('Nuclear Engineering', 'Nuclear Engineering'), ('Physics', 'Physics')], default='Professor', max_length=225)),
                ('contact_name', models.TextField(max_length=225, null=True)),
                ('address', wagtail.fields.RichTextField(default=' National Institute of Technology Tiruchirappalli-620 015')),
                ('phone_number', models.TextField(blank=True, max_length=225, null=True)),
                ('email', models.TextField(max_length=225, null=True)),
                ('image', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtailimages.image')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page',),
        ),
        migrations.CreateModel(
            name='Information',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sort_order', models.IntegerField(blank=True, editable=False, null=True)),
                ('title', models.CharField(max_length=225, null=True)),
                ('text', wagtail.fields.RichTextField(null=True)),
                ('page', modelcluster.fields.ParentalKey(on_delete=django.db.models.deletion.CASCADE, related_name='information', to='researchers.researcherpage')),
            ],
            options={
                'ordering': ['sort_order'],
                'abstract': False,
            },
        ),
    ]