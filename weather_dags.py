import os
import json
import logging
from datetime import datetime
from pathlib import Path


import requests
import pandas as pd
from airflow import DAG
from airflow.operators.python import PythonOperator

ACCESS_KEY = 'demo_yandex_weather_api_key_ca6d09349ba0'
REQUERST_URL = 'https://api.weather.yandex.ru/graphql/query'
REQUEST_HEADERS = {
    "X-Yandex-Weather-Key": ACCESS_KEY 
}
HOME_PATH = Path('/home/dmymrin/weather/')

if not HOME_PATH.exists:
    HOME_PATH.mkdir(parents=True)
    

WEATHER_FORECAST_QUERY = """{
  Adygeysk: weatherByPoint(request: {lat: 44.878414, lon: 39.190289}) {
    ...WeatherData
  }
  Maykop: weatherByPoint(request: {lat: 44.6098268, lon: 40.1006606}) {
    ...WeatherData
  }
  GornoAltaysk: weatherByPoint(request: {lat: 51.9581028, lon: 85.9603235}) {
    ...WeatherData
  }
  Aleysk: weatherByPoint(request: {lat: 52.4922513, lon: 82.7793606}) {
    ...WeatherData
  }
  Barnaul: weatherByPoint(request: {lat: 53.3479968, lon: 83.7798064}) {
    ...WeatherData
  }
  Belokuriha: weatherByPoint(request: {lat: 51.996152, lon: 84.9839604}) {
    ...WeatherData
  }
  Biysk: weatherByPoint(request: {lat: 52.5393864, lon: 85.2138453}) {
    ...WeatherData
  }
  Gornyak: weatherByPoint(request: {lat: 50.9979622, lon: 81.4643358}) {
    ...WeatherData
  }
  Zarinsk: weatherByPoint(request: {lat: 53.7063476, lon: 84.9315081}) {
    ...WeatherData
  }
  Zmeinogorsk: weatherByPoint(request: {lat: 51.1581094, lon: 82.1872547}) {
    ...WeatherData
  }
  KamenNaObi: weatherByPoint(request: {lat: 53.7913974, lon: 81.3545053}) {
    ...WeatherData
  }
  Novoaltaysk: weatherByPoint(request: {lat: 53.4119759, lon: 83.9311069}) {
    ...WeatherData
  }
  Rubtsovsk: weatherByPoint(request: {lat: 51.5012067, lon: 81.2078695}) {
    ...WeatherData
  }
  Slavgorod: weatherByPoint(request: {lat: 52.999463, lon: 78.6459232}) {
    ...WeatherData
  }
  Yarovoe: weatherByPoint(request: {lat: 52.9252146, lon: 78.5729775}) {
    ...WeatherData
  }
  Belogorsk: weatherByPoint(request: {lat: 50.9213415, lon: 128.4739471}) {
    ...WeatherData
  }
  Blagoveschensk: weatherByPoint(request: {lat: 50.290659, lon: 127.527198}) {
    ...WeatherData
  }
  Zavitinsk: weatherByPoint(request: {lat: 50.1064111, lon: 129.4391813}) {
    ...WeatherData
  }
  Zeya: weatherByPoint(request: {lat: 53.7340088, lon: 127.265787}) {
    ...WeatherData
  }
  Raychihinsk: weatherByPoint(request: {lat: 49.7941615, lon: 129.4112492}) {
    ...WeatherData
  }
  Svobodnyy: weatherByPoint(request: {lat: 51.3614103, lon: 128.1219729}) {
    ...WeatherData
  }
  Skovorodino: weatherByPoint(request: {lat: 53.9871095, lon: 123.9437205}) {
    ...WeatherData
  }
  Tynda: weatherByPoint(request: {lat: 55.1546441, lon: 124.7468904}) {
    ...WeatherData
  }
  Tsiolkovskiy: weatherByPoint(request: {lat: 51.762481, lon: 128.1219846}) {
    ...WeatherData
  }
  Shimanovsk: weatherByPoint(request: {lat: 52.0051886, lon: 127.7005458}) {
    ...WeatherData
  }
  Arhangelsk: weatherByPoint(request: {lat: 64.5394289, lon: 40.5169606}) {
    ...WeatherData
  }
  Velsk: weatherByPoint(request: {lat: 61.066, lon: 42.1032789}) {
    ...WeatherData
  }
  Kargopol: weatherByPoint(request: {lat: 61.5009724, lon: 38.9636966}) {
    ...WeatherData
  }
  Koryazhma: weatherByPoint(request: {lat: 61.2885948, lon: 47.1003015}) {
    ...WeatherData
  }
  Kotlas: weatherByPoint(request: {lat: 61.2528972, lon: 46.633242}) {
    ...WeatherData
  }
  Mezen: weatherByPoint(request: {lat: 65.8398078, lon: 44.2532273}) {
    ...WeatherData
  }
  Mirnyy: weatherByPoint(request: {lat: 62.7645265, lon: 40.3360076}) {
    ...WeatherData
  }
  Novodvinsk: weatherByPoint(request: {lat: 64.4136851, lon: 40.8208143}) {
    ...WeatherData
  }
  Nyandoma: weatherByPoint(request: {lat: 61.6654674, lon: 40.2062947}) {
    ...WeatherData
  }
  Onega: weatherByPoint(request: {lat: 63.9162928, lon: 38.0805031}) {
    ...WeatherData
  }
  Severodvinsk: weatherByPoint(request: {lat: 64.5625385, lon: 39.8180934}) {
    ...WeatherData
  }
  Solvychegodsk: weatherByPoint(request: {lat: 61.3319616, lon: 46.920441}) {
    ...WeatherData
  }
  Shenkursk: weatherByPoint(request: {lat: 62.1057272, lon: 42.8996973}) {
    ...WeatherData
  }
  Astrahan: weatherByPoint(request: {lat: 46.3655652, lon: 48.0559236}) {
    ...WeatherData
  }
  Ahtubinsk: weatherByPoint(request: {lat: 48.2752034, lon: 46.1906462}) {
    ...WeatherData
  }
  Znamensk: weatherByPoint(request: {lat: 48.5866291, lon: 45.7368019}) {
    ...WeatherData
  }
  Kamyzyak: weatherByPoint(request: {lat: 46.110579, lon: 48.07333}) {
    ...WeatherData
  }
  Narimanov: weatherByPoint(request: {lat: 46.6916565, lon: 47.8502476}) {
    ...WeatherData
  }
  Harabali: weatherByPoint(request: {lat: 47.408999, lon: 47.2525345}) {
    ...WeatherData
  }
  Agidel: weatherByPoint(request: {lat: 55.8999056, lon: 53.9220144}) {
    ...WeatherData
  }
  Baymak: weatherByPoint(request: {lat: 52.5912896, lon: 58.3110998}) {
    ...WeatherData
  }
  Belebey: weatherByPoint(request: {lat: 54.1034582, lon: 54.1113129}) {
    ...WeatherData
  }
  Beloretsk: weatherByPoint(request: {lat: 53.9676488, lon: 58.4100419}) {
    ...WeatherData
  }
  Birsk: weatherByPoint(request: {lat: 55.4155753, lon: 55.5582214}) {
    ...WeatherData
  }
  Blagoveschensk_2: weatherByPoint(request: {lat: 55.0499867, lon: 55.9553186}) {
    ...WeatherData
  }
  Davlekanovo: weatherByPoint(request: {lat: 54.2226707, lon: 55.0312373}) {
    ...WeatherData
  }
  Dyurtyuli: weatherByPoint(request: {lat: 55.4848318, lon: 54.8524765}) {
    ...WeatherData
  }
  Ishimbay: weatherByPoint(request: {lat: 53.4545764, lon: 56.0438751}) {
    ...WeatherData
  }
  Kumertau: weatherByPoint(request: {lat: 52.7564939, lon: 55.7970197}) {
    ...WeatherData
  }
  Mezhgore: weatherByPoint(request: {lat: 54.2397689, lon: 57.9614547}) {
    ...WeatherData
  }
  Meleuz: weatherByPoint(request: {lat: 52.9589532, lon: 55.9282838}) {
    ...WeatherData
  }
  Neftekamsk: weatherByPoint(request: {lat: 56.088377, lon: 54.2483061}) {
    ...WeatherData
  }
  Oktyabrskiy: weatherByPoint(request: {lat: 54.4815311, lon: 53.4655972}) {
    ...WeatherData
  }
  Salavat: weatherByPoint(request: {lat: 53.3616974, lon: 55.9245224}) {
    ...WeatherData
  }
  Sibay: weatherByPoint(request: {lat: 52.7204651, lon: 58.6663783}) {
    ...WeatherData
  }
  Sterlitamak: weatherByPoint(request: {lat: 53.6300864, lon: 55.9317089}) {
    ...WeatherData
  }
  Tuymazy: weatherByPoint(request: {lat: 54.5999224, lon: 53.6950623}) {
    ...WeatherData
  }
  Ufa: weatherByPoint(request: {lat: 54.734944, lon: 55.9578468}) {
    ...WeatherData
  }
  Uchaly: weatherByPoint(request: {lat: 54.3067375, lon: 59.4125461}) {
    ...WeatherData
  }
  Yanaul: weatherByPoint(request: {lat: 56.2650146, lon: 54.929907}) {
    ...WeatherData
  }
  Alekseevka: weatherByPoint(request: {lat: 50.6299647, lon: 38.6880342}) {
    ...WeatherData
  }
  Belgorod: weatherByPoint(request: {lat: 50.5976472, lon: 36.5856652}) {
    ...WeatherData
  }
  Biryuch: weatherByPoint(request: {lat: 50.6484585, lon: 38.4005083}) {
    ...WeatherData
  }
  Valuyki: weatherByPoint(request: {lat: 50.2111207, lon: 38.0998772}) {
    ...WeatherData
  }
  Grayvoron: weatherByPoint(request: {lat: 50.4862958, lon: 35.6663877}) {
    ...WeatherData
  }
  Gubkin: weatherByPoint(request: {lat: 51.2837123, lon: 37.5347759}) {
    ...WeatherData
  }
  Korocha: weatherByPoint(request: {lat: 50.8129041, lon: 37.1896436}) {
    ...WeatherData
  }
  NovyyOskol: weatherByPoint(request: {lat: 50.7633747, lon: 37.8775484}) {
    ...WeatherData
  }
  StaryyOskol: weatherByPoint(request: {lat: 51.2967101, lon: 37.8350182}) {
    ...WeatherData
  }
  Stroitel: weatherByPoint(request: {lat: 50.7845099, lon: 36.4887648}) {
    ...WeatherData
  }
  Shebekino: weatherByPoint(request: {lat: 50.4004883, lon: 36.8877889}) {
    ...WeatherData
  }
  Bryansk: weatherByPoint(request: {lat: 53.2419535, lon: 34.3652146}) {
    ...WeatherData
  }
  Dyatkovo: weatherByPoint(request: {lat: 53.5958178, lon: 34.3551812}) {
    ...WeatherData
  }
  Zhukovka: weatherByPoint(request: {lat: 53.5340397, lon: 33.7302579}) {
    ...WeatherData
  }
  Zlynka: weatherByPoint(request: {lat: 52.4267015, lon: 31.7360399}) {
    ...WeatherData
  }
  Karachev: weatherByPoint(request: {lat: 53.1296524, lon: 34.9888727}) {
    ...WeatherData
  }
  Klintsy: weatherByPoint(request: {lat: 52.7529119, lon: 32.233911}) {
    ...WeatherData
  }
  Mglin: weatherByPoint(request: {lat: 53.0599771, lon: 32.8468129}) {
    ...WeatherData
  }
  Novozybkov: weatherByPoint(request: {lat: 52.537173, lon: 31.9357991}) {
    ...WeatherData
  }
  Pochep: weatherByPoint(request: {lat: 52.9154851, lon: 33.4744058}) {
    ...WeatherData
  }
  Sevsk: weatherByPoint(request: {lat: 52.1483358, lon: 34.4918415}) {
    ...WeatherData
  }
  Seltso: weatherByPoint(request: {lat: 53.3739884, lon: 34.1059172}) {
    ...WeatherData
  }
  Starodub: weatherByPoint(request: {lat: 52.5852257, lon: 32.760403}) {
    ...WeatherData
  }
  Surazh: weatherByPoint(request: {lat: 53.0170888, lon: 32.3938878}) {
    ...WeatherData
  }
  Trubchevsk: weatherByPoint(request: {lat: 52.5791734, lon: 33.7660547}) {
    ...WeatherData
  }
  Unecha: weatherByPoint(request: {lat: 52.8461199, lon: 32.6757629}) {
    ...WeatherData
  }
  Fokino: weatherByPoint(request: {lat: 53.4554145, lon: 34.4159238}) {
    ...WeatherData
  }
  Babushkin: weatherByPoint(request: {lat: 51.7112755, lon: 105.8673219}) {
    ...WeatherData
  }
  Gusinoozersk: weatherByPoint(request: {lat: 51.2865048, lon: 106.5230319}) {
    ...WeatherData
  }
  Zakamensk: weatherByPoint(request: {lat: 50.372713, lon: 103.286699}) {
    ...WeatherData
  }
  Kyahta: weatherByPoint(request: {lat: 50.346543, lon: 106.4533516}) {
    ...WeatherData
  }
  Severobaykalsk: weatherByPoint(request: {lat: 55.635614, lon: 109.3361505}) {
    ...WeatherData
  }
  UlanUde: weatherByPoint(request: {lat: 51.8335853, lon: 107.5842223}) {
    ...WeatherData
  }
  Aleksandrov: weatherByPoint(request: {lat: 56.391819, lon: 38.7111123}) {
    ...WeatherData
  }
  Vladimir: weatherByPoint(request: {lat: 56.1280804, lon: 40.4084376}) {
    ...WeatherData
  }
  Vyazniki: weatherByPoint(request: {lat: 56.29773, lon: 42.2687398}) {
    ...WeatherData
  }
  Gorohovets: weatherByPoint(request: {lat: 56.2021036, lon: 42.6926111}) {
    ...WeatherData
  }
  GusHrustalnyy: weatherByPoint(request: {lat: 55.6198751, lon: 40.6579929}) {
    ...WeatherData
  }
  Kameshkovo: weatherByPoint(request: {lat: 56.3490152, lon: 40.9955183}) {
    ...WeatherData
  }
  Karabanovo: weatherByPoint(request: {lat: 56.3131822, lon: 38.7034257}) {
    ...WeatherData
  }
  Kirzhach: weatherByPoint(request: {lat: 56.1486863, lon: 38.8635701}) {
    ...WeatherData
  }
  Kovrov: weatherByPoint(request: {lat: 56.3554349, lon: 41.3170576}) {
    ...WeatherData
  }
  Kolchugino: weatherByPoint(request: {lat: 56.3327254, lon: 39.391336}) {
    ...WeatherData
  }
  Kosterevo: weatherByPoint(request: {lat: 55.9337222, lon: 39.6247398}) {
    ...WeatherData
  }
  Kurlovo: weatherByPoint(request: {lat: 55.452698, lon: 40.6124108}) {
    ...WeatherData
  }
  Lakinsk: weatherByPoint(request: {lat: 56.0180587, lon: 39.956551}) {
    ...WeatherData
  }
  Melenki: weatherByPoint(request: {lat: 55.3387515, lon: 41.6340046}) {
    ...WeatherData
  }
  Murom: weatherByPoint(request: {lat: 55.5630311, lon: 42.0231362}) {
    ...WeatherData
  }
  Petushki: weatherByPoint(request: {lat: 55.9298134, lon: 39.4508075}) {
    ...WeatherData
  }
  Pokrov: weatherByPoint(request: {lat: 55.9166398, lon: 39.1734526}) {
    ...WeatherData
  }
  Raduzhnyy: weatherByPoint(request: {lat: 55.9960277, lon: 40.3321855}) {
    ...WeatherData
  }
  Sobinka: weatherByPoint(request: {lat: 55.9939169, lon: 40.0179653}) {
    ...WeatherData
  }
  Strunino: weatherByPoint(request: {lat: 56.3749967, lon: 38.5839667}) {
    ...WeatherData
  }
  Sudogda: weatherByPoint(request: {lat: 55.9498056, lon: 40.8562939}) {
    ...WeatherData
  }
  Suzdal: weatherByPoint(request: {lat: 56.4274441, lon: 40.4525692}) {
    ...WeatherData
  }
  YurevPolskiy: weatherByPoint(request: {lat: 56.4937757, lon: 39.6680539}) {
    ...WeatherData
  }
  Volgograd: weatherByPoint(request: {lat: 48.7070042, lon: 44.5170339}) {
    ...WeatherData
  }
  Volzhskiy: weatherByPoint(request: {lat: 48.7978209, lon: 44.7462538}) {
    ...WeatherData
  }
  Dubovka: weatherByPoint(request: {lat: 49.0554742, lon: 44.8270085}) {
    ...WeatherData
  }
  Zhirnovsk: weatherByPoint(request: {lat: 50.9768814, lon: 44.7858202}) {
    ...WeatherData
  }
  KalachNaDonu: weatherByPoint(request: {lat: 48.6889024, lon: 43.5306303}) {
    ...WeatherData
  }
  Kamyshin: weatherByPoint(request: {lat: 50.0651529, lon: 45.3844202}) {
    ...WeatherData
  }
  Kotelnikovo: weatherByPoint(request: {lat: 47.6310259, lon: 43.1330872}) {
    ...WeatherData
  }
  Kotovo: weatherByPoint(request: {lat: 50.3205766, lon: 44.8030699}) {
    ...WeatherData
  }
  Krasnoslobodsk: weatherByPoint(request: {lat: 48.7068721, lon: 44.5630857}) {
    ...WeatherData
  }
  Leninsk: weatherByPoint(request: {lat: 48.6936061, lon: 45.1992692}) {
    ...WeatherData
  }
  Mihaylovka: weatherByPoint(request: {lat: 50.0708719, lon: 43.2401512}) {
    ...WeatherData
  }
  Nikolaevsk: weatherByPoint(request: {lat: 50.0165306, lon: 45.4731658}) {
    ...WeatherData
  }
  Novoanninskiy: weatherByPoint(request: {lat: 50.5296067, lon: 42.6666439}) {
    ...WeatherData
  }
  Pallasovka: weatherByPoint(request: {lat: 50.0500944, lon: 46.8804277}) {
    ...WeatherData
  }
  PetrovVal: weatherByPoint(request: {lat: 50.1380557, lon: 45.20914}) {
    ...WeatherData
  }
  Serafimovich: weatherByPoint(request: {lat: 49.5663183, lon: 42.7360402}) {
    ...WeatherData
  }
  Surovikino: weatherByPoint(request: {lat: 48.618917, lon: 42.8541163}) {
    ...WeatherData
  }
  Uryupinsk: weatherByPoint(request: {lat: 50.7903789, lon: 42.0288513}) {
    ...WeatherData
  }
  Frolovo: weatherByPoint(request: {lat: 49.7649148, lon: 43.6648641}) {
    ...WeatherData
  }
  Babaevo: weatherByPoint(request: {lat: 59.3892583, lon: 35.9377058}) {
    ...WeatherData
  }
  Belozersk: weatherByPoint(request: {lat: 60.0308381, lon: 37.7890586}) {
    ...WeatherData
  }
  VelikiyUstyug: weatherByPoint(request: {lat: 60.7603913, lon: 46.3054414}) {
    ...WeatherData
  }
  Vologda: weatherByPoint(request: {lat: 59.2483905, lon: 39.8355662}) {
    ...WeatherData
  }
  Vytegra: weatherByPoint(request: {lat: 61.0063465, lon: 36.4495137}) {
    ...WeatherData
  }
  Gryazovets: weatherByPoint(request: {lat: 58.8757553, lon: 40.2485362}) {
    ...WeatherData
  }
  Kadnikov: weatherByPoint(request: {lat: 59.5037764, lon: 40.3441148}) {
    ...WeatherData
  }
  Kirillov: weatherByPoint(request: {lat: 59.8591523, lon: 38.3748782}) {
    ...WeatherData
  }
  Krasavino: weatherByPoint(request: {lat: 60.9612823, lon: 46.4814116}) {
    ...WeatherData
  }
  Nikolsk: weatherByPoint(request: {lat: 59.5351837, lon: 45.4576137}) {
    ...WeatherData
  }
  Sokol: weatherByPoint(request: {lat: 59.4758605, lon: 40.1114187}) {
    ...WeatherData
  }
  Totma: weatherByPoint(request: {lat: 59.9734998, lon: 42.7589506}) {
    ...WeatherData
  }
  Ustyuzhna: weatherByPoint(request: {lat: 58.8383117, lon: 36.4425478}) {
    ...WeatherData
  }
  Harovsk: weatherByPoint(request: {lat: 59.9479423, lon: 40.2000298}) {
    ...WeatherData
  }
  Cherepovets: weatherByPoint(request: {lat: 59.1269212, lon: 37.9090497}) {
    ...WeatherData
  }
  Bobrov: weatherByPoint(request: {lat: 51.0901649, lon: 40.0318256}) {
    ...WeatherData
  }
  Boguchar: weatherByPoint(request: {lat: 49.9352454, lon: 40.5590801}) {
    ...WeatherData
  }
  Borisoglebsk: weatherByPoint(request: {lat: 51.3655754, lon: 42.1008334}) {
    ...WeatherData
  }
  Buturlinovka: weatherByPoint(request: {lat: 50.8311818, lon: 40.5976923}) {
    ...WeatherData
  }
  Voronezh: weatherByPoint(request: {lat: 51.6593332, lon: 39.1969229}) {
    ...WeatherData
  }
  Kalach: weatherByPoint(request: {lat: 50.4242134, lon: 41.0162014}) {
    ...WeatherData
  }
  Liski: weatherByPoint(request: {lat: 50.9945626, lon: 39.5184909}) {
    ...WeatherData
  }
  Novovoronezh: weatherByPoint(request: {lat: 51.3091524, lon: 39.2162843}) {
    ...WeatherData
  }
  Novohopersk: weatherByPoint(request: {lat: 51.0952211, lon: 41.6173404}) {
    ...WeatherData
  }
  Ostrogozhsk: weatherByPoint(request: {lat: 50.8677905, lon: 39.0407746}) {
    ...WeatherData
  }
  Pavlovsk: weatherByPoint(request: {lat: 50.453455, lon: 40.136874}) {
    ...WeatherData
  }
  Povorino: weatherByPoint(request: {lat: 51.1954419, lon: 42.2472726}) {
    ...WeatherData
  }
  Rossosh: weatherByPoint(request: {lat: 50.1701949, lon: 39.6226965}) {
    ...WeatherData
  }
  Semiluki: weatherByPoint(request: {lat: 51.6951644, lon: 39.0190454}) {
    ...WeatherData
  }
  Ertil: weatherByPoint(request: {lat: 51.830932, lon: 40.8074182}) {
    ...WeatherData
  }
  Buynaksk: weatherByPoint(request: {lat: 42.8214424, lon: 47.1165263}) {
    ...WeatherData
  }
  DagestanskieOgni: weatherByPoint(request: {lat: 42.1152296, lon: 48.1939354}) {
    ...WeatherData
  }
  Derbent: weatherByPoint(request: {lat: 42.058966, lon: 48.2907452}) {
    ...WeatherData
  }
  Izberbash: weatherByPoint(request: {lat: 42.5650962, lon: 47.8710051}) {
    ...WeatherData
  }
  Kaspiysk: weatherByPoint(request: {lat: 42.8916007, lon: 47.6367066}) {
    ...WeatherData
  }
  Kizilyurt: weatherByPoint(request: {lat: 43.203825, lon: 46.8729636}) {
    ...WeatherData
  }
  Kizlyar: weatherByPoint(request: {lat: 43.8484083, lon: 46.7233699}) {
    ...WeatherData
  }
  Mahachkala: weatherByPoint(request: {lat: 42.9849159, lon: 47.5047181}) {
    ...WeatherData
  }
  Hasavyurt: weatherByPoint(request: {lat: 43.2504665, lon: 46.5851292}) {
    ...WeatherData
  }
  YuzhnoSuhokumsk: weatherByPoint(request: {lat: 44.6602467, lon: 45.6499523}) {
    ...WeatherData
  }
  Birobidzhan: weatherByPoint(request: {lat: 48.7946446, lon: 132.9217207}) {
    ...WeatherData
  }
  Obluche: weatherByPoint(request: {lat: 49.0189345, lon: 131.0540102}) {
    ...WeatherData
  }
  Baley: weatherByPoint(request: {lat: 51.5823759, lon: 116.6379549}) {
    ...WeatherData
  }
  Borzya: weatherByPoint(request: {lat: 50.3876058, lon: 116.5234779}) {
    ...WeatherData
  }
  Krasnokamensk: weatherByPoint(request: {lat: 50.0929703, lon: 118.0323936}) {
    ...WeatherData
  }
  Mogocha: weatherByPoint(request: {lat: 53.7361398, lon: 119.7660867}) {
    ...WeatherData
  }
  Nerchinsk: weatherByPoint(request: {lat: 51.9594977, lon: 116.5852383}) {
    ...WeatherData
  }
  PetrovskZabaykalskiy: weatherByPoint(
    request: {lat: 51.2748592, lon: 108.846681}
  ) {
    ...WeatherData
  }
  Sretensk: weatherByPoint(request: {lat: 52.2461454, lon: 117.7117842}) {
    ...WeatherData
  }
  Hilok: weatherByPoint(request: {lat: 51.3634856, lon: 110.4590898}) {
    ...WeatherData
  }
  Chita: weatherByPoint(request: {lat: 52.0340142, lon: 113.4994}) {
    ...WeatherData
  }
  Shilka: weatherByPoint(request: {lat: 51.8497035, lon: 116.0334461}) {
    ...WeatherData
  }
  Vichuga: weatherByPoint(request: {lat: 57.2044698, lon: 41.9132201}) {
    ...WeatherData
  }
  GavrilovPosad: weatherByPoint(request: {lat: 56.5586946, lon: 40.1228906}) {
    ...WeatherData
  }
  Zavolzhsk: weatherByPoint(request: {lat: 57.4918141, lon: 42.1375625}) {
    ...WeatherData
  }
  Ivanovo: weatherByPoint(request: {lat: 56.9993792, lon: 40.9728272}) {
    ...WeatherData
  }
  Kineshma: weatherByPoint(request: {lat: 57.4425463, lon: 42.168914}) {
    ...WeatherData
  }
  Komsomolsk: weatherByPoint(request: {lat: 57.0273052, lon: 40.3776851}) {
    ...WeatherData
  }
  Kohma: weatherByPoint(request: {lat: 56.9324606, lon: 41.0931657}) {
    ...WeatherData
  }
  Navoloki: weatherByPoint(request: {lat: 57.4679066, lon: 41.9608002}) {
    ...WeatherData
  }
  Ples: weatherByPoint(request: {lat: 57.4606031, lon: 41.5122672}) {
    ...WeatherData
  }
  Privolzhsk: weatherByPoint(request: {lat: 57.3805743, lon: 41.2808565}) {
    ...WeatherData
  }
  Puchezh: weatherByPoint(request: {lat: 56.9820688, lon: 43.1683321}) {
    ...WeatherData
  }
  Rodniki: weatherByPoint(request: {lat: 57.1025975, lon: 41.7298834}) {
    ...WeatherData
  }
  Teykovo: weatherByPoint(request: {lat: 56.8542719, lon: 40.5353874}) {
    ...WeatherData
  }
  Furmanov: weatherByPoint(request: {lat: 57.2539276, lon: 41.1054432}) {
    ...WeatherData
  }
  Shuya: weatherByPoint(request: {lat: 56.8560234, lon: 41.3800939}) {
    ...WeatherData
  }
  Yuzha: weatherByPoint(request: {lat: 56.5926877, lon: 42.0458099}) {
    ...WeatherData
  }
  Yurevets: weatherByPoint(request: {lat: 57.3177781, lon: 43.1110401}) {
    ...WeatherData
  }
  Karabulak: weatherByPoint(request: {lat: 43.3055248, lon: 44.9094582}) {
    ...WeatherData
  }
  Magas: weatherByPoint(request: {lat: 43.1688611, lon: 44.8131207}) {
    ...WeatherData
  }
  Malgobek: weatherByPoint(request: {lat: 43.5096646, lon: 44.5901963}) {
    ...WeatherData
  }
  Nazran: weatherByPoint(request: {lat: 43.2257841, lon: 44.7645779}) {
    ...WeatherData
  }
  Sunzha: weatherByPoint(request: {lat: 43.3204196, lon: 45.0476331}) {
    ...WeatherData
  }
  Alzamay: weatherByPoint(request: {lat: 55.5551233, lon: 98.6643699}) {
    ...WeatherData
  }
  Angarsk: weatherByPoint(request: {lat: 52.544879, lon: 103.888543}) {
    ...WeatherData
  }
  Baykalsk: weatherByPoint(request: {lat: 51.5230393, lon: 104.1487532}) {
    ...WeatherData
  }
  Biryusinsk: weatherByPoint(request: {lat: 55.9609167, lon: 97.8205348}) {
    ...WeatherData
  }
  Bodaybo: weatherByPoint(request: {lat: 57.8468636, lon: 114.1866287}) {
    ...WeatherData
  }
  Bratsk: weatherByPoint(request: {lat: 56.1513108, lon: 101.6340035}) {
    ...WeatherData
  }
  Vihorevka: weatherByPoint(request: {lat: 56.1208145, lon: 101.1702926}) {
    ...WeatherData
  }
  ZheleznogorskIlimskiy: weatherByPoint(
    request: {lat: 56.5847888, lon: 104.114275}
  ) {
    ...WeatherData
  }
  Zima: weatherByPoint(request: {lat: 53.920693, lon: 102.0491772}) {
    ...WeatherData
  }
  Irkutsk: weatherByPoint(request: {lat: 52.2864036, lon: 104.2807466}) {
    ...WeatherData
  }
  Kirensk: weatherByPoint(request: {lat: 57.7756595, lon: 108.1109412}) {
    ...WeatherData
  }
  Nizhneudinsk: weatherByPoint(request: {lat: 54.8968931, lon: 99.0314056}) {
    ...WeatherData
  }
  Sayansk: weatherByPoint(request: {lat: 54.1107238, lon: 102.18015}) {
    ...WeatherData
  }
  Svirsk: weatherByPoint(request: {lat: 53.0842668, lon: 103.3364093}) {
    ...WeatherData
  }
  Slyudyanka: weatherByPoint(request: {lat: 51.6563983, lon: 103.7187545}) {
    ...WeatherData
  }
  Tayshet: weatherByPoint(request: {lat: 55.9405334, lon: 98.0030145}) {
    ...WeatherData
  }
  Tulun: weatherByPoint(request: {lat: 54.557162, lon: 100.5780603}) {
    ...WeatherData
  }
  UsoleSibirskoe: weatherByPoint(request: {lat: 52.7565808, lon: 103.6388109}) {
    ...WeatherData
  }
  UstIlimsk: weatherByPoint(request: {lat: 57.9430504, lon: 102.7415734}) {
    ...WeatherData
  }
  UstKut: weatherByPoint(request: {lat: 56.7928178, lon: 105.7757343}) {
    ...WeatherData
  }
  Cheremhovo: weatherByPoint(request: {lat: 53.1369095, lon: 103.0901268}) {
    ...WeatherData
  }
  Shelehov: weatherByPoint(request: {lat: 52.2102538, lon: 104.0973294}) {
    ...WeatherData
  }
  Baksan: weatherByPoint(request: {lat: 43.6819137, lon: 43.5345036}) {
    ...WeatherData
  }
  Mayskiy: weatherByPoint(request: {lat: 43.6281516, lon: 44.0517314}) {
    ...WeatherData
  }
  Nalchik: weatherByPoint(request: {lat: 43.4845464, lon: 43.60713}) {
    ...WeatherData
  }
  Nartkala: weatherByPoint(request: {lat: 43.5578075, lon: 43.8575925}) {
    ...WeatherData
  }
  Prohladnyy: weatherByPoint(request: {lat: 43.7589602, lon: 44.0102409}) {
    ...WeatherData
  }
  Terek: weatherByPoint(request: {lat: 43.4839358, lon: 44.1402161}) {
    ...WeatherData
  }
  Tyrnyauz: weatherByPoint(request: {lat: 43.3981585, lon: 42.9213582}) {
    ...WeatherData
  }
  Chegem: weatherByPoint(request: {lat: 43.5671525, lon: 43.5865792}) {
    ...WeatherData
  }
  Bagrationovsk: weatherByPoint(request: {lat: 54.3866518, lon: 20.6418091}) {
    ...WeatherData
  }
  Baltiysk: weatherByPoint(request: {lat: 54.6513372, lon: 19.9140572}) {
    ...WeatherData
  }
  Gvardeysk: weatherByPoint(request: {lat: 54.6588378, lon: 21.0501388}) {
    ...WeatherData
  }
  Gurevsk: weatherByPoint(request: {lat: 54.770638, lon: 20.6039767}) {
    ...WeatherData
  }
  Gusev: weatherByPoint(request: {lat: 54.5915455, lon: 22.1942445}) {
    ...WeatherData
  }
  Zelenogradsk: weatherByPoint(request: {lat: 54.9600185, lon: 20.4753652}) {
    ...WeatherData
  }
  Kaliningrad: weatherByPoint(request: {lat: 54.7074702, lon: 20.5073241}) {
    ...WeatherData
  }
  Krasnoznamensk: weatherByPoint(request: {lat: 54.9453423, lon: 22.4928745}) {
    ...WeatherData
  }
  Ladushkin: weatherByPoint(request: {lat: 54.5692156, lon: 20.1690153}) {
    ...WeatherData
  }
  Mamonovo: weatherByPoint(request: {lat: 54.4646036, lon: 19.9453482}) {
    ...WeatherData
  }
  Neman: weatherByPoint(request: {lat: 55.0316524, lon: 22.0324064}) {
    ...WeatherData
  }
  Nesterov: weatherByPoint(request: {lat: 54.6313814, lon: 22.5713736}) {
    ...WeatherData
  }
  Ozersk: weatherByPoint(request: {lat: 54.4084705, lon: 22.0134438}) {
    ...WeatherData
  }
  Pionerskiy: weatherByPoint(request: {lat: 54.9516574, lon: 20.2277424}) {
    ...WeatherData
  }
  Polessk: weatherByPoint(request: {lat: 54.8625126, lon: 21.0998067}) {
    ...WeatherData
  }
  Pravdinsk: weatherByPoint(request: {lat: 54.4430986, lon: 21.0085269}) {
    ...WeatherData
  }
  Primorsk: weatherByPoint(request: {lat: 54.7311437, lon: 19.9981926}) {
    ...WeatherData
  }
  Svetlogorsk: weatherByPoint(request: {lat: 54.9439286, lon: 20.1514295}) {
    ...WeatherData
  }
  Svetlyy: weatherByPoint(request: {lat: 54.6772897, lon: 20.1357595}) {
    ...WeatherData
  }
  Slavsk: weatherByPoint(request: {lat: 55.0449714, lon: 21.6742367}) {
    ...WeatherData
  }
  Sovetsk: weatherByPoint(request: {lat: 55.0809336, lon: 21.8886106}) {
    ...WeatherData
  }
  Chernyahovsk: weatherByPoint(request: {lat: 54.6244751, lon: 21.7969062}) {
    ...WeatherData
  }
  Gorodovikovsk: weatherByPoint(request: {lat: 46.0875083, lon: 41.935537}) {
    ...WeatherData
  }
  Lagan: weatherByPoint(request: {lat: 45.3930912, lon: 47.3432602}) {
    ...WeatherData
  }
  Elista: weatherByPoint(request: {lat: 46.3083344, lon: 44.2702088}) {
    ...WeatherData
  }
  Balabanovo: weatherByPoint(request: {lat: 55.1773714, lon: 36.6566951}) {
    ...WeatherData
  }
  Belousovo: weatherByPoint(request: {lat: 55.0956803, lon: 36.677629}) {
    ...WeatherData
  }
  Borovsk: weatherByPoint(request: {lat: 55.2130096, lon: 36.4926251}) {
    ...WeatherData
  }
  Ermolino: weatherByPoint(request: {lat: 55.1971758, lon: 36.5952722}) {
    ...WeatherData
  }
  Zhizdra: weatherByPoint(request: {lat: 53.7521926, lon: 34.7386592}) {
    ...WeatherData
  }
  Zhukov: weatherByPoint(request: {lat: 55.0301833, lon: 36.7394903}) {
    ...WeatherData
  }
  Kaluga: weatherByPoint(request: {lat: 54.5059848, lon: 36.2516245}) {
    ...WeatherData
  }
  Kirov: weatherByPoint(request: {lat: 54.0790111, lon: 34.3076201}) {
    ...WeatherData
  }
  Kozelsk: weatherByPoint(request: {lat: 54.0347201, lon: 35.780768}) {
    ...WeatherData
  }
  Kondrovo: weatherByPoint(request: {lat: 54.7959473, lon: 35.9274842}) {
    ...WeatherData
  }
  Kremenki: weatherByPoint(request: {lat: 54.8862447, lon: 37.1168701}) {
    ...WeatherData
  }
  Lyudinovo: weatherByPoint(request: {lat: 53.8700828, lon: 34.4385915}) {
    ...WeatherData
  }
  Maloyaroslavets: weatherByPoint(request: {lat: 55.0177123, lon: 36.4633603}) {
    ...WeatherData
  }
  Medyn: weatherByPoint(request: {lat: 54.9689785, lon: 35.8872168}) {
    ...WeatherData
  }
  Meschovsk: weatherByPoint(request: {lat: 54.3191471, lon: 35.2816918}) {
    ...WeatherData
  }
  Mosalsk: weatherByPoint(request: {lat: 54.4824939, lon: 34.9872239}) {
    ...WeatherData
  }
  Obninsk: weatherByPoint(request: {lat: 55.0943144, lon: 36.6121639}) {
    ...WeatherData
  }
  Sosenskiy: weatherByPoint(request: {lat: 54.0566016, lon: 35.9621646}) {
    ...WeatherData
  }
  SpasDemensk: weatherByPoint(request: {lat: 54.409922, lon: 34.0189631}) {
    ...WeatherData
  }
  Suhinichi: weatherByPoint(request: {lat: 54.097296, lon: 35.3443568}) {
    ...WeatherData
  }
  Tarusa: weatherByPoint(request: {lat: 54.7236477, lon: 37.1671}) {
    ...WeatherData
  }
  Yuhnov: weatherByPoint(request: {lat: 54.7446445, lon: 35.2424346}) {
    ...WeatherData
  }
  Vilyuchinsk: weatherByPoint(request: {lat: 52.9302415, lon: 158.4057632}) {
    ...WeatherData
  }
  Elizovo: weatherByPoint(request: {lat: 53.1830375, lon: 158.3883548}) {
    ...WeatherData
  }
  PetropavlovskKamchatskiy: weatherByPoint(
    request: {lat: 53.036908, lon: 158.6559254}
  ) {
    ...WeatherData
  }
  Karachaevsk: weatherByPoint(request: {lat: 43.7732525, lon: 41.9143472}) {
    ...WeatherData
  }
  Teberda: weatherByPoint(request: {lat: 43.4437731, lon: 41.7415142}) {
    ...WeatherData
  }
  UstDzheguta: weatherByPoint(request: {lat: 44.0838442, lon: 41.9711046}) {
    ...WeatherData
  }
  Cherkessk: weatherByPoint(request: {lat: 44.2269425, lon: 42.0466704}) {
    ...WeatherData
  }
  Belomorsk: weatherByPoint(request: {lat: 64.5378417, lon: 34.7799462}) {
    ...WeatherData
  }
  Kem: weatherByPoint(request: {lat: 64.9543539, lon: 34.5949263}) {
    ...WeatherData
  }
  Kondopoga: weatherByPoint(request: {lat: 62.2059817, lon: 34.2682122}) {
    ...WeatherData
  }
  Kostomuksha: weatherByPoint(request: {lat: 64.5889398, lon: 30.6016832}) {
    ...WeatherData
  }
  Lahdenpohya: weatherByPoint(request: {lat: 61.518881, lon: 30.1996116}) {
    ...WeatherData
  }
  Medvezhegorsk: weatherByPoint(request: {lat: 62.9127626, lon: 34.4568489}) {
    ...WeatherData
  }
  Olonets: weatherByPoint(request: {lat: 60.9794025, lon: 32.9725519}) {
    ...WeatherData
  }
  Petrozavodsk: weatherByPoint(request: {lat: 61.7891264, lon: 34.3596434}) {
    ...WeatherData
  }
  Pitkyaranta: weatherByPoint(request: {lat: 61.5757191, lon: 31.4640557}) {
    ...WeatherData
  }
  Pudozh: weatherByPoint(request: {lat: 61.8058821, lon: 36.5329941}) {
    ...WeatherData
  }
  Segezha: weatherByPoint(request: {lat: 63.7437572, lon: 34.3126982}) {
    ...WeatherData
  }
  Sortavala: weatherByPoint(request: {lat: 61.703367, lon: 30.6916998}) {
    ...WeatherData
  }
  Suoyarvi: weatherByPoint(request: {lat: 62.0787293, lon: 32.3499386}) {
    ...WeatherData
  }
  AnzheroSudzhensk: weatherByPoint(request: {lat: 56.0786281, lon: 86.0201278}) {
    ...WeatherData
  }
  Belovo: weatherByPoint(request: {lat: 54.4220968, lon: 86.3037373}) {
    ...WeatherData
  }
  Berezovskiy: weatherByPoint(request: {lat: 55.6693513, lon: 86.2744459}) {
    ...WeatherData
  }
  Gurevsk_2: weatherByPoint(request: {lat: 54.2859263, lon: 85.9475985}) {
    ...WeatherData
  }
  Kaltan: weatherByPoint(request: {lat: 53.5210919, lon: 87.2771636}) {
    ...WeatherData
  }
  Kemerovo: weatherByPoint(request: {lat: 55.3910651, lon: 86.0467781}) {
    ...WeatherData
  }
  Kiselevsk: weatherByPoint(request: {lat: 54.0059999, lon: 86.6366116}) {
    ...WeatherData
  }
  LeninskKuznetskiy: weatherByPoint(request: {lat: 54.6674492, lon: 86.1797324}) {
    ...WeatherData
  }
  Mariinsk: weatherByPoint(request: {lat: 56.2127383, lon: 87.7454924}) {
    ...WeatherData
  }
  Mezhdurechensk: weatherByPoint(request: {lat: 53.6865289, lon: 88.0702754}) {
    ...WeatherData
  }
  Myski: weatherByPoint(request: {lat: 53.7125695, lon: 87.8055646}) {
    ...WeatherData
  }
  Novokuznetsk: weatherByPoint(request: {lat: 53.794315, lon: 87.2142745}) {
    ...WeatherData
  }
  Osinniki: weatherByPoint(request: {lat: 53.5988055, lon: 87.3371272}) {
    ...WeatherData
  }
  Polysaevo: weatherByPoint(request: {lat: 54.6055, lon: 86.2809208}) {
    ...WeatherData
  }
  Prokopevsk: weatherByPoint(request: {lat: 53.8604265, lon: 86.7183577}) {
    ...WeatherData
  }
  Salair: weatherByPoint(request: {lat: 54.2351735, lon: 85.8030733}) {
    ...WeatherData
  }
  Tayga: weatherByPoint(request: {lat: 56.0622131, lon: 85.6207182}) {
    ...WeatherData
  }
  Tashtagol: weatherByPoint(request: {lat: 52.759313, lon: 87.8476546}) {
    ...WeatherData
  }
  Topki: weatherByPoint(request: {lat: 55.2764707, lon: 85.6152619}) {
    ...WeatherData
  }
  Yurga: weatherByPoint(request: {lat: 55.7202694, lon: 84.8886399}) {
    ...WeatherData
  }
  BelayaHolunitsa: weatherByPoint(request: {lat: 58.8415239, lon: 50.8460699}) {
    ...WeatherData
  }
  VyatskiePolyany: weatherByPoint(request: {lat: 56.2284817, lon: 51.0614855}) {
    ...WeatherData
  }
  Zuevka: weatherByPoint(request: {lat: 58.4032152, lon: 51.1331606}) {
    ...WeatherData
  }
  Kirov_2: weatherByPoint(request: {lat: 58.6035264, lon: 49.6679304}) {
    ...WeatherData
  }
  KirovoChepetsk: weatherByPoint(request: {lat: 58.5559424, lon: 50.0316848}) {
    ...WeatherData
  }
  Kirs: weatherByPoint(request: {lat: 59.340056, lon: 52.2414437}) {
    ...WeatherData
  }
  Kotelnich: weatherByPoint(request: {lat: 58.3034832, lon: 48.3475597}) {
    ...WeatherData
  }
  Luza: weatherByPoint(request: {lat: 60.6290609, lon: 47.2612445}) {
    ...WeatherData
  }
  Malmyzh: weatherByPoint(request: {lat: 56.5243844, lon: 50.6782739}) {
    ...WeatherData
  }
  Murashi: weatherByPoint(request: {lat: 59.3955383, lon: 48.9638417}) {
    ...WeatherData
  }
  Nolinsk: weatherByPoint(request: {lat: 57.5597284, lon: 49.93575}) {
    ...WeatherData
  }
  Omutninsk: weatherByPoint(request: {lat: 58.6698913, lon: 52.1894564}) {
    ...WeatherData
  }
  Orlov: weatherByPoint(request: {lat: 58.5389776, lon: 48.8927723}) {
    ...WeatherData
  }
  Slobodskoy: weatherByPoint(request: {lat: 58.7311574, lon: 50.1669249}) {
    ...WeatherData
  }
  Sovetsk_2: weatherByPoint(request: {lat: 57.584196, lon: 48.9590272}) {
    ...WeatherData
  }
  Sosnovka: weatherByPoint(request: {lat: 56.2532741, lon: 51.2833642}) {
    ...WeatherData
  }
  Urzhum: weatherByPoint(request: {lat: 57.1097477, lon: 50.0058097}) {
    ...WeatherData
  }
  Yaransk: weatherByPoint(request: {lat: 57.3040326, lon: 47.8478737}) {
    ...WeatherData
  }
  Vorkuta: weatherByPoint(request: {lat: 67.4974082, lon: 64.061034}) {
    ...WeatherData
  }
  Vuktyl: weatherByPoint(request: {lat: 63.8615274, lon: 57.3165402}) {
    ...WeatherData
  }
  Emva: weatherByPoint(request: {lat: 62.5965137, lon: 50.8732125}) {
    ...WeatherData
  }
  Inta: weatherByPoint(request: {lat: 66.0367316, lon: 60.1152961}) {
    ...WeatherData
  }
  Mikun: weatherByPoint(request: {lat: 62.3579068, lon: 50.0719503}) {
    ...WeatherData
  }
  Pechora: weatherByPoint(request: {lat: 65.148584, lon: 57.2239777}) {
    ...WeatherData
  }
  Sosnogorsk: weatherByPoint(request: {lat: 63.5989841, lon: 53.876293}) {
    ...WeatherData
  }
  Syktyvkar: weatherByPoint(request: {lat: 61.6686617, lon: 50.8358151}) {
    ...WeatherData
  }
  Usinsk: weatherByPoint(request: {lat: 65.994147, lon: 57.5569423}) {
    ...WeatherData
  }
  Uhta: weatherByPoint(request: {lat: 63.5565514, lon: 53.7014239}) {
    ...WeatherData
  }
  Buy: weatherByPoint(request: {lat: 58.4733277, lon: 41.5306822}) {
    ...WeatherData
  }
  Volgorechensk: weatherByPoint(request: {lat: 57.4424559, lon: 41.1594201}) {
    ...WeatherData
  }
  Galich: weatherByPoint(request: {lat: 58.3828191, lon: 42.3654013}) {
    ...WeatherData
  }
  Kologriv: weatherByPoint(request: {lat: 58.8269323, lon: 44.3184927}) {
    ...WeatherData
  }
  Kostroma: weatherByPoint(request: {lat: 57.768, lon: 40.927}) {
    ...WeatherData
  }
  Makarev: weatherByPoint(request: {lat: 57.8807152, lon: 43.8014197}) {
    ...WeatherData
  }
  Manturovo: weatherByPoint(request: {lat: 58.3265441, lon: 44.757494}) {
    ...WeatherData
  }
  Nerehta: weatherByPoint(request: {lat: 57.4543369, lon: 40.5723598}) {
    ...WeatherData
  }
  Neya: weatherByPoint(request: {lat: 58.2943349, lon: 43.8780948}) {
    ...WeatherData
  }
  Soligalich: weatherByPoint(request: {lat: 59.0784867, lon: 42.2878423}) {
    ...WeatherData
  }
  Chuhloma: weatherByPoint(request: {lat: 58.753421, lon: 42.6884958}) {
    ...WeatherData
  }
  Sharya: weatherByPoint(request: {lat: 58.3760542, lon: 45.4062414}) {
    ...WeatherData
  }
  Abinsk: weatherByPoint(request: {lat: 44.8679655, lon: 38.1618157}) {
    ...WeatherData
  }
  Anapa: weatherByPoint(request: {lat: 44.8950433, lon: 37.3163282}) {
    ...WeatherData
  }
  Apsheronsk: weatherByPoint(request: {lat: 44.4584006, lon: 39.7299824}) {
    ...WeatherData
  }
  Armavir: weatherByPoint(request: {lat: 45.0012149, lon: 41.1324168}) {
    ...WeatherData
  }
  Belorechensk: weatherByPoint(request: {lat: 44.7651876, lon: 39.8781494}) {
    ...WeatherData
  }
  Gelendzhik: weatherByPoint(request: {lat: 44.5630007, lon: 38.0790852}) {
    ...WeatherData
  }
  GoryachiyKlyuch: weatherByPoint(request: {lat: 44.6344864, lon: 39.1354738}) {
    ...WeatherData
  }
  Gulkevichi: weatherByPoint(request: {lat: 45.3605121, lon: 40.6918389}) {
    ...WeatherData
  }
  Eysk: weatherByPoint(request: {lat: 46.71157, lon: 38.2763895}) {
    ...WeatherData
  }
  Korenovsk: weatherByPoint(request: {lat: 45.4641703, lon: 39.458949}) {
    ...WeatherData
  }
  Krasnodar: weatherByPoint(request: {lat: 45.0401604, lon: 38.9759647}) {
    ...WeatherData
  }
  Kropotkin: weatherByPoint(request: {lat: 45.4333007, lon: 40.5727951}) {
    ...WeatherData
  }
  Krymsk: weatherByPoint(request: {lat: 44.9344404, lon: 37.9855795}) {
    ...WeatherData
  }
  Kurganinsk: weatherByPoint(request: {lat: 44.8877025, lon: 40.5913245}) {
    ...WeatherData
  }
  Labinsk: weatherByPoint(request: {lat: 44.6354363, lon: 40.7245341}) {
    ...WeatherData
  }
  Novokubansk: weatherByPoint(request: {lat: 45.1038699, lon: 41.0475175}) {
    ...WeatherData
  }
  Novorossiysk: weatherByPoint(request: {lat: 44.7235026, lon: 37.7686135}) {
    ...WeatherData
  }
  PrimorskoAhtarsk: weatherByPoint(request: {lat: 46.0515432, lon: 38.1704875}) {
    ...WeatherData
  }
  SlavyanskNaKubani: weatherByPoint(request: {lat: 45.2603626, lon: 38.1259774}) {
    ...WeatherData
  }
  Sochi: weatherByPoint(request: {lat: 43.5854551, lon: 39.7231548}) {
    ...WeatherData
  }
  Temryuk: weatherByPoint(request: {lat: 45.2610949, lon: 37.4454412}) {
    ...WeatherData
  }
  Timashevsk: weatherByPoint(request: {lat: 45.615923, lon: 38.9351837}) {
    ...WeatherData
  }
  Tihoretsk: weatherByPoint(request: {lat: 45.8546345, lon: 40.1260267}) {
    ...WeatherData
  }
  Tuapse: weatherByPoint(request: {lat: 44.1105335, lon: 39.0824904}) {
    ...WeatherData
  }
  UstLabinsk: weatherByPoint(request: {lat: 45.2227359, lon: 39.6929577}) {
    ...WeatherData
  }
  Hadyzhensk: weatherByPoint(request: {lat: 44.4122963, lon: 39.5320258}) {
    ...WeatherData
  }
  Artemovsk: weatherByPoint(request: {lat: 54.3473075, lon: 93.4358377}) {
    ...WeatherData
  }
  Achinsk: weatherByPoint(request: {lat: 56.253907, lon: 90.4794397}) {
    ...WeatherData
  }
  Bogotol: weatherByPoint(request: {lat: 56.2098468, lon: 89.5299336}) {
    ...WeatherData
  }
  Borodino: weatherByPoint(request: {lat: 55.9054121, lon: 94.9020967}) {
    ...WeatherData
  }
  Divnogorsk: weatherByPoint(request: {lat: 55.9576784, lon: 92.3800687}) {
    ...WeatherData
  }
  Dudinka: weatherByPoint(request: {lat: 69.4031364, lon: 86.1907218}) {
    ...WeatherData
  }
  Eniseysk: weatherByPoint(request: {lat: 58.4485261, lon: 92.1651083}) {
    ...WeatherData
  }
  Zheleznogorsk: weatherByPoint(request: {lat: 56.2529035, lon: 93.532273}) {
    ...WeatherData
  }
  Zaozernyy: weatherByPoint(request: {lat: 55.9617752, lon: 94.7091491}) {
    ...WeatherData
  }
  Zelenogorsk: weatherByPoint(request: {lat: 56.1131564, lon: 94.5888103}) {
    ...WeatherData
  }
  Igarka: weatherByPoint(request: {lat: 67.4666901, lon: 86.5812794}) {
    ...WeatherData
  }
  Ilanskiy: weatherByPoint(request: {lat: 56.2374037, lon: 96.067267}) {
    ...WeatherData
  }
  Kansk: weatherByPoint(request: {lat: 56.2051282, lon: 95.7051096}) {
    ...WeatherData
  }
  Kodinsk: weatherByPoint(request: {lat: 58.6032644, lon: 99.1797962}) {
    ...WeatherData
  }
  Krasnoyarsk: weatherByPoint(request: {lat: 56.0093879, lon: 92.8524806}) {
    ...WeatherData
  }
  Lesosibirsk: weatherByPoint(request: {lat: 58.221681, lon: 92.5037872}) {
    ...WeatherData
  }
  Minusinsk: weatherByPoint(request: {lat: 53.7104586, lon: 91.6872907}) {
    ...WeatherData
  }
  Nazarovo: weatherByPoint(request: {lat: 56.0113799, lon: 90.4168775}) {
    ...WeatherData
  }
  Norilsk: weatherByPoint(request: {lat: 69.3489978, lon: 88.2009846}) {
    ...WeatherData
  }
  Sosnovoborsk: weatherByPoint(request: {lat: 56.1202647, lon: 93.3354121}) {
    ...WeatherData
  }
  Uzhur: weatherByPoint(request: {lat: 55.3141969, lon: 89.8333918}) {
    ...WeatherData
  }
  Uyar: weatherByPoint(request: {lat: 55.8131263, lon: 94.3282601}) {
    ...WeatherData
  }
  Sharypovo: weatherByPoint(request: {lat: 55.5389739, lon: 89.1801044}) {
    ...WeatherData
  }
  Alupka: weatherByPoint(request: {lat: 44.4164605, lon: 34.0444797}) {
    ...WeatherData
  }
  Alushta: weatherByPoint(request: {lat: 44.6764304, lon: 34.4100624}) {
    ...WeatherData
  }
  Armyansk: weatherByPoint(request: {lat: 46.1059307, lon: 33.6910012}) {
    ...WeatherData
  }
  Bahchisaray: weatherByPoint(request: {lat: 44.7514769, lon: 33.8752176}) {
    ...WeatherData
  }
  Belogorsk_2: weatherByPoint(request: {lat: 45.057202, lon: 34.5999029}) {
    ...WeatherData
  }
  Dzhankoy: weatherByPoint(request: {lat: 45.7092306, lon: 34.3883372}) {
    ...WeatherData
  }
  Evpatoriya: weatherByPoint(request: {lat: 45.190629, lon: 33.367634}) {
    ...WeatherData
  }
  Kerch: weatherByPoint(request: {lat: 45.3562627, lon: 36.4674513}) {
    ...WeatherData
  }
  Krasnoperekopsk: weatherByPoint(request: {lat: 45.9537576, lon: 33.7921939}) {
    ...WeatherData
  }
  Saki: weatherByPoint(request: {lat: 45.1341997, lon: 33.6033383}) {
    ...WeatherData
  }
  Simferopol: weatherByPoint(request: {lat: 44.9482948, lon: 34.1001151}) {
    ...WeatherData
  }
  StaryyKrym: weatherByPoint(request: {lat: 45.029058, lon: 35.0901474}) {
    ...WeatherData
  }
  Sudak: weatherByPoint(request: {lat: 44.8504679, lon: 34.9762034}) {
    ...WeatherData
  }
  Feodosiya: weatherByPoint(request: {lat: 45.0318393, lon: 35.3824259}) {
    ...WeatherData
  }
  Schelkino: weatherByPoint(request: {lat: 45.4288991, lon: 35.825165}) {
    ...WeatherData
  }
  Yalta: weatherByPoint(request: {lat: 44.4953612, lon: 34.166308}) {
    ...WeatherData
  }
  Dalmatovo: weatherByPoint(request: {lat: 56.262114, lon: 62.9387011}) {
    ...WeatherData
  }
  Kataysk: weatherByPoint(request: {lat: 56.290809, lon: 62.5800359}) {
    ...WeatherData
  }
  Kurgan: weatherByPoint(request: {lat: 55.4443883, lon: 65.3161963}) {
    ...WeatherData
  }
  Kurtamysh: weatherByPoint(request: {lat: 54.9368539, lon: 64.4203722}) {
    ...WeatherData
  }
  Makushino: weatherByPoint(request: {lat: 55.2153947, lon: 67.2451705}) {
    ...WeatherData
  }
  Petuhovo: weatherByPoint(request: {lat: 55.0650077, lon: 67.8873408}) {
    ...WeatherData
  }
  Shadrinsk: weatherByPoint(request: {lat: 56.0870344, lon: 63.6297182}) {
    ...WeatherData
  }
  Shumiha: weatherByPoint(request: {lat: 55.2280246, lon: 63.2901272}) {
    ...WeatherData
  }
  Schuche: weatherByPoint(request: {lat: 55.2087637, lon: 62.7478548}) {
    ...WeatherData
  }
  Dmitriev: weatherByPoint(request: {lat: 52.1268464, lon: 35.0739038}) {
    ...WeatherData
  }
  Zheleznogorsk_2: weatherByPoint(request: {lat: 52.3380202, lon: 35.3516867}) {
    ...WeatherData
  }
  Kursk: weatherByPoint(request: {lat: 51.7303637, lon: 36.1925603}) {
    ...WeatherData
  }
  Kurchatov: weatherByPoint(request: {lat: 51.6604083, lon: 35.6572224}) {
    ...WeatherData
  }
  Lgov: weatherByPoint(request: {lat: 51.6597148, lon: 35.2612491}) {
    ...WeatherData
  }
  Oboyan: weatherByPoint(request: {lat: 51.2119324, lon: 36.2755133}) {
    ...WeatherData
  }
  Rylsk: weatherByPoint(request: {lat: 51.5681314, lon: 34.6802597}) {
    ...WeatherData
  }
  Sudzha: weatherByPoint(request: {lat: 51.1918927, lon: 35.2720915}) {
    ...WeatherData
  }
  Fatezh: weatherByPoint(request: {lat: 52.0917728, lon: 35.8538706}) {
    ...WeatherData
  }
  Schigry: weatherByPoint(request: {lat: 51.8786014, lon: 36.8910945}) {
    ...WeatherData
  }
  Boksitogorsk: weatherByPoint(request: {lat: 59.4734797, lon: 33.845688}) {
    ...WeatherData
  }
  Volosovo: weatherByPoint(request: {lat: 59.4445408, lon: 29.4923355}) {
    ...WeatherData
  }
  Volhov: weatherByPoint(request: {lat: 59.9005958, lon: 32.3520756}) {
    ...WeatherData
  }
  Vsevolozhsk: weatherByPoint(request: {lat: 60.0191278, lon: 30.6456718}) {
    ...WeatherData
  }
  Vyborg: weatherByPoint(request: {lat: 60.7130801, lon: 28.7328336}) {
    ...WeatherData
  }
  Vysotsk: weatherByPoint(request: {lat: 60.6296236, lon: 28.5709314}) {
    ...WeatherData
  }
  Gatchina: weatherByPoint(request: {lat: 59.565237, lon: 30.1282473}) {
    ...WeatherData
  }
  Ivangorod: weatherByPoint(request: {lat: 59.3766119, lon: 28.2231659}) {
    ...WeatherData
  }
  Kamennogorsk: weatherByPoint(request: {lat: 60.950855, lon: 29.1308372}) {
    ...WeatherData
  }
  Kingisepp: weatherByPoint(request: {lat: 59.3740435, lon: 28.6112444}) {
    ...WeatherData
  }
  Kirishi: weatherByPoint(request: {lat: 59.4742862, lon: 32.0624947}) {
    ...WeatherData
  }
  Kirovsk: weatherByPoint(request: {lat: 59.8754216, lon: 30.981364}) {
    ...WeatherData
  }
  Kommunar: weatherByPoint(request: {lat: 59.6215133, lon: 30.3934125}) {
    ...WeatherData
  }
  Kudrovo: weatherByPoint(request: {lat: 59.9075226, lon: 30.5121008}) {
    ...WeatherData
  }
  LodeynoePole: weatherByPoint(request: {lat: 60.7320936, lon: 33.5521022}) {
    ...WeatherData
  }
  Luga: weatherByPoint(request: {lat: 58.7374031, lon: 29.8465776}) {
    ...WeatherData
  }
  Lyuban: weatherByPoint(request: {lat: 59.3493847, lon: 31.2484801}) {
    ...WeatherData
  }
  Murino: weatherByPoint(request: {lat: 60.044862, lon: 30.4571456}) {
    ...WeatherData
  }
  Nikolskoe: weatherByPoint(request: {lat: 59.7043309, lon: 30.7874571}) {
    ...WeatherData
  }
  NovayaLadoga: weatherByPoint(request: {lat: 60.1100135, lon: 32.3141203}) {
    ...WeatherData
  }
  Otradnoe: weatherByPoint(request: {lat: 59.7726848, lon: 30.7988557}) {
    ...WeatherData
  }
  Pikalevo: weatherByPoint(request: {lat: 59.5132022, lon: 34.1772776}) {
    ...WeatherData
  }
  Podporozhe: weatherByPoint(request: {lat: 60.9127549, lon: 34.1567664}) {
    ...WeatherData
  }
  Primorsk_2: weatherByPoint(request: {lat: 60.3660209, lon: 28.6135772}) {
    ...WeatherData
  }
  Priozersk: weatherByPoint(request: {lat: 61.0330896, lon: 30.1587851}) {
    ...WeatherData
  }
  Svetogorsk: weatherByPoint(request: {lat: 61.1111282, lon: 28.8725865}) {
    ...WeatherData
  }
  Sertolovo: weatherByPoint(request: {lat: 60.1446932, lon: 30.2095918}) {
    ...WeatherData
  }
  Slantsy: weatherByPoint(request: {lat: 59.1178185, lon: 28.0881475}) {
    ...WeatherData
  }
  SosnovyyBor: weatherByPoint(request: {lat: 59.8772884, lon: 29.1291619}) {
    ...WeatherData
  }
  Syasstroy: weatherByPoint(request: {lat: 60.1401739, lon: 32.5601559}) {
    ...WeatherData
  }
  Tihvin: weatherByPoint(request: {lat: 59.6272904, lon: 33.5072731}) {
    ...WeatherData
  }
  Tosno: weatherByPoint(request: {lat: 59.5407098, lon: 30.877812}) {
    ...WeatherData
  }
  Shlisselburg: weatherByPoint(request: {lat: 59.9443714, lon: 31.0333365}) {
    ...WeatherData
  }
  Gryazi: weatherByPoint(request: {lat: 52.4874097, lon: 39.9331142}) {
    ...WeatherData
  }
  Dankov: weatherByPoint(request: {lat: 53.2577411, lon: 39.1456184}) {
    ...WeatherData
  }
  Elets: weatherByPoint(request: {lat: 52.6152411, lon: 38.5289342}) {
    ...WeatherData
  }
  Zadonsk: weatherByPoint(request: {lat: 52.4004179, lon: 38.9205032}) {
    ...WeatherData
  }
  Lebedyan: weatherByPoint(request: {lat: 53.0156117, lon: 39.143536}) {
    ...WeatherData
  }
  Lipetsk: weatherByPoint(request: {lat: 52.610249, lon: 39.5947883}) {
    ...WeatherData
  }
  Usman: weatherByPoint(request: {lat: 52.0442648, lon: 39.726401}) {
    ...WeatherData
  }
  Chaplygin: weatherByPoint(request: {lat: 53.24048, lon: 39.9670973}) {
    ...WeatherData
  }
  Magadan: weatherByPoint(request: {lat: 59.5681332, lon: 150.8084956}) {
    ...WeatherData
  }
  Susuman: weatherByPoint(request: {lat: 62.7805882, lon: 148.1540281}) {
    ...WeatherData
  }
  Volzhsk: weatherByPoint(request: {lat: 55.8623156, lon: 48.3715083}) {
    ...WeatherData
  }
  Zvenigovo: weatherByPoint(request: {lat: 55.9738571, lon: 48.0170245}) {
    ...WeatherData
  }
  YoshkarOla: weatherByPoint(request: {lat: 56.6343662, lon: 47.8999706}) {
    ...WeatherData
  }
  Kozmodemyansk: weatherByPoint(request: {lat: 56.3334036, lon: 46.546675}) {
    ...WeatherData
  }
  Ardatov: weatherByPoint(request: {lat: 54.8465544, lon: 46.2411232}) {
    ...WeatherData
  }
  Insar: weatherByPoint(request: {lat: 53.8770022, lon: 44.3696566}) {
    ...WeatherData
  }
  Kovylkino: weatherByPoint(request: {lat: 54.0391072, lon: 43.9191539}) {
    ...WeatherData
  }
  Krasnoslobodsk_2: weatherByPoint(request: {lat: 54.4248207, lon: 43.7845011}) {
    ...WeatherData
  }
  Ruzaevka: weatherByPoint(request: {lat: 54.0581967, lon: 44.9490466}) {
    ...WeatherData
  }
  Saransk: weatherByPoint(request: {lat: 54.1809332, lon: 45.1862632}) {
    ...WeatherData
  }
  Temnikov: weatherByPoint(request: {lat: 54.6310583, lon: 43.2161099}) {
    ...WeatherData
  }
  Aprelevka: weatherByPoint(request: {lat: 55.5276918, lon: 37.065143}) {
    ...WeatherData
  }
  Balashiha: weatherByPoint(request: {lat: 55.796389, lon: 37.938283}) {
    ...WeatherData
  }
  Beloozyorskiy: weatherByPoint(request: {lat: 55.4595766, lon: 38.4389742}) {
    ...WeatherData
  }
  Bronnitsy: weatherByPoint(request: {lat: 55.4255379, lon: 38.264145}) {
    ...WeatherData
  }
  Vereya: weatherByPoint(request: {lat: 55.343369, lon: 36.185694}) {
    ...WeatherData
  }
  Vidnoe: weatherByPoint(request: {lat: 55.551725, lon: 37.7061984}) {
    ...WeatherData
  }
  Volokolamsk: weatherByPoint(request: {lat: 56.0356499, lon: 35.9585112}) {
    ...WeatherData
  }
  Voskresensk: weatherByPoint(request: {lat: 55.3071519, lon: 38.7027953}) {
    ...WeatherData
  }
  Vysokovsk: weatherByPoint(request: {lat: 56.3359513, lon: 36.5251837}) {
    ...WeatherData
  }
  Golitsyno: weatherByPoint(request: {lat: 55.6190582, lon: 36.9856793}) {
    ...WeatherData
  }
  Dedovsk: weatherByPoint(request: {lat: 55.8703276, lon: 37.1245043}) {
    ...WeatherData
  }
  Dzerzhinskiy: weatherByPoint(request: {lat: 55.6240869, lon: 37.8440276}) {
    ...WeatherData
  }
  Dmitrov: weatherByPoint(request: {lat: 56.3477457, lon: 37.526672}) {
    ...WeatherData
  }
  Dolgoprudnyy: weatherByPoint(request: {lat: 55.9385999, lon: 37.5101021}) {
    ...WeatherData
  }
  Domodedovo: weatherByPoint(request: {lat: 55.4363283, lon: 37.7664984}) {
    ...WeatherData
  }
  Drezna: weatherByPoint(request: {lat: 55.7443143, lon: 38.8498479}) {
    ...WeatherData
  }
  Dubna: weatherByPoint(request: {lat: 56.741786, lon: 37.1757223}) {
    ...WeatherData
  }
  Egorevsk: weatherByPoint(request: {lat: 55.3830113, lon: 39.0358317}) {
    ...WeatherData
  }
  Zhukovskiy: weatherByPoint(request: {lat: 55.599803, lon: 38.1224298}) {
    ...WeatherData
  }
  Zaraysk: weatherByPoint(request: {lat: 54.762456, lon: 38.8850978}) {
    ...WeatherData
  }
  Zvenigorod: weatherByPoint(request: {lat: 55.7297089, lon: 36.8554029}) {
    ...WeatherData
  }
  Ivanteevka: weatherByPoint(request: {lat: 55.9741665, lon: 37.9207539}) {
    ...WeatherData
  }
  Istra: weatherByPoint(request: {lat: 55.9062267, lon: 36.8601454}) {
    ...WeatherData
  }
  Kashira: weatherByPoint(request: {lat: 54.853337, lon: 38.1904392}) {
    ...WeatherData
  }
  Klin: weatherByPoint(request: {lat: 56.3425605, lon: 36.7240032}) {
    ...WeatherData
  }
  Kolomna: weatherByPoint(request: {lat: 55.102814, lon: 38.7531002}) {
    ...WeatherData
  }
  Korolyov: weatherByPoint(request: {lat: 55.9161773, lon: 37.8545415}) {
    ...WeatherData
  }
  Kotelniki: weatherByPoint(request: {lat: 55.6597925, lon: 37.8631156}) {
    ...WeatherData
  }
  Krasnoarmeysk: weatherByPoint(request: {lat: 56.105426, lon: 38.140838}) {
    ...WeatherData
  }
  Krasnogorsk: weatherByPoint(request: {lat: 55.8317203, lon: 37.3295266}) {
    ...WeatherData
  }
  Krasnozavodsk: weatherByPoint(request: {lat: 56.4409979, lon: 38.2320307}) {
    ...WeatherData
  }
  Krasnoznamensk_2: weatherByPoint(request: {lat: 55.5978959, lon: 37.0393709}) {
    ...WeatherData
  }
  Kubinka: weatherByPoint(request: {lat: 55.5754955, lon: 36.6951995}) {
    ...WeatherData
  }
  Kurovskoe: weatherByPoint(request: {lat: 55.5792277, lon: 38.9207723}) {
    ...WeatherData
  }
  LikinoDulyovo: weatherByPoint(request: {lat: 55.7078257, lon: 38.9578093}) {
    ...WeatherData
  }
  Lobnya: weatherByPoint(request: {lat: 56.0328881, lon: 37.4614035}) {
    ...WeatherData
  }
  LosinoPetrovskiy: weatherByPoint(request: {lat: 55.8713214, lon: 38.200599}) {
    ...WeatherData
  }
  Luhovitsy: weatherByPoint(request: {lat: 54.9652077, lon: 39.0260266}) {
    ...WeatherData
  }
  Lytkarino: weatherByPoint(request: {lat: 55.5778163, lon: 37.9033507}) {
    ...WeatherData
  }
  Lyubertsy: weatherByPoint(request: {lat: 55.676499, lon: 37.898125}) {
    ...WeatherData
  }
  Mozhaysk: weatherByPoint(request: {lat: 55.5069259, lon: 36.024043}) {
    ...WeatherData
  }
  Mytischi: weatherByPoint(request: {lat: 55.9105782, lon: 37.7363579}) {
    ...WeatherData
  }
  NaroFominsk: weatherByPoint(request: {lat: 55.386185, lon: 36.734484}) {
    ...WeatherData
  }
  Noginsk: weatherByPoint(request: {lat: 55.8686133, lon: 38.4622104}) {
    ...WeatherData
  }
  Odintsovo: weatherByPoint(request: {lat: 55.6789455, lon: 37.263686}) {
    ...WeatherData
  }
  Ozyory: weatherByPoint(request: {lat: 54.8541006, lon: 38.5599196}) {
    ...WeatherData
  }
  OrehovoZuevo: weatherByPoint(request: {lat: 55.8151421, lon: 38.9869822}) {
    ...WeatherData
  }
  PavlovskiyPosad: weatherByPoint(request: {lat: 55.7807244, lon: 38.6596983}) {
    ...WeatherData
  }
  Peresvet: weatherByPoint(request: {lat: 56.4158326, lon: 38.1733534}) {
    ...WeatherData
  }
  Podolsk: weatherByPoint(request: {lat: 55.4389322, lon: 37.5703482}) {
    ...WeatherData
  }
  Protvino: weatherByPoint(request: {lat: 54.8705984, lon: 37.2182749}) {
    ...WeatherData
  }
  Pushkino: weatherByPoint(request: {lat: 56.0103638, lon: 37.8471403}) {
    ...WeatherData
  }
  Puschino: weatherByPoint(request: {lat: 54.8324412, lon: 37.6210346}) {
    ...WeatherData
  }
  Ramenskoe: weatherByPoint(request: {lat: 55.5495132, lon: 38.2728914}) {
    ...WeatherData
  }
  Reutov: weatherByPoint(request: {lat: 55.7582621, lon: 37.8618553}) {
    ...WeatherData
  }
  Roshal: weatherByPoint(request: {lat: 55.6632776, lon: 39.8656147}) {
    ...WeatherData
  }
  Ruza: weatherByPoint(request: {lat: 55.7014744, lon: 36.1959206}) {
    ...WeatherData
  }
  SergievPosad: weatherByPoint(request: {lat: 56.3062548, lon: 38.1502661}) {
    ...WeatherData
  }
  Serpuhov: weatherByPoint(request: {lat: 54.9226466, lon: 37.4033859}) {
    ...WeatherData
  }
  Solnechnogorsk: weatherByPoint(request: {lat: 56.185102, lon: 36.977631}) {
    ...WeatherData
  }
  StarayaKupavna: weatherByPoint(request: {lat: 55.810648, lon: 38.175624}) {
    ...WeatherData
  }
  Stupino: weatherByPoint(request: {lat: 54.886274, lon: 38.078228}) {
    ...WeatherData
  }
  Taldom: weatherByPoint(request: {lat: 56.7308564, lon: 37.5276003}) {
    ...WeatherData
  }
  Fryazino: weatherByPoint(request: {lat: 55.9590588, lon: 38.0410235}) {
    ...WeatherData
  }
  Himki: weatherByPoint(request: {lat: 55.888657, lon: 37.4303702}) {
    ...WeatherData
  }
  Hotkovo: weatherByPoint(request: {lat: 56.2516982, lon: 37.9396017}) {
    ...WeatherData
  }
  Chernogolovka: weatherByPoint(request: {lat: 56.010005, lon: 38.379245}) {
    ...WeatherData
  }
  Chehov: weatherByPoint(request: {lat: 55.1508011, lon: 37.4533252}) {
    ...WeatherData
  }
  Shatura: weatherByPoint(request: {lat: 55.5777427, lon: 39.5445712}) {
    ...WeatherData
  }
  Schyolkovo: weatherByPoint(request: {lat: 55.9233801, lon: 37.9783707}) {
    ...WeatherData
  }
  Elektrogorsk: weatherByPoint(request: {lat: 55.8780241, lon: 38.7806752}) {
    ...WeatherData
  }
  Elektrostal: weatherByPoint(request: {lat: 55.7847291, lon: 38.4447045}) {
    ...WeatherData
  }
  Elektrougli: weatherByPoint(request: {lat: 55.7170877, lon: 38.2192563}) {
    ...WeatherData
  }
  Yahroma: weatherByPoint(request: {lat: 56.2890516, lon: 37.4831799}) {
    ...WeatherData
  }
  Apatity: weatherByPoint(request: {lat: 67.5677761, lon: 33.4067929}) {
    ...WeatherData
  }
  Gadzhievo: weatherByPoint(request: {lat: 69.2491311, lon: 33.315341}) {
    ...WeatherData
  }
  Zaozersk: weatherByPoint(request: {lat: 69.4003584, lon: 32.4501496}) {
    ...WeatherData
  }
  Zapolyarnyy: weatherByPoint(request: {lat: 69.4132852, lon: 30.7984312}) {
    ...WeatherData
  }
  Kandalaksha: weatherByPoint(request: {lat: 67.1567974, lon: 32.4143218}) {
    ...WeatherData
  }
  Kirovsk_2: weatherByPoint(request: {lat: 67.6150424, lon: 33.663735}) {
    ...WeatherData
  }
  Kovdor: weatherByPoint(request: {lat: 67.5661417, lon: 30.4741941}) {
    ...WeatherData
  }
  Kola: weatherByPoint(request: {lat: 68.8786028, lon: 33.0262299}) {
    ...WeatherData
  }
  Monchegorsk: weatherByPoint(request: {lat: 67.9386153, lon: 32.9359719}) {
    ...WeatherData
  }
  Murmansk: weatherByPoint(request: {lat: 69.007721, lon: 33.0685865}) {
    ...WeatherData
  }
  Olenegorsk: weatherByPoint(request: {lat: 68.1422058, lon: 33.2669407}) {
    ...WeatherData
  }
  Ostrovnoy: weatherByPoint(request: {lat: 68.0510344, lon: 39.5077846}) {
    ...WeatherData
  }
  PolyarnyeZori: weatherByPoint(request: {lat: 67.373084, lon: 32.4975636}) {
    ...WeatherData
  }
  Polyarnyy: weatherByPoint(request: {lat: 69.1989583, lon: 33.4508591}) {
    ...WeatherData
  }
  Severomorsk: weatherByPoint(request: {lat: 69.0766801, lon: 33.4177759}) {
    ...WeatherData
  }
  Snezhnogorsk: weatherByPoint(request: {lat: 69.1921409, lon: 33.2383502}) {
    ...WeatherData
  }
  NaryanMar: weatherByPoint(request: {lat: 67.6379672, lon: 53.0069565}) {
    ...WeatherData
  }
  Arzamas: weatherByPoint(request: {lat: 55.3945814, lon: 43.8408141}) {
    ...WeatherData
  }
  Balahna: weatherByPoint(request: {lat: 56.495036, lon: 43.5758423}) {
    ...WeatherData
  }
  Bogorodsk: weatherByPoint(request: {lat: 56.1020828, lon: 43.5135442}) {
    ...WeatherData
  }
  Bor: weatherByPoint(request: {lat: 56.3565458, lon: 44.0646481}) {
    ...WeatherData
  }
  Vetluga: weatherByPoint(request: {lat: 57.8559204, lon: 45.7761957}) {
    ...WeatherData
  }
  Volodarsk: weatherByPoint(request: {lat: 56.2169751, lon: 43.1596417}) {
    ...WeatherData
  }
  Vorsma: weatherByPoint(request: {lat: 55.989943, lon: 43.2718859}) {
    ...WeatherData
  }
  Vyksa: weatherByPoint(request: {lat: 55.3207727, lon: 42.1678834}) {
    ...WeatherData
  }
  Gorbatov: weatherByPoint(request: {lat: 56.1307769, lon: 43.0626185}) {
    ...WeatherData
  }
  Gorodets: weatherByPoint(request: {lat: 56.6449218, lon: 43.4723104}) {
    ...WeatherData
  }
  Dzerzhinsk: weatherByPoint(request: {lat: 56.2376047, lon: 43.4599416}) {
    ...WeatherData
  }
  Zavolzhe: weatherByPoint(request: {lat: 56.6404286, lon: 43.3872492}) {
    ...WeatherData
  }
  Knyaginino: weatherByPoint(request: {lat: 55.8205915, lon: 45.032337}) {
    ...WeatherData
  }
  Kstovo: weatherByPoint(request: {lat: 56.1432084, lon: 44.1664198}) {
    ...WeatherData
  }
  Kulebaki: weatherByPoint(request: {lat: 55.4296181, lon: 42.5125538}) {
    ...WeatherData
  }
  Lukoyanov: weatherByPoint(request: {lat: 55.0326225, lon: 44.4933807}) {
    ...WeatherData
  }
  Lyskovo: weatherByPoint(request: {lat: 56.0262359, lon: 45.035771}) {
    ...WeatherData
  }
  Navashino: weatherByPoint(request: {lat: 55.543811, lon: 42.1887089}) {
    ...WeatherData
  }
  NizhniyNovgorod: weatherByPoint(request: {lat: 56.3240627, lon: 44.0053913}) {
    ...WeatherData
  }
  Pavlovo: weatherByPoint(request: {lat: 55.9797564, lon: 43.0995042}) {
    ...WeatherData
  }
  Pervomaysk: weatherByPoint(request: {lat: 54.8675792, lon: 43.8013992}) {
    ...WeatherData
  }
  Perevoz: weatherByPoint(request: {lat: 55.5967718, lon: 44.5448369}) {
    ...WeatherData
  }
  Sarov: weatherByPoint(request: {lat: 54.9228268, lon: 43.3448089}) {
    ...WeatherData
  }
  Semenov: weatherByPoint(request: {lat: 56.7889794, lon: 44.4902885}) {
    ...WeatherData
  }
  Sergach: weatherByPoint(request: {lat: 55.5201515, lon: 45.4813231}) {
    ...WeatherData
  }
  Uren: weatherByPoint(request: {lat: 57.4612572, lon: 45.7833293}) {
    ...WeatherData
  }
  Chkalovsk: weatherByPoint(request: {lat: 56.7651262, lon: 43.242077}) {
    ...WeatherData
  }
  Shahunya: weatherByPoint(request: {lat: 57.6764293, lon: 46.6129009}) {
    ...WeatherData
  }
  Borovichi: weatherByPoint(request: {lat: 58.3840197, lon: 33.9175929}) {
    ...WeatherData
  }
  Valday: weatherByPoint(request: {lat: 57.9823766, lon: 33.2369436}) {
    ...WeatherData
  }
  VelikiyNovgorod: weatherByPoint(request: {lat: 58.5213846, lon: 31.2755394}) {
    ...WeatherData
  }
  MalayaVishera: weatherByPoint(request: {lat: 58.8458379, lon: 32.2247401}) {
    ...WeatherData
  }
  Okulovka: weatherByPoint(request: {lat: 58.3910296, lon: 33.2901557}) {
    ...WeatherData
  }
  Pestovo: weatherByPoint(request: {lat: 58.5973723, lon: 35.8143898}) {
    ...WeatherData
  }
  Soltsy: weatherByPoint(request: {lat: 58.1201281, lon: 30.309351}) {
    ...WeatherData
  }
  StarayaRussa: weatherByPoint(request: {lat: 57.990737, lon: 31.3554897}) {
    ...WeatherData
  }
  Holm: weatherByPoint(request: {lat: 57.145108, lon: 31.1787499}) {
    ...WeatherData
  }
  Chudovo: weatherByPoint(request: {lat: 59.1248394, lon: 31.6866241}) {
    ...WeatherData
  }
  Barabinsk: weatherByPoint(request: {lat: 55.35146, lon: 78.3464506}) {
    ...WeatherData
  }
  Berdsk: weatherByPoint(request: {lat: 54.7582156, lon: 83.1070605}) {
    ...WeatherData
  }
  Bolotnoe: weatherByPoint(request: {lat: 55.6692421, lon: 84.3906889}) {
    ...WeatherData
  }
  Iskitim: weatherByPoint(request: {lat: 54.6267603, lon: 83.2951244}) {
    ...WeatherData
  }
  Karasuk: weatherByPoint(request: {lat: 53.7343189, lon: 78.0422967}) {
    ...WeatherData
  }
  Kargat: weatherByPoint(request: {lat: 55.1945666, lon: 80.2829495}) {
    ...WeatherData
  }
  Kuybyshev: weatherByPoint(request: {lat: 55.4685094, lon: 78.3242048}) {
    ...WeatherData
  }
  Kupino: weatherByPoint(request: {lat: 54.366055, lon: 77.2973368}) {
    ...WeatherData
  }
  Novosibirsk: weatherByPoint(request: {lat: 55.028191, lon: 82.9211489}) {
    ...WeatherData
  }
  Ob: weatherByPoint(request: {lat: 54.9945576, lon: 82.6937181}) {
    ...WeatherData
  }
  Tatarsk: weatherByPoint(request: {lat: 55.2146167, lon: 75.9739914}) {
    ...WeatherData
  }
  Toguchin: weatherByPoint(request: {lat: 55.2251631, lon: 84.4104118}) {
    ...WeatherData
  }
  Cherepanovo: weatherByPoint(request: {lat: 54.2206476, lon: 83.3724521}) {
    ...WeatherData
  }
  Chulym: weatherByPoint(request: {lat: 55.0906867, lon: 80.9592508}) {
    ...WeatherData
  }
  Isilkul: weatherByPoint(request: {lat: 54.9096002, lon: 71.2816284}) {
    ...WeatherData
  }
  Kalachinsk: weatherByPoint(request: {lat: 55.0598155, lon: 74.5653644}) {
    ...WeatherData
  }
  Nazyvaevsk: weatherByPoint(request: {lat: 55.5689323, lon: 71.3503426}) {
    ...WeatherData
  }
  Omsk: weatherByPoint(request: {lat: 54.9848566, lon: 73.3674517}) {
    ...WeatherData
  }
  Tara: weatherByPoint(request: {lat: 56.9160511, lon: 74.3649194}) {
    ...WeatherData
  }
  Tyukalinsk: weatherByPoint(request: {lat: 55.8703415, lon: 72.1954747}) {
    ...WeatherData
  }
  Abdulino: weatherByPoint(request: {lat: 53.6778906, lon: 53.6472483}) {
    ...WeatherData
  }
  Buguruslan: weatherByPoint(request: {lat: 53.6523728, lon: 52.4326853}) {
    ...WeatherData
  }
  Buzuluk: weatherByPoint(request: {lat: 52.7881277, lon: 52.2624877}) {
    ...WeatherData
  }
  Gay: weatherByPoint(request: {lat: 51.4649189, lon: 58.4436875}) {
    ...WeatherData
  }
  Kuvandyk: weatherByPoint(request: {lat: 51.4783857, lon: 57.3612636}) {
    ...WeatherData
  }
  Mednogorsk: weatherByPoint(request: {lat: 51.4037617, lon: 57.583163}) {
    ...WeatherData
  }
  Novotroitsk: weatherByPoint(request: {lat: 51.1964202, lon: 58.3018192}) {
    ...WeatherData
  }
  Orenburg: weatherByPoint(request: {lat: 51.7875092, lon: 55.1018828}) {
    ...WeatherData
  }
  Orsk: weatherByPoint(request: {lat: 51.2294282, lon: 58.4752777}) {
    ...WeatherData
  }
  SolIletsk: weatherByPoint(request: {lat: 51.1633736, lon: 54.9896726}) {
    ...WeatherData
  }
  Sorochinsk: weatherByPoint(request: {lat: 52.426685, lon: 53.1542745}) {
    ...WeatherData
  }
  Yasnyy: weatherByPoint(request: {lat: 51.036838, lon: 59.874344}) {
    ...WeatherData
  }
  Bolhov: weatherByPoint(request: {lat: 53.4438496, lon: 36.0076833}) {
    ...WeatherData
  }
  Dmitrovsk: weatherByPoint(request: {lat: 52.5054851, lon: 35.1415009}) {
    ...WeatherData
  }
  Livny: weatherByPoint(request: {lat: 52.4284558, lon: 37.6039506}) {
    ...WeatherData
  }
  Maloarhangelsk: weatherByPoint(request: {lat: 52.4002192, lon: 36.5038579}) {
    ...WeatherData
  }
  Mtsensk: weatherByPoint(request: {lat: 53.2788438, lon: 36.5749105}) {
    ...WeatherData
  }
  Novosil: weatherByPoint(request: {lat: 52.97454, lon: 37.0437146}) {
    ...WeatherData
  }
  Oryol: weatherByPoint(request: {lat: 52.9671298, lon: 36.0696427}) {
    ...WeatherData
  }
  Belinskiy: weatherByPoint(request: {lat: 52.9640996, lon: 43.4183212}) {
    ...WeatherData
  }
  Gorodische: weatherByPoint(request: {lat: 53.2726916, lon: 45.7026142}) {
    ...WeatherData
  }
  Zarechnyy: weatherByPoint(request: {lat: 53.1960836, lon: 45.1689907}) {
    ...WeatherData
  }
  Kamenka: weatherByPoint(request: {lat: 53.1855463, lon: 44.0469717}) {
    ...WeatherData
  }
  Kuznetsk: weatherByPoint(request: {lat: 53.1130888, lon: 46.605092}) {
    ...WeatherData
  }
  NizhniyLomov: weatherByPoint(request: {lat: 53.5300905, lon: 43.6730217}) {
    ...WeatherData
  }
  Nikolsk_2: weatherByPoint(request: {lat: 53.7137496, lon: 46.0799857}) {
    ...WeatherData
  }
  Penza: weatherByPoint(request: {lat: 53.1753314, lon: 45.0348625}) {
    ...WeatherData
  }
  Serdobsk: weatherByPoint(request: {lat: 52.4697595, lon: 44.2122414}) {
    ...WeatherData
  }
  Spassk: weatherByPoint(request: {lat: 53.9271974, lon: 43.1859073}) {
    ...WeatherData
  }
  Sursk: weatherByPoint(request: {lat: 53.0761357, lon: 45.6910796}) {
    ...WeatherData
  }
  Aleksandrovsk: weatherByPoint(request: {lat: 59.1613221, lon: 57.5763459}) {
    ...WeatherData
  }
  Berezniki: weatherByPoint(request: {lat: 59.4079923, lon: 56.8039427}) {
    ...WeatherData
  }
  Vereschagino: weatherByPoint(request: {lat: 58.0797571, lon: 54.6581309}) {
    ...WeatherData
  }
  Gornozavodsk: weatherByPoint(request: {lat: 58.3742532, lon: 58.3231716}) {
    ...WeatherData
  }
  Gremyachinsk: weatherByPoint(request: {lat: 58.5626082, lon: 57.8520572}) {
    ...WeatherData
  }
  Gubaha: weatherByPoint(request: {lat: 58.8371721, lon: 57.554533}) {
    ...WeatherData
  }
  Dobryanka: weatherByPoint(request: {lat: 58.469685, lon: 56.4130737}) {
    ...WeatherData
  }
  Kizel: weatherByPoint(request: {lat: 59.0512783, lon: 57.6471028}) {
    ...WeatherData
  }
  Krasnovishersk: weatherByPoint(request: {lat: 60.3901321, lon: 57.0535682}) {
    ...WeatherData
  }
  Krasnokamsk: weatherByPoint(request: {lat: 58.0822065, lon: 55.7479936}) {
    ...WeatherData
  }
  Kudymkar: weatherByPoint(request: {lat: 59.0167925, lon: 54.6572508}) {
    ...WeatherData
  }
  Kungur: weatherByPoint(request: {lat: 57.4283296, lon: 56.9438656}) {
    ...WeatherData
  }
  Lysva: weatherByPoint(request: {lat: 58.0995875, lon: 57.8086825}) {
    ...WeatherData
  }
  Nytva: weatherByPoint(request: {lat: 57.9336725, lon: 55.3356084}) {
    ...WeatherData
  }
  Osa: weatherByPoint(request: {lat: 57.2889515, lon: 55.4688668}) {
    ...WeatherData
  }
  Ohansk: weatherByPoint(request: {lat: 57.7180034, lon: 55.3872469}) {
    ...WeatherData
  }
  Ocher: weatherByPoint(request: {lat: 57.8852686, lon: 54.7161091}) {
    ...WeatherData
  }
  Perm: weatherByPoint(request: {lat: 58.0102583, lon: 56.2342034}) {
    ...WeatherData
  }
  Solikamsk: weatherByPoint(request: {lat: 59.6482998, lon: 56.771009}) {
    ...WeatherData
  }
  Usole: weatherByPoint(request: {lat: 59.4277573, lon: 56.6837872}) {
    ...WeatherData
  }
  Chaykovskiy: weatherByPoint(request: {lat: 56.7781501, lon: 54.1477965}) {
    ...WeatherData
  }
  Cherdyn: weatherByPoint(request: {lat: 60.4011933, lon: 56.4799933}) {
    ...WeatherData
  }
  Chermoz: weatherByPoint(request: {lat: 58.7842834, lon: 56.1507138}) {
    ...WeatherData
  }
  Chernushka: weatherByPoint(request: {lat: 56.5160768, lon: 56.0763049}) {
    ...WeatherData
  }
  Chusovoy: weatherByPoint(request: {lat: 58.2974596, lon: 57.8193615}) {
    ...WeatherData
  }
  Arsenev: weatherByPoint(request: {lat: 44.1622031, lon: 133.2696209}) {
    ...WeatherData
  }
  Artem: weatherByPoint(request: {lat: 43.3501675, lon: 132.1596175}) {
    ...WeatherData
  }
  BolshoyKamen: weatherByPoint(request: {lat: 43.1111742, lon: 132.3480082}) {
    ...WeatherData
  }
  Vladivostok: weatherByPoint(request: {lat: 43.1164904, lon: 131.8823937}) {
    ...WeatherData
  }
  Dalnegorsk: weatherByPoint(request: {lat: 44.5539457, lon: 135.5662716}) {
    ...WeatherData
  }
  Dalnerechensk: weatherByPoint(request: {lat: 45.9308483, lon: 133.7316907}) {
    ...WeatherData
  }
  Lesozavodsk: weatherByPoint(request: {lat: 45.4780092, lon: 133.4186199}) {
    ...WeatherData
  }
  Nahodka: weatherByPoint(request: {lat: 42.8239372, lon: 132.8927361}) {
    ...WeatherData
  }
  Partizansk: weatherByPoint(request: {lat: 43.1280578, lon: 133.1264567}) {
    ...WeatherData
  }
  SpasskDalniy: weatherByPoint(request: {lat: 44.5901175, lon: 132.8157288}) {
    ...WeatherData
  }
  Ussuriysk: weatherByPoint(request: {lat: 43.7971818, lon: 131.9518229}) {
    ...WeatherData
  }
  Fokino_2: weatherByPoint(request: {lat: 42.9706317, lon: 132.4110196}) {
    ...WeatherData
  }
  VelikieLuki: weatherByPoint(request: {lat: 56.332208, lon: 30.5508641}) {
    ...WeatherData
  }
  Gdov: weatherByPoint(request: {lat: 58.7432429, lon: 27.8264809}) {
    ...WeatherData
  }
  Dno: weatherByPoint(request: {lat: 57.826974, lon: 29.9629389}) {
    ...WeatherData
  }
  Nevel: weatherByPoint(request: {lat: 56.0201973, lon: 29.9239983}) {
    ...WeatherData
  }
  Novorzhev: weatherByPoint(request: {lat: 57.029807, lon: 29.3433083}) {
    ...WeatherData
  }
  Novosokolniki: weatherByPoint(request: {lat: 56.3408431, lon: 30.1527573}) {
    ...WeatherData
  }
  Opochka: weatherByPoint(request: {lat: 56.710725, lon: 28.6717519}) {
    ...WeatherData
  }
  Ostrov: weatherByPoint(request: {lat: 57.3451528, lon: 28.3437593}) {
    ...WeatherData
  }
  Pechory: weatherByPoint(request: {lat: 57.8145817, lon: 27.622259}) {
    ...WeatherData
  }
  Porhov: weatherByPoint(request: {lat: 57.7765219, lon: 29.5436626}) {
    ...WeatherData
  }
  Pskov: weatherByPoint(request: {lat: 57.8194415, lon: 28.3317198}) {
    ...WeatherData
  }
  Pustoshka: weatherByPoint(request: {lat: 56.3374813, lon: 29.3668055}) {
    ...WeatherData
  }
  Pytalovo: weatherByPoint(request: {lat: 57.0637952, lon: 27.9236214}) {
    ...WeatherData
  }
  Sebezh: weatherByPoint(request: {lat: 56.2908554, lon: 28.4724326}) {
    ...WeatherData
  }
  Azov: weatherByPoint(request: {lat: 47.1121589, lon: 39.4232555}) {
    ...WeatherData
  }
  Aksay: weatherByPoint(request: {lat: 47.2676314, lon: 39.8756872}) {
    ...WeatherData
  }
  Bataysk: weatherByPoint(request: {lat: 47.1383299, lon: 39.7507179}) {
    ...WeatherData
  }
  BelayaKalitva: weatherByPoint(request: {lat: 48.1769737, lon: 40.8033529}) {
    ...WeatherData
  }
  Volgodonsk: weatherByPoint(request: {lat: 47.5165338, lon: 42.1984951}) {
    ...WeatherData
  }
  Gukovo: weatherByPoint(request: {lat: 48.0448904, lon: 39.9484672}) {
    ...WeatherData
  }
  Donetsk: weatherByPoint(request: {lat: 48.3350706, lon: 39.945891}) {
    ...WeatherData
  }
  Zverevo: weatherByPoint(request: {lat: 48.0435487, lon: 40.1265822}) {
    ...WeatherData
  }
  Zernograd: weatherByPoint(request: {lat: 46.8495958, lon: 40.312837}) {
    ...WeatherData
  }
  KamenskShahtinskiy: weatherByPoint(request: {lat: 48.3205326, lon: 40.2689583}) {
    ...WeatherData
  }
  Konstantinovsk: weatherByPoint(request: {lat: 47.5773717, lon: 41.0967445}) {
    ...WeatherData
  }
  KrasnyySulin: weatherByPoint(request: {lat: 47.8831311, lon: 40.0781298}) {
    ...WeatherData
  }
  Millerovo: weatherByPoint(request: {lat: 48.9260077, lon: 40.3984087}) {
    ...WeatherData
  }
  Morozovsk: weatherByPoint(request: {lat: 48.3511807, lon: 41.8309225}) {
    ...WeatherData
  }
  Novocherkassk: weatherByPoint(request: {lat: 47.411919, lon: 40.1042098}) {
    ...WeatherData
  }
  Novoshahtinsk: weatherByPoint(request: {lat: 47.757773, lon: 39.9363697}) {
    ...WeatherData
  }
  Proletarsk: weatherByPoint(request: {lat: 46.7038963, lon: 41.727594}) {
    ...WeatherData
  }
  RostovNaDonu: weatherByPoint(request: {lat: 47.2224566, lon: 39.718803}) {
    ...WeatherData
  }
  Salsk: weatherByPoint(request: {lat: 46.4752095, lon: 41.5410415}) {
    ...WeatherData
  }
  Semikarakorsk: weatherByPoint(request: {lat: 47.5177337, lon: 40.8114167}) {
    ...WeatherData
  }
  Taganrog: weatherByPoint(request: {lat: 47.2094917, lon: 38.9350989}) {
    ...WeatherData
  }
  Tsimlyansk: weatherByPoint(request: {lat: 47.6477448, lon: 42.0931505}) {
    ...WeatherData
  }
  Shahty: weatherByPoint(request: {lat: 47.7085287, lon: 40.2159846}) {
    ...WeatherData
  }
  Kasimov: weatherByPoint(request: {lat: 54.9373475, lon: 41.3913211}) {
    ...WeatherData
  }
  Korablino: weatherByPoint(request: {lat: 53.9246659, lon: 40.0227745}) {
    ...WeatherData
  }
  Mihaylov: weatherByPoint(request: {lat: 54.2297402, lon: 39.0091481}) {
    ...WeatherData
  }
  Novomichurinsk: weatherByPoint(request: {lat: 54.0376572, lon: 39.74654}) {
    ...WeatherData
  }
  Rybnoe: weatherByPoint(request: {lat: 54.7256164, lon: 39.5134398}) {
    ...WeatherData
  }
  Ryazhsk: weatherByPoint(request: {lat: 53.7067584, lon: 40.0522274}) {
    ...WeatherData
  }
  Ryazan: weatherByPoint(request: {lat: 54.6254445, lon: 39.7358609}) {
    ...WeatherData
  }
  Sasovo: weatherByPoint(request: {lat: 54.3508885, lon: 41.9117422}) {
    ...WeatherData
  }
  Skopin: weatherByPoint(request: {lat: 53.823543, lon: 39.5492421}) {
    ...WeatherData
  }
  SpasKlepiki: weatherByPoint(request: {lat: 55.1291721, lon: 40.1745338}) {
    ...WeatherData
  }
  SpasskRyazanskiy: weatherByPoint(request: {lat: 54.4070719, lon: 40.3763426}) {
    ...WeatherData
  }
  Shatsk: weatherByPoint(request: {lat: 54.0287312, lon: 41.7181803}) {
    ...WeatherData
  }
  Zhigulevsk: weatherByPoint(request: {lat: 53.4011981, lon: 49.4945176}) {
    ...WeatherData
  }
  Kinel: weatherByPoint(request: {lat: 53.2210298, lon: 50.6343776}) {
    ...WeatherData
  }
  Neftegorsk: weatherByPoint(request: {lat: 52.7972914, lon: 51.1637392}) {
    ...WeatherData
  }
  Novokuybyshevsk: weatherByPoint(request: {lat: 53.0994565, lon: 49.9477382}) {
    ...WeatherData
  }
  Oktyabrsk: weatherByPoint(request: {lat: 53.1640488, lon: 48.670762}) {
    ...WeatherData
  }
  Otradnyy: weatherByPoint(request: {lat: 53.3800848, lon: 51.3438605}) {
    ...WeatherData
  }
  Pohvistnevo: weatherByPoint(request: {lat: 53.6498299, lon: 52.1235156}) {
    ...WeatherData
  }
  Samara: weatherByPoint(request: {lat: 53.1950306, lon: 50.1069518}) {
    ...WeatherData
  }
  Syzran: weatherByPoint(request: {lat: 53.1558674, lon: 48.4744629}) {
    ...WeatherData
  }
  Tolyatti: weatherByPoint(request: {lat: 53.5205348, lon: 49.3894028}) {
    ...WeatherData
  }
  Chapaevsk: weatherByPoint(request: {lat: 52.928961, lon: 49.8673269}) {
    ...WeatherData
  }
  SanktPeterburg: weatherByPoint(request: {lat: 59.9391313, lon: 30.3159004}) {
    ...WeatherData
  }
  Arkadak: weatherByPoint(request: {lat: 51.938831, lon: 43.4999221}) {
    ...WeatherData
  }
  Atkarsk: weatherByPoint(request: {lat: 51.8736062, lon: 45.0003247}) {
    ...WeatherData
  }
  Balakovo: weatherByPoint(request: {lat: 52.0224231, lon: 47.7827765}) {
    ...WeatherData
  }
  Balashov: weatherByPoint(request: {lat: 51.5388697, lon: 43.1839757}) {
    ...WeatherData
  }
  Volsk: weatherByPoint(request: {lat: 52.0459865, lon: 47.3873595}) {
    ...WeatherData
  }
  Ershov: weatherByPoint(request: {lat: 51.3508505, lon: 48.2762226}) {
    ...WeatherData
  }
  Kalininsk: weatherByPoint(request: {lat: 51.4993591, lon: 44.4710435}) {
    ...WeatherData
  }
  Krasnoarmeysk_2: weatherByPoint(request: {lat: 51.023541, lon: 45.695044}) {
    ...WeatherData
  }
  KrasnyyKut: weatherByPoint(request: {lat: 50.9598317, lon: 46.9712016}) {
    ...WeatherData
  }
  Marks: weatherByPoint(request: {lat: 51.7133337, lon: 46.7400339}) {
    ...WeatherData
  }
  Novouzensk: weatherByPoint(request: {lat: 50.455199, lon: 48.1413153}) {
    ...WeatherData
  }
  Petrovsk: weatherByPoint(request: {lat: 52.3094237, lon: 45.3851877}) {
    ...WeatherData
  }
  Pugachev: weatherByPoint(request: {lat: 52.0159921, lon: 48.7972223}) {
    ...WeatherData
  }
  Rtischevo: weatherByPoint(request: {lat: 52.2616271, lon: 43.7842248}) {
    ...WeatherData
  }
  Saratov: weatherByPoint(request: {lat: 51.533557, lon: 46.034257}) {
    ...WeatherData
  }
  Hvalynsk: weatherByPoint(request: {lat: 52.4951572, lon: 48.1045771}) {
    ...WeatherData
  }
  Shihany: weatherByPoint(request: {lat: 52.1147391, lon: 47.2023118}) {
    ...WeatherData
  }
  Engels: weatherByPoint(request: {lat: 51.4854003, lon: 46.126722}) {
    ...WeatherData
  }
  AleksandrovskSahalinskiy: weatherByPoint(
    request: {lat: 50.8974378, lon: 142.1578559}
  ) {
    ...WeatherData
  }
  Aniva: weatherByPoint(request: {lat: 46.713152, lon: 142.5265804}) {
    ...WeatherData
  }
  Dolinsk: weatherByPoint(request: {lat: 47.3255783, lon: 142.7945071}) {
    ...WeatherData
  }
  Korsakov: weatherByPoint(request: {lat: 46.6324545, lon: 142.799445}) {
    ...WeatherData
  }
  Kurilsk: weatherByPoint(request: {lat: 45.2270954, lon: 147.8796323}) {
    ...WeatherData
  }
  Makarov: weatherByPoint(request: {lat: 48.6236334, lon: 142.7803205}) {
    ...WeatherData
  }
  Nevelsk: weatherByPoint(request: {lat: 46.6526899, lon: 141.8630725}) {
    ...WeatherData
  }
  Oha: weatherByPoint(request: {lat: 53.5867839, lon: 142.9412411}) {
    ...WeatherData
  }
  Poronaysk: weatherByPoint(request: {lat: 49.238866, lon: 143.1008333}) {
    ...WeatherData
  }
  SeveroKurilsk: weatherByPoint(request: {lat: 50.6730577, lon: 156.1282211}) {
    ...WeatherData
  }
  Tomari: weatherByPoint(request: {lat: 47.7620108, lon: 142.0615837}) {
    ...WeatherData
  }
  Uglegorsk: weatherByPoint(request: {lat: 49.0815774, lon: 142.0692639}) {
    ...WeatherData
  }
  Holmsk: weatherByPoint(request: {lat: 47.0408423, lon: 142.041688}) {
    ...WeatherData
  }
  YuzhnoSahalinsk: weatherByPoint(request: {lat: 46.9591631, lon: 142.737976}) {
    ...WeatherData
  }
  Alapaevsk: weatherByPoint(request: {lat: 57.8475571, lon: 61.6693817}) {
    ...WeatherData
  }
  Aramil: weatherByPoint(request: {lat: 56.694632, lon: 60.8343125}) {
    ...WeatherData
  }
  Artemovskiy: weatherByPoint(request: {lat: 57.3384177, lon: 61.8947443}) {
    ...WeatherData
  }
  Asbest: weatherByPoint(request: {lat: 57.0052277, lon: 61.4581156}) {
    ...WeatherData
  }
  Berezovskiy_2: weatherByPoint(request: {lat: 56.9095924, lon: 60.8180907}) {
    ...WeatherData
  }
  Bogdanovich: weatherByPoint(request: {lat: 56.7764795, lon: 62.0463679}) {
    ...WeatherData
  }
  VerhniyTagil: weatherByPoint(request: {lat: 57.3763758, lon: 59.9517653}) {
    ...WeatherData
  }
  VerhnyayaPyshma: weatherByPoint(request: {lat: 56.9758903, lon: 60.5650383}) {
    ...WeatherData
  }
  VerhnyayaSalda: weatherByPoint(request: {lat: 58.0465803, lon: 60.5560164}) {
    ...WeatherData
  }
  VerhnyayaTura: weatherByPoint(request: {lat: 58.3643685, lon: 59.8265235}) {
    ...WeatherData
  }
  Verhoture: weatherByPoint(request: {lat: 58.8622073, lon: 60.8103945}) {
    ...WeatherData
  }
  Volchansk: weatherByPoint(request: {lat: 59.9351707, lon: 60.0798618}) {
    ...WeatherData
  }
  Degtyarsk: weatherByPoint(request: {lat: 56.7048206, lon: 60.079138}) {
    ...WeatherData
  }
  Ekaterinburg: weatherByPoint(request: {lat: 56.8385216, lon: 60.6054911}) {
    ...WeatherData
  }
  Zarechnyy_2: weatherByPoint(request: {lat: 56.8102931, lon: 61.3380029}) {
    ...WeatherData
  }
  Ivdel: weatherByPoint(request: {lat: 60.6944496, lon: 60.4245069}) {
    ...WeatherData
  }
  Irbit: weatherByPoint(request: {lat: 57.6838362, lon: 63.057675}) {
    ...WeatherData
  }
  KamenskUralskiy: weatherByPoint(request: {lat: 56.414962, lon: 61.9188674}) {
    ...WeatherData
  }
  Kamyshlov: weatherByPoint(request: {lat: 56.8465034, lon: 62.7119766}) {
    ...WeatherData
  }
  Karpinsk: weatherByPoint(request: {lat: 59.7665925, lon: 60.0011703}) {
    ...WeatherData
  }
  Kachkanar: weatherByPoint(request: {lat: 58.7051762, lon: 59.4839155}) {
    ...WeatherData
  }
  Kirovgrad: weatherByPoint(request: {lat: 57.4299433, lon: 60.0624051}) {
    ...WeatherData
  }
  Krasnoturinsk: weatherByPoint(request: {lat: 59.7636635, lon: 60.1934525}) {
    ...WeatherData
  }
  Krasnouralsk: weatherByPoint(request: {lat: 58.348651, lon: 60.0408764}) {
    ...WeatherData
  }
  Krasnoufimsk: weatherByPoint(request: {lat: 56.612387, lon: 57.7636637}) {
    ...WeatherData
  }
  Kushva: weatherByPoint(request: {lat: 58.2826013, lon: 59.7645766}) {
    ...WeatherData
  }
  Lesnoy: weatherByPoint(request: {lat: 58.6348516, lon: 59.7981565}) {
    ...WeatherData
  }
  Mihaylovsk: weatherByPoint(request: {lat: 56.4370039, lon: 59.1137316}) {
    ...WeatherData
  }
  Nevyansk: weatherByPoint(request: {lat: 57.49131, lon: 60.2183429}) {
    ...WeatherData
  }
  NizhnieSergi: weatherByPoint(request: {lat: 56.6544959, lon: 59.2953035}) {
    ...WeatherData
  }
  NizhniyTagil: weatherByPoint(request: {lat: 57.910126, lon: 59.9812853}) {
    ...WeatherData
  }
  NizhnyayaSalda: weatherByPoint(request: {lat: 58.0748272, lon: 60.7025418}) {
    ...WeatherData
  }
  NizhnyayaTura: weatherByPoint(request: {lat: 58.6309267, lon: 59.8520344}) {
    ...WeatherData
  }
  NovayaLyalya: weatherByPoint(request: {lat: 59.0538977, lon: 60.5944825}) {
    ...WeatherData
  }
  Novouralsk: weatherByPoint(request: {lat: 57.2472567, lon: 60.0956714}) {
    ...WeatherData
  }
  Pervouralsk: weatherByPoint(request: {lat: 56.9080085, lon: 59.942926}) {
    ...WeatherData
  }
  Polevskoy: weatherByPoint(request: {lat: 56.4956952, lon: 60.2365298}) {
    ...WeatherData
  }
  Revda: weatherByPoint(request: {lat: 56.7986319, lon: 59.9071591}) {
    ...WeatherData
  }
  Rezh: weatherByPoint(request: {lat: 57.3717477, lon: 61.3833842}) {
    ...WeatherData
  }
  Severouralsk: weatherByPoint(request: {lat: 60.1533109, lon: 59.9525245}) {
    ...WeatherData
  }
  Serov: weatherByPoint(request: {lat: 59.6047724, lon: 60.5753882}) {
    ...WeatherData
  }
  Sredneuralsk: weatherByPoint(request: {lat: 56.9918901, lon: 60.4771018}) {
    ...WeatherData
  }
  SuhoyLog: weatherByPoint(request: {lat: 56.9076193, lon: 62.0358093}) {
    ...WeatherData
  }
  Sysert: weatherByPoint(request: {lat: 56.5005715, lon: 60.8190003}) {
    ...WeatherData
  }
  Tavda: weatherByPoint(request: {lat: 58.0434672, lon: 65.274217}) {
    ...WeatherData
  }
  Talitsa: weatherByPoint(request: {lat: 57.0122687, lon: 63.7320757}) {
    ...WeatherData
  }
  Turinsk: weatherByPoint(request: {lat: 58.0393524, lon: 63.6981973}) {
    ...WeatherData
  }
  Sevastopol: weatherByPoint(request: {lat: 44.6167013, lon: 33.525355}) {
    ...WeatherData
  }
  Alagir: weatherByPoint(request: {lat: 43.0417684, lon: 44.2199715}) {
    ...WeatherData
  }
  Ardon: weatherByPoint(request: {lat: 43.1755152, lon: 44.2955775}) {
    ...WeatherData
  }
  Beslan: weatherByPoint(request: {lat: 43.1937529, lon: 44.5338707}) {
    ...WeatherData
  }
  Vladikavkaz: weatherByPoint(request: {lat: 43.020588, lon: 44.6819182}) {
    ...WeatherData
  }
  Digora: weatherByPoint(request: {lat: 43.1567628, lon: 44.1549483}) {
    ...WeatherData
  }
  Mozdok: weatherByPoint(request: {lat: 43.7471342, lon: 44.6569607}) {
    ...WeatherData
  }
  Velizh: weatherByPoint(request: {lat: 55.6057916, lon: 31.1856206}) {
    ...WeatherData
  }
  Vyazma: weatherByPoint(request: {lat: 55.2116983, lon: 34.2951663}) {
    ...WeatherData
  }
  Gagarin: weatherByPoint(request: {lat: 55.5525228, lon: 34.9950502}) {
    ...WeatherData
  }
  Demidov: weatherByPoint(request: {lat: 55.2682105, lon: 31.5062809}) {
    ...WeatherData
  }
  Desnogorsk: weatherByPoint(request: {lat: 54.146457, lon: 33.2833222}) {
    ...WeatherData
  }
  Dorogobuzh: weatherByPoint(request: {lat: 54.9136959, lon: 33.3023162}) {
    ...WeatherData
  }
  Duhovschina: weatherByPoint(request: {lat: 55.1950257, lon: 32.401252}) {
    ...WeatherData
  }
  Elnya: weatherByPoint(request: {lat: 54.5837795, lon: 33.1749867}) {
    ...WeatherData
  }
  Pochinok: weatherByPoint(request: {lat: 54.406244, lon: 32.4398039}) {
    ...WeatherData
  }
  Roslavl: weatherByPoint(request: {lat: 53.9449558, lon: 32.8480258}) {
    ...WeatherData
  }
  Rudnya: weatherByPoint(request: {lat: 54.9441093, lon: 31.0794806}) {
    ...WeatherData
  }
  Safonovo: weatherByPoint(request: {lat: 55.1199661, lon: 33.2336988}) {
    ...WeatherData
  }
  Smolensk: weatherByPoint(request: {lat: 54.782635, lon: 32.045251}) {
    ...WeatherData
  }
  Sychevka: weatherByPoint(request: {lat: 55.8308821, lon: 34.2778793}) {
    ...WeatherData
  }
  Yartsevo: weatherByPoint(request: {lat: 55.0564732, lon: 32.6902302}) {
    ...WeatherData
  }
  Blagodarnyy: weatherByPoint(request: {lat: 45.0989782, lon: 43.4306455}) {
    ...WeatherData
  }
  Budennovsk: weatherByPoint(request: {lat: 44.7816067, lon: 44.1650339}) {
    ...WeatherData
  }
  Georgievsk: weatherByPoint(request: {lat: 44.1485694, lon: 43.4739851}) {
    ...WeatherData
  }
  Essentuki: weatherByPoint(request: {lat: 44.0446186, lon: 42.8588653}) {
    ...WeatherData
  }
  Zheleznovodsk: weatherByPoint(request: {lat: 44.1320568, lon: 43.0306461}) {
    ...WeatherData
  }
  Zelenokumsk: weatherByPoint(request: {lat: 44.4032668, lon: 43.8841877}) {
    ...WeatherData
  }
  Izobilnyy: weatherByPoint(request: {lat: 45.3684296, lon: 41.708702}) {
    ...WeatherData
  }
  Ipatovo: weatherByPoint(request: {lat: 45.7181751, lon: 42.8970206}) {
    ...WeatherData
  }
  Kislovodsk: weatherByPoint(request: {lat: 43.9052044, lon: 42.7168721}) {
    ...WeatherData
  }
  Lermontov: weatherByPoint(request: {lat: 44.1054107, lon: 42.973135}) {
    ...WeatherData
  }
  MineralnyeVody: weatherByPoint(request: {lat: 44.2087273, lon: 43.138408}) {
    ...WeatherData
  }
  Mihaylovsk_2: weatherByPoint(request: {lat: 45.1297323, lon: 42.0288443}) {
    ...WeatherData
  }
  Nevinnomyssk: weatherByPoint(request: {lat: 44.6226031, lon: 41.9476723}) {
    ...WeatherData
  }
  Neftekumsk: weatherByPoint(request: {lat: 44.7544552, lon: 44.9865347}) {
    ...WeatherData
  }
  Novoaleksandrovsk: weatherByPoint(request: {lat: 45.4932733, lon: 41.2153996}) {
    ...WeatherData
  }
  Novopavlovsk: weatherByPoint(request: {lat: 43.9617097, lon: 43.6342865}) {
    ...WeatherData
  }
  Pyatigorsk: weatherByPoint(request: {lat: 44.041091, lon: 43.0661553}) {
    ...WeatherData
  }
  Svetlograd: weatherByPoint(request: {lat: 45.328659, lon: 42.8565714}) {
    ...WeatherData
  }
  Stavropol: weatherByPoint(request: {lat: 45.044516, lon: 41.9689655}) {
    ...WeatherData
  }
  Zherdevka: weatherByPoint(request: {lat: 51.8422192, lon: 41.4617687}) {
    ...WeatherData
  }
  Kirsanov: weatherByPoint(request: {lat: 52.6506335, lon: 42.7286445}) {
    ...WeatherData
  }
  Kotovsk: weatherByPoint(request: {lat: 52.5924489, lon: 41.5101237}) {
    ...WeatherData
  }
  Michurinsk: weatherByPoint(request: {lat: 52.8912389, lon: 40.5104443}) {
    ...WeatherData
  }
  Morshansk: weatherByPoint(request: {lat: 53.4436216, lon: 41.8115478}) {
    ...WeatherData
  }
  Rasskazovo: weatherByPoint(request: {lat: 52.6538833, lon: 41.874285}) {
    ...WeatherData
  }
  Tambov: weatherByPoint(request: {lat: 52.7213154, lon: 41.452264}) {
    ...WeatherData
  }
  Uvarovo: weatherByPoint(request: {lat: 51.9767841, lon: 42.2529799}) {
    ...WeatherData
  }
  Agryz: weatherByPoint(request: {lat: 56.5232864, lon: 52.9943775}) {
    ...WeatherData
  }
  Aznakaevo: weatherByPoint(request: {lat: 54.8598642, lon: 53.0745527}) {
    ...WeatherData
  }
  Almetevsk: weatherByPoint(request: {lat: 54.9014619, lon: 52.2970467}) {
    ...WeatherData
  }
  Arsk: weatherByPoint(request: {lat: 56.0912567, lon: 49.877067}) {
    ...WeatherData
  }
  Bavly: weatherByPoint(request: {lat: 54.4062891, lon: 53.2458065}) {
    ...WeatherData
  }
  Bolgar: weatherByPoint(request: {lat: 54.974891, lon: 49.0303882}) {
    ...WeatherData
  }
  Bugulma: weatherByPoint(request: {lat: 54.5363495, lon: 52.7895849}) {
    ...WeatherData
  }
  Buinsk: weatherByPoint(request: {lat: 54.9641538, lon: 48.2901209}) {
    ...WeatherData
  }
  Elabuga: weatherByPoint(request: {lat: 55.7567107, lon: 52.0543794}) {
    ...WeatherData
  }
  Zainsk: weatherByPoint(request: {lat: 55.299053, lon: 52.0062972}) {
    ...WeatherData
  }
  Zelenodolsk: weatherByPoint(request: {lat: 55.8466651, lon: 48.5010954}) {
    ...WeatherData
  }
  Innopolis: weatherByPoint(request: {lat: 55.7521699, lon: 48.7446846}) {
    ...WeatherData
  }
  Kazan: weatherByPoint(request: {lat: 55.7943584, lon: 49.1114975}) {
    ...WeatherData
  }
  Kukmor: weatherByPoint(request: {lat: 56.1861392, lon: 50.8970238}) {
    ...WeatherData
  }
  Laishevo: weatherByPoint(request: {lat: 55.4042867, lon: 49.5499838}) {
    ...WeatherData
  }
  Leninogorsk: weatherByPoint(request: {lat: 54.5967034, lon: 52.4431906}) {
    ...WeatherData
  }
  Mamadysh: weatherByPoint(request: {lat: 55.7150413, lon: 51.4129016}) {
    ...WeatherData
  }
  Mendeleevsk: weatherByPoint(request: {lat: 55.895169, lon: 52.3143347}) {
    ...WeatherData
  }
  Menzelinsk: weatherByPoint(request: {lat: 55.7270698, lon: 53.1003968}) {
    ...WeatherData
  }
  NaberezhnyeChelny: weatherByPoint(request: {lat: 55.7434619, lon: 52.3959165}) {
    ...WeatherData
  }
  Nizhnekamsk: weatherByPoint(request: {lat: 55.6313609, lon: 51.8144669}) {
    ...WeatherData
  }
  Nurlat: weatherByPoint(request: {lat: 54.4281461, lon: 50.8049337}) {
    ...WeatherData
  }
  Tetyushi: weatherByPoint(request: {lat: 54.936516, lon: 48.8314533}) {
    ...WeatherData
  }
  Chistopol: weatherByPoint(request: {lat: 55.3699139, lon: 50.6285784}) {
    ...WeatherData
  }
  Andreapol: weatherByPoint(request: {lat: 56.6506724, lon: 32.2620163}) {
    ...WeatherData
  }
  Bezhetsk: weatherByPoint(request: {lat: 57.7860089, lon: 36.6904983}) {
    ...WeatherData
  }
  Belyy: weatherByPoint(request: {lat: 55.8339056, lon: 32.9389741}) {
    ...WeatherData
  }
  Bologoe: weatherByPoint(request: {lat: 57.8855767, lon: 34.0537771}) {
    ...WeatherData
  }
  Vesegonsk: weatherByPoint(request: {lat: 58.6582598, lon: 37.2567558}) {
    ...WeatherData
  }
  VyshniyVolochek: weatherByPoint(request: {lat: 57.568302, lon: 34.5404016}) {
    ...WeatherData
  }
  ZapadnayaDvina: weatherByPoint(request: {lat: 56.2566492, lon: 32.0805315}) {
    ...WeatherData
  }
  Zubtsov: weatherByPoint(request: {lat: 56.1760868, lon: 34.5825515}) {
    ...WeatherData
  }
  Kalyazin: weatherByPoint(request: {lat: 57.2579478, lon: 37.7819693}) {
    ...WeatherData
  }
  Kashin: weatherByPoint(request: {lat: 57.360194, lon: 37.6119436}) {
    ...WeatherData
  }
  Kimry: weatherByPoint(request: {lat: 56.8733213, lon: 37.3556605}) {
    ...WeatherData
  }
  Konakovo: weatherByPoint(request: {lat: 56.7275204, lon: 36.8012716}) {
    ...WeatherData
  }
  KrasnyyHolm: weatherByPoint(request: {lat: 58.0571446, lon: 37.1126156}) {
    ...WeatherData
  }
  Kuvshinovo: weatherByPoint(request: {lat: 57.0265168, lon: 34.1676009}) {
    ...WeatherData
  }
  Lihoslavl: weatherByPoint(request: {lat: 57.1221304, lon: 35.4667605}) {
    ...WeatherData
  }
  Nelidovo: weatherByPoint(request: {lat: 56.2232566, lon: 32.7767459}) {
    ...WeatherData
  }
  Ostashkov: weatherByPoint(request: {lat: 57.1456744, lon: 33.1115372}) {
    ...WeatherData
  }
  Rzhev: weatherByPoint(request: {lat: 56.262881, lon: 34.3291002}) {
    ...WeatherData
  }
  Staritsa: weatherByPoint(request: {lat: 56.514876, lon: 34.9336396}) {
    ...WeatherData
  }
  Tver: weatherByPoint(request: {lat: 56.8586059, lon: 35.9116761}) {
    ...WeatherData
  }
  Torzhok: weatherByPoint(request: {lat: 57.04133, lon: 34.9602344}) {
    ...WeatherData
  }
  Toropets: weatherByPoint(request: {lat: 56.5012188, lon: 31.6355466}) {
    ...WeatherData
  }
  Udomlya: weatherByPoint(request: {lat: 57.8787314, lon: 35.0167348}) {
    ...WeatherData
  }
  Asino: weatherByPoint(request: {lat: 56.9907085, lon: 86.1765257}) {
    ...WeatherData
  }
  Kedrovyy: weatherByPoint(request: {lat: 57.561869, lon: 79.5677821}) {
    ...WeatherData
  }
  Kolpashevo: weatherByPoint(request: {lat: 58.3114253, lon: 82.9025829}) {
    ...WeatherData
  }
  Seversk: weatherByPoint(request: {lat: 56.6031285, lon: 84.8809926}) {
    ...WeatherData
  }
  Strezhevoy: weatherByPoint(request: {lat: 60.732895, lon: 77.604122}) {
    ...WeatherData
  }
  Tomsk: weatherByPoint(request: {lat: 56.4845804, lon: 84.9481582}) {
    ...WeatherData
  }
  Aleksin: weatherByPoint(request: {lat: 54.5083349, lon: 37.0478067}) {
    ...WeatherData
  }
  Belev: weatherByPoint(request: {lat: 53.8114179, lon: 36.1382247}) {
    ...WeatherData
  }
  Bogoroditsk: weatherByPoint(request: {lat: 53.7701014, lon: 38.1225152}) {
    ...WeatherData
  }
  Bolohovo: weatherByPoint(request: {lat: 54.0820349, lon: 37.826724}) {
    ...WeatherData
  }
  Venev: weatherByPoint(request: {lat: 54.3542315, lon: 38.2642236}) {
    ...WeatherData
  }
  Donskoy: weatherByPoint(request: {lat: 53.9678944, lon: 38.3371824}) {
    ...WeatherData
  }
  Efremov: weatherByPoint(request: {lat: 53.1464766, lon: 38.0921657}) {
    ...WeatherData
  }
  Kimovsk: weatherByPoint(request: {lat: 53.9698378, lon: 38.5380808}) {
    ...WeatherData
  }
  Kireevsk: weatherByPoint(request: {lat: 53.9319555, lon: 37.9220351}) {
    ...WeatherData
  }
  Lipki: weatherByPoint(request: {lat: 53.9417551, lon: 37.7020148}) {
    ...WeatherData
  }
  Novomoskovsk: weatherByPoint(request: {lat: 54.0109075, lon: 38.2914024}) {
    ...WeatherData
  }
  Plavsk: weatherByPoint(request: {lat: 53.7096415, lon: 37.2862352}) {
    ...WeatherData
  }
  Sovetsk_3: weatherByPoint(request: {lat: 53.9338874, lon: 37.6316141}) {
    ...WeatherData
  }
  Suvorov: weatherByPoint(request: {lat: 54.1343585, lon: 36.4807419}) {
    ...WeatherData
  }
  Tula: weatherByPoint(request: {lat: 54.1920559, lon: 37.6153842}) {
    ...WeatherData
  }
  Uzlovaya: weatherByPoint(request: {lat: 53.9730452, lon: 38.1763201}) {
    ...WeatherData
  }
  Chekalin: weatherByPoint(request: {lat: 54.0984438, lon: 36.2474142}) {
    ...WeatherData
  }
  Schekino: weatherByPoint(request: {lat: 54.0020652, lon: 37.5176288}) {
    ...WeatherData
  }
  Yasnogorsk: weatherByPoint(request: {lat: 54.4795484, lon: 37.6896048}) {
    ...WeatherData
  }
  AkDovurak: weatherByPoint(request: {lat: 51.178452, lon: 90.5985129}) {
    ...WeatherData
  }
  Kyzyl: weatherByPoint(request: {lat: 51.7191047, lon: 94.4376882}) {
    ...WeatherData
  }
  Turan: weatherByPoint(request: {lat: 52.1449619, lon: 93.9173396}) {
    ...WeatherData
  }
  Chadan: weatherByPoint(request: {lat: 51.2844502, lon: 91.5788609}) {
    ...WeatherData
  }
  Shagonar: weatherByPoint(request: {lat: 51.5346393, lon: 92.9199675}) {
    ...WeatherData
  }
  Zavodoukovsk: weatherByPoint(request: {lat: 56.5027463, lon: 66.5513613}) {
    ...WeatherData
  }
  Ishim: weatherByPoint(request: {lat: 56.1104858, lon: 69.4795776}) {
    ...WeatherData
  }
  Tobolsk: weatherByPoint(request: {lat: 58.2017299, lon: 68.2538558}) {
    ...WeatherData
  }
  Tyumen: weatherByPoint(request: {lat: 57.1529744, lon: 65.5344099}) {
    ...WeatherData
  }
  Yalutorovsk: weatherByPoint(request: {lat: 56.6547289, lon: 66.3122992}) {
    ...WeatherData
  }
  Votkinsk: weatherByPoint(request: {lat: 57.0518149, lon: 53.9873096}) {
    ...WeatherData
  }
  Glazov: weatherByPoint(request: {lat: 58.1359233, lon: 52.6635038}) {
    ...WeatherData
  }
  Izhevsk: weatherByPoint(request: {lat: 56.852738, lon: 53.2114896}) {
    ...WeatherData
  }
  Kambarka: weatherByPoint(request: {lat: 56.2659916, lon: 54.193374}) {
    ...WeatherData
  }
  Mozhga: weatherByPoint(request: {lat: 56.4427774, lon: 52.2137886}) {
    ...WeatherData
  }
  Sarapul: weatherByPoint(request: {lat: 56.4615767, lon: 53.8037657}) {
    ...WeatherData
  }
  Barysh: weatherByPoint(request: {lat: 53.6533992, lon: 47.1181134}) {
    ...WeatherData
  }
  Dimitrovgrad: weatherByPoint(request: {lat: 54.2167926, lon: 49.6262585}) {
    ...WeatherData
  }
  Inza: weatherByPoint(request: {lat: 53.8549647, lon: 46.3533459}) {
    ...WeatherData
  }
  Novoulyanovsk: weatherByPoint(request: {lat: 54.1447956, lon: 48.3910789}) {
    ...WeatherData
  }
  Sengiley: weatherByPoint(request: {lat: 53.958964, lon: 48.7768269}) {
    ...WeatherData
  }
  Ulyanovsk: weatherByPoint(request: {lat: 54.3079415, lon: 48.3748487}) {
    ...WeatherData
  }
  Amursk: weatherByPoint(request: {lat: 50.2344147, lon: 136.8792444}) {
    ...WeatherData
  }
  Bikin: weatherByPoint(request: {lat: 46.8185743, lon: 134.2550718}) {
    ...WeatherData
  }
  Vyazemskiy: weatherByPoint(request: {lat: 47.5353379, lon: 134.7553856}) {
    ...WeatherData
  }
  KomsomolskNaAmure: weatherByPoint(request: {lat: 50.5498936, lon: 137.0079408}) {
    ...WeatherData
  }
  NikolaevskNaAmure: weatherByPoint(request: {lat: 53.1460657, lon: 140.7111367}) {
    ...WeatherData
  }
  SovetskayaGavan: weatherByPoint(request: {lat: 48.9664966, lon: 140.285174}) {
    ...WeatherData
  }
  Habarovsk: weatherByPoint(request: {lat: 48.4647258, lon: 135.0598942}) {
    ...WeatherData
  }
  Abaza: weatherByPoint(request: {lat: 52.6516647, lon: 90.0885686}) {
    ...WeatherData
  }
  Abakan: weatherByPoint(request: {lat: 53.7223325, lon: 91.4436721}) {
    ...WeatherData
  }
  Sayanogorsk: weatherByPoint(request: {lat: 53.1008083, lon: 91.4122454}) {
    ...WeatherData
  }
  Sorsk: weatherByPoint(request: {lat: 54.0002888, lon: 90.2594446}) {
    ...WeatherData
  }
  Chernogorsk: weatherByPoint(request: {lat: 53.8259342, lon: 91.3260229}) {
    ...WeatherData
  }
  Beloyarskiy: weatherByPoint(request: {lat: 63.7121099, lon: 66.6772226}) {
    ...WeatherData
  }
  Kogalym: weatherByPoint(request: {lat: 62.2639527, lon: 74.4829794}) {
    ...WeatherData
  }
  Langepas: weatherByPoint(request: {lat: 61.2536939, lon: 75.1807763}) {
    ...WeatherData
  }
  Lyantor: weatherByPoint(request: {lat: 61.6392863, lon: 72.179409}) {
    ...WeatherData
  }
  Megion: weatherByPoint(request: {lat: 61.0318712, lon: 76.1025878}) {
    ...WeatherData
  }
  Nefteyugansk: weatherByPoint(request: {lat: 61.0882676, lon: 72.6164079}) {
    ...WeatherData
  }
  Nizhnevartovsk: weatherByPoint(request: {lat: 60.9396698, lon: 76.5696184}) {
    ...WeatherData
  }
  Nyagan: weatherByPoint(request: {lat: 62.1454701, lon: 65.3946047}) {
    ...WeatherData
  }
  Pokachi: weatherByPoint(request: {lat: 61.7422169, lon: 75.5941517}) {
    ...WeatherData
  }
  PytYah: weatherByPoint(request: {lat: 60.7585833, lon: 72.8365617}) {
    ...WeatherData
  }
  Raduzhnyy_2: weatherByPoint(request: {lat: 62.1342888, lon: 77.4584094}) {
    ...WeatherData
  }
  Sovetskiy: weatherByPoint(request: {lat: 61.3706913, lon: 63.5667222}) {
    ...WeatherData
  }
  Surgut: weatherByPoint(request: {lat: 61.2541083, lon: 73.3961587}) {
    ...WeatherData
  }
  Uray: weatherByPoint(request: {lat: 60.1296954, lon: 64.8038508}) {
    ...WeatherData
  }
  HantyMansiysk: weatherByPoint(request: {lat: 61.0023984, lon: 69.0184798}) {
    ...WeatherData
  }
  Yugorsk: weatherByPoint(request: {lat: 61.3123568, lon: 63.3365484}) {
    ...WeatherData
  }
  Asha: weatherByPoint(request: {lat: 54.9906527, lon: 57.2783953}) {
    ...WeatherData
  }
  Bakal: weatherByPoint(request: {lat: 54.9406399, lon: 58.8051698}) {
    ...WeatherData
  }
  Verhneuralsk: weatherByPoint(request: {lat: 53.8760961, lon: 59.2169852}) {
    ...WeatherData
  }
  VerhniyUfaley: weatherByPoint(request: {lat: 56.0487158, lon: 60.2318886}) {
    ...WeatherData
  }
  Emanzhelinsk: weatherByPoint(request: {lat: 54.7554548, lon: 61.3243477}) {
    ...WeatherData
  }
  Zlatoust: weatherByPoint(request: {lat: 55.1714905, lon: 59.6725549}) {
    ...WeatherData
  }
  Karabash: weatherByPoint(request: {lat: 55.4852323, lon: 60.2358881}) {
    ...WeatherData
  }
  Kartaly: weatherByPoint(request: {lat: 53.0536197, lon: 60.6478408}) {
    ...WeatherData
  }
  Kasli: weatherByPoint(request: {lat: 55.8868784, lon: 60.7421663}) {
    ...WeatherData
  }
  KatavIvanovsk: weatherByPoint(request: {lat: 54.7521438, lon: 58.1983648}) {
    ...WeatherData
  }
  Kopeysk: weatherByPoint(request: {lat: 55.116665, lon: 61.6179185}) {
    ...WeatherData
  }
  Korkino: weatherByPoint(request: {lat: 54.8903147, lon: 61.4034576}) {
    ...WeatherData
  }
  Kusa: weatherByPoint(request: {lat: 55.3386053, lon: 59.4385778}) {
    ...WeatherData
  }
  Kyshtym: weatherByPoint(request: {lat: 55.7061276, lon: 60.5563781}) {
    ...WeatherData
  }
  Magnitogorsk: weatherByPoint(request: {lat: 53.4072153, lon: 58.9791437}) {
    ...WeatherData
  }
  Miass: weatherByPoint(request: {lat: 55.0456457, lon: 60.1077572}) {
    ...WeatherData
  }
  Minyar: weatherByPoint(request: {lat: 55.0709557, lon: 57.548478}) {
    ...WeatherData
  }
  Nyazepetrovsk: weatherByPoint(request: {lat: 56.0536895, lon: 59.6097202}) {
    ...WeatherData
  }
  Ozersk_2: weatherByPoint(request: {lat: 55.763154, lon: 60.7076198}) {
    ...WeatherData
  }
  Plast: weatherByPoint(request: {lat: 54.3692764, lon: 60.8151894}) {
    ...WeatherData
  }
  Satka: weatherByPoint(request: {lat: 55.0405288, lon: 59.0288975}) {
    ...WeatherData
  }
  Sim: weatherByPoint(request: {lat: 54.9907827, lon: 57.6900155}) {
    ...WeatherData
  }
  Snezhinsk: weatherByPoint(request: {lat: 56.0851495, lon: 60.7324914}) {
    ...WeatherData
  }
  Trehgornyy: weatherByPoint(request: {lat: 54.8178249, lon: 58.4464194}) {
    ...WeatherData
  }
  Troitsk: weatherByPoint(request: {lat: 54.0843745, lon: 61.5586831}) {
    ...WeatherData
  }
  UstKatav: weatherByPoint(request: {lat: 54.9260812, lon: 58.152805}) {
    ...WeatherData
  }
  Chebarkul: weatherByPoint(request: {lat: 54.9818567, lon: 60.3773121}) {
    ...WeatherData
  }
  Chelyabinsk: weatherByPoint(request: {lat: 55.1602624, lon: 61.4008078}) {
    ...WeatherData
  }
  Yuzhnouralsk: weatherByPoint(request: {lat: 54.448927, lon: 61.2581158}) {
    ...WeatherData
  }
  Yuryuzan: weatherByPoint(request: {lat: 54.854662, lon: 58.4226698}) {
    ...WeatherData
  }
  Argun: weatherByPoint(request: {lat: 43.2916774, lon: 45.8723105}) {
    ...WeatherData
  }
  Groznyy: weatherByPoint(request: {lat: 43.3180145, lon: 45.698291}) {
    ...WeatherData
  }
  Gudermes: weatherByPoint(request: {lat: 43.3519142, lon: 46.1035645}) {
    ...WeatherData
  }
  Kurchaloy: weatherByPoint(request: {lat: 43.2046547, lon: 46.0889364}) {
    ...WeatherData
  }
  UrusMartan: weatherByPoint(request: {lat: 43.120175, lon: 45.539276}) {
    ...WeatherData
  }
  Shali: weatherByPoint(request: {lat: 43.1488691, lon: 45.9009629}) {
    ...WeatherData
  }
  Alatyr: weatherByPoint(request: {lat: 54.8397989, lon: 46.5721997}) {
    ...WeatherData
  }
  Kanash: weatherByPoint(request: {lat: 55.507, lon: 47.4918273}) {
    ...WeatherData
  }
  Kozlovka: weatherByPoint(request: {lat: 55.8406025, lon: 48.2577735}) {
    ...WeatherData
  }
  MariinskiyPosad: weatherByPoint(request: {lat: 56.111923, lon: 47.7142942}) {
    ...WeatherData
  }
  Novocheboksarsk: weatherByPoint(request: {lat: 56.1094977, lon: 47.4791113}) {
    ...WeatherData
  }
  Tsivilsk: weatherByPoint(request: {lat: 55.8650213, lon: 47.4729349}) {
    ...WeatherData
  }
  Cheboksary: weatherByPoint(request: {lat: 56.1438298, lon: 47.2489782}) {
    ...WeatherData
  }
  Shumerlya: weatherByPoint(request: {lat: 55.4962415, lon: 46.4182681}) {
    ...WeatherData
  }
  Yadrin: weatherByPoint(request: {lat: 55.9406974, lon: 46.2020896}) {
    ...WeatherData
  }
  Anadyr: weatherByPoint(request: {lat: 64.7313924, lon: 177.5015421}) {
    ...WeatherData
  }
  Bilibino: weatherByPoint(request: {lat: 68.0584191, lon: 166.4388172}) {
    ...WeatherData
  }
  Pevek: weatherByPoint(request: {lat: 69.7016661, lon: 170.2999022}) {
    ...WeatherData
  }
  Aldan: weatherByPoint(request: {lat: 58.6094283, lon: 125.3817188}) {
    ...WeatherData
  }
  Verhoyansk: weatherByPoint(request: {lat: 67.5502451, lon: 133.390735}) {
    ...WeatherData
  }
  Vilyuysk: weatherByPoint(request: {lat: 63.7517616, lon: 121.627284}) {
    ...WeatherData
  }
  Lensk: weatherByPoint(request: {lat: 60.7276196, lon: 114.9548255}) {
    ...WeatherData
  }
  Mirnyy_2: weatherByPoint(request: {lat: 62.536232, lon: 113.9667728}) {
    ...WeatherData
  }
  Neryungri: weatherByPoint(request: {lat: 56.6599953, lon: 124.7202403}) {
    ...WeatherData
  }
  Nyurba: weatherByPoint(request: {lat: 63.2828955, lon: 118.3242437}) {
    ...WeatherData
  }
  Olekminsk: weatherByPoint(request: {lat: 60.3758006, lon: 120.4060878}) {
    ...WeatherData
  }
  Pokrovsk: weatherByPoint(request: {lat: 61.4843503, lon: 129.1482392}) {
    ...WeatherData
  }
  Srednekolymsk: weatherByPoint(request: {lat: 67.4582218, lon: 153.7069425}) {
    ...WeatherData
  }
  Tommot: weatherByPoint(request: {lat: 58.9586859, lon: 126.2875462}) {
    ...WeatherData
  }
  Udachnyy: weatherByPoint(request: {lat: 66.4071765, lon: 112.3061555}) {
    ...WeatherData
  }
  Yakutsk: weatherByPoint(request: {lat: 62.0281405, lon: 129.7325887}) {
    ...WeatherData
  }
  Gubkinskiy: weatherByPoint(request: {lat: 64.4457594, lon: 76.4713274}) {
    ...WeatherData
  }
  Labytnangi: weatherByPoint(request: {lat: 66.6592841, lon: 66.3883009}) {
    ...WeatherData
  }
  Muravlenko: weatherByPoint(request: {lat: 63.7940552, lon: 74.4948635}) {
    ...WeatherData
  }
  Nadym: weatherByPoint(request: {lat: 65.5377966, lon: 72.5182736}) {
    ...WeatherData
  }
  NovyyUrengoy: weatherByPoint(request: {lat: 66.0839433, lon: 76.6809681}) {
    ...WeatherData
  }
  Noyabrsk: weatherByPoint(request: {lat: 63.2018039, lon: 75.4510581}) {
    ...WeatherData
  }
  Salehard: weatherByPoint(request: {lat: 66.5492077, lon: 66.6085318}) {
    ...WeatherData
  }
  TarkoSale: weatherByPoint(request: {lat: 64.9118803, lon: 77.7610236}) {
    ...WeatherData
  }
  GavrilovYam: weatherByPoint(request: {lat: 57.3091058, lon: 39.8546444}) {
    ...WeatherData
  }
  Danilov: weatherByPoint(request: {lat: 58.1860098, lon: 40.1795067}) {
    ...WeatherData
  }
  Lyubim: weatherByPoint(request: {lat: 58.3620228, lon: 40.686841}) {
    ...WeatherData
  }
  Myshkin: weatherByPoint(request: {lat: 57.7881684, lon: 38.4544224}) {
    ...WeatherData
  }
  PereslavlZalesskiy: weatherByPoint(request: {lat: 56.7360544, lon: 38.8543617}) {
    ...WeatherData
  }
  Poshehone: weatherByPoint(request: {lat: 58.5062879, lon: 39.1208434}) {
    ...WeatherData
  }
  Rostov: weatherByPoint(request: {lat: 57.2051315, lon: 39.4378622}) {
    ...WeatherData
  }
  Rybinsk: weatherByPoint(request: {lat: 58.0485495, lon: 38.8584119}) {
    ...WeatherData
  }
  Tutaev: weatherByPoint(request: {lat: 57.8674993, lon: 39.5369627}) {
    ...WeatherData
  }
  Uglich: weatherByPoint(request: {lat: 57.5224249, lon: 38.3020044}) {
    ...WeatherData
  }
  Yaroslavl: weatherByPoint(request: {lat: 57.6215477, lon: 39.8977411}) {
    ...WeatherData
  }
  CAD: weatherByPoint(request: {lat: 55.754600, lon: 37.587400}) {
    ...WeatherData
  }
  NAD: weatherByPoint(request: {lat: 55.895400, lon: 37.482700}) {
    ...WeatherData
  }
  NWAD: weatherByPoint(request: {lat: 55.814700, lon: 37.335200}) {
    ...WeatherData
  }
  WAD: weatherByPoint(request: {lat: 55.737100, lon: 37.267800}) {
    ...WeatherData
  }
  NEAD: weatherByPoint(request: {lat: 55.875100, lon: 37.623800}) {
    ...WeatherData
  }
  EAD: weatherByPoint(request: {lat: 55.801200, lon: 37.718400}) {
    ...WeatherData
  }
  SAD: weatherByPoint(request: {lat: 55.665500, lon: 37.601200}) {
    ...WeatherData
  }
  SEAD: weatherByPoint(request: {lat: 55.712900, lon: 37.751300}) {
    ...WeatherData
  }
  SWAD: weatherByPoint(request: {lat: 55.694300, lon: 37.526500}) {
    ...WeatherData
  }
  ZAD: weatherByPoint(request: {lat: 55.986500, lon: 37.135300}) {
    ...WeatherData
  }
  TAD: weatherByPoint(request: {lat: 55.481100, lon: 37.295600}) {
    ...WeatherData
  }
  NovAD: weatherByPoint(request: {lat: 55.630200, lon: 37.403800}) {
    ...WeatherData
  }
  Mos: weatherByPoint(request: {lat: 55.751244, lon: 37.618423}) {
    ...WeatherData
  }
}

fragment DaypartData on Daypart {
  avgTemperature
  cloudiness
  condition
  daytime
  feelsLike
  freshSnow
  humidity
  iceAreaFraction
  iceThickness
  leafWetnessPercent
  maxDewPoint
  maxKpIndex
  maxSoilTemperature
  maxTemperature
  meanSeaLevelPressure
  minSoilTemperature
  minTemperature
  phenomCondition
  pollution {
    maxAqi
    minAqi
  }
  prec
  precProbability
  precStrength
  precType
  pressure
  pressure
  roadCondition
  seaCurrentDirection
  seaCurrentSpeed
  snowDepth
  soilMoisture
  soilTemperature
  swellDirection
  swellHeight
  swellPeriod
  temperature
  uvIndex
  visibility
  waterTemperature
  waveAngle
  waveDirection
  waveHeight
  waveMaxHeight
  wavePeriod
  windAngle
  windDirection
  windGust
  windSpeed
}

fragment WeatherData on Weather {
  forecast {
    days(limit: 1) {
      time
      summary {
        day {
          ...DaypartData
        }
        night {
          ...DaypartData
        }
      }
    }
  }
}"""

