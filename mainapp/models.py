import datetime

from django.core.exceptions import ObjectDoesNotExist
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Create your models here.
DEFAULT_MAX_LENGTH = 255


class CommonModel(models.Model):
    """
    Contains common info like name, slug, description and notes.
    """

    name = models.CharField(max_length=DEFAULT_MAX_LENGTH)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)

    class Meta:
        abstract = True


class Facility(CommonModel):
    """
    Represents a place, identified by its postal address,
    where the Products are stored.
    It ALWAYS must contain an ALTAIR member as responsible for the facility
    and the products within.
    """
    address = models.TextField(blank=True, null=True)
    custodian = models.ForeignKey('AltairProfile', on_delete=models.PROTECT)


# FacilityLocation
class FacilityLocation(models.Model):
    """
    It identifies a specific location inside a Facility where
    any product is stored.
    Besides the exact location, it must contain the start date when
    the product was moved there and the end date where it was removed from
    (null for indicating currently present).
    """
    facility = models.ForeignKey('Facility', on_delete=models.PROTECT)
    rack = models.CharField(max_length=DEFAULT_MAX_LENGTH)
    shelf = models.CharField(max_length=DEFAULT_MAX_LENGTH)
    number = models.CharField(max_length=DEFAULT_MAX_LENGTH)
    start_date = models.DateTimeField(auto_now=True)
    end_end = models.DateTimeField(blank=True, null=True)
    notes = models.TextField(blank=True, null=True)


class Manufacturer(CommonModel):
    """
    Atari, Nintendo, Sega, Commodore, Amstrad, Konami, Microsoft, etc.
    """
    image = models.ImageField(upload_to='media/')


# Consola, micro-ordenador, ordenador,
# cable, caja, monitor, televisor, misc
class ProductCategory(CommonModel):
    """

    """
    colour = models.IntegerField()
    # order
    icon = models.ImageField(upload_to='media/')

# class CategoryOrder(CommonModel):


# # Caja Atari 2600 CKultur, etc.
# class ProductGroup(CommonModel):
#     """
#
#     """
#     products  # on_delete=models.PROTECT
#     group_category
#     image
#
# ## product_set, Área RetroPixel, Almacén
# class GroupCategory(CommonModel):
#
#     image

PRODUCT_STATE_CHOICES = [
    ('AVAILABLE', 'Available'),
    ('NEEDSREPAIR', 'Needs repair'),
    ('MAINTENANCE', 'Maintenance'),
    ('BROKEN', 'Broken'),
    ('MISSING', 'Missing'),
    ('DELETED', 'Deleted')
]

PRODUCT_REGION_CHOICES = [
    ('US', 'American'),
    ('EEC', 'EEC'),
    ('FR', 'France'),
]

PRODUCT_MIN_YEAR = 1964  # CKultur's year


def year_choices():
    return [(elem, elem) for elem in range(PRODUCT_MIN_YEAR, datetime.date.today().year + 1)]


def max_value_current_year(value):
    return MaxValueValidator(datetime.date.today().year)(value)

class Product(CommonModel):
    """
    Represents a product saved in the database.
    """
    manufacturer = models.ForeignKey('Manufacturer', on_delete=models.PROTECT)
    owner = models.ForeignKey('AltairProfile', on_delete=models.PROTECT, related_name='owned_products')
    category = models.ForeignKey('ProductCategory', on_delete=models.PROTECT)
    # country: USA, Spain, France
    # encoding format: NTSC, PAL/SECAM, SECAM
    # Voltage: 120 V, 220 V
    region = models.CharField(
        choices=PRODUCT_REGION_CHOICES,
        blank=True,
        null=True,
        max_length=DEFAULT_MAX_LENGTH
    )
    # flags = models.IntegerField(default_value=0x00)  # 0x
    state = models.CharField(choices=PRODUCT_STATE_CHOICES, max_length=DEFAULT_MAX_LENGTH)  # on_delete=models.PROTECT
    location = models.ForeignKey('FacilityLocation', on_delete=models.PROTECT)
    model_name = models.CharField(max_length=DEFAULT_MAX_LENGTH, blank=True, null=True)
    serial_no = models.CharField(max_length=DEFAULT_MAX_LENGTH, blank=True, null=True)
    product_no = models.CharField(max_length=DEFAULT_MAX_LENGTH, blank=True, null=True)
    year = models.IntegerField(
        choices=year_choices(),
        blank=True,
        null=True,
        validators=[
            MinValueValidator(PRODUCT_MIN_YEAR),
            max_value_current_year
        ]
    )
    image = models.ImageField(upload_to='media/', blank=True, null=True)
    value = models.IntegerField(blank=True, null=True)
    donor = models.ForeignKey(
        'AltairProfile',
        on_delete=models.PROTECT,
        blank=True,
        null=True,
        related_name='donated_products'
    )


TV_DISPLAY_TECH_CHOICES = [
    ('CRT', 'CRT'),
    ('PLASMA', 'Plasma'),
    ('LCD', 'LCD')
]

TV_DISPLAY_RATIO_CHOICES = [
    ('FOUR_THREE', '4:3'),
    ('SIXTEEN_NINE', '16:9'),
]


class Television(Product):

    width = models.IntegerField(verbose_name='Width')
    height = models.IntegerField(verbose_name='Height')
    display_tech = models.CharField(choices=TV_DISPLAY_TECH_CHOICES, max_length=DEFAULT_MAX_LENGTH)
    display_ratio = models.CharField(choices=TV_DISPLAY_RATIO_CHOICES, max_length=DEFAULT_MAX_LENGTH)
    screen_size = models.IntegerField()  # Inches

    scart_connectors = models.IntegerField()
    composite_connectors = models.IntegerField()
    hdmi_connectors = models.IntegerField()


class Monitor(Product):

    width = models.IntegerField(verbose_name='Width')
    height = models.IntegerField(verbose_name='Height')
    display_tech = models.CharField(choices=TV_DISPLAY_TECH_CHOICES, max_length=DEFAULT_MAX_LENGTH)
    display_ratio = models.CharField(choices=TV_DISPLAY_RATIO_CHOICES, max_length=DEFAULT_MAX_LENGTH)
    screen_size = models.IntegerField()  # Inches


# Presidente, Vicepresidente, secretario, tesorero => Model as group
# ALTAIR, usuario extra
# id/pk represents ALTAIR number
class AltairProfile(models.Model):
    """
    """
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    phone = models.CharField(max_length=15, null=True, blank=True)
    address = models.TextField()
    dni = models.CharField(max_length=9)
    image = models.ImageField(blank=True, null=True)
    join_date = models.DateField()

    def __unicode__(self):
        return 'User profile: %s (%s %s)' \
               % (self.user.username, self.user.first_name, self.user.last_name)

    # def gravator_url(self):
    #     return "http://www.gravatar.com/avatar/%s?s=50" % hashlib.md5(self.user.email).hexdigest()

    class Meta:
        get_latest_by = "join_date"
        ordering = ['user']
        verbose_name = "User profile"
        verbose_name_plural = "User profiles"


def get_or_create_userprofile(user):
    if user:
        # up = get_object_or_404(UserProfile, user=user)
        try:
            up = AltairProfile.objects.get(user=user)
            if up:
                return up
        except ObjectDoesNotExist:
            pass
    up = AltairProfile(user=user, join_date=timezone.now())
    up.save()

    return up


User.profile = property(lambda u: get_or_create_userprofile(user=u))


class LogEntry(models.Model):

    date = models.DateTimeField()
    value = models.TextField()
