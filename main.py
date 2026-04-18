def almashtir(sonlar):
    yangi_sonlar = []
    for son in sonlar:
        raqamlar = [int(x) for x in str(son)]
        ortacha = sum(raqamlar) / len(raqamlar)
        standart_deviasiya = (sum((x - ortacha) ** 2 for x in raqamlar) / len(raqamlar)) ** 0.5
        yangi_sonlar.append(round(standart_deviasiya))
    return yangi_sonlar

sonlar = [123, 456, 789]
print(almashtir(sonlar))
