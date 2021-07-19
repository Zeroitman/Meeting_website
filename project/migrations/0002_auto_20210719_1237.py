# Generated by Django 2.2.4 on 2021-07-19 12:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import django.db.models.expressions


class Migration(migrations.Migration):

    dependencies = [
        ('project', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Rating',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('from_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='from_people', to=settings.AUTH_USER_MODEL, verbose_name='Лайк от')),
                ('to_user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='to_people', to=settings.AUTH_USER_MODEL, verbose_name='Лайк для')),
            ],
            options={
                'verbose_name': 'Оценка',
                'verbose_name_plural': 'Оценки',
            },
        ),
        migrations.AddConstraint(
            model_name='rating',
            constraint=models.CheckConstraint(check=models.Q(_negated=True, from_user=django.db.models.expressions.F('to_user')), name='users_cannot_rate_themselves'),
        ),
    ]