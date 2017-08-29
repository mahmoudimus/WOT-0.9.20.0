# 2017.08.29 21:49:28 St�edn� Evropa (letn� �as)
# Embedded file name: scripts/client/gui/shared/economics.py
from ItemRestore import getVehicleRestorePrice
from gui.shared.money import Money, Currency

def getActionPrc(price, defaultPrice):

    def calculate(price, defaultPrice):
        price = price or 0
        defaultPrice = defaultPrice or 0
        if defaultPrice == 0 or price == defaultPrice:
            return 0
        return int(round((1 - float(price) / defaultPrice) * 100))

    if isinstance(price, Money):
        for currency in Currency.BY_WEIGHT:
            value = calculate(price.get(currency), defaultPrice.get(currency))
            if value != 0:
                return value

        return 0
    return calculate(price, defaultPrice)


def calcRentPackages(vehicle, proxy):
    result = []
    if proxy is not None and vehicle.isRentable:
        rentCost = proxy.shop.getVehicleRentPrices().get(vehicle.intCD, {})
        defaultRentCost = proxy.shop.defaults.getVehicleRentPrices().get(vehicle.intCD, {})
        if len(rentCost) and len(defaultRentCost) is not None:
            for key in sorted(rentCost.keys()):
                rentPrice = Money.makeFromMoneyTuple(rentCost[key].get('cost', ()))
                defaultRentPrice = Money.makeFromMoneyTuple(defaultRentCost.get(key, {}).get('cost', rentPrice))
                result.append({'days': key,
                 'rentPrice': rentPrice,
                 'defaultRentPrice': defaultRentPrice})

    return result


def getPremiumCostActionPrc(discounts, packet, proxy):
    defaultPremiumCost = proxy.shop.defaults.premiumCost
    premiumCost = proxy.shop.getPremiumCostWithDiscount(discounts)
    return getActionPrc(premiumCost.get(packet), defaultPremiumCost.get(packet))


def calcVehicleRestorePrice(defaultPrice, proxy):
    """
    # calculate vehicle restore price
    :param defaultPrice: <Money> default buy price
    :return: <Money> restore price
    """
    exchangeRate = proxy.exchangeRate
    sellPriceFactor = proxy.sellPriceModif
    restorePriceModif = proxy.vehiclesRestoreConfig.restorePriceModif
    return Money.makeFromMoneyTuple(getVehicleRestorePrice(defaultPrice, exchangeRate, sellPriceFactor, restorePriceModif))


def getGUIPrice(item, money, exchangeRate):
    """
    # chooses one of item prices to display in GUI
    :param item: <GUIItem>
    :param money: <Money>
    :param exchangeRate: <int> gold exchange rate
    :return: <Money> one price to display in GUI
    """
    mayRent, rentReason = item.mayRent(money)
    if item.isRestorePossible():
        if item.isRestoreAvailable():
            if item.mayRestoreWithExchange(money, exchangeRate) or not mayRent:
                return item.restorePrice
            else:
                return item.minRentPrice
        elif item.hasRestoreCooldown():
            return item.minRentPrice or item.restorePrice
    return item.minRentPrice or item.getBuyPrice(preferred=False).price
# okay decompyling c:\Users\PC\wotmods\files\originals\res\packages\scripts\scripts\client\gui\shared\economics.pyc 
# decompiled 1 files: 1 okay, 0 failed, 0 verify failed
# 2017.08.29 21:49:28 St�edn� Evropa (letn� �as)