WEATHER_NOW_QUERY = """{
  Adygeysk: weatherByPoint(request: {lat: 44.878414, lon: 39.190289}) {
    ...WeatherNow
  }
  Maykop: weatherByPoint(request: {lat: 44.6098268, lon: 40.1006606}) {
    ...WeatherNow
  }
  GornoAltaysk: weatherByPoint(request: {lat: 51.9581028, lon: 85.9603235}) {
    ...WeatherNow
  }
  Aleysk: weatherByPoint(request: {lat: 52.4922513, lon: 82.7793606}) {
    ...WeatherNow
  }
  Barnaul: weatherByPoint(request: {lat: 53.3479968, lon: 83.7798064}) {
    ...WeatherNow
  }
  Belokuriha: weatherByPoint(request: {lat: 51.996152, lon: 84.9839604}) {
    ...WeatherNow
  }
  Biysk: weatherByPoint(request: {lat: 52.5393864, lon: 85.2138453}) {
    ...WeatherNow
  }
  Gornyak: weatherByPoint(request: {lat: 50.9979622, lon: 81.4643358}) {
    ...WeatherNow
  }
  Zarinsk: weatherByPoint(request: {lat: 53.7063476, lon: 84.9315081}) {
    ...WeatherNow
  }
  Zmeinogorsk: weatherByPoint(request: {lat: 51.1581094, lon: 82.1872547}) {
    ...WeatherNow
  }
  KamenNaObi: weatherByPoint(request: {lat: 53.7913974, lon: 81.3545053}) {
    ...WeatherNow
  }
  Novoaltaysk: weatherByPoint(request: {lat: 53.4119759, lon: 83.9311069}) {
    ...WeatherNow
  }
  Rubtsovsk: weatherByPoint(request: {lat: 51.5012067, lon: 81.2078695}) {
    ...WeatherNow
  }
  Slavgorod: weatherByPoint(request: {lat: 52.999463, lon: 78.6459232}) {
    ...WeatherNow
  }
  Yarovoe: weatherByPoint(request: {lat: 52.9252146, lon: 78.5729775}) {
    ...WeatherNow
  }
  Belogorsk: weatherByPoint(request: {lat: 50.9213415, lon: 128.4739471}) {
    ...WeatherNow
  }
  Blagoveschensk: weatherByPoint(request: {lat: 50.290659, lon: 127.527198}) {
    ...WeatherNow
  }
  Zavitinsk: weatherByPoint(request: {lat: 50.1064111, lon: 129.4391813}) {
    ...WeatherNow
  }
  Zeya: weatherByPoint(request: {lat: 53.7340088, lon: 127.265787}) {
    ...WeatherNow
  }
  Raychihinsk: weatherByPoint(request: {lat: 49.7941615, lon: 129.4112492}) {
    ...WeatherNow
  }
  Svobodnyy: weatherByPoint(request: {lat: 51.3614103, lon: 128.1219729}) {
    ...WeatherNow
  }
  Skovorodino: weatherByPoint(request: {lat: 53.9871095, lon: 123.9437205}) {
    ...WeatherNow
  }
  Tynda: weatherByPoint(request: {lat: 55.1546441, lon: 124.7468904}) {
    ...WeatherNow
  }
  Tsiolkovskiy: weatherByPoint(request: {lat: 51.762481, lon: 128.1219846}) {
    ...WeatherNow
  }
  Shimanovsk: weatherByPoint(request: {lat: 52.0051886, lon: 127.7005458}) {
    ...WeatherNow
  }
  Arhangelsk: weatherByPoint(request: {lat: 64.5394289, lon: 40.5169606}) {
    ...WeatherNow
  }
  Velsk: weatherByPoint(request: {lat: 61.066, lon: 42.1032789}) {
    ...WeatherNow
  }
  Kargopol: weatherByPoint(request: {lat: 61.5009724, lon: 38.9636966}) {
    ...WeatherNow
  }
  Koryazhma: weatherByPoint(request: {lat: 61.2885948, lon: 47.1003015}) {
    ...WeatherNow
  }
  Kotlas: weatherByPoint(request: {lat: 61.2528972, lon: 46.633242}) {
    ...WeatherNow
  }
  Mezen: weatherByPoint(request: {lat: 65.8398078, lon: 44.2532273}) {
    ...WeatherNow
  }
  Mirnyy: weatherByPoint(request: {lat: 62.7645265, lon: 40.3360076}) {
    ...WeatherNow
  }
  Novodvinsk: weatherByPoint(request: {lat: 64.4136851, lon: 40.8208143}) {
    ...WeatherNow
  }
  Nyandoma: weatherByPoint(request: {lat: 61.6654674, lon: 40.2062947}) {
    ...WeatherNow
  }
  Onega: weatherByPoint(request: {lat: 63.9162928, lon: 38.0805031}) {
    ...WeatherNow
  }
  Severodvinsk: weatherByPoint(request: {lat: 64.5625385, lon: 39.8180934}) {
    ...WeatherNow
  }
  Solvychegodsk: weatherByPoint(request: {lat: 61.3319616, lon: 46.920441}) {
    ...WeatherNow
  }
  Shenkursk: weatherByPoint(request: {lat: 62.1057272, lon: 42.8996973}) {
    ...WeatherNow
  }
  Astrahan: weatherByPoint(request: {lat: 46.3655652, lon: 48.0559236}) {
    ...WeatherNow
  }
  Ahtubinsk: weatherByPoint(request: {lat: 48.2752034, lon: 46.1906462}) {
    ...WeatherNow
  }
  Znamensk: weatherByPoint(request: {lat: 48.5866291, lon: 45.7368019}) {
    ...WeatherNow
  }
  Kamyzyak: weatherByPoint(request: {lat: 46.110579, lon: 48.07333}) {
    ...WeatherNow
  }
  Narimanov: weatherByPoint(request: {lat: 46.6916565, lon: 47.8502476}) {
    ...WeatherNow
  }
  Harabali: weatherByPoint(request: {lat: 47.408999, lon: 47.2525345}) {
    ...WeatherNow
  }
  Agidel: weatherByPoint(request: {lat: 55.8999056, lon: 53.9220144}) {
    ...WeatherNow
  }
  Baymak: weatherByPoint(request: {lat: 52.5912896, lon: 58.3110998}) {
    ...WeatherNow
  }
  Belebey: weatherByPoint(request: {lat: 54.1034582, lon: 54.1113129}) {
    ...WeatherNow
  }
  Beloretsk: weatherByPoint(request: {lat: 53.9676488, lon: 58.4100419}) {
    ...WeatherNow
  }
  Birsk: weatherByPoint(request: {lat: 55.4155753, lon: 55.5582214}) {
    ...WeatherNow
  }
  Blagoveschensk_2: weatherByPoint(request: {lat: 55.0499867, lon: 55.9553186}) {
    ...WeatherNow
  }
  Davlekanovo: weatherByPoint(request: {lat: 54.2226707, lon: 55.0312373}) {
    ...WeatherNow
  }
  Dyurtyuli: weatherByPoint(request: {lat: 55.4848318, lon: 54.8524765}) {
    ...WeatherNow
  }
  Ishimbay: weatherByPoint(request: {lat: 53.4545764, lon: 56.0438751}) {
    ...WeatherNow
  }
  Kumertau: weatherByPoint(request: {lat: 52.7564939, lon: 55.7970197}) {
    ...WeatherNow
  }
  Mezhgore: weatherByPoint(request: {lat: 54.2397689, lon: 57.9614547}) {
    ...WeatherNow
  }
  Meleuz: weatherByPoint(request: {lat: 52.9589532, lon: 55.9282838}) {
    ...WeatherNow
  }
  Neftekamsk: weatherByPoint(request: {lat: 56.088377, lon: 54.2483061}) {
    ...WeatherNow
  }
  Oktyabrskiy: weatherByPoint(request: {lat: 54.4815311, lon: 53.4655972}) {
    ...WeatherNow
  }
  Salavat: weatherByPoint(request: {lat: 53.3616974, lon: 55.9245224}) {
    ...WeatherNow
  }
  Sibay: weatherByPoint(request: {lat: 52.7204651, lon: 58.6663783}) {
    ...WeatherNow
  }
  Sterlitamak: weatherByPoint(request: {lat: 53.6300864, lon: 55.9317089}) {
    ...WeatherNow
  }
  Tuymazy: weatherByPoint(request: {lat: 54.5999224, lon: 53.6950623}) {
    ...WeatherNow
  }
  Ufa: weatherByPoint(request: {lat: 54.734944, lon: 55.9578468}) {
    ...WeatherNow
  }
  Uchaly: weatherByPoint(request: {lat: 54.3067375, lon: 59.4125461}) {
    ...WeatherNow
  }
  Yanaul: weatherByPoint(request: {lat: 56.2650146, lon: 54.929907}) {
    ...WeatherNow
  }
  Alekseevka: weatherByPoint(request: {lat: 50.6299647, lon: 38.6880342}) {
    ...WeatherNow
  }
  Belgorod: weatherByPoint(request: {lat: 50.5976472, lon: 36.5856652}) {
    ...WeatherNow
  }
  Biryuch: weatherByPoint(request: {lat: 50.6484585, lon: 38.4005083}) {
    ...WeatherNow
  }
  Valuyki: weatherByPoint(request: {lat: 50.2111207, lon: 38.0998772}) {
    ...WeatherNow
  }
  Grayvoron: weatherByPoint(request: {lat: 50.4862958, lon: 35.6663877}) {
    ...WeatherNow
  }
  Gubkin: weatherByPoint(request: {lat: 51.2837123, lon: 37.5347759}) {
    ...WeatherNow
  }
  Korocha: weatherByPoint(request: {lat: 50.8129041, lon: 37.1896436}) {
    ...WeatherNow
  }
  NovyyOskol: weatherByPoint(request: {lat: 50.7633747, lon: 37.8775484}) {
    ...WeatherNow
  }
  StaryyOskol: weatherByPoint(request: {lat: 51.2967101, lon: 37.8350182}) {
    ...WeatherNow
  }
  Stroitel: weatherByPoint(request: {lat: 50.7845099, lon: 36.4887648}) {
    ...WeatherNow
  }
  Shebekino: weatherByPoint(request: {lat: 50.4004883, lon: 36.8877889}) {
    ...WeatherNow
  }
  Bryansk: weatherByPoint(request: {lat: 53.2419535, lon: 34.3652146}) {
    ...WeatherNow
  }
  Dyatkovo: weatherByPoint(request: {lat: 53.5958178, lon: 34.3551812}) {
    ...WeatherNow
  }
  Zhukovka: weatherByPoint(request: {lat: 53.5340397, lon: 33.7302579}) {
    ...WeatherNow
  }
  Zlynka: weatherByPoint(request: {lat: 52.4267015, lon: 31.7360399}) {
    ...WeatherNow
  }
  Karachev: weatherByPoint(request: {lat: 53.1296524, lon: 34.9888727}) {
    ...WeatherNow
  }
  Klintsy: weatherByPoint(request: {lat: 52.7529119, lon: 32.233911}) {
    ...WeatherNow
  }
  Mglin: weatherByPoint(request: {lat: 53.0599771, lon: 32.8468129}) {
    ...WeatherNow
  }
  Novozybkov: weatherByPoint(request: {lat: 52.537173, lon: 31.9357991}) {
    ...WeatherNow
  }
  Pochep: weatherByPoint(request: {lat: 52.9154851, lon: 33.4744058}) {
    ...WeatherNow
  }
  Sevsk: weatherByPoint(request: {lat: 52.1483358, lon: 34.4918415}) {
    ...WeatherNow
  }
  Seltso: weatherByPoint(request: {lat: 53.3739884, lon: 34.1059172}) {
    ...WeatherNow
  }
  Starodub: weatherByPoint(request: {lat: 52.5852257, lon: 32.760403}) {
    ...WeatherNow
  }
  Surazh: weatherByPoint(request: {lat: 53.0170888, lon: 32.3938878}) {
    ...WeatherNow
  }
  Trubchevsk: weatherByPoint(request: {lat: 52.5791734, lon: 33.7660547}) {
    ...WeatherNow
  }
  Unecha: weatherByPoint(request: {lat: 52.8461199, lon: 32.6757629}) {
    ...WeatherNow
  }
  Fokino: weatherByPoint(request: {lat: 53.4554145, lon: 34.4159238}) {
    ...WeatherNow
  }
  Babushkin: weatherByPoint(request: {lat: 51.7112755, lon: 105.8673219}) {
    ...WeatherNow
  }
  Gusinoozersk: weatherByPoint(request: {lat: 51.2865048, lon: 106.5230319}) {
    ...WeatherNow
  }
  Zakamensk: weatherByPoint(request: {lat: 50.372713, lon: 103.286699}) {
    ...WeatherNow
  }
  Kyahta: weatherByPoint(request: {lat: 50.346543, lon: 106.4533516}) {
    ...WeatherNow
  }
  Severobaykalsk: weatherByPoint(request: {lat: 55.635614, lon: 109.3361505}) {
    ...WeatherNow
  }
  UlanUde: weatherByPoint(request: {lat: 51.8335853, lon: 107.5842223}) {
    ...WeatherNow
  }
  Aleksandrov: weatherByPoint(request: {lat: 56.391819, lon: 38.7111123}) {
    ...WeatherNow
  }
  Vladimir: weatherByPoint(request: {lat: 56.1280804, lon: 40.4084376}) {
    ...WeatherNow
  }
  Vyazniki: weatherByPoint(request: {lat: 56.29773, lon: 42.2687398}) {
    ...WeatherNow
  }
  Gorohovets: weatherByPoint(request: {lat: 56.2021036, lon: 42.6926111}) {
    ...WeatherNow
  }
  GusHrustalnyy: weatherByPoint(request: {lat: 55.6198751, lon: 40.6579929}) {
    ...WeatherNow
  }
  Kameshkovo: weatherByPoint(request: {lat: 56.3490152, lon: 40.9955183}) {
    ...WeatherNow
  }
  Karabanovo: weatherByPoint(request: {lat: 56.3131822, lon: 38.7034257}) {
    ...WeatherNow
  }
  Kirzhach: weatherByPoint(request: {lat: 56.1486863, lon: 38.8635701}) {
    ...WeatherNow
  }
  Kovrov: weatherByPoint(request: {lat: 56.3554349, lon: 41.3170576}) {
    ...WeatherNow
  }
  Kolchugino: weatherByPoint(request: {lat: 56.3327254, lon: 39.391336}) {
    ...WeatherNow
  }
  Kosterevo: weatherByPoint(request: {lat: 55.9337222, lon: 39.6247398}) {
    ...WeatherNow
  }
  Kurlovo: weatherByPoint(request: {lat: 55.452698, lon: 40.6124108}) {
    ...WeatherNow
  }
  Lakinsk: weatherByPoint(request: {lat: 56.0180587, lon: 39.956551}) {
    ...WeatherNow
  }
  Melenki: weatherByPoint(request: {lat: 55.3387515, lon: 41.6340046}) {
    ...WeatherNow
  }
  Murom: weatherByPoint(request: {lat: 55.5630311, lon: 42.0231362}) {
    ...WeatherNow
  }
  Petushki: weatherByPoint(request: {lat: 55.9298134, lon: 39.4508075}) {
    ...WeatherNow
  }
  Pokrov: weatherByPoint(request: {lat: 55.9166398, lon: 39.1734526}) {
    ...WeatherNow
  }
  Raduzhnyy: weatherByPoint(request: {lat: 55.9960277, lon: 40.3321855}) {
    ...WeatherNow
  }
  Sobinka: weatherByPoint(request: {lat: 55.9939169, lon: 40.0179653}) {
    ...WeatherNow
  }
  Strunino: weatherByPoint(request: {lat: 56.3749967, lon: 38.5839667}) {
    ...WeatherNow
  }
  Sudogda: weatherByPoint(request: {lat: 55.9498056, lon: 40.8562939}) {
    ...WeatherNow
  }
  Suzdal: weatherByPoint(request: {lat: 56.4274441, lon: 40.4525692}) {
    ...WeatherNow
  }
  YurevPolskiy: weatherByPoint(request: {lat: 56.4937757, lon: 39.6680539}) {
    ...WeatherNow
  }
  Volgograd: weatherByPoint(request: {lat: 48.7070042, lon: 44.5170339}) {
    ...WeatherNow
  }
  Volzhskiy: weatherByPoint(request: {lat: 48.7978209, lon: 44.7462538}) {
    ...WeatherNow
  }
  Dubovka: weatherByPoint(request: {lat: 49.0554742, lon: 44.8270085}) {
    ...WeatherNow
  }
  Zhirnovsk: weatherByPoint(request: {lat: 50.9768814, lon: 44.7858202}) {
    ...WeatherNow
  }
  KalachNaDonu: weatherByPoint(request: {lat: 48.6889024, lon: 43.5306303}) {
    ...WeatherNow
  }
  Kamyshin: weatherByPoint(request: {lat: 50.0651529, lon: 45.3844202}) {
    ...WeatherNow
  }
  Kotelnikovo: weatherByPoint(request: {lat: 47.6310259, lon: 43.1330872}) {
    ...WeatherNow
  }
  Kotovo: weatherByPoint(request: {lat: 50.3205766, lon: 44.8030699}) {
    ...WeatherNow
  }
  Krasnoslobodsk: weatherByPoint(request: {lat: 48.7068721, lon: 44.5630857}) {
    ...WeatherNow
  }
  Leninsk: weatherByPoint(request: {lat: 48.6936061, lon: 45.1992692}) {
    ...WeatherNow
  }
  Mihaylovka: weatherByPoint(request: {lat: 50.0708719, lon: 43.2401512}) {
    ...WeatherNow
  }
  Nikolaevsk: weatherByPoint(request: {lat: 50.0165306, lon: 45.4731658}) {
    ...WeatherNow
  }
  Novoanninskiy: weatherByPoint(request: {lat: 50.5296067, lon: 42.6666439}) {
    ...WeatherNow
  }
  Pallasovka: weatherByPoint(request: {lat: 50.0500944, lon: 46.8804277}) {
    ...WeatherNow
  }
  PetrovVal: weatherByPoint(request: {lat: 50.1380557, lon: 45.20914}) {
    ...WeatherNow
  }
  Serafimovich: weatherByPoint(request: {lat: 49.5663183, lon: 42.7360402}) {
    ...WeatherNow
  }
  Surovikino: weatherByPoint(request: {lat: 48.618917, lon: 42.8541163}) {
    ...WeatherNow
  }
  Uryupinsk: weatherByPoint(request: {lat: 50.7903789, lon: 42.0288513}) {
    ...WeatherNow
  }
  Frolovo: weatherByPoint(request: {lat: 49.7649148, lon: 43.6648641}) {
    ...WeatherNow
  }
  Babaevo: weatherByPoint(request: {lat: 59.3892583, lon: 35.9377058}) {
    ...WeatherNow
  }
  Belozersk: weatherByPoint(request: {lat: 60.0308381, lon: 37.7890586}) {
    ...WeatherNow
  }
  VelikiyUstyug: weatherByPoint(request: {lat: 60.7603913, lon: 46.3054414}) {
    ...WeatherNow
  }
  Vologda: weatherByPoint(request: {lat: 59.2483905, lon: 39.8355662}) {
    ...WeatherNow
  }
  Vytegra: weatherByPoint(request: {lat: 61.0063465, lon: 36.4495137}) {
    ...WeatherNow
  }
  Gryazovets: weatherByPoint(request: {lat: 58.8757553, lon: 40.2485362}) {
    ...WeatherNow
  }
  Kadnikov: weatherByPoint(request: {lat: 59.5037764, lon: 40.3441148}) {
    ...WeatherNow
  }
  Kirillov: weatherByPoint(request: {lat: 59.8591523, lon: 38.3748782}) {
    ...WeatherNow
  }
  Krasavino: weatherByPoint(request: {lat: 60.9612823, lon: 46.4814116}) {
    ...WeatherNow
  }
  Nikolsk: weatherByPoint(request: {lat: 59.5351837, lon: 45.4576137}) {
    ...WeatherNow
  }
  Sokol: weatherByPoint(request: {lat: 59.4758605, lon: 40.1114187}) {
    ...WeatherNow
  }
  Totma: weatherByPoint(request: {lat: 59.9734998, lon: 42.7589506}) {
    ...WeatherNow
  }
  Ustyuzhna: weatherByPoint(request: {lat: 58.8383117, lon: 36.4425478}) {
    ...WeatherNow
  }
  Harovsk: weatherByPoint(request: {lat: 59.9479423, lon: 40.2000298}) {
    ...WeatherNow
  }
  Cherepovets: weatherByPoint(request: {lat: 59.1269212, lon: 37.9090497}) {
    ...WeatherNow
  }
  Bobrov: weatherByPoint(request: {lat: 51.0901649, lon: 40.0318256}) {
    ...WeatherNow
  }
  Boguchar: weatherByPoint(request: {lat: 49.9352454, lon: 40.5590801}) {
    ...WeatherNow
  }
  Borisoglebsk: weatherByPoint(request: {lat: 51.3655754, lon: 42.1008334}) {
    ...WeatherNow
  }
  Buturlinovka: weatherByPoint(request: {lat: 50.8311818, lon: 40.5976923}) {
    ...WeatherNow
  }
  Voronezh: weatherByPoint(request: {lat: 51.6593332, lon: 39.1969229}) {
    ...WeatherNow
  }
  Kalach: weatherByPoint(request: {lat: 50.4242134, lon: 41.0162014}) {
    ...WeatherNow
  }
  Liski: weatherByPoint(request: {lat: 50.9945626, lon: 39.5184909}) {
    ...WeatherNow
  }
  Novovoronezh: weatherByPoint(request: {lat: 51.3091524, lon: 39.2162843}) {
    ...WeatherNow
  }
  Novohopersk: weatherByPoint(request: {lat: 51.0952211, lon: 41.6173404}) {
    ...WeatherNow
  }
  Ostrogozhsk: weatherByPoint(request: {lat: 50.8677905, lon: 39.0407746}) {
    ...WeatherNow
  }
  Pavlovsk: weatherByPoint(request: {lat: 50.453455, lon: 40.136874}) {
    ...WeatherNow
  }
  Povorino: weatherByPoint(request: {lat: 51.1954419, lon: 42.2472726}) {
    ...WeatherNow
  }
  Rossosh: weatherByPoint(request: {lat: 50.1701949, lon: 39.6226965}) {
    ...WeatherNow
  }
  Semiluki: weatherByPoint(request: {lat: 51.6951644, lon: 39.0190454}) {
    ...WeatherNow
  }
  Ertil: weatherByPoint(request: {lat: 51.830932, lon: 40.8074182}) {
    ...WeatherNow
  }
  Buynaksk: weatherByPoint(request: {lat: 42.8214424, lon: 47.1165263}) {
    ...WeatherNow
  }
  DagestanskieOgni: weatherByPoint(request: {lat: 42.1152296, lon: 48.1939354}) {
    ...WeatherNow
  }
  Derbent: weatherByPoint(request: {lat: 42.058966, lon: 48.2907452}) {
    ...WeatherNow
  }
  Izberbash: weatherByPoint(request: {lat: 42.5650962, lon: 47.8710051}) {
    ...WeatherNow
  }
  Kaspiysk: weatherByPoint(request: {lat: 42.8916007, lon: 47.6367066}) {
    ...WeatherNow
  }
  Kizilyurt: weatherByPoint(request: {lat: 43.203825, lon: 46.8729636}) {
    ...WeatherNow
  }
  Kizlyar: weatherByPoint(request: {lat: 43.8484083, lon: 46.7233699}) {
    ...WeatherNow
  }
  Mahachkala: weatherByPoint(request: {lat: 42.9849159, lon: 47.5047181}) {
    ...WeatherNow
  }
  Hasavyurt: weatherByPoint(request: {lat: 43.2504665, lon: 46.5851292}) {
    ...WeatherNow
  }
  YuzhnoSuhokumsk: weatherByPoint(request: {lat: 44.6602467, lon: 45.6499523}) {
    ...WeatherNow
  }
  Birobidzhan: weatherByPoint(request: {lat: 48.7946446, lon: 132.9217207}) {
    ...WeatherNow
  }
  Obluche: weatherByPoint(request: {lat: 49.0189345, lon: 131.0540102}) {
    ...WeatherNow
  }
  Baley: weatherByPoint(request: {lat: 51.5823759, lon: 116.6379549}) {
    ...WeatherNow
  }
  Borzya: weatherByPoint(request: {lat: 50.3876058, lon: 116.5234779}) {
    ...WeatherNow
  }
  Krasnokamensk: weatherByPoint(request: {lat: 50.0929703, lon: 118.0323936}) {
    ...WeatherNow
  }
  Mogocha: weatherByPoint(request: {lat: 53.7361398, lon: 119.7660867}) {
    ...WeatherNow
  }
  Nerchinsk: weatherByPoint(request: {lat: 51.9594977, lon: 116.5852383}) {
    ...WeatherNow
  }
  PetrovskZabaykalskiy: weatherByPoint(request: {lat: 51.2748592, lon: 108.846681}) {
    ...WeatherNow
  }
  Sretensk: weatherByPoint(request: {lat: 52.2461454, lon: 117.7117842}) {
    ...WeatherNow
  }
  Hilok: weatherByPoint(request: {lat: 51.3634856, lon: 110.4590898}) {
    ...WeatherNow
  }
  Chita: weatherByPoint(request: {lat: 52.0340142, lon: 113.4994}) {
    ...WeatherNow
  }
  Shilka: weatherByPoint(request: {lat: 51.8497035, lon: 116.0334461}) {
    ...WeatherNow
  }
  Vichuga: weatherByPoint(request: {lat: 57.2044698, lon: 41.9132201}) {
    ...WeatherNow
  }
  GavrilovPosad: weatherByPoint(request: {lat: 56.5586946, lon: 40.1228906}) {
    ...WeatherNow
  }
  Zavolzhsk: weatherByPoint(request: {lat: 57.4918141, lon: 42.1375625}) {
    ...WeatherNow
  }
  Ivanovo: weatherByPoint(request: {lat: 56.9993792, lon: 40.9728272}) {
    ...WeatherNow
  }
  Kineshma: weatherByPoint(request: {lat: 57.4425463, lon: 42.168914}) {
    ...WeatherNow
  }
  Komsomolsk: weatherByPoint(request: {lat: 57.0273052, lon: 40.3776851}) {
    ...WeatherNow
  }
  Kohma: weatherByPoint(request: {lat: 56.9324606, lon: 41.0931657}) {
    ...WeatherNow
  }
  Navoloki: weatherByPoint(request: {lat: 57.4679066, lon: 41.9608002}) {
    ...WeatherNow
  }
  Ples: weatherByPoint(request: {lat: 57.4606031, lon: 41.5122672}) {
    ...WeatherNow
  }
  Privolzhsk: weatherByPoint(request: {lat: 57.3805743, lon: 41.2808565}) {
    ...WeatherNow
  }
  Puchezh: weatherByPoint(request: {lat: 56.9820688, lon: 43.1683321}) {
    ...WeatherNow
  }
  Rodniki: weatherByPoint(request: {lat: 57.1025975, lon: 41.7298834}) {
    ...WeatherNow
  }
  Teykovo: weatherByPoint(request: {lat: 56.8542719, lon: 40.5353874}) {
    ...WeatherNow
  }
  Furmanov: weatherByPoint(request: {lat: 57.2539276, lon: 41.1054432}) {
    ...WeatherNow
  }
  Shuya: weatherByPoint(request: {lat: 56.8560234, lon: 41.3800939}) {
    ...WeatherNow
  }
  Yuzha: weatherByPoint(request: {lat: 56.5926877, lon: 42.0458099}) {
    ...WeatherNow
  }
  Yurevets: weatherByPoint(request: {lat: 57.3177781, lon: 43.1110401}) {
    ...WeatherNow
  }
  Karabulak: weatherByPoint(request: {lat: 43.3055248, lon: 44.9094582}) {
    ...WeatherNow
  }
  Magas: weatherByPoint(request: {lat: 43.1688611, lon: 44.8131207}) {
    ...WeatherNow
  }
  Malgobek: weatherByPoint(request: {lat: 43.5096646, lon: 44.5901963}) {
    ...WeatherNow
  }
  Nazran: weatherByPoint(request: {lat: 43.2257841, lon: 44.7645779}) {
    ...WeatherNow
  }
  Sunzha: weatherByPoint(request: {lat: 43.3204196, lon: 45.0476331}) {
    ...WeatherNow
  }
  Alzamay: weatherByPoint(request: {lat: 55.5551233, lon: 98.6643699}) {
    ...WeatherNow
  }
  Angarsk: weatherByPoint(request: {lat: 52.544879, lon: 103.888543}) {
    ...WeatherNow
  }
  Baykalsk: weatherByPoint(request: {lat: 51.5230393, lon: 104.1487532}) {
    ...WeatherNow
  }
  Biryusinsk: weatherByPoint(request: {lat: 55.9609167, lon: 97.8205348}) {
    ...WeatherNow
  }
  Bodaybo: weatherByPoint(request: {lat: 57.8468636, lon: 114.1866287}) {
    ...WeatherNow
  }
  Bratsk: weatherByPoint(request: {lat: 56.1513108, lon: 101.6340035}) {
    ...WeatherNow
  }
  Vihorevka: weatherByPoint(request: {lat: 56.1208145, lon: 101.1702926}) {
    ...WeatherNow
  }
  ZheleznogorskIlimskiy: weatherByPoint(request: {lat: 56.5847888, lon: 104.114275}) {
    ...WeatherNow
  }
  Zima: weatherByPoint(request: {lat: 53.920693, lon: 102.0491772}) {
    ...WeatherNow
  }
  Irkutsk: weatherByPoint(request: {lat: 52.2864036, lon: 104.2807466}) {
    ...WeatherNow
  }
  Kirensk: weatherByPoint(request: {lat: 57.7756595, lon: 108.1109412}) {
    ...WeatherNow
  }
  Nizhneudinsk: weatherByPoint(request: {lat: 54.8968931, lon: 99.0314056}) {
    ...WeatherNow
  }
  Sayansk: weatherByPoint(request: {lat: 54.1107238, lon: 102.18015}) {
    ...WeatherNow
  }
  Svirsk: weatherByPoint(request: {lat: 53.0842668, lon: 103.3364093}) {
    ...WeatherNow
  }
  Slyudyanka: weatherByPoint(request: {lat: 51.6563983, lon: 103.7187545}) {
    ...WeatherNow
  }
  Tayshet: weatherByPoint(request: {lat: 55.9405334, lon: 98.0030145}) {
    ...WeatherNow
  }
  Tulun: weatherByPoint(request: {lat: 54.557162, lon: 100.5780603}) {
    ...WeatherNow
  }
  UsoleSibirskoe: weatherByPoint(request: {lat: 52.7565808, lon: 103.6388109}) {
    ...WeatherNow
  }
  UstIlimsk: weatherByPoint(request: {lat: 57.9430504, lon: 102.7415734}) {
    ...WeatherNow
  }
  UstKut: weatherByPoint(request: {lat: 56.7928178, lon: 105.7757343}) {
    ...WeatherNow
  }
  Cheremhovo: weatherByPoint(request: {lat: 53.1369095, lon: 103.0901268}) {
    ...WeatherNow
  }
  Shelehov: weatherByPoint(request: {lat: 52.2102538, lon: 104.0973294}) {
    ...WeatherNow
  }
  Baksan: weatherByPoint(request: {lat: 43.6819137, lon: 43.5345036}) {
    ...WeatherNow
  }
  Mayskiy: weatherByPoint(request: {lat: 43.6281516, lon: 44.0517314}) {
    ...WeatherNow
  }
  Nalchik: weatherByPoint(request: {lat: 43.4845464, lon: 43.60713}) {
    ...WeatherNow
  }
  Nartkala: weatherByPoint(request: {lat: 43.5578075, lon: 43.8575925}) {
    ...WeatherNow
  }
  Prohladnyy: weatherByPoint(request: {lat: 43.7589602, lon: 44.0102409}) {
    ...WeatherNow
  }
  Terek: weatherByPoint(request: {lat: 43.4839358, lon: 44.1402161}) {
    ...WeatherNow
  }
  Tyrnyauz: weatherByPoint(request: {lat: 43.3981585, lon: 42.9213582}) {
    ...WeatherNow
  }
  Chegem: weatherByPoint(request: {lat: 43.5671525, lon: 43.5865792}) {
    ...WeatherNow
  }
  Bagrationovsk: weatherByPoint(request: {lat: 54.3866518, lon: 20.6418091}) {
    ...WeatherNow
  }
  Baltiysk: weatherByPoint(request: {lat: 54.6513372, lon: 19.9140572}) {
    ...WeatherNow
  }
  Gvardeysk: weatherByPoint(request: {lat: 54.6588378, lon: 21.0501388}) {
    ...WeatherNow
  }
  Gurevsk: weatherByPoint(request: {lat: 54.770638, lon: 20.6039767}) {
    ...WeatherNow
  }
  Gusev: weatherByPoint(request: {lat: 54.5915455, lon: 22.1942445}) {
    ...WeatherNow
  }
  Zelenogradsk: weatherByPoint(request: {lat: 54.9600185, lon: 20.4753652}) {
    ...WeatherNow
  }
  Kaliningrad: weatherByPoint(request: {lat: 54.7074702, lon: 20.5073241}) {
    ...WeatherNow
  }
  Krasnoznamensk: weatherByPoint(request: {lat: 54.9453423, lon: 22.4928745}) {
    ...WeatherNow
  }
  Ladushkin: weatherByPoint(request: {lat: 54.5692156, lon: 20.1690153}) {
    ...WeatherNow
  }
  Mamonovo: weatherByPoint(request: {lat: 54.4646036, lon: 19.9453482}) {
    ...WeatherNow
  }
  Neman: weatherByPoint(request: {lat: 55.0316524, lon: 22.0324064}) {
    ...WeatherNow
  }
  Nesterov: weatherByPoint(request: {lat: 54.6313814, lon: 22.5713736}) {
    ...WeatherNow
  }
  Ozersk: weatherByPoint(request: {lat: 54.4084705, lon: 22.0134438}) {
    ...WeatherNow
  }
  Pionerskiy: weatherByPoint(request: {lat: 54.9516574, lon: 20.2277424}) {
    ...WeatherNow
  }
  Polessk: weatherByPoint(request: {lat: 54.8625126, lon: 21.0998067}) {
    ...WeatherNow
  }
  Pravdinsk: weatherByPoint(request: {lat: 54.4430986, lon: 21.0085269}) {
    ...WeatherNow
  }
  Primorsk: weatherByPoint(request: {lat: 54.7311437, lon: 19.9981926}) {
    ...WeatherNow
  }
  Svetlogorsk: weatherByPoint(request: {lat: 54.9439286, lon: 20.1514295}) {
    ...WeatherNow
  }
  Svetlyy: weatherByPoint(request: {lat: 54.6772897, lon: 20.1357595}) {
    ...WeatherNow
  }
  Slavsk: weatherByPoint(request: {lat: 55.0449714, lon: 21.6742367}) {
    ...WeatherNow
  }
  Sovetsk: weatherByPoint(request: {lat: 55.0809336, lon: 21.8886106}) {
    ...WeatherNow
  }
  Chernyahovsk: weatherByPoint(request: {lat: 54.6244751, lon: 21.7969062}) {
    ...WeatherNow
  }
  Gorodovikovsk: weatherByPoint(request: {lat: 46.0875083, lon: 41.935537}) {
    ...WeatherNow
  }
  Lagan: weatherByPoint(request: {lat: 45.3930912, lon: 47.3432602}) {
    ...WeatherNow
  }
  Elista: weatherByPoint(request: {lat: 46.3083344, lon: 44.2702088}) {
    ...WeatherNow
  }
  Balabanovo: weatherByPoint(request: {lat: 55.1773714, lon: 36.6566951}) {
    ...WeatherNow
  }
  Belousovo: weatherByPoint(request: {lat: 55.0956803, lon: 36.677629}) {
    ...WeatherNow
  }
  Borovsk: weatherByPoint(request: {lat: 55.2130096, lon: 36.4926251}) {
    ...WeatherNow
  }
  Ermolino: weatherByPoint(request: {lat: 55.1971758, lon: 36.5952722}) {
    ...WeatherNow
  }
  Zhizdra: weatherByPoint(request: {lat: 53.7521926, lon: 34.7386592}) {
    ...WeatherNow
  }
  Zhukov: weatherByPoint(request: {lat: 55.0301833, lon: 36.7394903}) {
    ...WeatherNow
  }
  Kaluga: weatherByPoint(request: {lat: 54.5059848, lon: 36.2516245}) {
    ...WeatherNow
  }
  Kirov: weatherByPoint(request: {lat: 54.0790111, lon: 34.3076201}) {
    ...WeatherNow
  }
  Kozelsk: weatherByPoint(request: {lat: 54.0347201, lon: 35.780768}) {
    ...WeatherNow
  }
  Kondrovo: weatherByPoint(request: {lat: 54.7959473, lon: 35.9274842}) {
    ...WeatherNow
  }
  Kremenki: weatherByPoint(request: {lat: 54.8862447, lon: 37.1168701}) {
    ...WeatherNow
  }
  Lyudinovo: weatherByPoint(request: {lat: 53.8700828, lon: 34.4385915}) {
    ...WeatherNow
  }
  Maloyaroslavets: weatherByPoint(request: {lat: 55.0177123, lon: 36.4633603}) {
    ...WeatherNow
  }
  Medyn: weatherByPoint(request: {lat: 54.9689785, lon: 35.8872168}) {
    ...WeatherNow
  }
  Meschovsk: weatherByPoint(request: {lat: 54.3191471, lon: 35.2816918}) {
    ...WeatherNow
  }
  Mosalsk: weatherByPoint(request: {lat: 54.4824939, lon: 34.9872239}) {
    ...WeatherNow
  }
  Obninsk: weatherByPoint(request: {lat: 55.0943144, lon: 36.6121639}) {
    ...WeatherNow
  }
  Sosenskiy: weatherByPoint(request: {lat: 54.0566016, lon: 35.9621646}) {
    ...WeatherNow
  }
  SpasDemensk: weatherByPoint(request: {lat: 54.409922, lon: 34.0189631}) {
    ...WeatherNow
  }
  Suhinichi: weatherByPoint(request: {lat: 54.097296, lon: 35.3443568}) {
    ...WeatherNow
  }
  Tarusa: weatherByPoint(request: {lat: 54.7236477, lon: 37.1671}) {
    ...WeatherNow
  }
  Yuhnov: weatherByPoint(request: {lat: 54.7446445, lon: 35.2424346}) {
    ...WeatherNow
  }
  Vilyuchinsk: weatherByPoint(request: {lat: 52.9302415, lon: 158.4057632}) {
    ...WeatherNow
  }
  Elizovo: weatherByPoint(request: {lat: 53.1830375, lon: 158.3883548}) {
    ...WeatherNow
  }
  PetropavlovskKamchatskiy: weatherByPoint(request: {lat: 53.036908, lon: 158.6559254}) {
    ...WeatherNow
  }
  Karachaevsk: weatherByPoint(request: {lat: 43.7732525, lon: 41.9143472}) {
    ...WeatherNow
  }
  Teberda: weatherByPoint(request: {lat: 43.4437731, lon: 41.7415142}) {
    ...WeatherNow
  }
  UstDzheguta: weatherByPoint(request: {lat: 44.0838442, lon: 41.9711046}) {
    ...WeatherNow
  }
  Cherkessk: weatherByPoint(request: {lat: 44.2269425, lon: 42.0466704}) {
    ...WeatherNow
  }
  Belomorsk: weatherByPoint(request: {lat: 64.5378417, lon: 34.7799462}) {
    ...WeatherNow
  }
  Kem: weatherByPoint(request: {lat: 64.9543539, lon: 34.5949263}) {
    ...WeatherNow
  }
  Kondopoga: weatherByPoint(request: {lat: 62.2059817, lon: 34.2682122}) {
    ...WeatherNow
  }
  Kostomuksha: weatherByPoint(request: {lat: 64.5889398, lon: 30.6016832}) {
    ...WeatherNow
  }
  Lahdenpohya: weatherByPoint(request: {lat: 61.518881, lon: 30.1996116}) {
    ...WeatherNow
  }
  Medvezhegorsk: weatherByPoint(request: {lat: 62.9127626, lon: 34.4568489}) {
    ...WeatherNow
  }
  Olonets: weatherByPoint(request: {lat: 60.9794025, lon: 32.9725519}) {
    ...WeatherNow
  }
  Petrozavodsk: weatherByPoint(request: {lat: 61.7891264, lon: 34.3596434}) {
    ...WeatherNow
  }
  Pitkyaranta: weatherByPoint(request: {lat: 61.5757191, lon: 31.4640557}) {
    ...WeatherNow
  }
  Pudozh: weatherByPoint(request: {lat: 61.8058821, lon: 36.5329941}) {
    ...WeatherNow
  }
  Segezha: weatherByPoint(request: {lat: 63.7437572, lon: 34.3126982}) {
    ...WeatherNow
  }
  Sortavala: weatherByPoint(request: {lat: 61.703367, lon: 30.6916998}) {
    ...WeatherNow
  }
  Suoyarvi: weatherByPoint(request: {lat: 62.0787293, lon: 32.3499386}) {
    ...WeatherNow
  }
  AnzheroSudzhensk: weatherByPoint(request: {lat: 56.0786281, lon: 86.0201278}) {
    ...WeatherNow
  }
  Belovo: weatherByPoint(request: {lat: 54.4220968, lon: 86.3037373}) {
    ...WeatherNow
  }
  Berezovskiy: weatherByPoint(request: {lat: 55.6693513, lon: 86.2744459}) {
    ...WeatherNow
  }
  Gurevsk_2: weatherByPoint(request: {lat: 54.2859263, lon: 85.9475985}) {
    ...WeatherNow
  }
  Kaltan: weatherByPoint(request: {lat: 53.5210919, lon: 87.2771636}) {
    ...WeatherNow
  }
  Kemerovo: weatherByPoint(request: {lat: 55.3910651, lon: 86.0467781}) {
    ...WeatherNow
  }
  Kiselevsk: weatherByPoint(request: {lat: 54.0059999, lon: 86.6366116}) {
    ...WeatherNow
  }
  LeninskKuznetskiy: weatherByPoint(request: {lat: 54.6674492, lon: 86.1797324}) {
    ...WeatherNow
  }
  Mariinsk: weatherByPoint(request: {lat: 56.2127383, lon: 87.7454924}) {
    ...WeatherNow
  }
  Mezhdurechensk: weatherByPoint(request: {lat: 53.6865289, lon: 88.0702754}) {
    ...WeatherNow
  }
  Myski: weatherByPoint(request: {lat: 53.7125695, lon: 87.8055646}) {
    ...WeatherNow
  }
  Novokuznetsk: weatherByPoint(request: {lat: 53.794315, lon: 87.2142745}) {
    ...WeatherNow
  }
  Osinniki: weatherByPoint(request: {lat: 53.5988055, lon: 87.3371272}) {
    ...WeatherNow
  }
  Polysaevo: weatherByPoint(request: {lat: 54.6055, lon: 86.2809208}) {
    ...WeatherNow
  }
  Prokopevsk: weatherByPoint(request: {lat: 53.8604265, lon: 86.7183577}) {
    ...WeatherNow
  }
  Salair: weatherByPoint(request: {lat: 54.2351735, lon: 85.8030733}) {
    ...WeatherNow
  }
  Tayga: weatherByPoint(request: {lat: 56.0622131, lon: 85.6207182}) {
    ...WeatherNow
  }
  Tashtagol: weatherByPoint(request: {lat: 52.759313, lon: 87.8476546}) {
    ...WeatherNow
  }
  Topki: weatherByPoint(request: {lat: 55.2764707, lon: 85.6152619}) {
    ...WeatherNow
  }
  Yurga: weatherByPoint(request: {lat: 55.7202694, lon: 84.8886399}) {
    ...WeatherNow
  }
  BelayaHolunitsa: weatherByPoint(request: {lat: 58.8415239, lon: 50.8460699}) {
    ...WeatherNow
  }
  VyatskiePolyany: weatherByPoint(request: {lat: 56.2284817, lon: 51.0614855}) {
    ...WeatherNow
  }
  Zuevka: weatherByPoint(request: {lat: 58.4032152, lon: 51.1331606}) {
    ...WeatherNow
  }
  Kirov_2: weatherByPoint(request: {lat: 58.6035264, lon: 49.6679304}) {
    ...WeatherNow
  }
  KirovoChepetsk: weatherByPoint(request: {lat: 58.5559424, lon: 50.0316848}) {
    ...WeatherNow
  }
  Kirs: weatherByPoint(request: {lat: 59.340056, lon: 52.2414437}) {
    ...WeatherNow
  }
  Kotelnich: weatherByPoint(request: {lat: 58.3034832, lon: 48.3475597}) {
    ...WeatherNow
  }
  Luza: weatherByPoint(request: {lat: 60.6290609, lon: 47.2612445}) {
    ...WeatherNow
  }
  Malmyzh: weatherByPoint(request: {lat: 56.5243844, lon: 50.6782739}) {
    ...WeatherNow
  }
  Murashi: weatherByPoint(request: {lat: 59.3955383, lon: 48.9638417}) {
    ...WeatherNow
  }
  Nolinsk: weatherByPoint(request: {lat: 57.5597284, lon: 49.93575}) {
    ...WeatherNow
  }
  Omutninsk: weatherByPoint(request: {lat: 58.6698913, lon: 52.1894564}) {
    ...WeatherNow
  }
  Orlov: weatherByPoint(request: {lat: 58.5389776, lon: 48.8927723}) {
    ...WeatherNow
  }
  Slobodskoy: weatherByPoint(request: {lat: 58.7311574, lon: 50.1669249}) {
    ...WeatherNow
  }
  Sovetsk_2: weatherByPoint(request: {lat: 57.584196, lon: 48.9590272}) {
    ...WeatherNow
  }
  Sosnovka: weatherByPoint(request: {lat: 56.2532741, lon: 51.2833642}) {
    ...WeatherNow
  }
  Urzhum: weatherByPoint(request: {lat: 57.1097477, lon: 50.0058097}) {
    ...WeatherNow
  }
  Yaransk: weatherByPoint(request: {lat: 57.3040326, lon: 47.8478737}) {
    ...WeatherNow
  }
  Vorkuta: weatherByPoint(request: {lat: 67.4974082, lon: 64.061034}) {
    ...WeatherNow
  }
  Vuktyl: weatherByPoint(request: {lat: 63.8615274, lon: 57.3165402}) {
    ...WeatherNow
  }
  Emva: weatherByPoint(request: {lat: 62.5965137, lon: 50.8732125}) {
    ...WeatherNow
  }
  Inta: weatherByPoint(request: {lat: 66.0367316, lon: 60.1152961}) {
    ...WeatherNow
  }
  Mikun: weatherByPoint(request: {lat: 62.3579068, lon: 50.0719503}) {
    ...WeatherNow
  }
  Pechora: weatherByPoint(request: {lat: 65.148584, lon: 57.2239777}) {
    ...WeatherNow
  }
  Sosnogorsk: weatherByPoint(request: {lat: 63.5989841, lon: 53.876293}) {
    ...WeatherNow
  }
  Syktyvkar: weatherByPoint(request: {lat: 61.6686617, lon: 50.8358151}) {
    ...WeatherNow
  }
  Usinsk: weatherByPoint(request: {lat: 65.994147, lon: 57.5569423}) {
    ...WeatherNow
  }
  Uhta: weatherByPoint(request: {lat: 63.5565514, lon: 53.7014239}) {
    ...WeatherNow
  }
  Buy: weatherByPoint(request: {lat: 58.4733277, lon: 41.5306822}) {
    ...WeatherNow
  }
  Volgorechensk: weatherByPoint(request: {lat: 57.4424559, lon: 41.1594201}) {
    ...WeatherNow
  }
  Galich: weatherByPoint(request: {lat: 58.3828191, lon: 42.3654013}) {
    ...WeatherNow
  }
  Kologriv: weatherByPoint(request: {lat: 58.8269323, lon: 44.3184927}) {
    ...WeatherNow
  }
  Kostroma: weatherByPoint(request: {lat: 57.768, lon: 40.927}) {
    ...WeatherNow
  }
  Makarev: weatherByPoint(request: {lat: 57.8807152, lon: 43.8014197}) {
    ...WeatherNow
  }
  Manturovo: weatherByPoint(request: {lat: 58.3265441, lon: 44.757494}) {
    ...WeatherNow
  }
  Nerehta: weatherByPoint(request: {lat: 57.4543369, lon: 40.5723598}) {
    ...WeatherNow
  }
  Neya: weatherByPoint(request: {lat: 58.2943349, lon: 43.8780948}) {
    ...WeatherNow
  }
  Soligalich: weatherByPoint(request: {lat: 59.0784867, lon: 42.2878423}) {
    ...WeatherNow
  }
  Chuhloma: weatherByPoint(request: {lat: 58.753421, lon: 42.6884958}) {
    ...WeatherNow
  }
  Sharya: weatherByPoint(request: {lat: 58.3760542, lon: 45.4062414}) {
    ...WeatherNow
  }
  Abinsk: weatherByPoint(request: {lat: 44.8679655, lon: 38.1618157}) {
    ...WeatherNow
  }
  Anapa: weatherByPoint(request: {lat: 44.8950433, lon: 37.3163282}) {
    ...WeatherNow
  }
  Apsheronsk: weatherByPoint(request: {lat: 44.4584006, lon: 39.7299824}) {
    ...WeatherNow
  }
  Armavir: weatherByPoint(request: {lat: 45.0012149, lon: 41.1324168}) {
    ...WeatherNow
  }
  Belorechensk: weatherByPoint(request: {lat: 44.7651876, lon: 39.8781494}) {
    ...WeatherNow
  }
  Gelendzhik: weatherByPoint(request: {lat: 44.5630007, lon: 38.0790852}) {
    ...WeatherNow
  }
  GoryachiyKlyuch: weatherByPoint(request: {lat: 44.6344864, lon: 39.1354738}) {
    ...WeatherNow
  }
  Gulkevichi: weatherByPoint(request: {lat: 45.3605121, lon: 40.6918389}) {
    ...WeatherNow
  }
  Eysk: weatherByPoint(request: {lat: 46.71157, lon: 38.2763895}) {
    ...WeatherNow
  }
  Korenovsk: weatherByPoint(request: {lat: 45.4641703, lon: 39.458949}) {
    ...WeatherNow
  }
  Krasnodar: weatherByPoint(request: {lat: 45.0401604, lon: 38.9759647}) {
    ...WeatherNow
  }
  Kropotkin: weatherByPoint(request: {lat: 45.4333007, lon: 40.5727951}) {
    ...WeatherNow
  }
  Krymsk: weatherByPoint(request: {lat: 44.9344404, lon: 37.9855795}) {
    ...WeatherNow
  }
  Kurganinsk: weatherByPoint(request: {lat: 44.8877025, lon: 40.5913245}) {
    ...WeatherNow
  }
  Labinsk: weatherByPoint(request: {lat: 44.6354363, lon: 40.7245341}) {
    ...WeatherNow
  }
  Novokubansk: weatherByPoint(request: {lat: 45.1038699, lon: 41.0475175}) {
    ...WeatherNow
  }
  Novorossiysk: weatherByPoint(request: {lat: 44.7235026, lon: 37.7686135}) {
    ...WeatherNow
  }
  PrimorskoAhtarsk: weatherByPoint(request: {lat: 46.0515432, lon: 38.1704875}) {
    ...WeatherNow
  }
  SlavyanskNaKubani: weatherByPoint(request: {lat: 45.2603626, lon: 38.1259774}) {
    ...WeatherNow
  }
  Sochi: weatherByPoint(request: {lat: 43.5854551, lon: 39.7231548}) {
    ...WeatherNow
  }
  Temryuk: weatherByPoint(request: {lat: 45.2610949, lon: 37.4454412}) {
    ...WeatherNow
  }
  Timashevsk: weatherByPoint(request: {lat: 45.615923, lon: 38.9351837}) {
    ...WeatherNow
  }
  Tihoretsk: weatherByPoint(request: {lat: 45.8546345, lon: 40.1260267}) {
    ...WeatherNow
  }
  Tuapse: weatherByPoint(request: {lat: 44.1105335, lon: 39.0824904}) {
    ...WeatherNow
  }
  UstLabinsk: weatherByPoint(request: {lat: 45.2227359, lon: 39.6929577}) {
    ...WeatherNow
  }
  Hadyzhensk: weatherByPoint(request: {lat: 44.4122963, lon: 39.5320258}) {
    ...WeatherNow
  }
  Artemovsk: weatherByPoint(request: {lat: 54.3473075, lon: 93.4358377}) {
    ...WeatherNow
  }
  Achinsk: weatherByPoint(request: {lat: 56.253907, lon: 90.4794397}) {
    ...WeatherNow
  }
  Bogotol: weatherByPoint(request: {lat: 56.2098468, lon: 89.5299336}) {
    ...WeatherNow
  }
  Borodino: weatherByPoint(request: {lat: 55.9054121, lon: 94.9020967}) {
    ...WeatherNow
  }
  Divnogorsk: weatherByPoint(request: {lat: 55.9576784, lon: 92.3800687}) {
    ...WeatherNow
  }
  Dudinka: weatherByPoint(request: {lat: 69.4031364, lon: 86.1907218}) {
    ...WeatherNow
  }
  Eniseysk: weatherByPoint(request: {lat: 58.4485261, lon: 92.1651083}) {
    ...WeatherNow
  }
  Zheleznogorsk: weatherByPoint(request: {lat: 56.2529035, lon: 93.532273}) {
    ...WeatherNow
  }
  Zaozernyy: weatherByPoint(request: {lat: 55.9617752, lon: 94.7091491}) {
    ...WeatherNow
  }
  Zelenogorsk: weatherByPoint(request: {lat: 56.1131564, lon: 94.5888103}) {
    ...WeatherNow
  }
  Igarka: weatherByPoint(request: {lat: 67.4666901, lon: 86.5812794}) {
    ...WeatherNow
  }
  Ilanskiy: weatherByPoint(request: {lat: 56.2374037, lon: 96.067267}) {
    ...WeatherNow
  }
  Kansk: weatherByPoint(request: {lat: 56.2051282, lon: 95.7051096}) {
    ...WeatherNow
  }
  Kodinsk: weatherByPoint(request: {lat: 58.6032644, lon: 99.1797962}) {
    ...WeatherNow
  }
  Krasnoyarsk: weatherByPoint(request: {lat: 56.0093879, lon: 92.8524806}) {
    ...WeatherNow
  }
  Lesosibirsk: weatherByPoint(request: {lat: 58.221681, lon: 92.5037872}) {
    ...WeatherNow
  }
  Minusinsk: weatherByPoint(request: {lat: 53.7104586, lon: 91.6872907}) {
    ...WeatherNow
  }
  Nazarovo: weatherByPoint(request: {lat: 56.0113799, lon: 90.4168775}) {
    ...WeatherNow
  }
  Norilsk: weatherByPoint(request: {lat: 69.3489978, lon: 88.2009846}) {
    ...WeatherNow
  }
  Sosnovoborsk: weatherByPoint(request: {lat: 56.1202647, lon: 93.3354121}) {
    ...WeatherNow
  }
  Uzhur: weatherByPoint(request: {lat: 55.3141969, lon: 89.8333918}) {
    ...WeatherNow
  }
  Uyar: weatherByPoint(request: {lat: 55.8131263, lon: 94.3282601}) {
    ...WeatherNow
  }
  Sharypovo: weatherByPoint(request: {lat: 55.5389739, lon: 89.1801044}) {
    ...WeatherNow
  }
  Alupka: weatherByPoint(request: {lat: 44.4164605, lon: 34.0444797}) {
    ...WeatherNow
  }
  Alushta: weatherByPoint(request: {lat: 44.6764304, lon: 34.4100624}) {
    ...WeatherNow
  }
  Armyansk: weatherByPoint(request: {lat: 46.1059307, lon: 33.6910012}) {
    ...WeatherNow
  }
  Bahchisaray: weatherByPoint(request: {lat: 44.7514769, lon: 33.8752176}) {
    ...WeatherNow
  }
  Belogorsk_2: weatherByPoint(request: {lat: 45.057202, lon: 34.5999029}) {
    ...WeatherNow
  }
  Dzhankoy: weatherByPoint(request: {lat: 45.7092306, lon: 34.3883372}) {
    ...WeatherNow
  }
  Evpatoriya: weatherByPoint(request: {lat: 45.190629, lon: 33.367634}) {
    ...WeatherNow
  }
  Kerch: weatherByPoint(request: {lat: 45.3562627, lon: 36.4674513}) {
    ...WeatherNow
  }
  Krasnoperekopsk: weatherByPoint(request: {lat: 45.9537576, lon: 33.7921939}) {
    ...WeatherNow
  }
  Saki: weatherByPoint(request: {lat: 45.1341997, lon: 33.6033383}) {
    ...WeatherNow
  }
  Simferopol: weatherByPoint(request: {lat: 44.9482948, lon: 34.1001151}) {
    ...WeatherNow
  }
  StaryyKrym: weatherByPoint(request: {lat: 45.029058, lon: 35.0901474}) {
    ...WeatherNow
  }
  Sudak: weatherByPoint(request: {lat: 44.8504679, lon: 34.9762034}) {
    ...WeatherNow
  }
  Feodosiya: weatherByPoint(request: {lat: 45.0318393, lon: 35.3824259}) {
    ...WeatherNow
  }
  Schelkino: weatherByPoint(request: {lat: 45.4288991, lon: 35.825165}) {
    ...WeatherNow
  }
  Yalta: weatherByPoint(request: {lat: 44.4953612, lon: 34.166308}) {
    ...WeatherNow
  }
  Dalmatovo: weatherByPoint(request: {lat: 56.262114, lon: 62.9387011}) {
    ...WeatherNow
  }
  Kataysk: weatherByPoint(request: {lat: 56.290809, lon: 62.5800359}) {
    ...WeatherNow
  }
  Kurgan: weatherByPoint(request: {lat: 55.4443883, lon: 65.3161963}) {
    ...WeatherNow
  }
  Kurtamysh: weatherByPoint(request: {lat: 54.9368539, lon: 64.4203722}) {
    ...WeatherNow
  }
  Makushino: weatherByPoint(request: {lat: 55.2153947, lon: 67.2451705}) {
    ...WeatherNow
  }
  Petuhovo: weatherByPoint(request: {lat: 55.0650077, lon: 67.8873408}) {
    ...WeatherNow
  }
  Shadrinsk: weatherByPoint(request: {lat: 56.0870344, lon: 63.6297182}) {
    ...WeatherNow
  }
  Shumiha: weatherByPoint(request: {lat: 55.2280246, lon: 63.2901272}) {
    ...WeatherNow
  }
  Schuche: weatherByPoint(request: {lat: 55.2087637, lon: 62.7478548}) {
    ...WeatherNow
  }
  Dmitriev: weatherByPoint(request: {lat: 52.1268464, lon: 35.0739038}) {
    ...WeatherNow
  }
  Zheleznogorsk_2: weatherByPoint(request: {lat: 52.3380202, lon: 35.3516867}) {
    ...WeatherNow
  }
  Kursk: weatherByPoint(request: {lat: 51.7303637, lon: 36.1925603}) {
    ...WeatherNow
  }
  Kurchatov: weatherByPoint(request: {lat: 51.6604083, lon: 35.6572224}) {
    ...WeatherNow
  }
  Lgov: weatherByPoint(request: {lat: 51.6597148, lon: 35.2612491}) {
    ...WeatherNow
  }
  Oboyan: weatherByPoint(request: {lat: 51.2119324, lon: 36.2755133}) {
    ...WeatherNow
  }
  Rylsk: weatherByPoint(request: {lat: 51.5681314, lon: 34.6802597}) {
    ...WeatherNow
  }
  Sudzha: weatherByPoint(request: {lat: 51.1918927, lon: 35.2720915}) {
    ...WeatherNow
  }
  Fatezh: weatherByPoint(request: {lat: 52.0917728, lon: 35.8538706}) {
    ...WeatherNow
  }
  Schigry: weatherByPoint(request: {lat: 51.8786014, lon: 36.8910945}) {
    ...WeatherNow
  }
  Boksitogorsk: weatherByPoint(request: {lat: 59.4734797, lon: 33.845688}) {
    ...WeatherNow
  }
  Volosovo: weatherByPoint(request: {lat: 59.4445408, lon: 29.4923355}) {
    ...WeatherNow
  }
  Volhov: weatherByPoint(request: {lat: 59.9005958, lon: 32.3520756}) {
    ...WeatherNow
  }
  Vsevolozhsk: weatherByPoint(request: {lat: 60.0191278, lon: 30.6456718}) {
    ...WeatherNow
  }
  Vyborg: weatherByPoint(request: {lat: 60.7130801, lon: 28.7328336}) {
    ...WeatherNow
  }
  Vysotsk: weatherByPoint(request: {lat: 60.6296236, lon: 28.5709314}) {
    ...WeatherNow
  }
  Gatchina: weatherByPoint(request: {lat: 59.565237, lon: 30.1282473}) {
    ...WeatherNow
  }
  Ivangorod: weatherByPoint(request: {lat: 59.3766119, lon: 28.2231659}) {
    ...WeatherNow
  }
  Kamennogorsk: weatherByPoint(request: {lat: 60.950855, lon: 29.1308372}) {
    ...WeatherNow
  }
  Kingisepp: weatherByPoint(request: {lat: 59.3740435, lon: 28.6112444}) {
    ...WeatherNow
  }
  Kirishi: weatherByPoint(request: {lat: 59.4742862, lon: 32.0624947}) {
    ...WeatherNow
  }
  Kirovsk: weatherByPoint(request: {lat: 59.8754216, lon: 30.981364}) {
    ...WeatherNow
  }
  Kommunar: weatherByPoint(request: {lat: 59.6215133, lon: 30.3934125}) {
    ...WeatherNow
  }
  Kudrovo: weatherByPoint(request: {lat: 59.9075226, lon: 30.5121008}) {
    ...WeatherNow
  }
  LodeynoePole: weatherByPoint(request: {lat: 60.7320936, lon: 33.5521022}) {
    ...WeatherNow
  }
  Luga: weatherByPoint(request: {lat: 58.7374031, lon: 29.8465776}) {
    ...WeatherNow
  }
  Lyuban: weatherByPoint(request: {lat: 59.3493847, lon: 31.2484801}) {
    ...WeatherNow
  }
  Murino: weatherByPoint(request: {lat: 60.044862, lon: 30.4571456}) {
    ...WeatherNow
  }
  Nikolskoe: weatherByPoint(request: {lat: 59.7043309, lon: 30.7874571}) {
    ...WeatherNow
  }
  NovayaLadoga: weatherByPoint(request: {lat: 60.1100135, lon: 32.3141203}) {
    ...WeatherNow
  }
  Otradnoe: weatherByPoint(request: {lat: 59.7726848, lon: 30.7988557}) {
    ...WeatherNow
  }
  Pikalevo: weatherByPoint(request: {lat: 59.5132022, lon: 34.1772776}) {
    ...WeatherNow
  }
  Podporozhe: weatherByPoint(request: {lat: 60.9127549, lon: 34.1567664}) {
    ...WeatherNow
  }
  Primorsk_2: weatherByPoint(request: {lat: 60.3660209, lon: 28.6135772}) {
    ...WeatherNow
  }
  Priozersk: weatherByPoint(request: {lat: 61.0330896, lon: 30.1587851}) {
    ...WeatherNow
  }
  Svetogorsk: weatherByPoint(request: {lat: 61.1111282, lon: 28.8725865}) {
    ...WeatherNow
  }
  Sertolovo: weatherByPoint(request: {lat: 60.1446932, lon: 30.2095918}) {
    ...WeatherNow
  }
  Slantsy: weatherByPoint(request: {lat: 59.1178185, lon: 28.0881475}) {
    ...WeatherNow
  }
  SosnovyyBor: weatherByPoint(request: {lat: 59.8772884, lon: 29.1291619}) {
    ...WeatherNow
  }
  Syasstroy: weatherByPoint(request: {lat: 60.1401739, lon: 32.5601559}) {
    ...WeatherNow
  }
  Tihvin: weatherByPoint(request: {lat: 59.6272904, lon: 33.5072731}) {
    ...WeatherNow
  }
  Tosno: weatherByPoint(request: {lat: 59.5407098, lon: 30.877812}) {
    ...WeatherNow
  }
  Shlisselburg: weatherByPoint(request: {lat: 59.9443714, lon: 31.0333365}) {
    ...WeatherNow
  }
  Gryazi: weatherByPoint(request: {lat: 52.4874097, lon: 39.9331142}) {
    ...WeatherNow
  }
  Dankov: weatherByPoint(request: {lat: 53.2577411, lon: 39.1456184}) {
    ...WeatherNow
  }
  Elets: weatherByPoint(request: {lat: 52.6152411, lon: 38.5289342}) {
    ...WeatherNow
  }
  Zadonsk: weatherByPoint(request: {lat: 52.4004179, lon: 38.9205032}) {
    ...WeatherNow
  }
  Lebedyan: weatherByPoint(request: {lat: 53.0156117, lon: 39.143536}) {
    ...WeatherNow
  }
  Lipetsk: weatherByPoint(request: {lat: 52.610249, lon: 39.5947883}) {
    ...WeatherNow
  }
  Usman: weatherByPoint(request: {lat: 52.0442648, lon: 39.726401}) {
    ...WeatherNow
  }
  Chaplygin: weatherByPoint(request: {lat: 53.24048, lon: 39.9670973}) {
    ...WeatherNow
  }
  Magadan: weatherByPoint(request: {lat: 59.5681332, lon: 150.8084956}) {
    ...WeatherNow
  }
  Susuman: weatherByPoint(request: {lat: 62.7805882, lon: 148.1540281}) {
    ...WeatherNow
  }
  Volzhsk: weatherByPoint(request: {lat: 55.8623156, lon: 48.3715083}) {
    ...WeatherNow
  }
  Zvenigovo: weatherByPoint(request: {lat: 55.9738571, lon: 48.0170245}) {
    ...WeatherNow
  }
  YoshkarOla: weatherByPoint(request: {lat: 56.6343662, lon: 47.8999706}) {
    ...WeatherNow
  }
  Kozmodemyansk: weatherByPoint(request: {lat: 56.3334036, lon: 46.546675}) {
    ...WeatherNow
  }
  Ardatov: weatherByPoint(request: {lat: 54.8465544, lon: 46.2411232}) {
    ...WeatherNow
  }
  Insar: weatherByPoint(request: {lat: 53.8770022, lon: 44.3696566}) {
    ...WeatherNow
  }
  Kovylkino: weatherByPoint(request: {lat: 54.0391072, lon: 43.9191539}) {
    ...WeatherNow
  }
  Krasnoslobodsk_2: weatherByPoint(request: {lat: 54.4248207, lon: 43.7845011}) {
    ...WeatherNow
  }
  Ruzaevka: weatherByPoint(request: {lat: 54.0581967, lon: 44.9490466}) {
    ...WeatherNow
  }
  Saransk: weatherByPoint(request: {lat: 54.1809332, lon: 45.1862632}) {
    ...WeatherNow
  }
  Temnikov: weatherByPoint(request: {lat: 54.6310583, lon: 43.2161099}) {
    ...WeatherNow
  }
  
  Aprelevka: weatherByPoint(request: {lat: 55.5276918, lon: 37.065143}) {
    ...WeatherNow
  }
  Balashiha: weatherByPoint(request: {lat: 55.796389, lon: 37.938283}) {
    ...WeatherNow
  }
  Beloozyorskiy: weatherByPoint(request: {lat: 55.4595766, lon: 38.4389742}) {
    ...WeatherNow
  }
  Bronnitsy: weatherByPoint(request: {lat: 55.4255379, lon: 38.264145}) {
    ...WeatherNow
  }
  Vereya: weatherByPoint(request: {lat: 55.343369, lon: 36.185694}) {
    ...WeatherNow
  }
  Vidnoe: weatherByPoint(request: {lat: 55.551725, lon: 37.7061984}) {
    ...WeatherNow
  }
  Volokolamsk: weatherByPoint(request: {lat: 56.0356499, lon: 35.9585112}) {
    ...WeatherNow
  }
  Voskresensk: weatherByPoint(request: {lat: 55.3071519, lon: 38.7027953}) {
    ...WeatherNow
  }
  Vysokovsk: weatherByPoint(request: {lat: 56.3359513, lon: 36.5251837}) {
    ...WeatherNow
  }
  Golitsyno: weatherByPoint(request: {lat: 55.6190582, lon: 36.9856793}) {
    ...WeatherNow
  }
  Dedovsk: weatherByPoint(request: {lat: 55.8703276, lon: 37.1245043}) {
    ...WeatherNow
  }
  Dzerzhinskiy: weatherByPoint(request: {lat: 55.6240869, lon: 37.8440276}) {
    ...WeatherNow
  }
  Dmitrov: weatherByPoint(request: {lat: 56.3477457, lon: 37.526672}) {
    ...WeatherNow
  }
  Dolgoprudnyy: weatherByPoint(request: {lat: 55.9385999, lon: 37.5101021}) {
    ...WeatherNow
  }
  Domodedovo: weatherByPoint(request: {lat: 55.4363283, lon: 37.7664984}) {
    ...WeatherNow
  }
  Drezna: weatherByPoint(request: {lat: 55.7443143, lon: 38.8498479}) {
    ...WeatherNow
  }
  Dubna: weatherByPoint(request: {lat: 56.741786, lon: 37.1757223}) {
    ...WeatherNow
  }
  Egorevsk: weatherByPoint(request: {lat: 55.3830113, lon: 39.0358317}) {
    ...WeatherNow
  }
  Zhukovskiy: weatherByPoint(request: {lat: 55.599803, lon: 38.1224298}) {
    ...WeatherNow
  }
  Zaraysk: weatherByPoint(request: {lat: 54.762456, lon: 38.8850978}) {
    ...WeatherNow
  }
  Zvenigorod: weatherByPoint(request: {lat: 55.7297089, lon: 36.8554029}) {
    ...WeatherNow
  }
  Ivanteevka: weatherByPoint(request: {lat: 55.9741665, lon: 37.9207539}) {
    ...WeatherNow
  }
  Istra: weatherByPoint(request: {lat: 55.9062267, lon: 36.8601454}) {
    ...WeatherNow
  }
  Kashira: weatherByPoint(request: {lat: 54.853337, lon: 38.1904392}) {
    ...WeatherNow
  }
  Klin: weatherByPoint(request: {lat: 56.3425605, lon: 36.7240032}) {
    ...WeatherNow
  }
  Kolomna: weatherByPoint(request: {lat: 55.102814, lon: 38.7531002}) {
    ...WeatherNow
  }
  Korolyov: weatherByPoint(request: {lat: 55.9161773, lon: 37.8545415}) {
    ...WeatherNow
  }
  Kotelniki: weatherByPoint(request: {lat: 55.6597925, lon: 37.8631156}) {
    ...WeatherNow
  }
  Krasnoarmeysk: weatherByPoint(request: {lat: 56.105426, lon: 38.140838}) {
    ...WeatherNow
  }
  Krasnogorsk: weatherByPoint(request: {lat: 55.8317203, lon: 37.3295266}) {
    ...WeatherNow
  }
  Krasnozavodsk: weatherByPoint(request: {lat: 56.4409979, lon: 38.2320307}) {
    ...WeatherNow
  }
  Krasnoznamensk_2: weatherByPoint(request: {lat: 55.5978959, lon: 37.0393709}) {
    ...WeatherNow
  }
  Kubinka: weatherByPoint(request: {lat: 55.5754955, lon: 36.6951995}) {
    ...WeatherNow
  }
  Kurovskoe: weatherByPoint(request: {lat: 55.5792277, lon: 38.9207723}) {
    ...WeatherNow
  }
  LikinoDulyovo: weatherByPoint(request: {lat: 55.7078257, lon: 38.9578093}) {
    ...WeatherNow
  }
  Lobnya: weatherByPoint(request: {lat: 56.0328881, lon: 37.4614035}) {
    ...WeatherNow
  }
  LosinoPetrovskiy: weatherByPoint(request: {lat: 55.8713214, lon: 38.200599}) {
    ...WeatherNow
  }
  Luhovitsy: weatherByPoint(request: {lat: 54.9652077, lon: 39.0260266}) {
    ...WeatherNow
  }
  Lytkarino: weatherByPoint(request: {lat: 55.5778163, lon: 37.9033507}) {
    ...WeatherNow
  }
  Lyubertsy: weatherByPoint(request: {lat: 55.676499, lon: 37.898125}) {
    ...WeatherNow
  }
  Mozhaysk: weatherByPoint(request: {lat: 55.5069259, lon: 36.024043}) {
    ...WeatherNow
  }
  Mytischi: weatherByPoint(request: {lat: 55.9105782, lon: 37.7363579}) {
    ...WeatherNow
  }
  NaroFominsk: weatherByPoint(request: {lat: 55.386185, lon: 36.734484}) {
    ...WeatherNow
  }
  Noginsk: weatherByPoint(request: {lat: 55.8686133, lon: 38.4622104}) {
    ...WeatherNow
  }
  Odintsovo: weatherByPoint(request: {lat: 55.6789455, lon: 37.263686}) {
    ...WeatherNow
  }
  Ozyory: weatherByPoint(request: {lat: 54.8541006, lon: 38.5599196}) {
    ...WeatherNow
  }
  OrehovoZuevo: weatherByPoint(request: {lat: 55.8151421, lon: 38.9869822}) {
    ...WeatherNow
  }
  PavlovskiyPosad: weatherByPoint(request: {lat: 55.7807244, lon: 38.6596983}) {
    ...WeatherNow
  }
  Peresvet: weatherByPoint(request: {lat: 56.4158326, lon: 38.1733534}) {
    ...WeatherNow
  }
  Podolsk: weatherByPoint(request: {lat: 55.4389322, lon: 37.5703482}) {
    ...WeatherNow
  }
  Protvino: weatherByPoint(request: {lat: 54.8705984, lon: 37.2182749}) {
    ...WeatherNow
  }
  Pushkino: weatherByPoint(request: {lat: 56.0103638, lon: 37.8471403}) {
    ...WeatherNow
  }
  Puschino: weatherByPoint(request: {lat: 54.8324412, lon: 37.6210346}) {
    ...WeatherNow
  }
  Ramenskoe: weatherByPoint(request: {lat: 55.5495132, lon: 38.2728914}) {
    ...WeatherNow
  }
  Reutov: weatherByPoint(request: {lat: 55.7582621, lon: 37.8618553}) {
    ...WeatherNow
  }
  Roshal: weatherByPoint(request: {lat: 55.6632776, lon: 39.8656147}) {
    ...WeatherNow
  }
  Ruza: weatherByPoint(request: {lat: 55.7014744, lon: 36.1959206}) {
    ...WeatherNow
  }
  SergievPosad: weatherByPoint(request: {lat: 56.3062548, lon: 38.1502661}) {
    ...WeatherNow
  }
  Serpuhov: weatherByPoint(request: {lat: 54.9226466, lon: 37.4033859}) {
    ...WeatherNow
  }
  Solnechnogorsk: weatherByPoint(request: {lat: 56.185102, lon: 36.977631}) {
    ...WeatherNow
  }
  StarayaKupavna: weatherByPoint(request: {lat: 55.810648, lon: 38.175624}) {
    ...WeatherNow
  }
  Stupino: weatherByPoint(request: {lat: 54.886274, lon: 38.078228}) {
    ...WeatherNow
  }
  Taldom: weatherByPoint(request: {lat: 56.7308564, lon: 37.5276003}) {
    ...WeatherNow
  }
  Fryazino: weatherByPoint(request: {lat: 55.9590588, lon: 38.0410235}) {
    ...WeatherNow
  }
  Himki: weatherByPoint(request: {lat: 55.888657, lon: 37.4303702}) {
    ...WeatherNow
  }
  Hotkovo: weatherByPoint(request: {lat: 56.2516982, lon: 37.9396017}) {
    ...WeatherNow
  }
  Chernogolovka: weatherByPoint(request: {lat: 56.010005, lon: 38.379245}) {
    ...WeatherNow
  }
  Chehov: weatherByPoint(request: {lat: 55.1508011, lon: 37.4533252}) {
    ...WeatherNow
  }
  Shatura: weatherByPoint(request: {lat: 55.5777427, lon: 39.5445712}) {
    ...WeatherNow
  }
  Schyolkovo: weatherByPoint(request: {lat: 55.9233801, lon: 37.9783707}) {
    ...WeatherNow
  }
  Elektrogorsk: weatherByPoint(request: {lat: 55.8780241, lon: 38.7806752}) {
    ...WeatherNow
  }
  Elektrostal: weatherByPoint(request: {lat: 55.7847291, lon: 38.4447045}) {
    ...WeatherNow
  }
  Elektrougli: weatherByPoint(request: {lat: 55.7170877, lon: 38.2192563}) {
    ...WeatherNow
  }
  Yahroma: weatherByPoint(request: {lat: 56.2890516, lon: 37.4831799}) {
    ...WeatherNow
  }
  Apatity: weatherByPoint(request: {lat: 67.5677761, lon: 33.4067929}) {
    ...WeatherNow
  }
  Gadzhievo: weatherByPoint(request: {lat: 69.2491311, lon: 33.315341}) {
    ...WeatherNow
  }
  Zaozersk: weatherByPoint(request: {lat: 69.4003584, lon: 32.4501496}) {
    ...WeatherNow
  }
  Zapolyarnyy: weatherByPoint(request: {lat: 69.4132852, lon: 30.7984312}) {
    ...WeatherNow
  }
  Kandalaksha: weatherByPoint(request: {lat: 67.1567974, lon: 32.4143218}) {
    ...WeatherNow
  }
  Kirovsk_2: weatherByPoint(request: {lat: 67.6150424, lon: 33.663735}) {
    ...WeatherNow
  }
  Kovdor: weatherByPoint(request: {lat: 67.5661417, lon: 30.4741941}) {
    ...WeatherNow
  }
  Kola: weatherByPoint(request: {lat: 68.8786028, lon: 33.0262299}) {
    ...WeatherNow
  }
  Monchegorsk: weatherByPoint(request: {lat: 67.9386153, lon: 32.9359719}) {
    ...WeatherNow
  }
  Murmansk: weatherByPoint(request: {lat: 69.007721, lon: 33.0685865}) {
    ...WeatherNow
  }
  Olenegorsk: weatherByPoint(request: {lat: 68.1422058, lon: 33.2669407}) {
    ...WeatherNow
  }
  Ostrovnoy: weatherByPoint(request: {lat: 68.0510344, lon: 39.5077846}) {
    ...WeatherNow
  }
  PolyarnyeZori: weatherByPoint(request: {lat: 67.373084, lon: 32.4975636}) {
    ...WeatherNow
  }
  Polyarnyy: weatherByPoint(request: {lat: 69.1989583, lon: 33.4508591}) {
    ...WeatherNow
  }
  Severomorsk: weatherByPoint(request: {lat: 69.0766801, lon: 33.4177759}) {
    ...WeatherNow
  }
  Snezhnogorsk: weatherByPoint(request: {lat: 69.1921409, lon: 33.2383502}) {
    ...WeatherNow
  }
  NaryanMar: weatherByPoint(request: {lat: 67.6379672, lon: 53.0069565}) {
    ...WeatherNow
  }
  Arzamas: weatherByPoint(request: {lat: 55.3945814, lon: 43.8408141}) {
    ...WeatherNow
  }
  Balahna: weatherByPoint(request: {lat: 56.495036, lon: 43.5758423}) {
    ...WeatherNow
  }
  Bogorodsk: weatherByPoint(request: {lat: 56.1020828, lon: 43.5135442}) {
    ...WeatherNow
  }
  Bor: weatherByPoint(request: {lat: 56.3565458, lon: 44.0646481}) {
    ...WeatherNow
  }
  Vetluga: weatherByPoint(request: {lat: 57.8559204, lon: 45.7761957}) {
    ...WeatherNow
  }
  Volodarsk: weatherByPoint(request: {lat: 56.2169751, lon: 43.1596417}) {
    ...WeatherNow
  }
  Vorsma: weatherByPoint(request: {lat: 55.989943, lon: 43.2718859}) {
    ...WeatherNow
  }
  Vyksa: weatherByPoint(request: {lat: 55.3207727, lon: 42.1678834}) {
    ...WeatherNow
  }
  Gorbatov: weatherByPoint(request: {lat: 56.1307769, lon: 43.0626185}) {
    ...WeatherNow
  }
  Gorodets: weatherByPoint(request: {lat: 56.6449218, lon: 43.4723104}) {
    ...WeatherNow
  }
  Dzerzhinsk: weatherByPoint(request: {lat: 56.2376047, lon: 43.4599416}) {
    ...WeatherNow
  }
  Zavolzhe: weatherByPoint(request: {lat: 56.6404286, lon: 43.3872492}) {
    ...WeatherNow
  }
  Knyaginino: weatherByPoint(request: {lat: 55.8205915, lon: 45.032337}) {
    ...WeatherNow
  }
  Kstovo: weatherByPoint(request: {lat: 56.1432084, lon: 44.1664198}) {
    ...WeatherNow
  }
  Kulebaki: weatherByPoint(request: {lat: 55.4296181, lon: 42.5125538}) {
    ...WeatherNow
  }
  Lukoyanov: weatherByPoint(request: {lat: 55.0326225, lon: 44.4933807}) {
    ...WeatherNow
  }
  Lyskovo: weatherByPoint(request: {lat: 56.0262359, lon: 45.035771}) {
    ...WeatherNow
  }
  Navashino: weatherByPoint(request: {lat: 55.543811, lon: 42.1887089}) {
    ...WeatherNow
  }
  NizhniyNovgorod: weatherByPoint(request: {lat: 56.3240627, lon: 44.0053913}) {
    ...WeatherNow
  }
  Pavlovo: weatherByPoint(request: {lat: 55.9797564, lon: 43.0995042}) {
    ...WeatherNow
  }
  Pervomaysk: weatherByPoint(request: {lat: 54.8675792, lon: 43.8013992}) {
    ...WeatherNow
  }
  Perevoz: weatherByPoint(request: {lat: 55.5967718, lon: 44.5448369}) {
    ...WeatherNow
  }
  Sarov: weatherByPoint(request: {lat: 54.9228268, lon: 43.3448089}) {
    ...WeatherNow
  }
  Semenov: weatherByPoint(request: {lat: 56.7889794, lon: 44.4902885}) {
    ...WeatherNow
  }
  Sergach: weatherByPoint(request: {lat: 55.5201515, lon: 45.4813231}) {
    ...WeatherNow
  }
  Uren: weatherByPoint(request: {lat: 57.4612572, lon: 45.7833293}) {
    ...WeatherNow
  }
  Chkalovsk: weatherByPoint(request: {lat: 56.7651262, lon: 43.242077}) {
    ...WeatherNow
  }
  Shahunya: weatherByPoint(request: {lat: 57.6764293, lon: 46.6129009}) {
    ...WeatherNow
  }
  Borovichi: weatherByPoint(request: {lat: 58.3840197, lon: 33.9175929}) {
    ...WeatherNow
  }
  Valday: weatherByPoint(request: {lat: 57.9823766, lon: 33.2369436}) {
    ...WeatherNow
  }
  VelikiyNovgorod: weatherByPoint(request: {lat: 58.5213846, lon: 31.2755394}) {
    ...WeatherNow
  }
  MalayaVishera: weatherByPoint(request: {lat: 58.8458379, lon: 32.2247401}) {
    ...WeatherNow
  }
  Okulovka: weatherByPoint(request: {lat: 58.3910296, lon: 33.2901557}) {
    ...WeatherNow
  }
  Pestovo: weatherByPoint(request: {lat: 58.5973723, lon: 35.8143898}) {
    ...WeatherNow
  }
  Soltsy: weatherByPoint(request: {lat: 58.1201281, lon: 30.309351}) {
    ...WeatherNow
  }
  StarayaRussa: weatherByPoint(request: {lat: 57.990737, lon: 31.3554897}) {
    ...WeatherNow
  }
  Holm: weatherByPoint(request: {lat: 57.145108, lon: 31.1787499}) {
    ...WeatherNow
  }
  Chudovo: weatherByPoint(request: {lat: 59.1248394, lon: 31.6866241}) {
    ...WeatherNow
  }
  Barabinsk: weatherByPoint(request: {lat: 55.35146, lon: 78.3464506}) {
    ...WeatherNow
  }
  Berdsk: weatherByPoint(request: {lat: 54.7582156, lon: 83.1070605}) {
    ...WeatherNow
  }
  Bolotnoe: weatherByPoint(request: {lat: 55.6692421, lon: 84.3906889}) {
    ...WeatherNow
  }
  Iskitim: weatherByPoint(request: {lat: 54.6267603, lon: 83.2951244}) {
    ...WeatherNow
  }
  Karasuk: weatherByPoint(request: {lat: 53.7343189, lon: 78.0422967}) {
    ...WeatherNow
  }
  Kargat: weatherByPoint(request: {lat: 55.1945666, lon: 80.2829495}) {
    ...WeatherNow
  }
  Kuybyshev: weatherByPoint(request: {lat: 55.4685094, lon: 78.3242048}) {
    ...WeatherNow
  }
  Kupino: weatherByPoint(request: {lat: 54.366055, lon: 77.2973368}) {
    ...WeatherNow
  }
  Novosibirsk: weatherByPoint(request: {lat: 55.028191, lon: 82.9211489}) {
    ...WeatherNow
  }
  Ob: weatherByPoint(request: {lat: 54.9945576, lon: 82.6937181}) {
    ...WeatherNow
  }
  Tatarsk: weatherByPoint(request: {lat: 55.2146167, lon: 75.9739914}) {
    ...WeatherNow
  }
  Toguchin: weatherByPoint(request: {lat: 55.2251631, lon: 84.4104118}) {
    ...WeatherNow
  }
  Cherepanovo: weatherByPoint(request: {lat: 54.2206476, lon: 83.3724521}) {
    ...WeatherNow
  }
  Chulym: weatherByPoint(request: {lat: 55.0906867, lon: 80.9592508}) {
    ...WeatherNow
  }
  Isilkul: weatherByPoint(request: {lat: 54.9096002, lon: 71.2816284}) {
    ...WeatherNow
  }
  Kalachinsk: weatherByPoint(request: {lat: 55.0598155, lon: 74.5653644}) {
    ...WeatherNow
  }
  Nazyvaevsk: weatherByPoint(request: {lat: 55.5689323, lon: 71.3503426}) {
    ...WeatherNow
  }
  Omsk: weatherByPoint(request: {lat: 54.9848566, lon: 73.3674517}) {
    ...WeatherNow
  }
  Tara: weatherByPoint(request: {lat: 56.9160511, lon: 74.3649194}) {
    ...WeatherNow
  }
  Tyukalinsk: weatherByPoint(request: {lat: 55.8703415, lon: 72.1954747}) {
    ...WeatherNow
  }
  Abdulino: weatherByPoint(request: {lat: 53.6778906, lon: 53.6472483}) {
    ...WeatherNow
  }
  Buguruslan: weatherByPoint(request: {lat: 53.6523728, lon: 52.4326853}) {
    ...WeatherNow
  }
  Buzuluk: weatherByPoint(request: {lat: 52.7881277, lon: 52.2624877}) {
    ...WeatherNow
  }
  Gay: weatherByPoint(request: {lat: 51.4649189, lon: 58.4436875}) {
    ...WeatherNow
  }
  Kuvandyk: weatherByPoint(request: {lat: 51.4783857, lon: 57.3612636}) {
    ...WeatherNow
  }
  Mednogorsk: weatherByPoint(request: {lat: 51.4037617, lon: 57.583163}) {
    ...WeatherNow
  }
  Novotroitsk: weatherByPoint(request: {lat: 51.1964202, lon: 58.3018192}) {
    ...WeatherNow
  }
  Orenburg: weatherByPoint(request: {lat: 51.7875092, lon: 55.1018828}) {
    ...WeatherNow
  }
  Orsk: weatherByPoint(request: {lat: 51.2294282, lon: 58.4752777}) {
    ...WeatherNow
  }
  SolIletsk: weatherByPoint(request: {lat: 51.1633736, lon: 54.9896726}) {
    ...WeatherNow
  }
  Sorochinsk: weatherByPoint(request: {lat: 52.426685, lon: 53.1542745}) {
    ...WeatherNow
  }
  Yasnyy: weatherByPoint(request: {lat: 51.036838, lon: 59.874344}) {
    ...WeatherNow
  }
  Bolhov: weatherByPoint(request: {lat: 53.4438496, lon: 36.0076833}) {
    ...WeatherNow
  }
  Dmitrovsk: weatherByPoint(request: {lat: 52.5054851, lon: 35.1415009}) {
    ...WeatherNow
  }
  Livny: weatherByPoint(request: {lat: 52.4284558, lon: 37.6039506}) {
    ...WeatherNow
  }
  Maloarhangelsk: weatherByPoint(request: {lat: 52.4002192, lon: 36.5038579}) {
    ...WeatherNow
  }
  Mtsensk: weatherByPoint(request: {lat: 53.2788438, lon: 36.5749105}) {
    ...WeatherNow
  }
  Novosil: weatherByPoint(request: {lat: 52.97454, lon: 37.0437146}) {
    ...WeatherNow
  }
  Oryol: weatherByPoint(request: {lat: 52.9671298, lon: 36.0696427}) {
    ...WeatherNow
  }
  Belinskiy: weatherByPoint(request: {lat: 52.9640996, lon: 43.4183212}) {
    ...WeatherNow
  }
  Gorodische: weatherByPoint(request: {lat: 53.2726916, lon: 45.7026142}) {
    ...WeatherNow
  }
  Zarechnyy: weatherByPoint(request: {lat: 53.1960836, lon: 45.1689907}) {
    ...WeatherNow
  }
  Kamenka: weatherByPoint(request: {lat: 53.1855463, lon: 44.0469717}) {
    ...WeatherNow
  }
  Kuznetsk: weatherByPoint(request: {lat: 53.1130888, lon: 46.605092}) {
    ...WeatherNow
  }
  NizhniyLomov: weatherByPoint(request: {lat: 53.5300905, lon: 43.6730217}) {
    ...WeatherNow
  }
  Nikolsk_2: weatherByPoint(request: {lat: 53.7137496, lon: 46.0799857}) {
    ...WeatherNow
  }
  Penza: weatherByPoint(request: {lat: 53.1753314, lon: 45.0348625}) {
    ...WeatherNow
  }
  Serdobsk: weatherByPoint(request: {lat: 52.4697595, lon: 44.2122414}) {
    ...WeatherNow
  }
  Spassk: weatherByPoint(request: {lat: 53.9271974, lon: 43.1859073}) {
    ...WeatherNow
  }
  Sursk: weatherByPoint(request: {lat: 53.0761357, lon: 45.6910796}) {
    ...WeatherNow
  }
  Aleksandrovsk: weatherByPoint(request: {lat: 59.1613221, lon: 57.5763459}) {
    ...WeatherNow
  }
  Berezniki: weatherByPoint(request: {lat: 59.4079923, lon: 56.8039427}) {
    ...WeatherNow
  }
  Vereschagino: weatherByPoint(request: {lat: 58.0797571, lon: 54.6581309}) {
    ...WeatherNow
  }
  Gornozavodsk: weatherByPoint(request: {lat: 58.3742532, lon: 58.3231716}) {
    ...WeatherNow
  }
  Gremyachinsk: weatherByPoint(request: {lat: 58.5626082, lon: 57.8520572}) {
    ...WeatherNow
  }
  Gubaha: weatherByPoint(request: {lat: 58.8371721, lon: 57.554533}) {
    ...WeatherNow
  }
  Dobryanka: weatherByPoint(request: {lat: 58.469685, lon: 56.4130737}) {
    ...WeatherNow
  }
  Kizel: weatherByPoint(request: {lat: 59.0512783, lon: 57.6471028}) {
    ...WeatherNow
  }
  Krasnovishersk: weatherByPoint(request: {lat: 60.3901321, lon: 57.0535682}) {
    ...WeatherNow
  }
  Krasnokamsk: weatherByPoint(request: {lat: 58.0822065, lon: 55.7479936}) {
    ...WeatherNow
  }
  Kudymkar: weatherByPoint(request: {lat: 59.0167925, lon: 54.6572508}) {
    ...WeatherNow
  }
  Kungur: weatherByPoint(request: {lat: 57.4283296, lon: 56.9438656}) {
    ...WeatherNow
  }
  Lysva: weatherByPoint(request: {lat: 58.0995875, lon: 57.8086825}) {
    ...WeatherNow
  }
  Nytva: weatherByPoint(request: {lat: 57.9336725, lon: 55.3356084}) {
    ...WeatherNow
  }
  Osa: weatherByPoint(request: {lat: 57.2889515, lon: 55.4688668}) {
    ...WeatherNow
  }
  Ohansk: weatherByPoint(request: {lat: 57.7180034, lon: 55.3872469}) {
    ...WeatherNow
  }
  Ocher: weatherByPoint(request: {lat: 57.8852686, lon: 54.7161091}) {
    ...WeatherNow
  }
  Perm: weatherByPoint(request: {lat: 58.0102583, lon: 56.2342034}) {
    ...WeatherNow
  }
  Solikamsk: weatherByPoint(request: {lat: 59.6482998, lon: 56.771009}) {
    ...WeatherNow
  }
  Usole: weatherByPoint(request: {lat: 59.4277573, lon: 56.6837872}) {
    ...WeatherNow
  }
  Chaykovskiy: weatherByPoint(request: {lat: 56.7781501, lon: 54.1477965}) {
    ...WeatherNow
  }
  Cherdyn: weatherByPoint(request: {lat: 60.4011933, lon: 56.4799933}) {
    ...WeatherNow
  }
  Chermoz: weatherByPoint(request: {lat: 58.7842834, lon: 56.1507138}) {
    ...WeatherNow
  }
  Chernushka: weatherByPoint(request: {lat: 56.5160768, lon: 56.0763049}) {
    ...WeatherNow
  }
  Chusovoy: weatherByPoint(request: {lat: 58.2974596, lon: 57.8193615}) {
    ...WeatherNow
  }
  Arsenev: weatherByPoint(request: {lat: 44.1622031, lon: 133.2696209}) {
    ...WeatherNow
  }
  Artem: weatherByPoint(request: {lat: 43.3501675, lon: 132.1596175}) {
    ...WeatherNow
  }
  BolshoyKamen: weatherByPoint(request: {lat: 43.1111742, lon: 132.3480082}) {
    ...WeatherNow
  }
  Vladivostok: weatherByPoint(request: {lat: 43.1164904, lon: 131.8823937}) {
    ...WeatherNow
  }
  Dalnegorsk: weatherByPoint(request: {lat: 44.5539457, lon: 135.5662716}) {
    ...WeatherNow
  }
  Dalnerechensk: weatherByPoint(request: {lat: 45.9308483, lon: 133.7316907}) {
    ...WeatherNow
  }
  Lesozavodsk: weatherByPoint(request: {lat: 45.4780092, lon: 133.4186199}) {
    ...WeatherNow
  }
  Nahodka: weatherByPoint(request: {lat: 42.8239372, lon: 132.8927361}) {
    ...WeatherNow
  }
  Partizansk: weatherByPoint(request: {lat: 43.1280578, lon: 133.1264567}) {
    ...WeatherNow
  }
  SpasskDalniy: weatherByPoint(request: {lat: 44.5901175, lon: 132.8157288}) {
    ...WeatherNow
  }
  Ussuriysk: weatherByPoint(request: {lat: 43.7971818, lon: 131.9518229}) {
    ...WeatherNow
  }
  Fokino_2: weatherByPoint(request: {lat: 42.9706317, lon: 132.4110196}) {
    ...WeatherNow
  }
  VelikieLuki: weatherByPoint(request: {lat: 56.332208, lon: 30.5508641}) {
    ...WeatherNow
  }
  Gdov: weatherByPoint(request: {lat: 58.7432429, lon: 27.8264809}) {
    ...WeatherNow
  }
  Dno: weatherByPoint(request: {lat: 57.826974, lon: 29.9629389}) {
    ...WeatherNow
  }
  Nevel: weatherByPoint(request: {lat: 56.0201973, lon: 29.9239983}) {
    ...WeatherNow
  }
  Novorzhev: weatherByPoint(request: {lat: 57.029807, lon: 29.3433083}) {
    ...WeatherNow
  }
  Novosokolniki: weatherByPoint(request: {lat: 56.3408431, lon: 30.1527573}) {
    ...WeatherNow
  }
  Opochka: weatherByPoint(request: {lat: 56.710725, lon: 28.6717519}) {
    ...WeatherNow
  }
  Ostrov: weatherByPoint(request: {lat: 57.3451528, lon: 28.3437593}) {
    ...WeatherNow
  }
  Pechory: weatherByPoint(request: {lat: 57.8145817, lon: 27.622259}) {
    ...WeatherNow
  }
  Porhov: weatherByPoint(request: {lat: 57.7765219, lon: 29.5436626}) {
    ...WeatherNow
  }
  Pskov: weatherByPoint(request: {lat: 57.8194415, lon: 28.3317198}) {
    ...WeatherNow
  }
  Pustoshka: weatherByPoint(request: {lat: 56.3374813, lon: 29.3668055}) {
    ...WeatherNow
  }
  Pytalovo: weatherByPoint(request: {lat: 57.0637952, lon: 27.9236214}) {
    ...WeatherNow
  }
  Sebezh: weatherByPoint(request: {lat: 56.2908554, lon: 28.4724326}) {
    ...WeatherNow
  }
  Azov: weatherByPoint(request: {lat: 47.1121589, lon: 39.4232555}) {
    ...WeatherNow
  }
  Aksay: weatherByPoint(request: {lat: 47.2676314, lon: 39.8756872}) {
    ...WeatherNow
  }
  Bataysk: weatherByPoint(request: {lat: 47.1383299, lon: 39.7507179}) {
    ...WeatherNow
  }
  BelayaKalitva: weatherByPoint(request: {lat: 48.1769737, lon: 40.8033529}) {
    ...WeatherNow
  }
  Volgodonsk: weatherByPoint(request: {lat: 47.5165338, lon: 42.1984951}) {
    ...WeatherNow
  }
  Gukovo: weatherByPoint(request: {lat: 48.0448904, lon: 39.9484672}) {
    ...WeatherNow
  }
  Donetsk: weatherByPoint(request: {lat: 48.3350706, lon: 39.945891}) {
    ...WeatherNow
  }
  Zverevo: weatherByPoint(request: {lat: 48.0435487, lon: 40.1265822}) {
    ...WeatherNow
  }
  Zernograd: weatherByPoint(request: {lat: 46.8495958, lon: 40.312837}) {
    ...WeatherNow
  }
  KamenskShahtinskiy: weatherByPoint(request: {lat: 48.3205326, lon: 40.2689583}) {
    ...WeatherNow
  }
  Konstantinovsk: weatherByPoint(request: {lat: 47.5773717, lon: 41.0967445}) {
    ...WeatherNow
  }
  KrasnyySulin: weatherByPoint(request: {lat: 47.8831311, lon: 40.0781298}) {
    ...WeatherNow
  }
  Millerovo: weatherByPoint(request: {lat: 48.9260077, lon: 40.3984087}) {
    ...WeatherNow
  }
  Morozovsk: weatherByPoint(request: {lat: 48.3511807, lon: 41.8309225}) {
    ...WeatherNow
  }
  Novocherkassk: weatherByPoint(request: {lat: 47.411919, lon: 40.1042098}) {
    ...WeatherNow
  }
  Novoshahtinsk: weatherByPoint(request: {lat: 47.757773, lon: 39.9363697}) {
    ...WeatherNow
  }
  Proletarsk: weatherByPoint(request: {lat: 46.7038963, lon: 41.727594}) {
    ...WeatherNow
  }
  RostovNaDonu: weatherByPoint(request: {lat: 47.2224566, lon: 39.718803}) {
    ...WeatherNow
  }
  Salsk: weatherByPoint(request: {lat: 46.4752095, lon: 41.5410415}) {
    ...WeatherNow
  }
  Semikarakorsk: weatherByPoint(request: {lat: 47.5177337, lon: 40.8114167}) {
    ...WeatherNow
  }
  Taganrog: weatherByPoint(request: {lat: 47.2094917, lon: 38.9350989}) {
    ...WeatherNow
  }
  Tsimlyansk: weatherByPoint(request: {lat: 47.6477448, lon: 42.0931505}) {
    ...WeatherNow
  }
  Shahty: weatherByPoint(request: {lat: 47.7085287, lon: 40.2159846}) {
    ...WeatherNow
  }
  Kasimov: weatherByPoint(request: {lat: 54.9373475, lon: 41.3913211}) {
    ...WeatherNow
  }
  Korablino: weatherByPoint(request: {lat: 53.9246659, lon: 40.0227745}) {
    ...WeatherNow
  }
  Mihaylov: weatherByPoint(request: {lat: 54.2297402, lon: 39.0091481}) {
    ...WeatherNow
  }
  Novomichurinsk: weatherByPoint(request: {lat: 54.0376572, lon: 39.74654}) {
    ...WeatherNow
  }
  Rybnoe: weatherByPoint(request: {lat: 54.7256164, lon: 39.5134398}) {
    ...WeatherNow
  }
  Ryazhsk: weatherByPoint(request: {lat: 53.7067584, lon: 40.0522274}) {
    ...WeatherNow
  }
  Ryazan: weatherByPoint(request: {lat: 54.6254445, lon: 39.7358609}) {
    ...WeatherNow
  }
  Sasovo: weatherByPoint(request: {lat: 54.3508885, lon: 41.9117422}) {
    ...WeatherNow
  }
  Skopin: weatherByPoint(request: {lat: 53.823543, lon: 39.5492421}) {
    ...WeatherNow
  }
  SpasKlepiki: weatherByPoint(request: {lat: 55.1291721, lon: 40.1745338}) {
    ...WeatherNow
  }
  SpasskRyazanskiy: weatherByPoint(request: {lat: 54.4070719, lon: 40.3763426}) {
    ...WeatherNow
  }
  Shatsk: weatherByPoint(request: {lat: 54.0287312, lon: 41.7181803}) {
    ...WeatherNow
  }
  Zhigulevsk: weatherByPoint(request: {lat: 53.4011981, lon: 49.4945176}) {
    ...WeatherNow
  }
  Kinel: weatherByPoint(request: {lat: 53.2210298, lon: 50.6343776}) {
    ...WeatherNow
  }
  Neftegorsk: weatherByPoint(request: {lat: 52.7972914, lon: 51.1637392}) {
    ...WeatherNow
  }
  Novokuybyshevsk: weatherByPoint(request: {lat: 53.0994565, lon: 49.9477382}) {
    ...WeatherNow
  }
  Oktyabrsk: weatherByPoint(request: {lat: 53.1640488, lon: 48.670762}) {
    ...WeatherNow
  }
  Otradnyy: weatherByPoint(request: {lat: 53.3800848, lon: 51.3438605}) {
    ...WeatherNow
  }
  Pohvistnevo: weatherByPoint(request: {lat: 53.6498299, lon: 52.1235156}) {
    ...WeatherNow
  }
  Samara: weatherByPoint(request: {lat: 53.1950306, lon: 50.1069518}) {
    ...WeatherNow
  }
  Syzran: weatherByPoint(request: {lat: 53.1558674, lon: 48.4744629}) {
    ...WeatherNow
  }
  Tolyatti: weatherByPoint(request: {lat: 53.5205348, lon: 49.3894028}) {
    ...WeatherNow
  }
  Chapaevsk: weatherByPoint(request: {lat: 52.928961, lon: 49.8673269}) {
    ...WeatherNow
  }
  SanktPeterburg: weatherByPoint(request: {lat: 59.9391313, lon: 30.3159004}) {
    ...WeatherNow
  }
  Arkadak: weatherByPoint(request: {lat: 51.938831, lon: 43.4999221}) {
    ...WeatherNow
  }
  Atkarsk: weatherByPoint(request: {lat: 51.8736062, lon: 45.0003247}) {
    ...WeatherNow
  }
  Balakovo: weatherByPoint(request: {lat: 52.0224231, lon: 47.7827765}) {
    ...WeatherNow
  }
  Balashov: weatherByPoint(request: {lat: 51.5388697, lon: 43.1839757}) {
    ...WeatherNow
  }
  Volsk: weatherByPoint(request: {lat: 52.0459865, lon: 47.3873595}) {
    ...WeatherNow
  }
  Ershov: weatherByPoint(request: {lat: 51.3508505, lon: 48.2762226}) {
    ...WeatherNow
  }
  Kalininsk: weatherByPoint(request: {lat: 51.4993591, lon: 44.4710435}) {
    ...WeatherNow
  }
  Krasnoarmeysk_2: weatherByPoint(request: {lat: 51.023541, lon: 45.695044}) {
    ...WeatherNow
  }
  KrasnyyKut: weatherByPoint(request: {lat: 50.9598317, lon: 46.9712016}) {
    ...WeatherNow
  }
  Marks: weatherByPoint(request: {lat: 51.7133337, lon: 46.7400339}) {
    ...WeatherNow
  }
  Novouzensk: weatherByPoint(request: {lat: 50.455199, lon: 48.1413153}) {
    ...WeatherNow
  }
  Petrovsk: weatherByPoint(request: {lat: 52.3094237, lon: 45.3851877}) {
    ...WeatherNow
  }
  Pugachev: weatherByPoint(request: {lat: 52.0159921, lon: 48.7972223}) {
    ...WeatherNow
  }
  Rtischevo: weatherByPoint(request: {lat: 52.2616271, lon: 43.7842248}) {
    ...WeatherNow
  }
  Saratov: weatherByPoint(request: {lat: 51.533557, lon: 46.034257}) {
    ...WeatherNow
  }
  Hvalynsk: weatherByPoint(request: {lat: 52.4951572, lon: 48.1045771}) {
    ...WeatherNow
  }
  Shihany: weatherByPoint(request: {lat: 52.1147391, lon: 47.2023118}) {
    ...WeatherNow
  }
  Engels: weatherByPoint(request: {lat: 51.4854003, lon: 46.126722}) {
    ...WeatherNow
  }
  AleksandrovskSahalinskiy: weatherByPoint(request: {lat: 50.8974378, lon: 142.1578559}) {
    ...WeatherNow
  }
  Aniva: weatherByPoint(request: {lat: 46.713152, lon: 142.5265804}) {
    ...WeatherNow
  }
  Dolinsk: weatherByPoint(request: {lat: 47.3255783, lon: 142.7945071}) {
    ...WeatherNow
  }
  Korsakov: weatherByPoint(request: {lat: 46.6324545, lon: 142.799445}) {
    ...WeatherNow
  }
  Kurilsk: weatherByPoint(request: {lat: 45.2270954, lon: 147.8796323}) {
    ...WeatherNow
  }
  Makarov: weatherByPoint(request: {lat: 48.6236334, lon: 142.7803205}) {
    ...WeatherNow
  }
  Nevelsk: weatherByPoint(request: {lat: 46.6526899, lon: 141.8630725}) {
    ...WeatherNow
  }
  Oha: weatherByPoint(request: {lat: 53.5867839, lon: 142.9412411}) {
    ...WeatherNow
  }
  Poronaysk: weatherByPoint(request: {lat: 49.238866, lon: 143.1008333}) {
    ...WeatherNow
  }
  SeveroKurilsk: weatherByPoint(request: {lat: 50.6730577, lon: 156.1282211}) {
    ...WeatherNow
  }
  Tomari: weatherByPoint(request: {lat: 47.7620108, lon: 142.0615837}) {
    ...WeatherNow
  }
  Uglegorsk: weatherByPoint(request: {lat: 49.0815774, lon: 142.0692639}) {
    ...WeatherNow
  }
  Holmsk: weatherByPoint(request: {lat: 47.0408423, lon: 142.041688}) {
    ...WeatherNow
  }
  YuzhnoSahalinsk: weatherByPoint(request: {lat: 46.9591631, lon: 142.737976}) {
    ...WeatherNow
  }
  Alapaevsk: weatherByPoint(request: {lat: 57.8475571, lon: 61.6693817}) {
    ...WeatherNow
  }
  Aramil: weatherByPoint(request: {lat: 56.694632, lon: 60.8343125}) {
    ...WeatherNow
  }
  Artemovskiy: weatherByPoint(request: {lat: 57.3384177, lon: 61.8947443}) {
    ...WeatherNow
  }
  Asbest: weatherByPoint(request: {lat: 57.0052277, lon: 61.4581156}) {
    ...WeatherNow
  }
  Berezovskiy_2: weatherByPoint(request: {lat: 56.9095924, lon: 60.8180907}) {
    ...WeatherNow
  }
  Bogdanovich: weatherByPoint(request: {lat: 56.7764795, lon: 62.0463679}) {
    ...WeatherNow
  }
  VerhniyTagil: weatherByPoint(request: {lat: 57.3763758, lon: 59.9517653}) {
    ...WeatherNow
  }
  VerhnyayaPyshma: weatherByPoint(request: {lat: 56.9758903, lon: 60.5650383}) {
    ...WeatherNow
  }
  VerhnyayaSalda: weatherByPoint(request: {lat: 58.0465803, lon: 60.5560164}) {
    ...WeatherNow
  }
  VerhnyayaTura: weatherByPoint(request: {lat: 58.3643685, lon: 59.8265235}) {
    ...WeatherNow
  }
  Verhoture: weatherByPoint(request: {lat: 58.8622073, lon: 60.8103945}) {
    ...WeatherNow
  }
  Volchansk: weatherByPoint(request: {lat: 59.9351707, lon: 60.0798618}) {
    ...WeatherNow
  }
  Degtyarsk: weatherByPoint(request: {lat: 56.7048206, lon: 60.079138}) {
    ...WeatherNow
  }
  Ekaterinburg: weatherByPoint(request: {lat: 56.8385216, lon: 60.6054911}) {
    ...WeatherNow
  }
  Zarechnyy_2: weatherByPoint(request: {lat: 56.8102931, lon: 61.3380029}) {
    ...WeatherNow
  }
  Ivdel: weatherByPoint(request: {lat: 60.6944496, lon: 60.4245069}) {
    ...WeatherNow
  }
  Irbit: weatherByPoint(request: {lat: 57.6838362, lon: 63.057675}) {
    ...WeatherNow
  }
  KamenskUralskiy: weatherByPoint(request: {lat: 56.414962, lon: 61.9188674}) {
    ...WeatherNow
  }
  Kamyshlov: weatherByPoint(request: {lat: 56.8465034, lon: 62.7119766}) {
    ...WeatherNow
  }
  Karpinsk: weatherByPoint(request: {lat: 59.7665925, lon: 60.0011703}) {
    ...WeatherNow
  }
  Kachkanar: weatherByPoint(request: {lat: 58.7051762, lon: 59.4839155}) {
    ...WeatherNow
  }
  Kirovgrad: weatherByPoint(request: {lat: 57.4299433, lon: 60.0624051}) {
    ...WeatherNow
  }
  Krasnoturinsk: weatherByPoint(request: {lat: 59.7636635, lon: 60.1934525}) {
    ...WeatherNow
  }
  Krasnouralsk: weatherByPoint(request: {lat: 58.348651, lon: 60.0408764}) {
    ...WeatherNow
  }
  Krasnoufimsk: weatherByPoint(request: {lat: 56.612387, lon: 57.7636637}) {
    ...WeatherNow
  }
  Kushva: weatherByPoint(request: {lat: 58.2826013, lon: 59.7645766}) {
    ...WeatherNow
  }
  Lesnoy: weatherByPoint(request: {lat: 58.6348516, lon: 59.7981565}) {
    ...WeatherNow
  }
  Mihaylovsk: weatherByPoint(request: {lat: 56.4370039, lon: 59.1137316}) {
    ...WeatherNow
  }
  Nevyansk: weatherByPoint(request: {lat: 57.49131, lon: 60.2183429}) {
    ...WeatherNow
  }
  NizhnieSergi: weatherByPoint(request: {lat: 56.6544959, lon: 59.2953035}) {
    ...WeatherNow
  }
  NizhniyTagil: weatherByPoint(request: {lat: 57.910126, lon: 59.9812853}) {
    ...WeatherNow
  }
  NizhnyayaSalda: weatherByPoint(request: {lat: 58.0748272, lon: 60.7025418}) {
    ...WeatherNow
  }
  NizhnyayaTura: weatherByPoint(request: {lat: 58.6309267, lon: 59.8520344}) {
    ...WeatherNow
  }
  NovayaLyalya: weatherByPoint(request: {lat: 59.0538977, lon: 60.5944825}) {
    ...WeatherNow
  }
  Novouralsk: weatherByPoint(request: {lat: 57.2472567, lon: 60.0956714}) {
    ...WeatherNow
  }
  Pervouralsk: weatherByPoint(request: {lat: 56.9080085, lon: 59.942926}) {
    ...WeatherNow
  }
  Polevskoy: weatherByPoint(request: {lat: 56.4956952, lon: 60.2365298}) {
    ...WeatherNow
  }
  Revda: weatherByPoint(request: {lat: 56.7986319, lon: 59.9071591}) {
    ...WeatherNow
  }
  Rezh: weatherByPoint(request: {lat: 57.3717477, lon: 61.3833842}) {
    ...WeatherNow
  }
  Severouralsk: weatherByPoint(request: {lat: 60.1533109, lon: 59.9525245}) {
    ...WeatherNow
  }
  Serov: weatherByPoint(request: {lat: 59.6047724, lon: 60.5753882}) {
    ...WeatherNow
  }
  Sredneuralsk: weatherByPoint(request: {lat: 56.9918901, lon: 60.4771018}) {
    ...WeatherNow
  }
  SuhoyLog: weatherByPoint(request: {lat: 56.9076193, lon: 62.0358093}) {
    ...WeatherNow
  }
  Sysert: weatherByPoint(request: {lat: 56.5005715, lon: 60.8190003}) {
    ...WeatherNow
  }
  Tavda: weatherByPoint(request: {lat: 58.0434672, lon: 65.274217}) {
    ...WeatherNow
  }
  Talitsa: weatherByPoint(request: {lat: 57.0122687, lon: 63.7320757}) {
    ...WeatherNow
  }
  Turinsk: weatherByPoint(request: {lat: 58.0393524, lon: 63.6981973}) {
    ...WeatherNow
  }
  Sevastopol: weatherByPoint(request: {lat: 44.6167013, lon: 33.525355}) {
    ...WeatherNow
  }
  Alagir: weatherByPoint(request: {lat: 43.0417684, lon: 44.2199715}) {
    ...WeatherNow
  }
  Ardon: weatherByPoint(request: {lat: 43.1755152, lon: 44.2955775}) {
    ...WeatherNow
  }
  Beslan: weatherByPoint(request: {lat: 43.1937529, lon: 44.5338707}) {
    ...WeatherNow
  }
  Vladikavkaz: weatherByPoint(request: {lat: 43.020588, lon: 44.6819182}) {
    ...WeatherNow
  }
  Digora: weatherByPoint(request: {lat: 43.1567628, lon: 44.1549483}) {
    ...WeatherNow
  }
  Mozdok: weatherByPoint(request: {lat: 43.7471342, lon: 44.6569607}) {
    ...WeatherNow
  }
  Velizh: weatherByPoint(request: {lat: 55.6057916, lon: 31.1856206}) {
    ...WeatherNow
  }
  Vyazma: weatherByPoint(request: {lat: 55.2116983, lon: 34.2951663}) {
    ...WeatherNow
  }
  Gagarin: weatherByPoint(request: {lat: 55.5525228, lon: 34.9950502}) {
    ...WeatherNow
  }
  Demidov: weatherByPoint(request: {lat: 55.2682105, lon: 31.5062809}) {
    ...WeatherNow
  }
  Desnogorsk: weatherByPoint(request: {lat: 54.146457, lon: 33.2833222}) {
    ...WeatherNow
  }
  Dorogobuzh: weatherByPoint(request: {lat: 54.9136959, lon: 33.3023162}) {
    ...WeatherNow
  }
  Duhovschina: weatherByPoint(request: {lat: 55.1950257, lon: 32.401252}) {
    ...WeatherNow
  }
  Elnya: weatherByPoint(request: {lat: 54.5837795, lon: 33.1749867}) {
    ...WeatherNow
  }
  Pochinok: weatherByPoint(request: {lat: 54.406244, lon: 32.4398039}) {
    ...WeatherNow
  }
  Roslavl: weatherByPoint(request: {lat: 53.9449558, lon: 32.8480258}) {
    ...WeatherNow
  }
  Rudnya: weatherByPoint(request: {lat: 54.9441093, lon: 31.0794806}) {
    ...WeatherNow
  }
  Safonovo: weatherByPoint(request: {lat: 55.1199661, lon: 33.2336988}) {
    ...WeatherNow
  }
  Smolensk: weatherByPoint(request: {lat: 54.782635, lon: 32.045251}) {
    ...WeatherNow
  }
  Sychevka: weatherByPoint(request: {lat: 55.8308821, lon: 34.2778793}) {
    ...WeatherNow
  }
  Yartsevo: weatherByPoint(request: {lat: 55.0564732, lon: 32.6902302}) {
    ...WeatherNow
  }
  Blagodarnyy: weatherByPoint(request: {lat: 45.0989782, lon: 43.4306455}) {
    ...WeatherNow
  }
  Budennovsk: weatherByPoint(request: {lat: 44.7816067, lon: 44.1650339}) {
    ...WeatherNow
  }
  Georgievsk: weatherByPoint(request: {lat: 44.1485694, lon: 43.4739851}) {
    ...WeatherNow
  }
  Essentuki: weatherByPoint(request: {lat: 44.0446186, lon: 42.8588653}) {
    ...WeatherNow
  }
  Zheleznovodsk: weatherByPoint(request: {lat: 44.1320568, lon: 43.0306461}) {
    ...WeatherNow
  }
  Zelenokumsk: weatherByPoint(request: {lat: 44.4032668, lon: 43.8841877}) {
    ...WeatherNow
  }
  Izobilnyy: weatherByPoint(request: {lat: 45.3684296, lon: 41.708702}) {
    ...WeatherNow
  }
  Ipatovo: weatherByPoint(request: {lat: 45.7181751, lon: 42.8970206}) {
    ...WeatherNow
  }
  Kislovodsk: weatherByPoint(request: {lat: 43.9052044, lon: 42.7168721}) {
    ...WeatherNow
  }
  Lermontov: weatherByPoint(request: {lat: 44.1054107, lon: 42.973135}) {
    ...WeatherNow
  }
  MineralnyeVody: weatherByPoint(request: {lat: 44.2087273, lon: 43.138408}) {
    ...WeatherNow
  }
  Mihaylovsk_2: weatherByPoint(request: {lat: 45.1297323, lon: 42.0288443}) {
    ...WeatherNow
  }
  Nevinnomyssk: weatherByPoint(request: {lat: 44.6226031, lon: 41.9476723}) {
    ...WeatherNow
  }
  Neftekumsk: weatherByPoint(request: {lat: 44.7544552, lon: 44.9865347}) {
    ...WeatherNow
  }
  Novoaleksandrovsk: weatherByPoint(request: {lat: 45.4932733, lon: 41.2153996}) {
    ...WeatherNow
  }
  Novopavlovsk: weatherByPoint(request: {lat: 43.9617097, lon: 43.6342865}) {
    ...WeatherNow
  }
  Pyatigorsk: weatherByPoint(request: {lat: 44.041091, lon: 43.0661553}) {
    ...WeatherNow
  }
  Svetlograd: weatherByPoint(request: {lat: 45.328659, lon: 42.8565714}) {
    ...WeatherNow
  }
  Stavropol: weatherByPoint(request: {lat: 45.044516, lon: 41.9689655}) {
    ...WeatherNow
  }
  Zherdevka: weatherByPoint(request: {lat: 51.8422192, lon: 41.4617687}) {
    ...WeatherNow
  }
  Kirsanov: weatherByPoint(request: {lat: 52.6506335, lon: 42.7286445}) {
    ...WeatherNow
  }
  Kotovsk: weatherByPoint(request: {lat: 52.5924489, lon: 41.5101237}) {
    ...WeatherNow
  }
  Michurinsk: weatherByPoint(request: {lat: 52.8912389, lon: 40.5104443}) {
    ...WeatherNow
  }
  Morshansk: weatherByPoint(request: {lat: 53.4436216, lon: 41.8115478}) {
    ...WeatherNow
  }
  Rasskazovo: weatherByPoint(request: {lat: 52.6538833, lon: 41.874285}) {
    ...WeatherNow
  }
  Tambov: weatherByPoint(request: {lat: 52.7213154, lon: 41.452264}) {
    ...WeatherNow
  }
  Uvarovo: weatherByPoint(request: {lat: 51.9767841, lon: 42.2529799}) {
    ...WeatherNow
  }
  Agryz: weatherByPoint(request: {lat: 56.5232864, lon: 52.9943775}) {
    ...WeatherNow
  }
  Aznakaevo: weatherByPoint(request: {lat: 54.8598642, lon: 53.0745527}) {
    ...WeatherNow
  }
  Almetevsk: weatherByPoint(request: {lat: 54.9014619, lon: 52.2970467}) {
    ...WeatherNow
  }
  Arsk: weatherByPoint(request: {lat: 56.0912567, lon: 49.877067}) {
    ...WeatherNow
  }
  Bavly: weatherByPoint(request: {lat: 54.4062891, lon: 53.2458065}) {
    ...WeatherNow
  }
  Bolgar: weatherByPoint(request: {lat: 54.974891, lon: 49.0303882}) {
    ...WeatherNow
  }
  Bugulma: weatherByPoint(request: {lat: 54.5363495, lon: 52.7895849}) {
    ...WeatherNow
  }
  Buinsk: weatherByPoint(request: {lat: 54.9641538, lon: 48.2901209}) {
    ...WeatherNow
  }
  Elabuga: weatherByPoint(request: {lat: 55.7567107, lon: 52.0543794}) {
    ...WeatherNow
  }
  Zainsk: weatherByPoint(request: {lat: 55.299053, lon: 52.0062972}) {
    ...WeatherNow
  }
  Zelenodolsk: weatherByPoint(request: {lat: 55.8466651, lon: 48.5010954}) {
    ...WeatherNow
  }
  Innopolis: weatherByPoint(request: {lat: 55.7521699, lon: 48.7446846}) {
    ...WeatherNow
  }
  Kazan: weatherByPoint(request: {lat: 55.7943584, lon: 49.1114975}) {
    ...WeatherNow
  }
  Kukmor: weatherByPoint(request: {lat: 56.1861392, lon: 50.8970238}) {
    ...WeatherNow
  }
  Laishevo: weatherByPoint(request: {lat: 55.4042867, lon: 49.5499838}) {
    ...WeatherNow
  }
  Leninogorsk: weatherByPoint(request: {lat: 54.5967034, lon: 52.4431906}) {
    ...WeatherNow
  }
  Mamadysh: weatherByPoint(request: {lat: 55.7150413, lon: 51.4129016}) {
    ...WeatherNow
  }
  Mendeleevsk: weatherByPoint(request: {lat: 55.895169, lon: 52.3143347}) {
    ...WeatherNow
  }
  Menzelinsk: weatherByPoint(request: {lat: 55.7270698, lon: 53.1003968}) {
    ...WeatherNow
  }
  NaberezhnyeChelny: weatherByPoint(request: {lat: 55.7434619, lon: 52.3959165}) {
    ...WeatherNow
  }
  Nizhnekamsk: weatherByPoint(request: {lat: 55.6313609, lon: 51.8144669}) {
    ...WeatherNow
  }
  Nurlat: weatherByPoint(request: {lat: 54.4281461, lon: 50.8049337}) {
    ...WeatherNow
  }
  Tetyushi: weatherByPoint(request: {lat: 54.936516, lon: 48.8314533}) {
    ...WeatherNow
  }
  Chistopol: weatherByPoint(request: {lat: 55.3699139, lon: 50.6285784}) {
    ...WeatherNow
  }
  Andreapol: weatherByPoint(request: {lat: 56.6506724, lon: 32.2620163}) {
    ...WeatherNow
  }
  Bezhetsk: weatherByPoint(request: {lat: 57.7860089, lon: 36.6904983}) {
    ...WeatherNow
  }
  Belyy: weatherByPoint(request: {lat: 55.8339056, lon: 32.9389741}) {
    ...WeatherNow
  }
  Bologoe: weatherByPoint(request: {lat: 57.8855767, lon: 34.0537771}) {
    ...WeatherNow
  }
  Vesegonsk: weatherByPoint(request: {lat: 58.6582598, lon: 37.2567558}) {
    ...WeatherNow
  }
  VyshniyVolochek: weatherByPoint(request: {lat: 57.568302, lon: 34.5404016}) {
    ...WeatherNow
  }
  ZapadnayaDvina: weatherByPoint(request: {lat: 56.2566492, lon: 32.0805315}) {
    ...WeatherNow
  }
  Zubtsov: weatherByPoint(request: {lat: 56.1760868, lon: 34.5825515}) {
    ...WeatherNow
  }
  Kalyazin: weatherByPoint(request: {lat: 57.2579478, lon: 37.7819693}) {
    ...WeatherNow
  }
  Kashin: weatherByPoint(request: {lat: 57.360194, lon: 37.6119436}) {
    ...WeatherNow
  }
  Kimry: weatherByPoint(request: {lat: 56.8733213, lon: 37.3556605}) {
    ...WeatherNow
  }
  Konakovo: weatherByPoint(request: {lat: 56.7275204, lon: 36.8012716}) {
    ...WeatherNow
  }
  KrasnyyHolm: weatherByPoint(request: {lat: 58.0571446, lon: 37.1126156}) {
    ...WeatherNow
  }
  Kuvshinovo: weatherByPoint(request: {lat: 57.0265168, lon: 34.1676009}) {
    ...WeatherNow
  }
  Lihoslavl: weatherByPoint(request: {lat: 57.1221304, lon: 35.4667605}) {
    ...WeatherNow
  }
  Nelidovo: weatherByPoint(request: {lat: 56.2232566, lon: 32.7767459}) {
    ...WeatherNow
  }
  Ostashkov: weatherByPoint(request: {lat: 57.1456744, lon: 33.1115372}) {
    ...WeatherNow
  }
  Rzhev: weatherByPoint(request: {lat: 56.262881, lon: 34.3291002}) {
    ...WeatherNow
  }
  Staritsa: weatherByPoint(request: {lat: 56.514876, lon: 34.9336396}) {
    ...WeatherNow
  }
  Tver: weatherByPoint(request: {lat: 56.8586059, lon: 35.9116761}) {
    ...WeatherNow
  }
  Torzhok: weatherByPoint(request: {lat: 57.04133, lon: 34.9602344}) {
    ...WeatherNow
  }
  Toropets: weatherByPoint(request: {lat: 56.5012188, lon: 31.6355466}) {
    ...WeatherNow
  }
  Udomlya: weatherByPoint(request: {lat: 57.8787314, lon: 35.0167348}) {
    ...WeatherNow
  }
  Asino: weatherByPoint(request: {lat: 56.9907085, lon: 86.1765257}) {
    ...WeatherNow
  }
  Kedrovyy: weatherByPoint(request: {lat: 57.561869, lon: 79.5677821}) {
    ...WeatherNow
  }
  Kolpashevo: weatherByPoint(request: {lat: 58.3114253, lon: 82.9025829}) {
    ...WeatherNow
  }
  Seversk: weatherByPoint(request: {lat: 56.6031285, lon: 84.8809926}) {
    ...WeatherNow
  }
  Strezhevoy: weatherByPoint(request: {lat: 60.732895, lon: 77.604122}) {
    ...WeatherNow
  }
  Tomsk: weatherByPoint(request: {lat: 56.4845804, lon: 84.9481582}) {
    ...WeatherNow
  }
  Aleksin: weatherByPoint(request: {lat: 54.5083349, lon: 37.0478067}) {
    ...WeatherNow
  }
  Belev: weatherByPoint(request: {lat: 53.8114179, lon: 36.1382247}) {
    ...WeatherNow
  }
  Bogoroditsk: weatherByPoint(request: {lat: 53.7701014, lon: 38.1225152}) {
    ...WeatherNow
  }
  Bolohovo: weatherByPoint(request: {lat: 54.0820349, lon: 37.826724}) {
    ...WeatherNow
  }
  Venev: weatherByPoint(request: {lat: 54.3542315, lon: 38.2642236}) {
    ...WeatherNow
  }
  Donskoy: weatherByPoint(request: {lat: 53.9678944, lon: 38.3371824}) {
    ...WeatherNow
  }
  Efremov: weatherByPoint(request: {lat: 53.1464766, lon: 38.0921657}) {
    ...WeatherNow
  }
  Kimovsk: weatherByPoint(request: {lat: 53.9698378, lon: 38.5380808}) {
    ...WeatherNow
  }
  Kireevsk: weatherByPoint(request: {lat: 53.9319555, lon: 37.9220351}) {
    ...WeatherNow
  }
  Lipki: weatherByPoint(request: {lat: 53.9417551, lon: 37.7020148}) {
    ...WeatherNow
  }
  Novomoskovsk: weatherByPoint(request: {lat: 54.0109075, lon: 38.2914024}) {
    ...WeatherNow
  }
  Plavsk: weatherByPoint(request: {lat: 53.7096415, lon: 37.2862352}) {
    ...WeatherNow
  }
  Sovetsk_3: weatherByPoint(request: {lat: 53.9338874, lon: 37.6316141}) {
    ...WeatherNow
  }
  Suvorov: weatherByPoint(request: {lat: 54.1343585, lon: 36.4807419}) {
    ...WeatherNow
  }
  Tula: weatherByPoint(request: {lat: 54.1920559, lon: 37.6153842}) {
    ...WeatherNow
  }
  Uzlovaya: weatherByPoint(request: {lat: 53.9730452, lon: 38.1763201}) {
    ...WeatherNow
  }
  Chekalin: weatherByPoint(request: {lat: 54.0984438, lon: 36.2474142}) {
    ...WeatherNow
  }
  Schekino: weatherByPoint(request: {lat: 54.0020652, lon: 37.5176288}) {
    ...WeatherNow
  }
  Yasnogorsk: weatherByPoint(request: {lat: 54.4795484, lon: 37.6896048}) {
    ...WeatherNow
  }
  AkDovurak: weatherByPoint(request: {lat: 51.178452, lon: 90.5985129}) {
    ...WeatherNow
  }
  Kyzyl: weatherByPoint(request: {lat: 51.7191047, lon: 94.4376882}) {
    ...WeatherNow
  }
  Turan: weatherByPoint(request: {lat: 52.1449619, lon: 93.9173396}) {
    ...WeatherNow
  }
  Chadan: weatherByPoint(request: {lat: 51.2844502, lon: 91.5788609}) {
    ...WeatherNow
  }
  Shagonar: weatherByPoint(request: {lat: 51.5346393, lon: 92.9199675}) {
    ...WeatherNow
  }
  Zavodoukovsk: weatherByPoint(request: {lat: 56.5027463, lon: 66.5513613}) {
    ...WeatherNow
  }
  Ishim: weatherByPoint(request: {lat: 56.1104858, lon: 69.4795776}) {
    ...WeatherNow
  }
  Tobolsk: weatherByPoint(request: {lat: 58.2017299, lon: 68.2538558}) {
    ...WeatherNow
  }
  Tyumen: weatherByPoint(request: {lat: 57.1529744, lon: 65.5344099}) {
    ...WeatherNow
  }
  Yalutorovsk: weatherByPoint(request: {lat: 56.6547289, lon: 66.3122992}) {
    ...WeatherNow
  }
  Votkinsk: weatherByPoint(request: {lat: 57.0518149, lon: 53.9873096}) {
    ...WeatherNow
  }
  Glazov: weatherByPoint(request: {lat: 58.1359233, lon: 52.6635038}) {
    ...WeatherNow
  }
  Izhevsk: weatherByPoint(request: {lat: 56.852738, lon: 53.2114896}) {
    ...WeatherNow
  }
  Kambarka: weatherByPoint(request: {lat: 56.2659916, lon: 54.193374}) {
    ...WeatherNow
  }
  Mozhga: weatherByPoint(request: {lat: 56.4427774, lon: 52.2137886}) {
    ...WeatherNow
  }
  Sarapul: weatherByPoint(request: {lat: 56.4615767, lon: 53.8037657}) {
    ...WeatherNow
  }
  Barysh: weatherByPoint(request: {lat: 53.6533992, lon: 47.1181134}) {
    ...WeatherNow
  }
  Dimitrovgrad: weatherByPoint(request: {lat: 54.2167926, lon: 49.6262585}) {
    ...WeatherNow
  }
  Inza: weatherByPoint(request: {lat: 53.8549647, lon: 46.3533459}) {
    ...WeatherNow
  }
  Novoulyanovsk: weatherByPoint(request: {lat: 54.1447956, lon: 48.3910789}) {
    ...WeatherNow
  }
  Sengiley: weatherByPoint(request: {lat: 53.958964, lon: 48.7768269}) {
    ...WeatherNow
  }
  Ulyanovsk: weatherByPoint(request: {lat: 54.3079415, lon: 48.3748487}) {
    ...WeatherNow
  }
  Amursk: weatherByPoint(request: {lat: 50.2344147, lon: 136.8792444}) {
    ...WeatherNow
  }
  Bikin: weatherByPoint(request: {lat: 46.8185743, lon: 134.2550718}) {
    ...WeatherNow
  }
  Vyazemskiy: weatherByPoint(request: {lat: 47.5353379, lon: 134.7553856}) {
    ...WeatherNow
  }
  KomsomolskNaAmure: weatherByPoint(request: {lat: 50.5498936, lon: 137.0079408}) {
    ...WeatherNow
  }
  NikolaevskNaAmure: weatherByPoint(request: {lat: 53.1460657, lon: 140.7111367}) {
    ...WeatherNow
  }
  SovetskayaGavan: weatherByPoint(request: {lat: 48.9664966, lon: 140.285174}) {
    ...WeatherNow
  }
  Habarovsk: weatherByPoint(request: {lat: 48.4647258, lon: 135.0598942}) {
    ...WeatherNow
  }
  Abaza: weatherByPoint(request: {lat: 52.6516647, lon: 90.0885686}) {
    ...WeatherNow
  }
  Abakan: weatherByPoint(request: {lat: 53.7223325, lon: 91.4436721}) {
    ...WeatherNow
  }
  Sayanogorsk: weatherByPoint(request: {lat: 53.1008083, lon: 91.4122454}) {
    ...WeatherNow
  }
  Sorsk: weatherByPoint(request: {lat: 54.0002888, lon: 90.2594446}) {
    ...WeatherNow
  }
  Chernogorsk: weatherByPoint(request: {lat: 53.8259342, lon: 91.3260229}) {
    ...WeatherNow
  }
  Beloyarskiy: weatherByPoint(request: {lat: 63.7121099, lon: 66.6772226}) {
    ...WeatherNow
  }
  Kogalym: weatherByPoint(request: {lat: 62.2639527, lon: 74.4829794}) {
    ...WeatherNow
  }
  Langepas: weatherByPoint(request: {lat: 61.2536939, lon: 75.1807763}) {
    ...WeatherNow
  }
  Lyantor: weatherByPoint(request: {lat: 61.6392863, lon: 72.179409}) {
    ...WeatherNow
  }
  Megion: weatherByPoint(request: {lat: 61.0318712, lon: 76.1025878}) {
    ...WeatherNow
  }
  Nefteyugansk: weatherByPoint(request: {lat: 61.0882676, lon: 72.6164079}) {
    ...WeatherNow
  }
  Nizhnevartovsk: weatherByPoint(request: {lat: 60.9396698, lon: 76.5696184}) {
    ...WeatherNow
  }
  Nyagan: weatherByPoint(request: {lat: 62.1454701, lon: 65.3946047}) {
    ...WeatherNow
  }
  Pokachi: weatherByPoint(request: {lat: 61.7422169, lon: 75.5941517}) {
    ...WeatherNow
  }
  PytYah: weatherByPoint(request: {lat: 60.7585833, lon: 72.8365617}) {
    ...WeatherNow
  }
  Raduzhnyy_2: weatherByPoint(request: {lat: 62.1342888, lon: 77.4584094}) {
    ...WeatherNow
  }
  Sovetskiy: weatherByPoint(request: {lat: 61.3706913, lon: 63.5667222}) {
    ...WeatherNow
  }
  Surgut: weatherByPoint(request: {lat: 61.2541083, lon: 73.3961587}) {
    ...WeatherNow
  }
  Uray: weatherByPoint(request: {lat: 60.1296954, lon: 64.8038508}) {
    ...WeatherNow
  }
  HantyMansiysk: weatherByPoint(request: {lat: 61.0023984, lon: 69.0184798}) {
    ...WeatherNow
  }
  Yugorsk: weatherByPoint(request: {lat: 61.3123568, lon: 63.3365484}) {
    ...WeatherNow
  }
  Asha: weatherByPoint(request: {lat: 54.9906527, lon: 57.2783953}) {
    ...WeatherNow
  }
  Bakal: weatherByPoint(request: {lat: 54.9406399, lon: 58.8051698}) {
    ...WeatherNow
  }
  Verhneuralsk: weatherByPoint(request: {lat: 53.8760961, lon: 59.2169852}) {
    ...WeatherNow
  }
  VerhniyUfaley: weatherByPoint(request: {lat: 56.0487158, lon: 60.2318886}) {
    ...WeatherNow
  }
  Emanzhelinsk: weatherByPoint(request: {lat: 54.7554548, lon: 61.3243477}) {
    ...WeatherNow
  }
  Zlatoust: weatherByPoint(request: {lat: 55.1714905, lon: 59.6725549}) {
    ...WeatherNow
  }
  Karabash: weatherByPoint(request: {lat: 55.4852323, lon: 60.2358881}) {
    ...WeatherNow
  }
  Kartaly: weatherByPoint(request: {lat: 53.0536197, lon: 60.6478408}) {
    ...WeatherNow
  }
  Kasli: weatherByPoint(request: {lat: 55.8868784, lon: 60.7421663}) {
    ...WeatherNow
  }
  KatavIvanovsk: weatherByPoint(request: {lat: 54.7521438, lon: 58.1983648}) {
    ...WeatherNow
  }
  Kopeysk: weatherByPoint(request: {lat: 55.116665, lon: 61.6179185}) {
    ...WeatherNow
  }
  Korkino: weatherByPoint(request: {lat: 54.8903147, lon: 61.4034576}) {
    ...WeatherNow
  }
  Kusa: weatherByPoint(request: {lat: 55.3386053, lon: 59.4385778}) {
    ...WeatherNow
  }
  Kyshtym: weatherByPoint(request: {lat: 55.7061276, lon: 60.5563781}) {
    ...WeatherNow
  }
  Magnitogorsk: weatherByPoint(request: {lat: 53.4072153, lon: 58.9791437}) {
    ...WeatherNow
  }
  Miass: weatherByPoint(request: {lat: 55.0456457, lon: 60.1077572}) {
    ...WeatherNow
  }
  Minyar: weatherByPoint(request: {lat: 55.0709557, lon: 57.548478}) {
    ...WeatherNow
  }
  Nyazepetrovsk: weatherByPoint(request: {lat: 56.0536895, lon: 59.6097202}) {
    ...WeatherNow
  }
  Ozersk_2: weatherByPoint(request: {lat: 55.763154, lon: 60.7076198}) {
    ...WeatherNow
  }
  Plast: weatherByPoint(request: {lat: 54.3692764, lon: 60.8151894}) {
    ...WeatherNow
  }
  Satka: weatherByPoint(request: {lat: 55.0405288, lon: 59.0288975}) {
    ...WeatherNow
  }
  Sim: weatherByPoint(request: {lat: 54.9907827, lon: 57.6900155}) {
    ...WeatherNow
  }
  Snezhinsk: weatherByPoint(request: {lat: 56.0851495, lon: 60.7324914}) {
    ...WeatherNow
  }
  Trehgornyy: weatherByPoint(request: {lat: 54.8178249, lon: 58.4464194}) {
    ...WeatherNow
  }
  Troitsk: weatherByPoint(request: {lat: 54.0843745, lon: 61.5586831}) {
    ...WeatherNow
  }
  UstKatav: weatherByPoint(request: {lat: 54.9260812, lon: 58.152805}) {
    ...WeatherNow
  }
  Chebarkul: weatherByPoint(request: {lat: 54.9818567, lon: 60.3773121}) {
    ...WeatherNow
  }
  Chelyabinsk: weatherByPoint(request: {lat: 55.1602624, lon: 61.4008078}) {
    ...WeatherNow
  }
  Yuzhnouralsk: weatherByPoint(request: {lat: 54.448927, lon: 61.2581158}) {
    ...WeatherNow
  }
  Yuryuzan: weatherByPoint(request: {lat: 54.854662, lon: 58.4226698}) {
    ...WeatherNow
  }
  Argun: weatherByPoint(request: {lat: 43.2916774, lon: 45.8723105}) {
    ...WeatherNow
  }
  Groznyy: weatherByPoint(request: {lat: 43.3180145, lon: 45.698291}) {
    ...WeatherNow
  }
  Gudermes: weatherByPoint(request: {lat: 43.3519142, lon: 46.1035645}) {
    ...WeatherNow
  }
  Kurchaloy: weatherByPoint(request: {lat: 43.2046547, lon: 46.0889364}) {
    ...WeatherNow
  }
  UrusMartan: weatherByPoint(request: {lat: 43.120175, lon: 45.539276}) {
    ...WeatherNow
  }
  Shali: weatherByPoint(request: {lat: 43.1488691, lon: 45.9009629}) {
    ...WeatherNow
  }
  Alatyr: weatherByPoint(request: {lat: 54.8397989, lon: 46.5721997}) {
    ...WeatherNow
  }
  Kanash: weatherByPoint(request: {lat: 55.507, lon: 47.4918273}) {
    ...WeatherNow
  }
  Kozlovka: weatherByPoint(request: {lat: 55.8406025, lon: 48.2577735}) {
    ...WeatherNow
  }
  MariinskiyPosad: weatherByPoint(request: {lat: 56.111923, lon: 47.7142942}) {
    ...WeatherNow
  }
  Novocheboksarsk: weatherByPoint(request: {lat: 56.1094977, lon: 47.4791113}) {
    ...WeatherNow
  }
  Tsivilsk: weatherByPoint(request: {lat: 55.8650213, lon: 47.4729349}) {
    ...WeatherNow
  }
  Cheboksary: weatherByPoint(request: {lat: 56.1438298, lon: 47.2489782}) {
    ...WeatherNow
  }
  Shumerlya: weatherByPoint(request: {lat: 55.4962415, lon: 46.4182681}) {
    ...WeatherNow
  }
  Yadrin: weatherByPoint(request: {lat: 55.9406974, lon: 46.2020896}) {
    ...WeatherNow
  }
  Anadyr: weatherByPoint(request: {lat: 64.7313924, lon: 177.5015421}) {
    ...WeatherNow
  }
  Bilibino: weatherByPoint(request: {lat: 68.0584191, lon: 166.4388172}) {
    ...WeatherNow
  }
  Pevek: weatherByPoint(request: {lat: 69.7016661, lon: 170.2999022}) {
    ...WeatherNow
  }
  Aldan: weatherByPoint(request: {lat: 58.6094283, lon: 125.3817188}) {
    ...WeatherNow
  }
  Verhoyansk: weatherByPoint(request: {lat: 67.5502451, lon: 133.390735}) {
    ...WeatherNow
  }
  Vilyuysk: weatherByPoint(request: {lat: 63.7517616, lon: 121.627284}) {
    ...WeatherNow
  }
  Lensk: weatherByPoint(request: {lat: 60.7276196, lon: 114.9548255}) {
    ...WeatherNow
  }
  Mirnyy_2: weatherByPoint(request: {lat: 62.536232, lon: 113.9667728}) {
    ...WeatherNow
  }
  Neryungri: weatherByPoint(request: {lat: 56.6599953, lon: 124.7202403}) {
    ...WeatherNow
  }
  Nyurba: weatherByPoint(request: {lat: 63.2828955, lon: 118.3242437}) {
    ...WeatherNow
  }
  Olekminsk: weatherByPoint(request: {lat: 60.3758006, lon: 120.4060878}) {
    ...WeatherNow
  }
  Pokrovsk: weatherByPoint(request: {lat: 61.4843503, lon: 129.1482392}) {
    ...WeatherNow
  }
  Srednekolymsk: weatherByPoint(request: {lat: 67.4582218, lon: 153.7069425}) {
    ...WeatherNow
  }
  Tommot: weatherByPoint(request: {lat: 58.9586859, lon: 126.2875462}) {
    ...WeatherNow
  }
  Udachnyy: weatherByPoint(request: {lat: 66.4071765, lon: 112.3061555}) {
    ...WeatherNow
  }
  Yakutsk: weatherByPoint(request: {lat: 62.0281405, lon: 129.7325887}) {
    ...WeatherNow
  }
  Gubkinskiy: weatherByPoint(request: {lat: 64.4457594, lon: 76.4713274}) {
    ...WeatherNow
  }
  Labytnangi: weatherByPoint(request: {lat: 66.6592841, lon: 66.3883009}) {
    ...WeatherNow
  }
  Muravlenko: weatherByPoint(request: {lat: 63.7940552, lon: 74.4948635}) {
    ...WeatherNow
  }
  Nadym: weatherByPoint(request: {lat: 65.5377966, lon: 72.5182736}) {
    ...WeatherNow
  }
  NovyyUrengoy: weatherByPoint(request: {lat: 66.0839433, lon: 76.6809681}) {
    ...WeatherNow
  }
  Noyabrsk: weatherByPoint(request: {lat: 63.2018039, lon: 75.4510581}) {
    ...WeatherNow
  }
  Salehard: weatherByPoint(request: {lat: 66.5492077, lon: 66.6085318}) {
    ...WeatherNow
  }
  TarkoSale: weatherByPoint(request: {lat: 64.9118803, lon: 77.7610236}) {
    ...WeatherNow
  }
  GavrilovYam: weatherByPoint(request: {lat: 57.3091058, lon: 39.8546444}) {
    ...WeatherNow
  }
  Danilov: weatherByPoint(request: {lat: 58.1860098, lon: 40.1795067}) {
    ...WeatherNow
  }
  Lyubim: weatherByPoint(request: {lat: 58.3620228, lon: 40.686841}) {
    ...WeatherNow
  }
  Myshkin: weatherByPoint(request: {lat: 57.7881684, lon: 38.4544224}) {
    ...WeatherNow
  }
  PereslavlZalesskiy: weatherByPoint(request: {lat: 56.7360544, lon: 38.8543617}) {
    ...WeatherNow
  }
  Poshehone: weatherByPoint(request: {lat: 58.5062879, lon: 39.1208434}) {
    ...WeatherNow
  }
  Rostov: weatherByPoint(request: {lat: 57.2051315, lon: 39.4378622}) {
    ...WeatherNow
  }
  Rybinsk: weatherByPoint(request: {lat: 58.0485495, lon: 38.8584119}) {
    ...WeatherNow
  }
  Tutaev: weatherByPoint(request: {lat: 57.8674993, lon: 39.5369627}) {
    ...WeatherNow
  }
  Uglich: weatherByPoint(request: {lat: 57.5224249, lon: 38.3020044}) {
    ...WeatherNow
  }
  Yaroslavl: weatherByPoint(request: {lat: 57.6215477, lon: 39.8977411}) {
    ...WeatherNow
  }
  CAD: weatherByPoint(request: {lat: 55.754600, lon: 37.587400}) {
    ...WeatherNow
  }
  NAD: weatherByPoint(request: {lat: 55.895400, lon: 37.482700}) {
    ...WeatherNow
  }
  NWAD: weatherByPoint(request: {lat: 55.814700, lon: 37.335200}) {
    ...WeatherNow
  }
  WAD: weatherByPoint(request: {lat: 55.737100, lon: 37.267800}) {
    ...WeatherNow
  }
  NEAD: weatherByPoint(request: {lat: 55.875100, lon: 37.623800}) {
    ...WeatherNow
  }
  EAD: weatherByPoint(request: {lat: 55.801200, lon: 37.718400}) {
    ...WeatherNow
  }
  SAD: weatherByPoint(request: {lat: 55.665500, lon: 37.601200}) {
    ...WeatherNow
  }
  SEAD: weatherByPoint(request: {lat: 55.712900, lon: 37.751300}) {
    ...WeatherNow
  }
  SWAD: weatherByPoint(request: {lat: 55.694300, lon: 37.526500}) {
    ...WeatherNow
  }
  ZAD: weatherByPoint(request: {lat: 55.986500, lon: 37.135300}) {
    ...WeatherNow
  }
  TAD: weatherByPoint(request: {lat: 55.481100, lon: 37.295600}) {
    ...WeatherNow
  }
  NovAD: weatherByPoint(request: {lat: 55.630200, lon: 37.403800}) {
    ...WeatherNow
  }
  Mos: weatherByPoint(request: {lat: 55.751244, lon: 37.618423}) {
    ...WeatherNow
  }
}

fragment WeatherNow on Weather {
  now {
    cloudiness
    condition
    daytime
    dewPoint
    drizzleProbability
    feelsLike
    heatIndex
    humidity
    iceAreaFraction
    iceThickness
    isThunder
    kpIndex
    leafWetnessIndex
    meanSeaLevelPressure
    moon {
      hemisphere
      days {
        phase
        fraction
        age
        time
        timestamp
        moonriseTime
        moonriseTimestamp
        moonsetTime
        moonsetTimestamp
      }
    }
    phenomCondition
    pollution {
      aqi
      co
      dominant
      density
      dustStormStrength
      no2
      o3
      pm10
      pm2p5
      so2
    }
    precProbability
    precStrength
    precType
    pressure
    roadCondition
    runCondition
    seaCurrentAngle
    seaCurrentDirection
    seaCurrentSpeed
    season
    snowDepth
    soilMoisture
    soilTemperature
    swellAngle
    swellDirection
    swellHeight
    swellPeriod
    temperature
    uv
    uvIndex
    visibility
    waterTemperature
    waveAngle
    waveDirection
    waveHeight
    waveMaxHeight
    wavePeriod
    windAngle
    windChill
    windDirection
    windGust
    windSpeed
  }
}
"""

