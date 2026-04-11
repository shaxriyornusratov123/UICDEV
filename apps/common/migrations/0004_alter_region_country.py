import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("common", "0002_remove_media_file_url_media_file_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="region",
            name="country",
            field=models.ForeignKey(
                blank=True,
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="regions",
                to="common.country",
            ),
        ),
    ]
