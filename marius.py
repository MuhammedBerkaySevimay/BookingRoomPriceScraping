import requests
from bs4 import BeautifulSoup
from selenium import webdriver
import json
import pandas as pd
import os
from setuptools import setup
with open("token.txt", "r") as dosya:
    token = dosya.read().strip()

Hotels = []
results = []

checkin = input("Check-in tarihini YYYY-AA-GG olarak giriniz. (Arada - işaretleri dahil): ")
checkout = input("Check-out tarihini YYYY-AA-GG olarak giriniz. (Arada - işaretleri dahil): ")
MariusHotel = {'name' : "Marius Hotel",
    'url' : "https://www.booking.com/hotel/tr/marius.tr.html?aid=304142&label=gen173nr-1FCAEoggI46AdIM1gEaE2IAQGYASi4ARjIAQzYAQHoAQH4AQuIAgGoAgS4AseovK8GwAIB0gIkNjhlNjcxODYtNzcxZC00NGUzLWI3MjEtNzQ2Y2I5OGM2YTcx2AIG4AIB&sid=b7ac61bf62b0cde97d9144f28453d42a&all_sr_blocks=912126303_362556976_2_1_0;checkin="+checkin+";checkout="+checkout+";dest_id=9121263;dest_type=hotel;dist=0;group_adults=2;group_children=0;hapos=1;highlighted_blocks=912126303_362556976_2_1_0;hpos=1;matching_block_id=912126303_362556976_2_1_0;no_rooms=1;req_adults=2;req_children=0;room1=A%2CA;sb_price_type=total;sr_order=popularity;sr_pri_blocks=912126303_362556976_2_1_0__39148;srepoch=1710168701;srpvid=fb87687835c00076;type=total;ucfs=1&selected_currency=EUR#hotelTmpl",
             "rooms" : {'Superior Çift Kişilik veya İki Yataklı Oda' : "Superior Çift Kişilik veya İki Yataklı Oda" ,
                         'Deluxe Çift Kişilik veya İki Yataklı Oda' : "Deluxe Çift Kişilik veya İki Yataklı Oda",
                           'Deluxe Üç Kişilik Oda': "Deluxe Üç Kişilik Oda",
                        'Deluxe Aile odası' : "Deluxe Aile Odası", 
                        'Superior Tek Kişilik Oda' : "Superior Tek Kişilik Oda" , 
                        'Deluxe Tek kişilik oda' : "Deluxe Tek Kişilik Oda"}}
Hotels.append(MariusHotel)

SuraHagiaSophiaHotel = {'name' : "Sura Hagia Sophia Hotel",
    'url' : "https://www.booking.com/hotel/tr/marius.tr.html?aid=304142&label=gen173nr-1FCAEoggI46AdIM1gEaE2IAQGYASi4ARjIAQzYAQHoAQH4AQuIAgGoAgS4AseovK8GwAIB0gIkNjhlNjcxODYtNzcxZC00NGUzLWI3MjEtNzQ2Y2I5OGM2YTcx2AIG4AIB&sid=b7ac61bf62b0cde97d9144f28453d42a&all_sr_blocks=912126303_362556976_2_1_0;checkin="+checkin+";checkout="+checkout+";dest_id=9121263;dest_type=hotel;dist=0;group_adults=2;group_children=0;hapos=1;highlighted_blocks=912126303_362556976_2_1_0;hpos=1;matching_block_id=912126303_362556976_2_1_0;no_rooms=1;req_adults=2;req_children=0;room1=A%2CA;sb_price_type=total;sr_order=popularity;sr_pri_blocks=912126303_362556976_2_1_0__39148;srepoch=1710168701;srpvid=fb87687835c00076;type=total;ucfs=1&selected_currency=EUR#hotelTmpl",
             "rooms" : {'Superior Çift Kişilik veya İki Yataklı Oda' : "Superior Çift Kişilik Oda" ,
                         'Deluxe Çift Kişilik veya İki Yataklı Oda' : "Comfort Çift Kişilik Oda",
                           'Deluxe Üç Kişilik Oda': "Eşleşen Oda Yok",
                        'Deluxe Aile odası' : "Eşleşen Oda Yok", 
                        'Superior Tek Kişilik Oda' : "Eşleşen Oda Yok" , 
                        'Deluxe Tek kişilik oda' : "Eşleşen Oda Yok"}}
Hotels.append(SuraHagiaSophiaHotel)

PierreLotiHotelOldCity = {'name' : "Pierre Loti Hotel Old City",
    'url' : "https://www.booking.com/hotel/tr/la-boutique-pierre-loti.tr.html?aid=304142&label=gen173nr-1FCAEoggI46AdIM1gEaE2IAQGYASi4ARjIAQzYAQHoAQH4AQuIAgGoAgS4AseovK8GwAIB0gIkNjhlNjcxODYtNzcxZC00NGUzLWI3MjEtNzQ2Y2I5OGM2YTcx2AIG4AIB&sid=b7ac61bf62b0cde97d9144f28453d42a&all_sr_blocks=8777901_377995327_2_1_0;checkin="+checkin+";checkout="+checkout+";dest_id=87779;dest_type=hotel;dist=0;group_adults=2;group_children=0;hapos=1;highlighted_blocks=8777901_377995327_2_1_0;hpos=1;matching_block_id=8777901_377995327_2_1_0;no_rooms=1;req_adults=2;req_children=0;room1=A%2CA;sb_price_type=total;sr_order=popularity;sr_pri_blocks=8777901_377995327_2_1_0__32805;srepoch=1710170208;srpvid=6c566b6f1c880038;type=total;ucfs=1&selected_currency=EUR#hotelTmpl",
             "rooms" : {'Superior Çift Kişilik veya İki Yataklı Oda' : "Çift Kişilik veya İki Yataklı Oda" ,
                         'Deluxe Çift Kişilik veya İki Yataklı Oda' : "Superior Çift Kişilik Oda",
                           'Deluxe Üç Kişilik Oda': "Çift Kişilik Oda + 1 İlave Yatak",
                        'Deluxe Aile odası' : "Eşleşen Oda Yok", 
                        'Superior Tek Kişilik Oda' : "Eşleşen Oda Yok" , 
                        'Deluxe Tek kişilik oda' : "Eşleşen Oda Yok"}}
