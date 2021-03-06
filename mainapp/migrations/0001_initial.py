# Generated by Django 4.0.4 on 2022-06-01 14:56

from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion
import mainapp.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AltairProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('phone', models.CharField(blank=True, max_length=15, null=True)),
                ('address', models.TextField()),
                ('dni', models.CharField(max_length=9)),
                ('image', models.ImageField(blank=True, null=True, upload_to='')),
                ('join_date', models.DateField()),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'User profile',
                'verbose_name_plural': 'User profiles',
                'ordering': ['user'],
                'get_latest_by': 'join_date',
            },
        ),
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('address', models.TextField(blank=True, null=True)),
                ('custodian', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mainapp.altairprofile')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='FacilityLocation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rack', models.CharField(max_length=255)),
                ('shelf', models.CharField(max_length=255)),
                ('number', models.CharField(max_length=255)),
                ('start_date', models.DateTimeField(auto_now=True)),
                ('end_end', models.DateTimeField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('facility', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mainapp.facility')),
            ],
        ),
        migrations.CreateModel(
            name='LogEntry',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField()),
                ('value', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Manufacturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('image', models.ImageField(upload_to='media/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Product',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('region', models.CharField(blank=True, choices=[('US', 'American'), ('EEC', 'EEC'), ('FR', 'France')], max_length=255, null=True)),
                ('state', models.CharField(choices=[('AVAILABLE', 'Available'), ('NEEDSREPAIR', 'Needs repair'), ('MAINTENANCE', 'Maintenance'), ('BROKEN', 'Broken'), ('MISSING', 'Missing'), ('DELETED', 'Deleted')], max_length=255)),
                ('model_name', models.CharField(blank=True, max_length=255, null=True)),
                ('serial_no', models.CharField(blank=True, max_length=255, null=True)),
                ('product_no', models.CharField(blank=True, max_length=255, null=True)),
                ('year', models.IntegerField(blank=True, choices=[(1964, 1964), (1965, 1965), (1966, 1966), (1967, 1967), (1968, 1968), (1969, 1969), (1970, 1970), (1971, 1971), (1972, 1972), (1973, 1973), (1974, 1974), (1975, 1975), (1976, 1976), (1977, 1977), (1978, 1978), (1979, 1979), (1980, 1980), (1981, 1981), (1982, 1982), (1983, 1983), (1984, 1984), (1985, 1985), (1986, 1986), (1987, 1987), (1988, 1988), (1989, 1989), (1990, 1990), (1991, 1991), (1992, 1992), (1993, 1993), (1994, 1994), (1995, 1995), (1996, 1996), (1997, 1997), (1998, 1998), (1999, 1999), (2000, 2000), (2001, 2001), (2002, 2002), (2003, 2003), (2004, 2004), (2005, 2005), (2006, 2006), (2007, 2007), (2008, 2008), (2009, 2009), (2010, 2010), (2011, 2011), (2012, 2012), (2013, 2013), (2014, 2014), (2015, 2015), (2016, 2016), (2017, 2017), (2018, 2018), (2019, 2019), (2020, 2020), (2021, 2021), (2022, 2022)], null=True, validators=[django.core.validators.MinValueValidator(1964), mainapp.models.max_value_current_year])),
                ('image', models.ImageField(blank=True, null=True, upload_to='media/')),
                ('value', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ProductCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.SlugField(unique=True)),
                ('description', models.TextField(blank=True, null=True)),
                ('notes', models.TextField(blank=True, null=True)),
                ('colour', models.IntegerField()),
                ('icon', models.ImageField(upload_to='media/')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Monitor',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mainapp.product')),
                ('width', models.IntegerField(verbose_name='Width')),
                ('height', models.IntegerField(verbose_name='Height')),
                ('display_tech', models.CharField(choices=[('CRT', 'CRT'), ('PLASMA', 'Plasma'), ('LCD', 'LCD')], max_length=255)),
                ('display_ratio', models.CharField(choices=[('FOUR_THREE', '4:3'), ('SIXTEEN_NINE', '16:9')], max_length=255)),
                ('screen_size', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
            bases=('mainapp.product',),
        ),
        migrations.CreateModel(
            name='Television',
            fields=[
                ('product_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='mainapp.product')),
                ('width', models.IntegerField(verbose_name='Width')),
                ('height', models.IntegerField(verbose_name='Height')),
                ('display_tech', models.CharField(choices=[('CRT', 'CRT'), ('PLASMA', 'Plasma'), ('LCD', 'LCD')], max_length=255)),
                ('display_ratio', models.CharField(choices=[('FOUR_THREE', '4:3'), ('SIXTEEN_NINE', '16:9')], max_length=255)),
                ('screen_size', models.IntegerField()),
                ('scart_connectors', models.IntegerField()),
                ('composite_connectors', models.IntegerField()),
                ('hdmi_connectors', models.IntegerField()),
            ],
            options={
                'abstract': False,
            },
            bases=('mainapp.product',),
        ),
        migrations.AddField(
            model_name='product',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mainapp.productcategory'),
        ),
        migrations.AddField(
            model_name='product',
            name='donor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='donated_products', to='mainapp.altairprofile'),
        ),
        migrations.AddField(
            model_name='product',
            name='location',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mainapp.facilitylocation'),
        ),
        migrations.AddField(
            model_name='product',
            name='manufacturer',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='mainapp.manufacturer'),
        ),
        migrations.AddField(
            model_name='product',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='owned_products', to='mainapp.altairprofile'),
        ),
    ]
