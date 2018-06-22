"""
##############          Classes and Object Oriented         #############



class LightBulb(object):

    def __init__(self):
        self.is_on = False

    def turn_on(self):
        if self.is_on: return

        print "Lights On"
        self.is_on = True

    def turn_off(self):
        if not self.is_on: return

        print "Lights Off"
        self.is_on = False

# Creating 3 light bulbs
l1 = LightBulb()
l2 = LightBulb()
l3 = LightBulb()

# Print 3 times "Lights On"
l1.turn_on()
l2.turn_on()
l3.turn_on()


# Does not print anything. because l1 is already turned on
l1.turn_on()
_____________________________________________________________________

class Invoice(object):
    def __init__(self, vat):
        self.vat = (1.0 + vat/100.0)

    def print_item(self, name, price):
        print "Item: %s, Price With VAT: %g" % (name, price * self.vat )

i = Invoice(18)
i.print_item("Veggy Burger", 100)

_____________________________________________________________________________


class Invoice(object):
    vats = {
            "Israel" : 1.18,
            "Italy" : 1.22,
            "Japan" : 1.08,
            "Jordan" : 1.16,
            "Thailand" : 0.07,
            }

    @classmethod
    def vat_by_country(cls, country):
        return Invoice.vats[country]

print Invoice.vat_by_country("Israel")
print Invoice.vat_by_country("Thailand")

______________________________________________________________________________
"""