Hotels.append(PierreLotiHotelOldCity)

KateHotel = {'name' : "Kate Hotel",
    'url' : "https://www.booking.com/hotel/tr/kate.tr.html?aid=304142&label=gen173nr-1FCAEoggI46AdIM1gEaFCIAQGYASi4ARjIAQzYAQHoAQH4AQuIAgGoAgS4AqbtvK8GwAIB0gIkMWZjYTRiNGQtNDhlYy00NjYxLWIzNDctNjI5NWQyZmJiOTgw2AIG4AIB&sid=b7ac61bf62b0cde97d9144f28453d42a&all_sr_blocks=958662718_368443198_0_1_0;checkin="+checkin+";checkout="+checkout+";dest_id=9586627;dest_type=hotel;dist=0;group_adults=2;group_children=0;hapos=1;highlighted_blocks=958662718_368443198_0_1_0;hpos=1;matching_block_id=958662718_368443198_0_1_0;no_rooms=1;req_adults=2;req_children=0;room1=A%2CA;sb_price_type=total;sr_order=popularity;sr_pri_blocks=958662718_368443198_0_1_0__48989;srepoch=1710176576;srpvid=ac2477df5a9a0141;type=total;ucfs=1&selected_currency=EUR#hotelTmpl",
             "rooms" : {'Superior Çift Kişilik veya İki Yataklı Oda' : "Eşleşen Oda Yok" ,
                         'Deluxe Çift Kişilik veya İki Yataklı Oda' : "Deluxe Çift Kişilik Oda",
                           'Deluxe Üç Kişilik Oda': "Deluxe Üç Kişilik Oda",
                        'Deluxe Aile odası' : "Lüks Dört Kişilik Oda", 
                        'Superior Tek Kişilik Oda' : "Eşleşen Oda Yok" , 
                        'Deluxe Tek kişilik oda' : "Eşleşen Oda Yok"}}
Hotels.append(KateHotel)

RomanceIstanbulBoutiqueClass = {'name' : "Romance Istanbul Hotel Boutique Class",
    'url' : "https://www.booking.com/hotel/tr/romancehotel.tr.html?aid=304142&label=gen173nr-1FCAEoggI46AdIM1gEaFCIAQGYASi4ARjIAQzYAQHoAQH4AQuIAgGoAgS4AqbtvK8GwAIB0gIkMWZjYTRiNGQtNDhlYy00NjYxLWIzNDctNjI5NWQyZmJiOTgw2AIG4AIB&sid=b7ac61bf62b0cde97d9144f28453d42a&all_sr_blocks=8610802_122791169_2_42_0;checkin="+checkin+";checkout="+checkout+";dest_id=86108;dest_type=hotel;dist=0;group_adults=2;group_children=0;hapos=1;highlighted_blocks=8610802_122791169_2_42_0;hpos=1;matching_block_id=8610802_122791169_2_42_0;no_rooms=1;req_adults=2;req_children=0;room1=A%2CA;sb_price_type=total;sr_order=popularity;sr_pri_blocks=8610802_122791169_2_42_0__103464;srepoch=1710176614;srpvid=d34977eaf6ec0130;type=total;ucfs=1&selected_currency=EUR#hotelTmpl",
             "rooms" : {'Superior Çift Kişilik veya İki Yataklı Oda' : "City Oda" ,
                         'Deluxe Çift Kişilik veya İki Yataklı Oda' : "Deluxe Oda",
                           'Deluxe Üç Kişilik Oda': "Deluxe Üç Kişilik Oda",
                        'Deluxe Aile odası' : "Grand Süit", 
                        'Superior Tek Kişilik Oda' : "Eşleşen Oda Yok" , 
                        'Deluxe Tek kişilik oda' : "Eşleşen Oda Yok"}}
Hotels.append(RomanceIstanbulBoutiqueClass)

LegacyOttomanHotel = {'name' : "Legacy Ottoman Hotel",
    'url' : "https://www.booking.com/hotel/tr/world-park.tr.html?label=gen173nr-1FCAEoggI46AdIM1gEaFCIAQGYASi4ARjIAQzYAQHoAQH4AQuIAgGoAgS4AqbtvK8GwAIB0gIkMWZjYTRiNGQtNDhlYy00NjYxLWIzNDctNjI5NWQyZmJiOTgw2AIG4AIB&sid=b7ac61bf62b0cde97d9144f28453d42a&aid=304142&ucfs=1&arphpl=1&checkin="+checkin+"&checkout="+checkout+"&dest_id=89920&dest_type=hotel&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=1&hapos=1&sr_order=popularity&srpvid=148978e2c6ca033d&srepoch=1710177094&all_sr_blocks=8992026_88796228_2_42_0&highlighted_blocks=8992026_88796228_2_42_0&matching_block_id=8992026_88796228_2_42_0&sr_pri_blocks=8992026_88796228_2_42_0__44307&from_sustainable_property_sr=1&from=searchresults&selected_currency=EUR#hotelTmpl",
             "rooms" : {'Superior Çift Kişilik veya İki Yataklı Oda' : "Superior Oda - Kral Boy Yataklı veya Tek Kişilik İki Yataklı" ,
                         'Deluxe Çift Kişilik veya İki Yataklı Oda' : "Deluxe Oda - Kral Boy Yataklı veya Tek Kişilik İki Yataklı, Şehir Manzaralı",
                           'Deluxe Üç Kişilik Oda': "Eşleşen Oda Yok",
                        'Deluxe Aile odası' : "Eşleşen Oda Yok", 
                        'Superior Tek Kişilik Oda' : "Eşleşen Oda Yok" , 
                        'Deluxe Tek kişilik oda' : "Eşleşen Oda Yok"}}
