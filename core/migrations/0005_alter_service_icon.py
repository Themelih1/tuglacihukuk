# Generated by Django 5.2.2 on 2025-06-18 14:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_siteowner_about_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='service',
            name='icon',
            field=models.CharField(choices=[('fas fa-gavel', 'Ceza Hukuku'), ('fas fa-home', 'Gayrimenkul Hukuku'), ('fas fa-briefcase', 'İş Hukuku'), ('fas fa-users', 'Aile Hukuku'), ('fas fa-file-contract', 'Sözleşmeler'), ('fas fa-landmark', 'Ticaret Hukuku'), ('fas fa-university', 'İdare Hukuku'), ('fas fa-heartbeat', 'Sağlık Hukuku'), ('fas fa-balance-scale', 'Miras Hukuku'), ('fas fa-plane-departure', 'Göçmenlik Hukuku'), ('fas fa-shield-alt', 'Sigorta Hukuku'), ('fas fa-globe', 'Uluslararası Hukuk'), ('fas fa-shield-virus', 'Tüketici Hukuku'), ('fas fa-child', 'Çocuk Hukuku'), ('fas fa-industry', 'Enerji ve Maden Hukuku'), ('fas fa-leaf', 'Çevre Hukuku')], max_length=50, verbose_name='İkon'),
        ),
    ]
