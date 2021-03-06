# Generated by Django 4.0.5 on 2022-06-30 06:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("researchers", "0005_remove_researcherpage_address_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="researcherpage",
            name="facebook_link",
            field=models.URLField(
                blank=True,
                default=None,
                help_text="Link to Facebook profile",
                max_length=225,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="researcherpage",
            name="google_scholar_link",
            field=models.URLField(
                blank=True,
                default=None,
                help_text="Link to Google Scholar profile",
                max_length=225,
                null=True,
            ),
        ),
        migrations.AddField(
            model_name="researcherpage",
            name="linkedin_link",
            field=models.URLField(
                blank=True,
                default=None,
                help_text="Link to LinkedIn profile",
                max_length=225,
                null=True,
            ),
        ),
    ]