Hotels.append(LegacyOttomanHotel)

EuroDesignHotel = {'name' : "Euro Design Hotel",
    'url' : "https://www.booking.com/hotel/tr/euro-design.tr.html?label=gen173nr-1FCAEoggI46AdIM1gEaFCIAQGYASi4ARjIAQzYAQHoAQH4AQuIAgGoAgS4AqbtvK8GwAIB0gIkMWZjYTRiNGQtNDhlYy00NjYxLWIzNDctNjI5NWQyZmJiOTgw2AIG4AIB&sid=b7ac61bf62b0cde97d9144f28453d42a&aid=304142&ucfs=1&arphpl=1&checkin="+checkin+"&checkout="+checkout+"&dest_id=5666398&dest_type=hotel&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=1&hapos=1&sr_order=popularity&srpvid=d670794a31f201e1&srepoch=1710177304&all_sr_blocks=566639810_215247332_2_1_0&highlighted_blocks=566639810_215247332_2_1_0&matching_block_id=566639810_215247332_2_1_0&sr_pri_blocks=566639810_215247332_2_1_0__28628&from_sustainable_property_sr=1&from=searchresults&selected_currency=EUR#hotelTmpl",
             "rooms" : {'Superior Çift Kişilik veya İki Yataklı Oda' : "Superior Çift Kişilik veya İki Yataklı Oda" ,
                         'Deluxe Çift Kişilik veya İki Yataklı Oda' : "Deluxe Çift Kişilik veya İki Yataklı Oda",
                           'Deluxe Üç Kişilik Oda': "Superior Üç Kişilik Oda",
                        'Deluxe Aile odası' : "Deluxe Aile Süiti", 
                        'Superior Tek Kişilik Oda' : "Eşleşen Oda Yok" , 
                        'Deluxe Tek kişilik oda' : "Eşleşen Oda Yok"}}
Hotels.append(EuroDesignHotel)

HotelSultaniaBoutiquClass = {'name' : "Hotel Sultania Boutique Class",
    'url' : "https://www.booking.com/hotel/tr/sultania.tr.html?aid=304142&label=gen173nr-1FCAEoggI46AdIM1gEaFCIAQGYASi4ARjIAQzYAQHoAQH4AQuIAgGoAgS4AqbtvK8GwAIB0gIkMWZjYTRiNGQtNDhlYy00NjYxLWIzNDctNjI5NWQyZmJiOTgw2AIG4AIB&sid=b7ac61bf62b0cde97d9144f28453d42a&all_sr_blocks=23879706_265669062_2_42_0;checkin="+checkin+";checkout="+checkout+";dest_id=238797;dest_type=hotel;dist=0;group_adults=2;group_children=0;hapos=1;highlighted_blocks=23879706_265669062_2_42_0;hpos=1;matching_block_id=23879706_265669062_2_42_0;no_rooms=1;req_adults=2;req_children=0;room1=A%2CA;sb_price_type=total;sr_order=popularity;sr_pri_blocks=23879706_265669062_2_42_0__107784;srepoch=1710177766;srpvid=bd857a34b23f00e7;type=total;ucfs=1&selected_currency=EUR#hotelTmpl",
             "rooms" : {'Superior Çift Kişilik veya İki Yataklı Oda' : "Eşleşen Oda Yok" ,
                         'Deluxe Çift Kişilik veya İki Yataklı Oda' : "Deluxe Çift Kişilik veya İki Yataklı Oda",
                           'Deluxe Üç Kişilik Oda': "Çift Kişilik Oda - İlave Yataklı",
                        'Deluxe Aile odası' : "Eşleşen Oda Yok", 
                        'Superior Tek Kişilik Oda' : "Eşleşen Oda Yok" , 
                        'Deluxe Tek kişilik oda' : "Eşleşen Oda Yok"}}
Hotels.append(HotelSultaniaBoutiquClass)

Han1772Hotel = {'name' : "Han 1772 Hotel",
    'url' : "https://www.booking.com/hotel/tr/han-1772-fatih1.tr.html?aid=304142&label=gen173nr-1FCAEoggI46AdIM1gEaFCIAQGYASi4ARjIAQzYAQHoAQH4AQuIAgGoAgS4AqbtvK8GwAIB0gIkMWZjYTRiNGQtNDhlYy00NjYxLWIzNDctNjI5NWQyZmJiOTgw2AIG4AIB&sid=b7ac61bf62b0cde97d9144f28453d42a&all_sr_blocks=862306901_354147836_0_1_0;checkin="+checkin+";checkout="+checkout+";dest_id=8623069;dest_type=hotel;dist=0;group_adults=2;group_children=0;hapos=1;highlighted_blocks=862306901_354147836_0_1_0;hpos=1;matching_block_id=862306901_354147836_0_1_0;no_rooms=1;req_adults=2;req_children=0;room1=A%2CA;sb_price_type=total;sr_order=popularity;sr_pri_blocks=862306901_354147836_0_1_0__38880;srepoch=1710178006;srpvid=427b7aa9d725035b;type=total;ucfs=1&selected_currency=EUR#hotelTmpl",
             "rooms" : {'Superior Çift Kişilik veya İki Yataklı Oda' : "Deluxe Çift Kişilik Oda" ,
                         'Deluxe Çift Kişilik veya İki Yataklı Oda' : "Süit",
                           'Deluxe Üç Kişilik Oda': "Eşleşen Oda Yok",
                        'Deluxe Aile odası' : "Eşleşen Oda Yok", 
                        'Superior Tek Kişilik Oda' : "Eşleşen Oda Yok" , 
                        'Deluxe Tek kişilik oda' : "Standart Tek Kişilik Oda"}}
