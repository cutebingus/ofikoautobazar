from django.db import models
from django.core.validators import RegexValidator
class Dealer(models.Model):
    jmeno = models.CharField(max_length=50, help_text="Zadejte své jméno", verbose_name='Jméno')
    prijmeni = models.CharField(max_length=50,help_text="Zadejte své příjmení", verbose_name='Příjmení')
    email = models.EmailField(verbose_name='Email',help_text="Zadejte svůj Emal", validators=[RegexValidator(regex='^[A-Za-z]+@[A-Za-z]+\.[A-Za-z]+$',
                                                          message='Zadejte prosím platnou emailovou adresu.')])
    tel = models.CharField(max_length=20,help_text="Zadejte své telefonní číslo", verbose_name='Tel. číslo', validators=[RegexValidator(regex='^(\\+420)? ?[1-9][0-9]{2}( ?[0-9]{3}){2}$',
                                                          message='Zadejte prosím platné telefonní číslo.'
                                                          )])
    adresa = models.CharField(max_length=255,help_text="Zadejte svou adresu", verbose_name='Adresa')

    def __str__(self):
        return f"{self.jmeno} {self.prijmeni}"

class Customer(models.Model):
    jmeno = models.CharField(max_length=50,help_text="Zadejte své jméno", verbose_name='Jméno')
    prijmeni = models.CharField(max_length=50,help_text="Zadejte své příjmení", verbose_name='Příjmení')
    email = models.EmailField(verbose_name='Email',help_text="Zadejte svůj Emal", unique=True,validators=[RegexValidator(regex='^[A-Za-z]+@[A-Za-z]+\.[A-Za-z]+$',
                                                          message='Zadejte prosím platnou emailovou adresu.')]
                                                          )
    tel = models.CharField(max_length=20,help_text="Zadejte své telefonní číslo", verbose_name='Tel. číslo',unique=True, validators=[RegexValidator(regex='^(\\+420)? ?[1-9][0-9]{2}( ?[0-9]{3}){2}$',
                                                          message='Zadejte prosím platné telefonní číslo.'
                                                          )])
    adresa = models.CharField(max_length=255,help_text="Zadejte svou adresu", verbose_name='Adresa')

    def __str__(self):
        return f"{self.jmeno} {self.prijmeni}"

class Meta:
        verbose_name = 'Autobazar'
        verbose_name_plural = 'Autobazary'
        ordering = ['nazev']


class Auta(models.Model):
    ZNACKY = [
        ('Toyota', 'Toyota'),
        ('Ford', 'Ford'),
        ('BMW', 'BMW'),
        ('Mercedes', 'Mercedes'),
        ('Audi', 'Audi'),
        ('Volkswagen', 'Volkswagen'),
    ]

    BARVY = [
        ('Červená', 'Červená'),
        ('Modrá', 'Modrá'),
        ('Zelená', 'Zelená'),
        ('Černá', 'Černá'),
        ('Bílá', 'Bílá'),
        ('Šedá', 'Šedá'),
    ]

    STAV = [
        ('Nový', 'Nový'),
        ('Použitý', 'Použitý'),
        ('Poškozený', 'Poškozený'),
    ]

    znacka = models.CharField(max_length=50, choices=ZNACKY)
    barva = models.CharField(max_length=50, choices=BARVY)
    stav = models.CharField(max_length=20, choices=STAV)
    popis = models.TextField()
    cena = models.DecimalField(max_digits=10, decimal_places=2)
    dealer = models.ForeignKey(Dealer, on_delete=models.CASCADE, related_name='auta')
    customer = models.ForeignKey(Customer, on_delete=models.SET_NULL, null=True, blank=True, related_name='auta')

    def __str__(self):
        return f"{self.znacka} - {self.barva} - {self.stav} - {self.cena} Kč"
