# Generated by Django 4.0.6 on 2022-08-04 17:49

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('student', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='student',
            name='otm',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.otm'),
        ),
        migrations.AlterField(
            model_name='student',
            name='student_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='student.studenttype'),
        ),
    ]
