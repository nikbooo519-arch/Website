from django.shortcuts import render

def index(request):
    return render(request, 'home/index.html')

def category_suv(request):
    cars = [
        {
            'name': 'BMW X5',
            'image': 'bmw- x5.jpg',
            'desc': 'Мощный кроссовер: 3.0 л, 340 л.с., полный привод. Идеален для города и лёгкого бездорожья.',
            'price': 'от 14 500 000 ₽'
        },
        {
            'name': 'BMW X7',
            'image': 'bmw- x7.jpg',
            'desc': 'Флагманский SUV: простор на 7 мест, премиальная отделка, топовые ассистенты водителя.',
            'price': 'от 16 800 000 ₽'
        },
        {
            'name': 'BMW X6',
            'image': 'bmw-x6.jpg',
            'desc': 'Хороший кроссовер: простор на 5 мест, премиальная отделка. Идеален для города.',
            'price': 'от 15 500 000 ₽'
        },
        {
            'name': 'BMW XM',
            'image': 'bmw- xm.jpg',
            'desc': 'Гибридный флагман M-серии: дерзкий дизайн, мощность более 650 л.с.',
            'price': 'от 22 000 000 ₽'
        }
    ]
    context = {
        'category_name': 'Внедорожники',
        'description': 'Мощные и проходимые: для города и бездорожья.',
        'cars': cars
    }
    return render(request, 'home/category_detail.html', context)

def category_sedan(request):
    cars = [
        {
            'name': 'BMW 5 Series',
            'image': 'bmw- 5.jpg',
            'desc': 'Баланс динамики и комфорта: бизнес-седан с отличной управляемостью.',
            'price': 'от 9 200 000 ₽'
        },
        {
            'name': 'BMW 7 Series',
            'image': 'bmw- 7.jpg',
            'desc': 'Роскошь и технологии: флагман среди седанов, максимум комфорта для водителя и пассажира.',
            'price': 'от 15 900 000 ₽'
        },
        {
            'name': 'BMW M5',
            'image': 'bmw- m5.jpg',
            'desc': 'Спорт-седан: 4.4 л, более 600 л.с., разгон до 100 км/ч менее 3.4 с.',
            'price': 'от 18 700 000 ₽'
        }
    ]
    context = {
        'category_name': 'Седаны',
        'description': 'Комфорт, статус и динамика: классика бизнес-класса.',
        'cars': cars
    }
    return render(request, 'home/category_detail.html', context)

def category_coupe(request):
    cars = [
        {
            'name': 'BMW 8 Series',
            'image': 'bmw-8.jpg',
            'desc': 'Элегантное купе: стиль и управляемость премиум-уровня.',
            'price': 'от 13 200 000 ₽'
        },
        {
            'name': 'BMW M8',
            'image': 'bmw-m8.jpg',
            'desc': 'Топовый спорткар: экстремальная динамика и агрессивный дизайн.',
            'price': 'от 17 500 000 ₽'
        },
        {
            'name': 'BMW Z4',
            'image': 'bmw-z4.jpg',
            'desc': 'Компактное купе-родстер: драйв и эмоции в чистом виде.',
            'price': 'от 6 900 000 ₽'
        }
    ]
    context = {
        'category_name': 'Купе',
        'description': 'Стиль и азарт: купе для тех, кто любит скорость.',
        'cars': cars
    }
    return render(request, 'home/category_detail.html', context)

def category_cabriolet(request):
    cars = [
        {
            'name': 'BMW 8 Series Convertible',
            'image': 'bmw-8-convertible.jpg',
            'desc': 'Кабриолет премиум-класса: роскошь и ветер в волосах.',
            'price': 'от 15 100 000 ₽'
        },
        {
            'name': 'BMW Z4 Roadster',
            'image': 'bmw-z4-roadster.jpg',
            'desc': 'Открытый родстер: компактный, лёгкий и очень динамичный.',
            'price': 'от 7 200 000 ₽'
        }
    ]
    context = {
        'category_name': 'Кабриолеты',
        'description': 'Ветер, солнце и драйв: кабриолеты для ярких эмоций.',
        'cars': cars
    }
    return render(request, 'home/category_detail.html', context)

def category_wagon(request):
    cars = [
        {
            'name': 'BMW 3 Series Touring',
            'image': 'bmw-3-touring.jpg',
            'desc': 'Практичный универсал: отличный баланс динамики и вместительности.',
            'price': 'от 8 100 000 ₽'
        },
        {
            'name': 'BMW 5 Series Touring',
            'image': 'bmw-5-touring.jpg',
            'desc': 'Премиальный универсал: комфорт бизнес-класса и огромный багажник.',
            'price': 'от 12 400 000 ₽'
        }
    ]
    context = {
        'category_name': 'Универсалы',
        'description': 'Практичность и стиль: универсалы для семьи и путешествий.',
        'cars': cars
    }
    return render(request, 'home/category_detail.html', context)

def category_hatchback(request):
    cars = [
        {
            'name': 'BMW 1 Series',
            'image': 'bmw-1.jpg',
            'desc': 'Компактный хэтчбек: манёвренность и удовольствие от вождения в городе.',
            'price': 'от 4 800 000 ₽'
        },
        {
            'name': 'BMW 2 Series Gran Coupe',
            'image': 'bmw-2-gran-coupe.jpg',
            'desc': 'Стильный городской хэтчбек: современный дизайн и продвинутые технологии.',
            'price': 'от 5 900 000 ₽'
        }
    ]
    context = {
        'category_name': 'Хэтчбеки',
        'description': 'Компактность и удобство: хэтчбеки для города.',
        'cars': cars
    }
    return render(request, 'home/category_detail.html', context)