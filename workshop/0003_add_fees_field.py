from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('workshop', '0002_remove_workshop_time'),  # This should match the previous migration number
    ]

    operations = [
        migrations.AddField(
            model_name='workshop',
            name='fees',
            field=models.IntegerField(default=0),  # You can set a default value here if needed
        ),
    ]
