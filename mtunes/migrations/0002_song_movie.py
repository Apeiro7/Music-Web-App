

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mtunes', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='song',
            name='movie',
            field=models.CharField(default='None', max_length=150),
        ),
    ]