Hotels.append(Han1772Hotel)

ErboyHotel = {'name' : "Erboy Hotel Istanbul Sirkeci",
    'url' : "https://www.booking.com/hotel/tr/erboyhotel.tr.html?label=gen173nr-1FCAEoggI46AdIM1gEaFCIAQGYASi4ARjIAQzYAQHoAQH4AQuIAgGoAgS4AqbtvK8GwAIB0gIkMWZjYTRiNGQtNDhlYy00NjYxLWIzNDctNjI5NWQyZmJiOTgw2AIG4AIB&sid=b7ac61bf62b0cde97d9144f28453d42a&aid=304142&ucfs=1&arphpl=1&checkin="+checkin+"&checkout="+checkout+"&dest_id=86298&dest_type=hotel&group_adults=2&req_adults=2&no_rooms=1&group_children=0&req_children=0&hpos=1&hapos=1&sr_order=popularity&srpvid=6fe37d692e9701db&srepoch=1710179412&all_sr_blocks=8629832_338503319_2_41_0&highlighted_blocks=8629832_338503319_2_41_0&matching_block_id=8629832_338503319_2_41_0&sr_pri_blocks=8629832_338503319_2_41_0__39877&from_sustainable_property_sr=1&from=searchresults&selected_currency=EUR#hotelTmpl",
             "rooms" : {'Superior Çift Kişilik veya İki Yataklı Oda' : "Standart Çift Kişilik veya İki Yataklı Oda" ,
                         'Deluxe Çift Kişilik veya İki Yataklı Oda' : "Eşleşen Oda Yok",
                           'Deluxe Üç Kişilik Oda': "Standart Üç Kişilik Oda",
                        'Deluxe Aile odası' : "Standart Aile Odası", 
                        'Superior Tek Kişilik Oda' : "Eşleşen Oda Yok" , 
                        'Deluxe Tek kişilik oda' : "Eşleşen Oda Yok"}}
Hotels.append(ErboyHotel)

HotelYasmakSultan = {'name' : "Hotel Yasmak Sultan",
    'url' : "https://www.booking.com/hotel/tr/yasmak.tr.html?aid=304142&label=gen173nr-1FCAEoggI46AdIM1gEaFCIAQGYASi4ARjIAQzYAQHoAQH4AQuIAgGoAgS4AqbtvK8GwAIB0gIkMWZjYTRiNGQtNDhlYy00NjYxLWIzNDctNjI5NWQyZmJiOTgw2AIG4AIB&sid=b7ac61bf62b0cde97d9144f28453d42a&all_sr_blocks=8608002_88795920_2_41_0;checkin="+checkin+";checkout="+checkout+";dest_id=86080;dest_type=hotel;dist=0;group_adults=2;group_children=0;hapos=1;highlighted_blocks=8608002_88795920_2_41_0;hpos=1;matching_block_id=8608002_88795920_2_41_0;no_rooms=1;req_adults=2;req_children=0;room1=A%2CA;sb_price_type=total;sr_order=popularity;sr_pri_blocks=8608002_88795920_2_41_0__103421;srepoch=1710179610;srpvid=178c7dcc1cb2001c;type=total;ucfs=1&selected_currency=EUR#hotelTmpl",
             "rooms" : {'Superior Çift Kişilik veya İki Yataklı Oda' : "Çift Kişilik veya İki Yataklı Oda" ,
                         'Deluxe Çift Kişilik veya İki Yataklı Oda' : "Deluxe Oda",
                           'Deluxe Üç Kişilik Oda': "Çift Kişilik veya İki Yataklı Oda + İlave Yatak",
                        'Deluxe Aile odası' : "Aile Odası", 
                        'Superior Tek Kişilik Oda' : "Eşleşen Oda Yok" , 
                        'Deluxe Tek kişilik oda' : "Eşleşen Oda Yok"}}
Hotels.append(HotelYasmakSultan)

SirkeciMansion = {'name' : "Sirkeci Mansion",
    'url' : "https://www.booking.com/hotel/tr/sirkeci-konak.tr.html?aid=304142&label=gen173nr-1FCAEoggI46AdIM1gEaFCIAQGYASi4ARjIAQzYAQHoAQH4AQuIAgGoAgS4AqbtvK8GwAIB0gIkMWZjYTRiNGQtNDhlYy00NjYxLWIzNDctNjI5NWQyZmJiOTgw2AIG4AIB&sid=b7ac61bf62b0cde97d9144f28453d42a&all_sr_blocks=8785102_358530670_0_1_0;checkin="+checkin+";checkout="+checkout+";dest_id=87851;dest_type=hotel;dist=0;group_adults=2;group_children=0;hapos=1;highlighted_blocks=8785102_358530670_0_1_0;hpos=1;matching_block_id=8785102_358530670_0_1_0;no_rooms=1;req_adults=2;req_children=0;room1=A%2CA;sb_price_type=total;sr_order=popularity;sr_pri_blocks=8785102_358530670_0_1_0__50490;srepoch=1710179768;srpvid=3c397e1d99110231;type=total;ucfs=1&selected_currency=EUR#hotelTmpl",
             "rooms" : {'Superior Çift Kişilik veya İki Yataklı Oda' : "Çift Kişilik Oda" ,
                         'Deluxe Çift Kişilik veya İki Yataklı Oda' : "Superior Çift Kişilik Oda",
                           'Deluxe Üç Kişilik Oda': "Standart Üç Kişilik Oda",
                        'Deluxe Aile odası' : "Aile Odası - Bağlantılı", 
                        'Superior Tek Kişilik Oda' : "Eşleşen Oda Yok" , 
                        'Deluxe Tek kişilik oda' : "Tek Kişilik Oda"}}
