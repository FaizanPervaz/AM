# Generated by Django 4.2.3 on 2023-07-18 13:03

from django.db import migrations, models
import django.db.models.deletion
import main.utils


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0006_alter_profile_photo'),
        ('main', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='listing',
            name='brand',
            field=models.CharField(choices=[('audi', 'Audi'), ('bmw', 'BMW'), ('mercedes', 'Mercedes'), ('volkswagen', 'Volkswagen'), ('porsche', 'Porsche'), ('opel', 'Opel'), ('renault', 'Renault'), ('peugeot', 'Peugeot'), ('citroen', 'Citroen'), ('fiat', 'Fiat'), ('alfa-romeo', 'Alfa Romeo'), ('lancia', 'Lancia'), ('toyota', 'Toyota'), ('honda', 'Honda'), ('nissan', 'Nissan'), ('mazda', 'Mazda'), ('mitsubishi', 'Mitsubishi'), ('subaru', 'Subaru'), ('suzuki', 'Suzuki'), ('hyundai', 'Hyundai'), ('kia', 'Kia'), ('chevrolet', 'Chevrolet'), ('ford', 'Ford'), ('chrysler', 'Chrysler'), ('dodge', 'Dodge'), ('jeep', 'Jeep'), ('tesla', 'Tesla'), ('volvo', 'Volvo'), ('saab', 'Saab'), ('skoda', 'Skoda'), ('seat', 'Seat'), ('jaguar', 'Jaguar'), ('land-rover', 'Land Rover'), ('mini', 'Mini'), ('lexus', 'Lexus'), ('infinity', 'Infinity'), ('hummer', 'Hummer'), ('lada', 'Lada'), ('lamborghini', 'Lamborghini'), ('maserati', 'Maserati'), ('bentley', 'Bentley'), ('ferrari', 'Ferrari'), ('aston-martin', 'Aston Martin'), ('rolls-royce', 'Rolls Royce'), ('bugatti', 'Bugatti'), ('lotus', 'Lotus'), ('pontiac', 'Pontiac'), ('cadillac', 'Cadillac'), ('lincoln', 'Lincoln'), ('mercury', 'Mercury'), ('gmc', 'GMC'), ('buick', 'Buick'), ('saturn', 'Saturn'), ('acura', 'Acura'), ('daihatsu', 'Daihatsu'), ('rover', 'Rover'), ('saipa', 'Saipa'), ('zotye', 'Zotye'), ('yamaha', 'Yamaha'), ('other', 'Other')], default=None, max_length=24),
        ),
        migrations.AddField(
            model_name='listing',
            name='color',
            field=models.CharField(default='White', max_length=24),
        ),
        migrations.AddField(
            model_name='listing',
            name='description',
            field=models.TextField(default=None),
        ),
        migrations.AddField(
            model_name='listing',
            name='engine',
            field=models.CharField(default=None, max_length=24),
        ),
        migrations.AddField(
            model_name='listing',
            name='image',
            field=models.ImageField(default='', upload_to=main.utils.user_listing_path),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='location',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.SET_NULL, to='users.location'),
        ),
        migrations.AddField(
            model_name='listing',
            name='mileage',
            field=models.PositiveIntegerField(default=0),
        ),
        migrations.AddField(
            model_name='listing',
            name='model',
            field=models.CharField(default='', max_length=64),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='listing',
            name='transmission',
            field=models.CharField(choices=[('manual', 'Manual'), ('automatic', 'Automatic'), ('semi-automatic', 'Semi-Automatic')], default=None, max_length=24),
        ),
        migrations.AddField(
            model_name='listing',
            name='vin',
            field=models.CharField(default='', max_length=17, unique=True),
            preserve_default=False,
        ),
    ]