#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Есть словарь координат городов
from pprint import pprint
sites = {
    'Moscow': (550, 370),
    'London': (510, 510),
    'Paris': (480, 480),
}

# Составим словарь словарей расстояний между ними
# расстояние на координатной сетке - корень из (x1 - x2) ** 2 + (y1 - y2) ** 2

distances = dict()
msc = sites['Moscow']
lnd = sites['London']
prs = sites['Paris']
msc_lnd = ((msc[0]- lnd[0])**2+(msc[1]- lnd[1])**2) **.5
msc_prs = ((msc[0]- prs[0])**2+(msc[1]- prs[1])**2) **.5
lnd_prs = ((lnd[0]- prs[0])**2+(lnd[1]- prs[1])**2) **.5
# TODO здесь заполнение словаря

distances['Moscow'] = {}
distances['Moscow']['London'] = msc_lnd
distances['Moscow']['Paris'] = msc_prs
distances['London'] = {}
distances['London']['Moscow'] = msc_lnd
distances['London']['Paris'] = lnd_prs
distances['Paris'] = {}
distances['Paris']['Moscow'] = msc_lnd
distances['Paris']['London'] = lnd_prs

pprint(distances)