Hotels.append(SirkeciMansion)

NeorionHotelSpecialClass = {'name' : "Neorion Hotel - Special Class",
    'url' : "https://www.booking.com/hotel/tr/neorion-sirkeci-group.tr.html?aid=304142&label=gen173nr-1FCAEoggI46AdIM1gEaFCIAQGYASi4ARjIAQzYAQHoAQH4AQuIAgGoAgS4AqbtvK8GwAIB0gIkMWZjYTRiNGQtNDhlYy00NjYxLWIzNDctNjI5NWQyZmJiOTgw2AIG4AIB&sid=b7ac61bf62b0cde97d9144f28453d42a&all_sr_blocks=30907402_164083360_0_1_0;checkin="+checkin+";checkout="+checkout+";dest_id=309074;dest_type=hotel;dist=0;group_adults=2;group_children=0;hapos=1;highlighted_blocks=30907402_164083360_0_1_0;hpos=1;matching_block_id=30907402_164083360_0_1_0;no_rooms=1;req_adults=2;req_children=0;room1=A%2CA;sb_price_type=total;sr_order=popularity;sr_pri_blocks=30907402_164083360_0_1_0__31065;srepoch=1710179965;srpvid=0a477e7df6a90318;type=total;ucfs=1&selected_currency=EUR#hotelTmpl",
             "rooms" : {'Superior Çift Kişilik veya İki Yataklı Oda' : "Eşleşen Oda Yok" ,
                         'Deluxe Çift Kişilik veya İki Yataklı Oda' : "Çift Kişilik veya İki Yataklı Oda",
                           'Deluxe Üç Kişilik Oda': "Üç Kişilik Oda",
                        'Deluxe Aile odası' : "Eşleşen Oda Yok", 
                        'Superior Tek Kişilik Oda' : "Eşleşen Oda Yok" , 
                        'Deluxe Tek kişilik oda' : "Tek Kişilik Oda"}}
Hotels.append(NeorionHotelSpecialClass)

LevniHotel = {'name' : "Levni Hotel & SPA - Special Category",
    'url' : "https://www.booking.com/hotel/tr/levni.tr.html?aid=304142&label=gen173nr-1FCAEoggI46AdIM1gEaFCIAQGYASi4ARjIAQzYAQHoAQH4AQuIAgGoAgS4AqbtvK8GwAIB0gIkMWZjYTRiNGQtNDhlYy00NjYxLWIzNDctNjI5NWQyZmJiOTgw2AIG4AIB&sid=b7ac61bf62b0cde97d9144f28453d42a&all_sr_blocks=26845601_89969199_0_1_0;checkin="+checkin+";checkout="+checkout+";dest_id=268456;dest_type=hotel;dist=0;group_adults=2;group_children=0;hapos=1;highlighted_blocks=26845601_89969199_0_1_0;hpos=1;matching_block_id=26845601_89969199_0_1_0;no_rooms=1;req_adults=2;req_children=0;room1=A%2CA;sb_price_type=total;sr_order=popularity;sr_pri_blocks=26845601_89969199_0_1_0__53460;srepoch=1710180292;srpvid=0b987f210a620360;type=total;ucfs=1&selected_currency=EUR#hotelTmpl",
             "rooms" : {'Superior Çift Kişilik veya İki Yataklı Oda' : "Standart Çift Kişilik veya İki Yataklı Oda" ,
                         'Deluxe Çift Kişilik veya İki Yataklı Oda' : "Deluxe Çift Kişilik veya İki Yataklı Oda",
                           'Deluxe Üç Kişilik Oda': "Standart Üç Kişilik Oda",
                        'Deluxe Aile odası' : "Aile Odası", 
                        'Superior Tek Kişilik Oda' : "Eşleşen Oda Yok" , 
                        'Deluxe Tek kişilik oda' : "Eşleşen Oda Yok"}}
Hotels.append(LevniHotel)

LivroHotel = {'name' : "Livro Hotel",
    'url' : "https://www.booking.com/hotel/tr/livro.tr.html?aid=304142&label=gen173nr-1FCAEoggI46AdIM1gEaFCIAQGYASi4ARjIAQzYAQHoAQH4AQuIAgGoAgS4AqbtvK8GwAIB0gIkMWZjYTRiNGQtNDhlYy00NjYxLWIzNDctNjI5NWQyZmJiOTgw2AIG4AIB&sid=b7ac61bf62b0cde97d9144f28453d42a&all_sr_blocks=920962801_363698143_2_1_0;checkin="+checkin+";checkout="+checkout+";dest_id=9209628;dest_type=hotel;dist=0;group_adults=2;group_children=0;hapos=1;highlighted_blocks=920962801_363698143_2_1_0;hpos=1;matching_block_id=920962801_363698143_2_1_0;no_rooms=1;req_adults=2;req_children=0;room1=A%2CA;sb_price_type=total;sr_order=popularity;sr_pri_blocks=920962801_363698143_2_1_0__43740;srepoch=1710180504;srpvid=5dbb7f8a695c018c;type=total;ucfs=1&selected_currency=EUR#hotelTmpl",
             "rooms" : {'Superior Çift Kişilik veya İki Yataklı Oda' : "Standart Çift Kişilik Oda" ,
                         'Deluxe Çift Kişilik veya İki Yataklı Oda' : "Superior Çift Kişilik veya İki Yataklı Oda",
                           'Deluxe Üç Kişilik Oda': "Eşleşen Oda Yok",
                        'Deluxe Aile odası' : "Deluxe Aile Odası", 
                        'Superior Tek Kişilik Oda' : "Eşleşen Oda Yok" , 
                        'Deluxe Tek kişilik oda' : "Eşleşen Oda Yok"}}