def make_weather_request(query: str):
    
    """
    
    Отправить запрос к yandex api.
    
    """
    
    responce = requests.post(
        REQUERST_URL, 
        headers=REQUEST_HEADERS, 
        json={'query': query}
    )

    if not responce.status_code == 200:
        logging.warning(f"Запрос не выполнен, код статуса {responce.status_code}")
        return
    
    weather_responce: dict = json.loads(responce.content)

    if 'errors' in weather_responce.keys():
        errors: dict = weather_responce['errors'][0]
        logging.warning(
            f"""Запрос вернулся с ошибкой\n"""\
            f"""Сообщение:{errors['message']}\n"""\
            f"""Строки: {errors['locations']}\n"""\
            f"""Ошибка: {errors['extensions']['code']}"""
        )
        return
    
    return weather_responce
    

def get_weather_forecast(query: str):
    
    """

    Получить прогноз погоды на данные сутки.
    
    """
    logging.info(f'Путь {os.getcwd()}')

    forecast_path = os.path.join(
        HOME_PATH, 'forecast'
    )

    logging.info(forecast_path)

    if not os.path.exists(forecast_path):
        os.mkdir(forecast_path)


    weather_forecast_responce = make_weather_request(query)
    
    if not weather_forecast_responce:
        return
    
    weather_forecast_data = weather_forecast_responce.get('data')
    
    rows = []

    for key, value in weather_forecast_data.items():
        weather_forecast_days = value['forecast']['days']
        for forecast in weather_forecast_days:
            date = forecast.get('time')
            day_data = {
                f'day_{k}': v for k, v in forecast['summary']['day'].items()
            }
            night_data = {
                f'night_{k}': v for k, v in forecast['summary']['night'].items()
            }

            all_data = {
                'area': key,
                'predict_date': date,
                **day_data,
                **night_data}

            rows.append(all_data)

    weather_on_week = pd.DataFrame(rows)

    dayli_forecast = os.path.join(
        forecast_path, f'weather_forrecast_{datetime.now().date().strftime("%Y%m%d")}.parquet'
    )

    weather_on_week.to_parquet(
        dayli_forecast, 
        index=False
    )

    logging.info('DAG выполнен корректно')


