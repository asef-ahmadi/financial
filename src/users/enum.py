from django.db import models


class Brands(models.TextChoices):
    ETOSE = 'E', 'اتوسه'
    MANGO = 'M', 'منگو'


class Sizes(models.TextChoices):
    FREE = '1', 'Free'
    TWO = '2', '2'
    THREE = '3', '3'
    FOUR = '4', '4'


class Tailors(models.TextChoices):
    HAZARE = 'H', 'رمضان هزاره'
    ANIS = 'A', 'انیس حسینی'
    NASER = 'N', 'سید ناصر حسینی'
    FATEME = 'F', 'فاطمه احمدی'
    ATEFE = 'J', 'عاطفه جعفری'
    NO = '-', 'بی تکلیف'


class Banks(models.TextChoices):
    SEPAH = 'sepah', 'سپه'
    MELAT = 'melat', 'ملت'
    TEJARAT_JADID = 'tejarat_jadid', 'تجارت جدید'
    MELI = 'meli', 'ملی'
    ANSAR = 'ansar', 'انصار'


class OurBanks(models.TextChoices):
    MELI = 'meli', 'ملی'
    SEPAH = 'sepah', 'سپه'


class OurCards(models.TextChoices):
    MELI = '6037991945247934', '6037991945247934'
    SEPAH = '5892101120360652', '5892101120360652'


class BankAccounts(models.TextChoices):
    HAZARE = '8135746477', '8135746477'
    ANIS = '535303789007', '535303789007'
    ATEFE = '', ''
    FATEME = '919303605111', '919303605111'
    NASER = '3737585912', '3737585912'


class CardNo(models.TextChoices):
    ramezan_hazare = '6104337610782417', '6104337610782417'
    seyed_muhammad_hadi_husseini = '5892101275284889', '5892101275284889'
    fariba_husseini = '61033724862539', '6043327482539'
    mohsen_Teymoori = '5892101240136370', '5892101240136370'
    seyed_naser_husseini = '5859831185441671', '5859831185441671'
    fateme_ahmadi = '603799******6172', '603799******6172'
    atefe_jafari = '5892101307714382', '5892101307714382'
