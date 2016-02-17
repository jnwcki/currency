
def eur_to_usd(eur):
    return round((eur / 0.9), 2)


def usd_to_eur(usd):
    return round((usd * 0.9), 2)


def list_eur_to_usd(eur_list):
    return [round((amount / .9), 2) for amount in eur_list]

def list_usd_to_eur(usd_list):
    return [round((amount * .9), 2) for amount in usd_list]


class Money:
    def __init__(self, amount=0, currency=None, target_currency=None):
        self.amount = amount
        self.currency = currency
        self.target_currency = target_currency


    def eur_to_usd(self, eur):
        return round((eur / 0.9), 2)

    def usd_to_eur(self, usd):
        return round((usd * 0.9), 2)

    def list_eur_to_usd(self, eur_list):
        return [round((amount / .9), 2) for amount in eur_list]

    def list_usd_to_eur(self, usd_list):
        return [round((amount * .9), 2) for amount in usd_list]

