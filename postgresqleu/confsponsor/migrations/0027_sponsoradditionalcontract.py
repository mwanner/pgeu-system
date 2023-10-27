# Generated by Django 3.2.14 on 2023-10-27 13:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('digisign', '0002_contract_dates'),
        ('confsponsor', '0026_sponsor_twittername_social'),
    ]

    operations = [
        migrations.CreateModel(
            name='SponsorAdditionalContract',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subject', models.CharField(max_length=100)),
                ('sponsorsigned', models.DateTimeField(blank=True, null=True)),
                ('completed', models.DateTimeField(blank=True, null=True)),
                ('contract', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='confsponsor.sponsorshipcontract')),
                ('digitalcontract', models.OneToOneField(blank=True, help_text='Contract, when using digital signatures', null=True, on_delete=django.db.models.deletion.SET_NULL, to='digisign.digisigndocument')),
                ('sent_to_manager', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('sponsor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='confsponsor.sponsor')),
            ],
        ),
    ]