def get_weather_now(query: str):
    
    weather_now_path = os.path.join(
        HOME_PATH, 'now'
    )

    if not os.path.exists(weather_now_path):
        os.mkdir(weather_now_path)
    
    weather_now_responce = make_weather_request(query)

    if not weather_now_responce:
        return
    
    weather_now_data: dict = weather_now_responce.get('data')
    rows = []
    for area, area_value in weather_now_data.items():
        flat = {'area': area}
        weather_now: dict = area_value.get('now')
        for weather_key, weather_value in weather_now.items():
            if isinstance(weather_value, dict):
                for sub_key, sub_value in weather_value.items():
                    if (isinstance(sub_value, list) 
                        and len(sub_value) > 0
                    ):
                        for item_key, item_value in sub_value[0].items():
                          flat[f"{weather_key}_{sub_key}_{item_key}"] = item_value
                    else:
                        flat[f'{weather_key}_{sub_key}'] = sub_value
            else:
                flat[weather_key] = weather_value

        rows.append(flat)

    weather_now_df = pd.DataFrame(rows)
    
    today_weaher_now_path = os.path.join(
        weather_now_path, f'{datetime.now().date().strftime("%Y%m%d")}'
    )

    if not os.path.exists(today_weaher_now_path):
        os.mkdir(today_weaher_now_path)

    today_weaher_now_filename = os.path.join(
        today_weaher_now_path, f'weather_now_{datetime.now().strftime("%Y%m%d_%H%M%S")}.parquet'
    )

    weather_now_df.to_parquet(
        today_weaher_now_filename, 
        index=False
    )
        
with DAG(
    dag_id='weather_forecast_dag',
    start_date=datetime(2025, 4, 22),
    schedule='0 0 * * *',
) as dag:
    
    get_daily_weather_forecast = PythonOperator(
        task_id='get_daily_weather_forecast',
        python_callable=get_weather_forecast,
        op_args=[WEATHER_FORECAST_QUERY]
    )

    get_daily_weather_forecast

with DAG(
    dag_id='weather_now_dag',
    start_date=datetime(2025, 4, 22),
    schedule='0 * * * *'
) as dag:
    
    get_now_weather = PythonOperator(
        task_id = 'get_now_weather',
        python_callable=get_weather_now,
        op_args=[WEATHER_NOW_QUERY]


    )

    get_now_weather