Hotels.append(LivroHotel)

# mercure hotel bookingde bulunamadi.
# MercureHotel = {'name' : "Mercure Istanbul Sirkeci",
#     'url' : "https://www.booking.com/hotel/tr/livro.tr.html?aid=304142&label=gen173nr-1FCAEoggI46AdIM1gEaFCIAQGYASi4ARjIAQzYAQHoAQH4AQuIAgGoAgS4AqbtvK8GwAIB0gIkMWZjYTRiNGQtNDhlYy00NjYxLWIzNDctNjI5NWQyZmJiOTgw2AIG4AIB&sid=b7ac61bf62b0cde97d9144f28453d42a&all_sr_blocks=920962801_363698143_2_1_0;checkin="+checkin+";checkout="+checkout+";dest_id=9209628;dest_type=hotel;dist=0;group_adults=2;group_children=0;hapos=1;highlighted_blocks=920962801_363698143_2_1_0;hpos=1;matching_block_id=920962801_363698143_2_1_0;no_rooms=1;req_adults=2;req_children=0;room1=A%2CA;sb_price_type=total;sr_order=popularity;sr_pri_blocks=920962801_363698143_2_1_0__43740;srepoch=1710180504;srpvid=5dbb7f8a695c018c;type=total;ucfs=1&selected_currency=EUR#hotelTmpl",
#              "rooms" : {'Superior Çift Kişilik veya İki Yataklı Oda' : "Standart Çift Kişilik Oda" ,
#                          'Deluxe Çift Kişilik veya İki Yataklı Oda' : "Superior Çift Kişilik veya İki Yataklı Oda",
#                            'Deluxe Üç Kişilik Oda': "Eşleşen Oda Yok",
#                         'Deluxe Aile odası' : "Deluxe Aile Odası", 
#                         'Superior Tek Kişilik Oda' : "Eşleşen Oda Yok" , 
#                         'Deluxe Tek kişilik oda' : "Eşleşen Oda Yok"}}
# Hotels.append(MercurHotel)

MestHotel = {'name' : "Mest Hotel İstanbul Sirkeci",
    'url' : "https://www.booking.com/hotel/tr/mest.tr.html?aid=304142&label=gen173nr-1FCAEoggI46AdIM1gEaFCIAQGYASi4ARjIAQzYAQHoAQH4AQuIAgGoAgS4AqbtvK8GwAIB0gIkMWZjYTRiNGQtNDhlYy00NjYxLWIzNDctNjI5NWQyZmJiOTgw2AIG4AIB&sid=b7ac61bf62b0cde97d9144f28453d42a&all_sr_blocks=754151504_332091114_2_1_0;checkin="+checkin+";checkout="+checkout+";dest_id=7541515;dest_type=hotel;dist=0;group_adults=2;group_children=0;hapos=1;highlighted_blocks=754151504_332091114_2_1_0;hpos=1;matching_block_id=754151504_332091114_2_1_0;no_rooms=1;req_adults=2;req_children=0;room1=A%2CA;sb_price_type=total;sr_order=popularity;sr_pri_blocks=754151504_332091114_2_1_0__45587;srepoch=1710180863;srpvid=20ce8036c49900f0;type=total;ucfs=1&selected_currency=EUR#hotelTmpl",
             "rooms" : {'Superior Çift Kişilik veya İki Yataklı Oda' : "Ekonomik Çift Kişilik Oda" ,
                         'Deluxe Çift Kişilik veya İki Yataklı Oda' : "Superior Çift Kişilik veya İki Yataklı Oda",
                           'Deluxe Üç Kişilik Oda': "Eşleşen Oda Yok",
                        'Deluxe Aile odası' : "Eşleşen Oda Yok", 
                        'Superior Tek Kişilik Oda' : "Eşleşen Oda Yok" , 
                        'Deluxe Tek kişilik oda' : "Eşleşen Oda Yok"}}
Hotels.append(MestHotel)

OrientBank = {'name' : "Orientbank Hotel Istanbul, Autograph Collection",
    'url' : "https://www.booking.com/hotel/tr/orientbank-istanbul-autograph-collection.tr.html?aid=304142&label=gen173nr-1FCAEoggI46AdIM1gEaFCIAQGYASi4ARjIAQzYAQHoAQH4AQuIAgGoAgS4AqbtvK8GwAIB0gIkMWZjYTRiNGQtNDhlYy00NjYxLWIzNDctNjI5NWQyZmJiOTgw2AIG4AIB&sid=b7ac61bf62b0cde97d9144f28453d42a&all_sr_blocks=718095801_301281763_0_2_0;checkin="+checkin+";checkout="+checkout+";dest_id=7180958;dest_type=hotel;dist=0;group_adults=2;group_children=0;hapos=1;highlighted_blocks=718095801_301281763_0_2_0;hpos=1;matching_block_id=718095801_301281763_0_2_0;no_rooms=1;req_adults=2;req_children=0;room1=A%2CA;sb_price_type=total;sr_order=popularity;sr_pri_blocks=718095801_301281763_0_2_0__77112;srepoch=1710181766;srpvid=1ef0810fe12403fa;type=total;ucfs=1&selected_currency=EUR#hotelTmpl",
             "rooms" : {'Superior Çift Kişilik veya İki Yataklı Oda' : "Eşleşen Oda Yok" ,
                         'Deluxe Çift Kişilik veya İki Yataklı Oda' : "Deluxe King Oda",
                           'Deluxe Üç Kişilik Oda': "Eşleşen Oda Yok",
                        'Deluxe Aile odası' : "Eşleşen Oda Yok", 
                        'Superior Tek Kişilik Oda' : "Eşleşen Oda Yok" , 
                        'Deluxe Tek kişilik oda' : "Eşleşen Oda Yok"}}
