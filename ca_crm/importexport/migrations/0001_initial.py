# Generated by Django 4.2.17 on 2025-02-13 06:01

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('custom_auth', '0003_alter_employeeprofile_user_alter_reportinguser_user'),
        ('clients', '0002_rename_account_manager_customer_accountant_name_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('location', models.CharField(max_length=120, unique=True)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('photo', models.CharField(blank=True, max_length=200, null=True)),
                ('is_active', models.BooleanField(default=True)),
                ('modified_date', models.DateTimeField(auto_now=True)),
                ('modified_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='location_modified', to='custom_auth.customuser')),
            ],
        ),
        migrations.CreateModel(
            name='Inward',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('company', models.CharField(max_length=100, verbose_name='Company')),
                ('inward_for', models.CharField(choices=[('partner', 'Partner'), ('other-users', 'Other Users'), ('team', 'Team')], max_length=100, verbose_name='Inward For')),
                ('inward_type', models.CharField(choices=[('returnable', 'Returnable'), ('non-returnable', 'Non-returnable')], max_length=50, verbose_name='Inward Type')),
                ('reference_to', models.CharField(choices=[('task', 'Task'), ('regular', 'Regular')], max_length=50, verbose_name='Reference To')),
                ('inward_title', models.CharField(max_length=120, verbose_name='Inward Title')),
                ('description', models.TextField(verbose_name='Description / Remarks')),
                ('file', models.FileField(blank=True, null=True, upload_to='inward_files/', verbose_name='File (if any)')),
                ('through', models.CharField(max_length=255, verbose_name='Through')),
                ('customer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inward_for_customer', to='clients.customer', verbose_name='Customer')),
                ('location', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='inward_location', to='importexport.location', verbose_name='Location')),
            ],
        ),
    ]
