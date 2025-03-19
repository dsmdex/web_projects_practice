from django.db import models
import datetime

# Global variables
BASE_PRICE = 25.00
TANDEM_SURCHARGE = 15.00
ELECTRIC_SURCHARGE = 25.00

# Create your models here.

class Bike(models.Model):
    """
    Represents a bike available for rental.

    This model stores information about the type and color of bikes in the rental inventory.

    Attributes:
        bike_type (str): The type of bike (e.g., 'Mountain', 'Road', 'City').
        color (str): The color of the bike.
    """
    # bike type constants
    STANDARD = "ST"
    TADNEM = "TA"
    ELECTRIC = "EL"

    BIKE_TYPE_CHOICES = [
        (STANDARD, 'Standard'),
        (TADNEM, "Tandem"),
        (ELECTRIC, "Electric")
    ]

    # model fields
    bike_type = models.CharField(max_length=2, choices=BIKE_TYPE_CHOICES, default=STANDARD)
    color = models.CharField(max_length=10, default="")

    def __str__(self):
        return f"{self.bike_type} - {self.color}"

class Renter(models.Model):
    """
    Represents someone wanting to rent a bike.

    Highlights info needed to be eligible for a renter 

    Attributes:
        first_name (First Name): Name for reference
        last_name (Last Name): Surname
        phone (Phone): Callback info
        vip_num (VIP Information): Confirmation number for rental
    """
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    phone = models.CharField(max_length=15)
    vip_num = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.first_name.title()} {self.last_name.title()} - #{self.phone}"

class Rental(models.Model):
    """
    Represents a bike rental contract.

    This model links a specific bike to a renter, including the rental date and price.

    Attributes:
        bike (Bike): The bike being rented.
        renter (Renter): The person renting the bike.
        date (Date): The date of the rental.
        price (Float): The price of the rental.
    """
    bike = models.ForeignKey(Bike, on_delete=models.CASCADE)
    renter = models.ForeignKey(Renter, on_delete=models.CASCADE)
    date = models.DateField(default=datetime.date.today)
    price = models.FloatField(default=0.0)

    
    def calc_price(self):
        curr_price = BASE_PRICE

        # Apply surcharges based on bike type
        if self.bike.bike_type == "TA":
            curr_price += TANDEM_SURCHARGE
        elif self.bike.bike_type == "EL":
            curr_price += ELECTRIC_SURCHARGE

        # Apply VIP discount if applicable
        if self.renter.vip_num > 0:
            curr_price *= 0.8  # Apply 20% discount

        self.price = curr_price
        return self.price

    