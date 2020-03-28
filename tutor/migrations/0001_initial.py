# Generated by Django 3.0.2 on 2020-03-27 23:59

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject_name', models.CharField(max_length=30)),
            ],
            options={
                'ordering': ['subject_name'],
            },
        ),
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone_number', models.CharField(blank=True, max_length=17, validators=[django.core.validators.RegexValidator(message="Phone number must be entered in the format: '+999999999'. Up to 15 digits allowed.", regex='^\\+?1?\\d{9,15}$')])),
                ('first_name', models.CharField(max_length=200)),
                ('last_name', models.CharField(max_length=200)),
                ('email_addr', models.EmailField(max_length=200)),
                ('pic', models.ImageField(default='/tutor/static/tutor/default_profile_pic.png', upload_to='profile_picture')),
                ('rating', models.DecimalField(decimal_places=2, max_digits=5, null=True)),
                ('subjects_can_help', models.ManyToManyField(to='tutor.Subject')),
                ('user', models.OneToOneField(default='', on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Job',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('course', models.CharField(default='', max_length=200)),
                ('subject', models.CharField(choices=[('none', 'None'), ('african-american studies', 'African-American & African Studies'), ('anthropology', 'Anthropology'), ('astronomy', 'Astronomy'), ('biology', 'Biology'), ('chemistry', 'Chemistry'), ('economics', 'Economics'), ('french', 'French'), ('german', 'German'), ('physics', 'Physics'), ('mathematics', 'Mathematics')], default='None', max_length=200)),
                ('notes', models.TextField(default='', max_length=1000)),
                ('client', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='tutor.Profile')),
                ('user', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
