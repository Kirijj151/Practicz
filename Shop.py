def shop(*args, **kwargs):
    summa = 0
    i = 0
    while i < len(args):
        summa += args[i]
        i += 1

    print("=" * 30)
    print("Цены товаров:", args)
    print("Общая стоимость:", summa, "руб")
    print("-" * 30)

    if "discount" in kwargs:
        discount = kwargs["discount"]
    else:
        discount = 0

    if "delivery" in kwargs:
        delivery = kwargs["delivery"]
    else:
        delivery = 0

    skidka = lambda price, disc: price - price * disc / 100

    cena_so_skidkoy = skidka(summa, discount)
    print("Скидка:", discount, "%")
    print("Цена со скидкой:", cena_so_skidkoy, "руб")

    itogo = cena_so_skidkoy + delivery
    print("Доставка:", delivery, "руб")
    print("Итого к оплате:", itogo, "руб")
    print("=" * 30)

    return itogo


shop(120, 250, 80, discount=10, delivery=40)