Hotels.append(OrientBank)



CityHall  = {'name' : "City Hall Hotel",
    'url' : "https://www.booking.com/hotel/tr/city-hall.tr.html?aid=304142&label=gen173nr-1FCAEoggI46AdIM1gEaFCIAQGYASi4ARjIAQzYAQHoAQH4AQuIAgGoAgS4Aoi9wa8GwAIB0gIkN2Q1ZGI0NDItNjg4Yi00OTY5LWJiZTUtOTMyZDUzYWZlNzg42AIG4AIB&sid=b7ac61bf62b0cde97d9144f28453d42a&all_sr_blocks=571684602_330685109_2_1_0;checkin="+checkin+";checkout="+checkout+";dest_id=5716846;dest_type=hotel;dist=0;group_adults=2;group_children=0;hapos=1;highlighted_blocks=571684602_330685109_2_1_0;hpos=1;matching_block_id=571684602_330685109_2_1_0;no_rooms=1;req_adults=2;req_children=0;room1=A%2CA;sb_price_type=total;sr_order=popularity;sr_pri_blocks=571684602_330685109_2_1_0__30139;srepoch=1710252121;srpvid=713d62ab699e02c6;type=total;ucfs=1&selected_currency=EUR#hotelTmpl",
             "rooms" : {'Superior Çift Kişilik veya İki Yataklı Oda' : "Standart Çift Kişilik Oda" ,
                         'Deluxe Çift Kişilik veya İki Yataklı Oda' : "Eşleşen Oda Yok",
                           'Deluxe Üç Kişilik Oda': "Eşleşen Oda Yok",
                        'Deluxe Aile odası' : "Eşleşen Oda Yok", 
                        'Superior Tek Kişilik Oda' : "Standart Tek Kişilik Oda" , 
                        'Deluxe Tek kişilik oda' : "Eşleşen Oda Yok"}}
Hotels.append(CityHall)

HennaHotel  = {'name' : "Henna Hotel",
    'url' : "https://www.booking.com/hotel/tr/henna-istanbul.tr.html?aid=304142&label=gen173nr-1FCAEoggI46AdIM1gEaFCIAQGYASi4ARjIAQzYAQHoAQH4AQuIAgGoAgS4Aoi9wa8GwAIB0gIkN2Q1ZGI0NDItNjg4Yi00OTY5LWJiZTUtOTMyZDUzYWZlNzg42AIG4AIB&sid=b7ac61bf62b0cde97d9144f28453d42a&all_sr_blocks=715971407_383305581_0_41_0;checkin="+checkin+";checkout="+checkout+";dest_id=-755070;dest_type=city;dist=0;group_adults=2;group_children=0;hapos=1;highlighted_blocks=715971407_383305581_0_41_0;hpos=1;matching_block_id=715971407_383305581_0_41_0;no_rooms=1;req_adults=2;req_children=0;room1=A%2CA;sb_price_type=total;sr_order=popularity;sr_pri_blocks=715971407_383305581_0_41_0__43862;srepoch=1710254621;srpvid=09ae678d4fe4001d;type=total;ucfs=1&selected_currency=EUR#hotelTmpl",
             "rooms" : {'Superior Çift Kişilik veya İki Yataklı Oda' : "Premier Çift Kişilik Oda" ,
                         'Deluxe Çift Kişilik veya İki Yataklı Oda' : "Superior Çift Kişilik Oda",
                           'Deluxe Üç Kişilik Oda': "Premier Üç Kişilik Oda",
                        'Deluxe Aile odası' : "Eşleşen Oda Yok", 
                        'Superior Tek Kişilik Oda' : "Tek Kişilik Premier Oda" , 
                        'Deluxe Tek kişilik oda' : "Eşleşen Oda Yok"}}
Hotels.append(HennaHotel)

Weingart  = {'name' : "Weingart İstanbul",
    'url' : "https://www.booking.com/hotel/tr/weingart.tr.html?aid=304142&label=gen173nr-1FCAEoggI46AdIM1gEaFCIAQGYASi4ARjIAQzYAQHoAQH4AQuIAgGoAgS4Aoi9wa8GwAIB0gIkN2Q1ZGI0NDItNjg4Yi00OTY5LWJiZTUtOTMyZDUzYWZlNzg42AIG4AIB&sid=b7ac61bf62b0cde97d9144f28453d42a&all_sr_blocks=715134508_298701498_2_1_0;checkin="+checkin+";checkout="+checkout+";dest_id=7151345;dest_type=hotel;dist=0;group_adults=2;group_children=0;hapos=1;highlighted_blocks=715134508_298701498_2_1_0;hpos=1;matching_block_id=715134508_298701498_2_1_0;no_rooms=1;req_adults=2;req_children=0;room1=A%2CA;sb_price_type=total;sr_order=popularity;sr_pri_blocks=715134508_298701498_2_1_0__36234;srepoch=1710253283;srpvid=2b2264f0e5530075;type=total;ucfs=1&selected_currency=EUR#hotelTmpl",
             "rooms" : {'Superior Çift Kişilik veya İki Yataklı Oda' : "Ekonomik Çift Kişilik veya İki Yataklı Oda" ,
                         'Deluxe Çift Kişilik veya İki Yataklı Oda' : "Superior Çift Kişilik veya İki Yataklı Oda",
                           'Deluxe Üç Kişilik Oda': "Standart Üç Kişilik Oda",
                        'Deluxe Aile odası' : "Bağlantılı İki Çift Kişilik Oda", 
                        'Superior Tek Kişilik Oda' : "Tek Kişilik Ekonomik Oda" , 
                        'Deluxe Tek kişilik oda' : "Standart Tek Kişilik Oda"}}
Hotels.append(Weingart)

TheGalata  = {'name' : "The Galata Istanbul Hotel MGallery",
    'url' : "https://www.booking.com/hotel/tr/galata-istanbul-mgallery-by-sofitel.tr.html?aid=304142&label=gen173nr-1FCAEoggI46AdIM1gEaFCIAQGYASi4ARjIAQzYAQHoAQH4AQuIAgGoAgS4Aoi9wa8GwAIB0gIkN2Q1ZGI0NDItNjg4Yi00OTY5LWJiZTUtOTMyZDUzYWZlNzg42AIG4AIB&sid=b7ac61bf62b0cde97d9144f28453d42a&all_sr_blocks=263687703_105333432_2_2_0;checkin="+checkin+";checkout="+checkout+";dest_id=2636877;dest_type=hotel;dist=0;group_adults=2;group_children=0;hapos=1;highlighted_blocks=263687703_105333432_2_2_0;hpos=1;matching_block_id=263687703_105333432_2_2_0;no_rooms=1;req_adults=2;req_children=0;room1=A%2CA;sb_price_type=total;sr_order=popularity;sr_pri_blocks=263687703_105333432_2_2_0__40824;srepoch=1710253548;srpvid=732c6575bdaf041e;type=total;ucfs=1&selected_currency=EUR#hotelTmpl",
             "rooms" : {'Superior Çift Kişilik veya İki Yataklı Oda' : "Klasik King Oda" ,
                         'Deluxe Çift Kişilik veya İki Yataklı Oda' : "Junior King Süit",
                           'Deluxe Üç Kişilik Oda': "Eşleşen Oda Yok",
                        'Deluxe Aile odası' : "Eşleşen Oda Yok", 
                        'Superior Tek Kişilik Oda' : "Eşleşen Oda Yok" , 
                        'Deluxe Tek kişilik oda' : "Eşleşen Oda Yok"}}
Hotels.append(TheGalata)

options = webdriver.ChromeOptions()
options.add_argument("--headless")
options.add_argument("--log-level=3")
driver = webdriver.Chrome(options=options)
current_directory = os.getcwd()

for hotel in Hotels:
    result = {'Name' : hotel['name']}
    result1 = {'Name' : hotel['name'] + " Oda isimleri"}
    print(result['Name'])
    payload = {'api_key': token, 'url': hotel['url'] }
    r = requests.get('http://api.scraperapi.com', params=payload)
    soup = BeautifulSoup(r.text,'html.parser')
    with open("main.html", "w", encoding="utf-8") as dosya:
        dosya.write(str(soup))
    
    
    dosya_yolu = 'file://' + current_directory + '/main.html'

    try:
      driver.get(dosya_yolu)  
      rooms = driver.execute_script("return window.booking.env.b_rooms_available_and_soldout")
      roomdata = json.dumps(rooms)
      roomdatas = json.loads(roomdata)
    
      for key,value in hotel["rooms"].items():
          for room in roomdatas:
              if value == room['b_name']:

                  try:
                      
                      for block in room['b_blocks']:
                          if block['b_cancellation_type'] == "free_cancellation":
                              result[str(key) + " (İade Edilebilir)"] = block['b_price']
                              result1[str(key) + " (İade Edilebilir)"] = hotel['rooms'][key]
                          else:
                              result[key] = block['b_price']
                              result1[key] = hotel['rooms'][key]

                      if str(key) + " (İade Edilebilir)" not in result:
                          result[str(key) + " (İade Edilebilir)"] = "Eşleşen Oda Yok"
                          result1[str(key) + " (İade Edilebilir)"] = "Eşleşen Oda Yok"
                      
                      if key not in result:
                          result[key] = "Eşleşen Oda Yok"
                          result1[key] = "Eşleşen Oda Yok"
                  except Exception as e:
                      print(e)
                      result[key] = room['b_blocks'][0]['b_price']
                      result1[key] = hotel['rooms'][key]
                  break
          else:
              if value != "Eşleşen Oda Yok":
                result[key] = "Seçilen tarihlerde bu oda müsait değil"
                result1[key] = hotel['rooms'][key]
                result[str(key) + " (İade Edilebilir)"] = "Seçilen tarihlerde bu oda müsait değil"
                result1[str(key) + " (İade Edilebilir)"] = hotel['rooms'][key]
              else:
                result[key] = value
                result1[key] = value
                result[str(key) + " (İade Edilebilir)"] = value
                result1[str(key) + " (İade Edilebilir)"] = value

        
      results.append(result)
    except Exception as e:
        print(e)
    if hotel['name'] != "Marius Hotel":
        results.append(result1)
    


writer = pd.ExcelWriter('veriler.xlsx') 
df = pd.DataFrame(results,columns=['Name','Superior Çift Kişilik veya İki Yataklı Oda','Superior Çift Kişilik veya İki Yataklı Oda (İade Edilebilir)','Deluxe Çift Kişilik veya İki Yataklı Oda','Deluxe Çift Kişilik veya İki Yataklı Oda (İade Edilebilir)',
                                   'Deluxe Üç Kişilik Oda','Deluxe Üç Kişilik Oda (İade Edilebilir)','Deluxe Aile odası','Deluxe Aile odası (İade Edilebilir)',
                                   'Superior Tek Kişilik Oda', 'Superior Tek Kişilik Oda (İade Edilebilir)' , 'Deluxe Tek kişilik oda' , 'Deluxe Tek kişilik oda (İade Edilebilir)'])
    


df.to_excel(writer, sheet_name='sheetName', index=False, na_rep='NaN')

for column in df:
    column_length = max(df[column].astype(str).map(len).max(), len(column))
    col_idx = df.columns.get_loc(column)
    writer.sheets['sheetName'].set_column(col_idx, col_idx, column_length)

writer.save()

        
        


