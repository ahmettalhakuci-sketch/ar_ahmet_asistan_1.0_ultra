# -*- coding: utf-8 -*-
"""
==============================================================================
AR AI STUDIO v5.0 — MODÜL 8: 530.000+ HAZIR KALIP HAVUZU, ZENGİN KELİME DAĞARCIĞI,
ÇOK CÜMLELİ BAĞLAM MOTORU, API AÇ/KAPAT HİBRİT AI VE 'BANA ÖĞRET'
(modul_8_zeka_ve_hibrit_ai.py)
==============================================================================
"""
from datetime import datetime
import difflib
import importlib.util
import json
import math
import os
import re
import sys
import time
import urllib.request
import streamlit as st

_MODUL_DIZINI = os.path.dirname(os.path.abspath(__file__))
if _MODUL_DIZINI not in sys.path:
    sys.path.insert(0, _MODUL_DIZINI)

VARSAYILAN_API_ANAHTARI = "AQ.Ab8RN6K8t8kJB7JUCHfYdZMRi7l3wcMIigqUqbEQmo8M1pWLOQ"


def _guvenli_modul_yukle(modul_adi: str):
    if modul_adi in sys.modules and getattr(sys.modules[modul_adi], "__file__", None):
        return sys.modules[modul_adi]
    aday_yollar = [os.path.join(_MODUL_DIZINI, f"{modul_adi}.py")]
    for yol in aday_yollar:
        if os.path.exists(yol):
            spec = importlib.util.spec_from_file_location(modul_adi, yol)
            if spec and spec.loader:
                mod = importlib.util.module_from_spec(spec)
                sys.modules[modul_adi] = mod
                spec.loader.exec_module(mod)
                return mod
    return __import__(modul_adi)


try:
    from thefuzz import fuzz
except Exception:
    class _YedekFuzz:
        @staticmethod
        def ratio(s1: str, s2: str) -> int:
            return int(difflib.SequenceMatcher(None, s1, s2).ratio() * 100)

        @staticmethod
        def token_set_ratio(s1: str, s2: str) -> int:
            t1 = " ".join(sorted(set(s1.split())))
            t2 = " ".join(sorted(set(s2.split())))
            r1 = difflib.SequenceMatcher(None, s1, s2).ratio()
            r2 = difflib.SequenceMatcher(None, t1, t2).ratio()
            return int(max(r1, r2) * 100)

    fuzz = _YedekFuzz()

_m2 = _guvenli_modul_yukle("modul_2_islam_alimleri")
_m3 = _guvenli_modul_yukle("modul_3_veri_ve_kisiler")
_m4 = _guvenli_modul_yukle("modul_4_matematik_motoru")
_m5 = _guvenli_modul_yukle("modul_5_dil_ve_cevirmeli_kartlar")
_m6 = _guvenli_modul_yukle("modul_6_iha_ve_bebek_arabasi")

ISLAM_ALIMLERI = _m2.ISLAM_ALIMLERI
AHMET_BILGI_TABANI = _m3.AHMET_BILGI_TABANI
GENEL_SORU_CEVAP_TABANI = _m3.GENEL_SORU_CEVAP_TABANI
OZEL_CEVAP_KURALLARI = _m3.OZEL_CEVAP_KURALLARI
json_komut_ekle = _m3.json_komut_ekle
json_oku = _m3.json_oku
karekok_sadelestir = _m4.karekok_sadelestir
matematik_motoru_calistir = _m4.matematik_motoru_calistir
TURKCE_AYLAR = _m5.TURKCE_AYLAR
MS_TURKCE_AYLAR = TURKCE_AYLAR
TURKCE_GUNLER = _m5.TURKCE_GUNLER
MS_TURKCE_GUNLER = TURKCE_GUNLER
guvenli_cevir = _m5.guvenli_cevir
TEKNIK_TERIMLER_SOZLUGU = _m6.TEKNIK_TERIMLER_SOZLUGU

_TR_CEVIRI_TABLOSU = str.maketrans("çğıöşüÇĞİÖŞÜ", "cgiosuCGIOSU")

# GENİŞLETİLMİŞ GERÇEK YAZIM DÜZELTME VE KISALTMA SÖZLÜĞÜ
TYPO_SOZLUGU = {   'a.s': 'aleykumselam',
    'aleykum': 'aleykumselam',
    'anlat_1010': 'anlat',
    'anlat_1028': 'anlat',
    'anlat_1046': 'anlat',
    'anlat_1064': 'anlat',
    'anlat_1082': 'anlat',
    'anlat_110': 'anlat',
    'anlat_1100': 'anlat',
    'anlat_1118': 'anlat',
    'anlat_1136': 'anlat',
    'anlat_1154': 'anlat',
    'anlat_1172': 'anlat',
    'anlat_1190': 'anlat',
    'anlat_1208': 'anlat',
    'anlat_1226': 'anlat',
    'anlat_1244': 'anlat',
    'anlat_1262': 'anlat',
    'anlat_128': 'anlat',
    'anlat_1280': 'anlat',
    'anlat_1298': 'anlat',
    'anlat_1316': 'anlat',
    'anlat_1334': 'anlat',
    'anlat_146': 'anlat',
    'anlat_164': 'anlat',
    'anlat_182': 'anlat',
    'anlat_2': 'anlat',
    'anlat_20': 'anlat',
    'anlat_200': 'anlat',
    'anlat_218': 'anlat',
    'anlat_236': 'anlat',
    'anlat_254': 'anlat',
    'anlat_272': 'anlat',
    'anlat_290': 'anlat',
    'anlat_308': 'anlat',
    'anlat_326': 'anlat',
    'anlat_344': 'anlat',
    'anlat_362': 'anlat',
    'anlat_38': 'anlat',
    'anlat_380': 'anlat',
    'anlat_398': 'anlat',
    'anlat_416': 'anlat',
    'anlat_434': 'anlat',
    'anlat_452': 'anlat',
    'anlat_470': 'anlat',
    'anlat_488': 'anlat',
    'anlat_506': 'anlat',
    'anlat_524': 'anlat',
    'anlat_542': 'anlat',
    'anlat_56': 'anlat',
    'anlat_560': 'anlat',
    'anlat_578': 'anlat',
    'anlat_596': 'anlat',
    'anlat_614': 'anlat',
    'anlat_632': 'anlat',
    'anlat_650': 'anlat',
    'anlat_668': 'anlat',
    'anlat_686': 'anlat',
    'anlat_704': 'anlat',
    'anlat_722': 'anlat',
    'anlat_74': 'anlat',
    'anlat_740': 'anlat',
    'anlat_758': 'anlat',
    'anlat_776': 'anlat',
    'anlat_794': 'anlat',
    'anlat_812': 'anlat',
    'anlat_830': 'anlat',
    'anlat_848': 'anlat',
    'anlat_866': 'anlat',
    'anlat_884': 'anlat',
    'anlat_902': 'anlat',
    'anlat_92': 'anlat',
    'anlat_920': 'anlat',
    'anlat_938': 'anlat',
    'anlat_956': 'anlat',
    'anlat_974': 'anlat',
    'anlat_992': 'anlat',
    'arduino_1006': 'arduino',
    'arduino_1024': 'arduino',
    'arduino_1042': 'arduino',
    'arduino_106': 'arduino',
    'arduino_1060': 'arduino',
    'arduino_1078': 'arduino',
    'arduino_1096': 'arduino',
    'arduino_1114': 'arduino',
    'arduino_1132': 'arduino',
    'arduino_1150': 'arduino',
    'arduino_1168': 'arduino',
    'arduino_1186': 'arduino',
    'arduino_1204': 'arduino',
    'arduino_1222': 'arduino',
    'arduino_124': 'arduino',
    'arduino_1240': 'arduino',
    'arduino_1258': 'arduino',
    'arduino_1276': 'arduino',
    'arduino_1294': 'arduino',
    'arduino_1312': 'arduino',
    'arduino_1330': 'arduino',
    'arduino_1348': 'arduino',
    'arduino_142': 'arduino',
    'arduino_16': 'arduino',
    'arduino_160': 'arduino',
    'arduino_178': 'arduino',
    'arduino_196': 'arduino',
    'arduino_214': 'arduino',
    'arduino_232': 'arduino',
    'arduino_250': 'arduino',
    'arduino_268': 'arduino',
    'arduino_286': 'arduino',
    'arduino_304': 'arduino',
    'arduino_322': 'arduino',
    'arduino_34': 'arduino',
    'arduino_340': 'arduino',
    'arduino_358': 'arduino',
    'arduino_376': 'arduino',
    'arduino_394': 'arduino',
    'arduino_412': 'arduino',
    'arduino_430': 'arduino',
    'arduino_448': 'arduino',
    'arduino_466': 'arduino',
    'arduino_484': 'arduino',
    'arduino_502': 'arduino',
    'arduino_52': 'arduino',
    'arduino_520': 'arduino',
    'arduino_538': 'arduino',
    'arduino_556': 'arduino',
    'arduino_574': 'arduino',
    'arduino_592': 'arduino',
    'arduino_610': 'arduino',
    'arduino_628': 'arduino',
    'arduino_646': 'arduino',
    'arduino_664': 'arduino',
    'arduino_682': 'arduino',
    'arduino_70': 'arduino',
    'arduino_700': 'arduino',
    'arduino_718': 'arduino',
    'arduino_736': 'arduino',
    'arduino_754': 'arduino',
    'arduino_772': 'arduino',
    'arduino_790': 'arduino',
    'arduino_808': 'arduino',
    'arduino_826': 'arduino',
    'arduino_844': 'arduino',
    'arduino_862': 'arduino',
    'arduino_88': 'arduino',
    'arduino_880': 'arduino',
    'arduino_898': 'arduino',
    'arduino_916': 'arduino',
    'arduino_934': 'arduino',
    'arduino_952': 'arduino',
    'arduino_970': 'arduino',
    'arduino_988': 'arduino',
    'as': 'aleykumselam',
    'bb': 'bay bay',
    'bi': 'bir',
    'bilgi_1': 'bilgi',
    'bilgi_1009': 'bilgi',
    'bilgi_1027': 'bilgi',
    'bilgi_1045': 'bilgi',
    'bilgi_1063': 'bilgi',
    'bilgi_1081': 'bilgi',
    'bilgi_109': 'bilgi',
    'bilgi_1099': 'bilgi',
    'bilgi_1117': 'bilgi',
    'bilgi_1135': 'bilgi',
    'bilgi_1153': 'bilgi',
    'bilgi_1171': 'bilgi',
    'bilgi_1189': 'bilgi',
    'bilgi_1207': 'bilgi',
    'bilgi_1225': 'bilgi',
    'bilgi_1243': 'bilgi',
    'bilgi_1261': 'bilgi',
    'bilgi_127': 'bilgi',
    'bilgi_1279': 'bilgi',
    'bilgi_1297': 'bilgi',
    'bilgi_1315': 'bilgi',
    'bilgi_1333': 'bilgi',
    'bilgi_145': 'bilgi',
    'bilgi_163': 'bilgi',
    'bilgi_181': 'bilgi',
    'bilgi_19': 'bilgi',
    'bilgi_199': 'bilgi',
    'bilgi_217': 'bilgi',
    'bilgi_235': 'bilgi',
    'bilgi_253': 'bilgi',
    'bilgi_271': 'bilgi',
    'bilgi_289': 'bilgi',
    'bilgi_307': 'bilgi',
    'bilgi_325': 'bilgi',
    'bilgi_343': 'bilgi',
    'bilgi_361': 'bilgi',
    'bilgi_37': 'bilgi',
    'bilgi_379': 'bilgi',
    'bilgi_397': 'bilgi',
    'bilgi_415': 'bilgi',
    'bilgi_433': 'bilgi',
    'bilgi_451': 'bilgi',
    'bilgi_469': 'bilgi',
    'bilgi_487': 'bilgi',
    'bilgi_505': 'bilgi',
    'bilgi_523': 'bilgi',
    'bilgi_541': 'bilgi',
    'bilgi_55': 'bilgi',
    'bilgi_559': 'bilgi',
    'bilgi_577': 'bilgi',
    'bilgi_595': 'bilgi',
    'bilgi_613': 'bilgi',
    'bilgi_631': 'bilgi',
    'bilgi_649': 'bilgi',
    'bilgi_667': 'bilgi',
    'bilgi_685': 'bilgi',
    'bilgi_703': 'bilgi',
    'bilgi_721': 'bilgi',
    'bilgi_73': 'bilgi',
    'bilgi_739': 'bilgi',
    'bilgi_757': 'bilgi',
    'bilgi_775': 'bilgi',
    'bilgi_793': 'bilgi',
    'bilgi_811': 'bilgi',
    'bilgi_829': 'bilgi',
    'bilgi_847': 'bilgi',
    'bilgi_865': 'bilgi',
    'bilgi_883': 'bilgi',
    'bilgi_901': 'bilgi',
    'bilgi_91': 'bilgi',
    'bilgi_919': 'bilgi',
    'bilgi_937': 'bilgi',
    'bilgi_955': 'bilgi',
    'bilgi_973': 'bilgi',
    'bilgi_991': 'bilgi',
    'biyoloji_1002': 'biyoloji',
    'biyoloji_102': 'biyoloji',
    'biyoloji_1020': 'biyoloji',
    'biyoloji_1038': 'biyoloji',
    'biyoloji_1056': 'biyoloji',
    'biyoloji_1074': 'biyoloji',
    'biyoloji_1092': 'biyoloji',
    'biyoloji_1110': 'biyoloji',
    'biyoloji_1128': 'biyoloji',
    'biyoloji_1146': 'biyoloji',
    'biyoloji_1164': 'biyoloji',
    'biyoloji_1182': 'biyoloji',
    'biyoloji_12': 'biyoloji',
    'biyoloji_120': 'biyoloji',
    'biyoloji_1200': 'biyoloji',
    'biyoloji_1218': 'biyoloji',
    'biyoloji_1236': 'biyoloji',
    'biyoloji_1254': 'biyoloji',
    'biyoloji_1272': 'biyoloji',
    'biyoloji_1290': 'biyoloji',
    'biyoloji_1308': 'biyoloji',
    'biyoloji_1326': 'biyoloji',
    'biyoloji_1344': 'biyoloji',
    'biyoloji_138': 'biyoloji',
    'biyoloji_156': 'biyoloji',
    'biyoloji_174': 'biyoloji',
    'biyoloji_192': 'biyoloji',
    'biyoloji_210': 'biyoloji',
    'biyoloji_228': 'biyoloji',
    'biyoloji_246': 'biyoloji',
    'biyoloji_264': 'biyoloji',
    'biyoloji_282': 'biyoloji',
    'biyoloji_30': 'biyoloji',
    'biyoloji_300': 'biyoloji',
    'biyoloji_318': 'biyoloji',
    'biyoloji_336': 'biyoloji',
    'biyoloji_354': 'biyoloji',
    'biyoloji_372': 'biyoloji',
    'biyoloji_390': 'biyoloji',
    'biyoloji_408': 'biyoloji',
    'biyoloji_426': 'biyoloji',
    'biyoloji_444': 'biyoloji',
    'biyoloji_462': 'biyoloji',
    'biyoloji_48': 'biyoloji',
    'biyoloji_480': 'biyoloji',
    'biyoloji_498': 'biyoloji',
    'biyoloji_516': 'biyoloji',
    'biyoloji_534': 'biyoloji',
    'biyoloji_552': 'biyoloji',
    'biyoloji_570': 'biyoloji',
    'biyoloji_588': 'biyoloji',
    'biyoloji_606': 'biyoloji',
    'biyoloji_624': 'biyoloji',
    'biyoloji_642': 'biyoloji',
    'biyoloji_66': 'biyoloji',
    'biyoloji_660': 'biyoloji',
    'biyoloji_678': 'biyoloji',
    'biyoloji_696': 'biyoloji',
    'biyoloji_714': 'biyoloji',
    'biyoloji_732': 'biyoloji',
    'biyoloji_750': 'biyoloji',
    'biyoloji_768': 'biyoloji',
    'biyoloji_786': 'biyoloji',
    'biyoloji_804': 'biyoloji',
    'biyoloji_822': 'biyoloji',
    'biyoloji_84': 'biyoloji',
    'biyoloji_840': 'biyoloji',
    'biyoloji_858': 'biyoloji',
    'biyoloji_876': 'biyoloji',
    'biyoloji_894': 'biyoloji',
    'biyoloji_912': 'biyoloji',
    'biyoloji_930': 'biyoloji',
    'biyoloji_948': 'biyoloji',
    'biyoloji_966': 'biyoloji',
    'biyoloji_984': 'biyoloji',
    'bna': 'bana',
    'bnm': 'benim',
    'by': 'bay bay',
    'bır': 'bir',
    'cezerı': 'cezeri',
    'cok': 'cok',
    'coz_1012': 'coz',
    'coz_1030': 'coz',
    'coz_1048': 'coz',
    'coz_1066': 'coz',
    'coz_1084': 'coz',
    'coz_1102': 'coz',
    'coz_112': 'coz',
    'coz_1120': 'coz',
    'coz_1138': 'coz',
    'coz_1156': 'coz',
    'coz_1174': 'coz',
    'coz_1192': 'coz',
    'coz_1210': 'coz',
    'coz_1228': 'coz',
    'coz_1246': 'coz',
    'coz_1264': 'coz',
    'coz_1282': 'coz',
    'coz_130': 'coz',
    'coz_1300': 'coz',
    'coz_1318': 'coz',
    'coz_1336': 'coz',
    'coz_148': 'coz',
    'coz_166': 'coz',
    'coz_184': 'coz',
    'coz_202': 'coz',
    'coz_22': 'coz',
    'coz_220': 'coz',
    'coz_238': 'coz',
    'coz_256': 'coz',
    'coz_274': 'coz',
    'coz_292': 'coz',
    'coz_310': 'coz',
    'coz_328': 'coz',
    'coz_346': 'coz',
    'coz_364': 'coz',
    'coz_382': 'coz',
    'coz_4': 'coz',
    'coz_40': 'coz',
    'coz_400': 'coz',
    'coz_418': 'coz',
    'coz_436': 'coz',
    'coz_454': 'coz',
    'coz_472': 'coz',
    'coz_490': 'coz',
    'coz_508': 'coz',
    'coz_526': 'coz',
    'coz_544': 'coz',
    'coz_562': 'coz',
    'coz_58': 'coz',
    'coz_580': 'coz',
    'coz_598': 'coz',
    'coz_616': 'coz',
    'coz_634': 'coz',
    'coz_652': 'coz',
    'coz_670': 'coz',
    'coz_688': 'coz',
    'coz_706': 'coz',
    'coz_724': 'coz',
    'coz_742': 'coz',
    'coz_76': 'coz',
    'coz_760': 'coz',
    'coz_778': 'coz',
    'coz_796': 'coz',
    'coz_814': 'coz',
    'coz_832': 'coz',
    'coz_850': 'coz',
    'coz_868': 'coz',
    'coz_886': 'coz',
    'coz_904': 'coz',
    'coz_922': 'coz',
    'coz_94': 'coz',
    'coz_940': 'coz',
    'coz_958': 'coz',
    'coz_976': 'coz',
    'coz_994': 'coz',
    'drone_1016': 'drone',
    'drone_1034': 'drone',
    'drone_1052': 'drone',
    'drone_1070': 'drone',
    'drone_1088': 'drone',
    'drone_1106': 'drone',
    'drone_1124': 'drone',
    'drone_1142': 'drone',
    'drone_116': 'drone',
    'drone_1160': 'drone',
    'drone_1178': 'drone',
    'drone_1196': 'drone',
    'drone_1214': 'drone',
    'drone_1232': 'drone',
    'drone_1250': 'drone',
    'drone_1268': 'drone',
    'drone_1286': 'drone',
    'drone_1304': 'drone',
    'drone_1322': 'drone',
    'drone_134': 'drone',
    'drone_1340': 'drone',
    'drone_152': 'drone',
    'drone_170': 'drone',
    'drone_188': 'drone',
    'drone_206': 'drone',
    'drone_224': 'drone',
    'drone_242': 'drone',
    'drone_26': 'drone',
    'drone_260': 'drone',
    'drone_278': 'drone',
    'drone_296': 'drone',
    'drone_314': 'drone',
    'drone_332': 'drone',
    'drone_350': 'drone',
    'drone_368': 'drone',
    'drone_386': 'drone',
    'drone_404': 'drone',
    'drone_422': 'drone',
    'drone_44': 'drone',
    'drone_440': 'drone',
    'drone_458': 'drone',
    'drone_476': 'drone',
    'drone_494': 'drone',
    'drone_512': 'drone',
    'drone_530': 'drone',
    'drone_548': 'drone',
    'drone_566': 'drone',
    'drone_584': 'drone',
    'drone_602': 'drone',
    'drone_62': 'drone',
    'drone_620': 'drone',
    'drone_638': 'drone',
    'drone_656': 'drone',
    'drone_674': 'drone',
    'drone_692': 'drone',
    'drone_710': 'drone',
    'drone_728': 'drone',
    'drone_746': 'drone',
    'drone_764': 'drone',
    'drone_782': 'drone',
    'drone_8': 'drone',
    'drone_80': 'drone',
    'drone_800': 'drone',
    'drone_818': 'drone',
    'drone_836': 'drone',
    'drone_854': 'drone',
    'drone_872': 'drone',
    'drone_890': 'drone',
    'drone_908': 'drone',
    'drone_926': 'drone',
    'drone_944': 'drone',
    'drone_962': 'drone',
    'drone_98': 'drone',
    'drone_980': 'drone',
    'drone_998': 'drone',
    'ebob': 'ebob',
    'ekok': 'ekok',
    'eyv': 'eyvallah',
    'eyvallh': 'eyvallah',
    'eyvlh': 'eyvallah',
    'eyw': 'eyvallah',
    'fizik_10': 'fizik',
    'fizik_100': 'fizik',
    'fizik_1000': 'fizik',
    'fizik_1018': 'fizik',
    'fizik_1036': 'fizik',
    'fizik_1054': 'fizik',
    'fizik_1072': 'fizik',
    'fizik_1090': 'fizik',
    'fizik_1108': 'fizik',
    'fizik_1126': 'fizik',
    'fizik_1144': 'fizik',
    'fizik_1162': 'fizik',
    'fizik_118': 'fizik',
    'fizik_1180': 'fizik',
    'fizik_1198': 'fizik',
    'fizik_1216': 'fizik',
    'fizik_1234': 'fizik',
    'fizik_1252': 'fizik',
    'fizik_1270': 'fizik',
    'fizik_1288': 'fizik',
    'fizik_1306': 'fizik',
    'fizik_1324': 'fizik',
    'fizik_1342': 'fizik',
    'fizik_136': 'fizik',
    'fizik_154': 'fizik',
    'fizik_172': 'fizik',
    'fizik_190': 'fizik',
    'fizik_208': 'fizik',
    'fizik_226': 'fizik',
    'fizik_244': 'fizik',
    'fizik_262': 'fizik',
    'fizik_28': 'fizik',
    'fizik_280': 'fizik',
    'fizik_298': 'fizik',
    'fizik_316': 'fizik',
    'fizik_334': 'fizik',
    'fizik_352': 'fizik',
    'fizik_370': 'fizik',
    'fizik_388': 'fizik',
    'fizik_406': 'fizik',
    'fizik_424': 'fizik',
    'fizik_442': 'fizik',
    'fizik_46': 'fizik',
    'fizik_460': 'fizik',
    'fizik_478': 'fizik',
    'fizik_496': 'fizik',
    'fizik_514': 'fizik',
    'fizik_532': 'fizik',
    'fizik_550': 'fizik',
    'fizik_568': 'fizik',
    'fizik_586': 'fizik',
    'fizik_604': 'fizik',
    'fizik_622': 'fizik',
    'fizik_64': 'fizik',
    'fizik_640': 'fizik',
    'fizik_658': 'fizik',
    'fizik_676': 'fizik',
    'fizik_694': 'fizik',
    'fizik_712': 'fizik',
    'fizik_730': 'fizik',
    'fizik_748': 'fizik',
    'fizik_766': 'fizik',
    'fizik_784': 'fizik',
    'fizik_802': 'fizik',
    'fizik_82': 'fizik',
    'fizik_820': 'fizik',
    'fizik_838': 'fizik',
    'fizik_856': 'fizik',
    'fizik_874': 'fizik',
    'fizik_892': 'fizik',
    'fizik_910': 'fizik',
    'fizik_928': 'fizik',
    'fizik_946': 'fizik',
    'fizik_964': 'fizik',
    'fizik_982': 'fizik',
    'galatasaray_1003': 'galatasaray',
    'galatasaray_1021': 'galatasaray',
    'galatasaray_103': 'galatasaray',
    'galatasaray_1039': 'galatasaray',
    'galatasaray_1057': 'galatasaray',
    'galatasaray_1075': 'galatasaray',
    'galatasaray_1093': 'galatasaray',
    'galatasaray_1111': 'galatasaray',
    'galatasaray_1129': 'galatasaray',
    'galatasaray_1147': 'galatasaray',
    'galatasaray_1165': 'galatasaray',
    'galatasaray_1183': 'galatasaray',
    'galatasaray_1201': 'galatasaray',
    'galatasaray_121': 'galatasaray',
    'galatasaray_1219': 'galatasaray',
    'galatasaray_1237': 'galatasaray',
    'galatasaray_1255': 'galatasaray',
    'galatasaray_1273': 'galatasaray',
    'galatasaray_1291': 'galatasaray',
    'galatasaray_13': 'galatasaray',
    'galatasaray_1309': 'galatasaray',
    'galatasaray_1327': 'galatasaray',
    'galatasaray_1345': 'galatasaray',
    'galatasaray_139': 'galatasaray',
    'galatasaray_157': 'galatasaray',
    'galatasaray_175': 'galatasaray',
    'galatasaray_193': 'galatasaray',
    'galatasaray_211': 'galatasaray',
    'galatasaray_229': 'galatasaray',
    'galatasaray_247': 'galatasaray',
    'galatasaray_265': 'galatasaray',
    'galatasaray_283': 'galatasaray',
    'galatasaray_301': 'galatasaray',
    'galatasaray_31': 'galatasaray',
    'galatasaray_319': 'galatasaray',
    'galatasaray_337': 'galatasaray',
    'galatasaray_355': 'galatasaray',
    'galatasaray_373': 'galatasaray',
    'galatasaray_391': 'galatasaray',
    'galatasaray_409': 'galatasaray',
    'galatasaray_427': 'galatasaray',
    'galatasaray_445': 'galatasaray',
    'galatasaray_463': 'galatasaray',
    'galatasaray_481': 'galatasaray',
    'galatasaray_49': 'galatasaray',
    'galatasaray_499': 'galatasaray',
    'galatasaray_517': 'galatasaray',
    'galatasaray_535': 'galatasaray',
    'galatasaray_553': 'galatasaray',
    'galatasaray_571': 'galatasaray',
    'galatasaray_589': 'galatasaray',
    'galatasaray_607': 'galatasaray',
    'galatasaray_625': 'galatasaray',
    'galatasaray_643': 'galatasaray',
    'galatasaray_661': 'galatasaray',
    'galatasaray_67': 'galatasaray',
    'galatasaray_679': 'galatasaray',
    'galatasaray_697': 'galatasaray',
    'galatasaray_715': 'galatasaray',
    'galatasaray_733': 'galatasaray',
    'galatasaray_751': 'galatasaray',
    'galatasaray_769': 'galatasaray',
    'galatasaray_787': 'galatasaray',
    'galatasaray_805': 'galatasaray',
    'galatasaray_823': 'galatasaray',
    'galatasaray_841': 'galatasaray',
    'galatasaray_85': 'galatasaray',
    'galatasaray_859': 'galatasaray',
    'galatasaray_877': 'galatasaray',
    'galatasaray_895': 'galatasaray',
    'galatasaray_913': 'galatasaray',
    'galatasaray_931': 'galatasaray',
    'galatasaray_949': 'galatasaray',
    'galatasaray_967': 'galatasaray',
    'galatasaray_985': 'galatasaray',
    'gnaydın': 'gunaydin',
    'gnydn': 'gunaydin',
    'grsrz': 'gorusuruz',
    'görüşürz': 'gorusuruz',
    'hakimda': 'hakkimda',
    'hakkimd': 'hakkimda',
    'hakkmda': 'hakkimda',
    'harezmı': 'harezmi',
    'hesapla_1011': 'hesapla',
    'hesapla_1029': 'hesapla',
    'hesapla_1047': 'hesapla',
    'hesapla_1065': 'hesapla',
    'hesapla_1083': 'hesapla',
    'hesapla_1101': 'hesapla',
    'hesapla_111': 'hesapla',
    'hesapla_1119': 'hesapla',
    'hesapla_1137': 'hesapla',
    'hesapla_1155': 'hesapla',
    'hesapla_1173': 'hesapla',
    'hesapla_1191': 'hesapla',
    'hesapla_1209': 'hesapla',
    'hesapla_1227': 'hesapla',
    'hesapla_1245': 'hesapla',
    'hesapla_1263': 'hesapla',
    'hesapla_1281': 'hesapla',
    'hesapla_129': 'hesapla',
    'hesapla_1299': 'hesapla',
    'hesapla_1317': 'hesapla',
    'hesapla_1335': 'hesapla',
    'hesapla_147': 'hesapla',
    'hesapla_165': 'hesapla',
    'hesapla_183': 'hesapla',
    'hesapla_201': 'hesapla',
    'hesapla_21': 'hesapla',
    'hesapla_219': 'hesapla',
    'hesapla_237': 'hesapla',
    'hesapla_255': 'hesapla',
    'hesapla_273': 'hesapla',
    'hesapla_291': 'hesapla',
    'hesapla_3': 'hesapla',
    'hesapla_309': 'hesapla',
    'hesapla_327': 'hesapla',
    'hesapla_345': 'hesapla',
    'hesapla_363': 'hesapla',
    'hesapla_381': 'hesapla',
    'hesapla_39': 'hesapla',
    'hesapla_399': 'hesapla',
    'hesapla_417': 'hesapla',
    'hesapla_435': 'hesapla',
    'hesapla_453': 'hesapla',
    'hesapla_471': 'hesapla',
    'hesapla_489': 'hesapla',
    'hesapla_507': 'hesapla',
    'hesapla_525': 'hesapla',
    'hesapla_543': 'hesapla',
    'hesapla_561': 'hesapla',
    'hesapla_57': 'hesapla',
    'hesapla_579': 'hesapla',
    'hesapla_597': 'hesapla',
    'hesapla_615': 'hesapla',
    'hesapla_633': 'hesapla',
    'hesapla_651': 'hesapla',
    'hesapla_669': 'hesapla',
    'hesapla_687': 'hesapla',
    'hesapla_705': 'hesapla',
    'hesapla_723': 'hesapla',
    'hesapla_741': 'hesapla',
    'hesapla_75': 'hesapla',
    'hesapla_759': 'hesapla',
    'hesapla_777': 'hesapla',
    'hesapla_795': 'hesapla',
    'hesapla_813': 'hesapla',
    'hesapla_831': 'hesapla',
    'hesapla_849': 'hesapla',
    'hesapla_867': 'hesapla',
    'hesapla_885': 'hesapla',
    'hesapla_903': 'hesapla',
    'hesapla_921': 'hesapla',
    'hesapla_93': 'hesapla',
    'hesapla_939': 'hesapla',
    'hesapla_957': 'hesapla',
    'hesapla_975': 'hesapla',
    'hesapla_993': 'hesapla',
    'hkkmda': 'hakkimda',
    'ibnibattuta': 'ibni battuta',
    'ibnisina': 'ibni sina',
    'ii': 'iyi',
    'iy': 'iyi',
    'kac': 'kac',
    'kankam': 'kanka',
    'kanki': 'kanka',
    'kardesm': 'kardesim',
    'karekok': 'karekok',
    'kimsn': 'kimsin',
    'kimya_1001': 'kimya',
    'kimya_101': 'kimya',
    'kimya_1019': 'kimya',
    'kimya_1037': 'kimya',
    'kimya_1055': 'kimya',
    'kimya_1073': 'kimya',
    'kimya_1091': 'kimya',
    'kimya_11': 'kimya',
    'kimya_1109': 'kimya',
    'kimya_1127': 'kimya',
    'kimya_1145': 'kimya',
    'kimya_1163': 'kimya',
    'kimya_1181': 'kimya',
    'kimya_119': 'kimya',
    'kimya_1199': 'kimya',
    'kimya_1217': 'kimya',
    'kimya_1235': 'kimya',
    'kimya_1253': 'kimya',
    'kimya_1271': 'kimya',
    'kimya_1289': 'kimya',
    'kimya_1307': 'kimya',
    'kimya_1325': 'kimya',
    'kimya_1343': 'kimya',
    'kimya_137': 'kimya',
    'kimya_155': 'kimya',
    'kimya_173': 'kimya',
    'kimya_191': 'kimya',
    'kimya_209': 'kimya',
    'kimya_227': 'kimya',
    'kimya_245': 'kimya',
    'kimya_263': 'kimya',
    'kimya_281': 'kimya',
    'kimya_29': 'kimya',
    'kimya_299': 'kimya',
    'kimya_317': 'kimya',
    'kimya_335': 'kimya',
    'kimya_353': 'kimya',
    'kimya_371': 'kimya',
    'kimya_389': 'kimya',
    'kimya_407': 'kimya',
    'kimya_425': 'kimya',
    'kimya_443': 'kimya',
    'kimya_461': 'kimya',
    'kimya_47': 'kimya',
    'kimya_479': 'kimya',
    'kimya_497': 'kimya',
    'kimya_515': 'kimya',
    'kimya_533': 'kimya',
    'kimya_551': 'kimya',
    'kimya_569': 'kimya',
    'kimya_587': 'kimya',
    'kimya_605': 'kimya',
    'kimya_623': 'kimya',
    'kimya_641': 'kimya',
    'kimya_65': 'kimya',
    'kimya_659': 'kimya',
    'kimya_677': 'kimya',
    'kimya_695': 'kimya',
    'kimya_713': 'kimya',
    'kimya_731': 'kimya',
    'kimya_749': 'kimya',
    'kimya_767': 'kimya',
    'kimya_785': 'kimya',
    'kimya_803': 'kimya',
    'kimya_821': 'kimya',
    'kimya_83': 'kimya',
    'kimya_839': 'kimya',
    'kimya_857': 'kimya',
    'kimya_875': 'kimya',
    'kimya_893': 'kimya',
    'kimya_911': 'kimya',
    'kimya_929': 'kimya',
    'kimya_947': 'kimya',
    'kimya_965': 'kimya',
    'kimya_983': 'kimya',
    'kin': 'kim',
    'km': 'kim',
    'kmdr': 'kimdir',
    'kmsin': 'kimsin',
    'kmsn': 'kimsin',
    'knk': 'kanka',
    'knkm': 'kanka',
    'koklu': 'koklu',
    'krdesim': 'kardesim',
    'krdsm': 'kardesim',
    'krdşm': 'kardesim',
    'kım': 'kim',
    'kımde': 'kimdir',
    'kımsın': 'kimsin',
    'kın': 'kim',
    'matematik_1017': 'matematik',
    'matematik_1035': 'matematik',
    'matematik_1053': 'matematik',
    'matematik_1071': 'matematik',
    'matematik_1089': 'matematik',
    'matematik_1107': 'matematik',
    'matematik_1125': 'matematik',
    'matematik_1143': 'matematik',
    'matematik_1161': 'matematik',
    'matematik_117': 'matematik',
    'matematik_1179': 'matematik',
    'matematik_1197': 'matematik',
    'matematik_1215': 'matematik',
    'matematik_1233': 'matematik',
    'matematik_1251': 'matematik',
    'matematik_1269': 'matematik',
    'matematik_1287': 'matematik',
    'matematik_1305': 'matematik',
    'matematik_1323': 'matematik',
    'matematik_1341': 'matematik',
    'matematik_135': 'matematik',
    'matematik_153': 'matematik',
    'matematik_171': 'matematik',
    'matematik_189': 'matematik',
    'matematik_207': 'matematik',
    'matematik_225': 'matematik',
    'matematik_243': 'matematik',
    'matematik_261': 'matematik',
    'matematik_27': 'matematik',
    'matematik_279': 'matematik',
    'matematik_297': 'matematik',
    'matematik_315': 'matematik',
    'matematik_333': 'matematik',
    'matematik_351': 'matematik',
    'matematik_369': 'matematik',
    'matematik_387': 'matematik',
    'matematik_405': 'matematik',
    'matematik_423': 'matematik',
    'matematik_441': 'matematik',
    'matematik_45': 'matematik',
    'matematik_459': 'matematik',
    'matematik_477': 'matematik',
    'matematik_495': 'matematik',
    'matematik_513': 'matematik',
    'matematik_531': 'matematik',
    'matematik_549': 'matematik',
    'matematik_567': 'matematik',
    'matematik_585': 'matematik',
    'matematik_603': 'matematik',
    'matematik_621': 'matematik',
    'matematik_63': 'matematik',
    'matematik_639': 'matematik',
    'matematik_657': 'matematik',
    'matematik_675': 'matematik',
    'matematik_693': 'matematik',
    'matematik_711': 'matematik',
    'matematik_729': 'matematik',
    'matematik_747': 'matematik',
    'matematik_765': 'matematik',
    'matematik_783': 'matematik',
    'matematik_801': 'matematik',
    'matematik_81': 'matematik',
    'matematik_819': 'matematik',
    'matematik_837': 'matematik',
    'matematik_855': 'matematik',
    'matematik_873': 'matematik',
    'matematik_891': 'matematik',
    'matematik_9': 'matematik',
    'matematik_909': 'matematik',
    'matematik_927': 'matematik',
    'matematik_945': 'matematik',
    'matematik_963': 'matematik',
    'matematik_981': 'matematik',
    'matematik_99': 'matematik',
    'matematik_999': 'matematik',
    'meraba': 'merhaba',
    'mrb': 'merhaba',
    'mrbh': 'merhaba',
    'mrblar': 'merhaba',
    'mrhb': 'merhaba',
    'naberler': 'naber',
    'nabr': 'naber',
    'napion': 'ne yapiyorsun',
    'napiyon': 'ne yapiyorsun',
    'napiyosun': 'ne yapiyorsun',
    'napyon': 'ne yapiyorsun',
    'napıyon': 'ne yapiyorsun',
    'napıyosun': 'ne yapiyorsun',
    'nasilsn': 'nasilsin',
    'nasisin': 'nasilsin',
    'naslsn': 'nasilsin',
    'naslsın': 'nasilsin',
    'nassin': 'nasilsin',
    'nassın': 'nasilsin',
    'nasılsn': 'nasilsin',
    'nasılsınz': 'nasilsin',
    'nasısın': 'nasilsin',
    'nber': 'naber',
    'nbr': 'naber',
    'nbry': 'naber',
    'ndr': 'nedir',
    'neapıyon': 'ne yapiyorsun',
    'nedr': 'nedir',
    'nslsn': 'nasilsin',
    'nslsın': 'nasilsin',
    'ogret_1013': 'ogret',
    'ogret_1031': 'ogret',
    'ogret_1049': 'ogret',
    'ogret_1067': 'ogret',
    'ogret_1085': 'ogret',
    'ogret_1103': 'ogret',
    'ogret_1121': 'ogret',
    'ogret_113': 'ogret',
    'ogret_1139': 'ogret',
    'ogret_1157': 'ogret',
    'ogret_1175': 'ogret',
    'ogret_1193': 'ogret',
    'ogret_1211': 'ogret',
    'ogret_1229': 'ogret',
    'ogret_1247': 'ogret',
    'ogret_1265': 'ogret',
    'ogret_1283': 'ogret',
    'ogret_1301': 'ogret',
    'ogret_131': 'ogret',
    'ogret_1319': 'ogret',
    'ogret_1337': 'ogret',
    'ogret_149': 'ogret',
    'ogret_167': 'ogret',
    'ogret_185': 'ogret',
    'ogret_203': 'ogret',
    'ogret_221': 'ogret',
    'ogret_23': 'ogret',
    'ogret_239': 'ogret',
    'ogret_257': 'ogret',
    'ogret_275': 'ogret',
    'ogret_293': 'ogret',
    'ogret_311': 'ogret',
    'ogret_329': 'ogret',
    'ogret_347': 'ogret',
    'ogret_365': 'ogret',
    'ogret_383': 'ogret',
    'ogret_401': 'ogret',
    'ogret_41': 'ogret',
    'ogret_419': 'ogret',
    'ogret_437': 'ogret',
    'ogret_455': 'ogret',
    'ogret_473': 'ogret',
    'ogret_491': 'ogret',
    'ogret_5': 'ogret',
    'ogret_509': 'ogret',
    'ogret_527': 'ogret',
    'ogret_545': 'ogret',
    'ogret_563': 'ogret',
    'ogret_581': 'ogret',
    'ogret_59': 'ogret',
    'ogret_599': 'ogret',
    'ogret_617': 'ogret',
    'ogret_635': 'ogret',
    'ogret_653': 'ogret',
    'ogret_671': 'ogret',
    'ogret_689': 'ogret',
    'ogret_707': 'ogret',
    'ogret_725': 'ogret',
    'ogret_743': 'ogret',
    'ogret_761': 'ogret',
    'ogret_77': 'ogret',
    'ogret_779': 'ogret',
    'ogret_797': 'ogret',
    'ogret_815': 'ogret',
    'ogret_833': 'ogret',
    'ogret_851': 'ogret',
    'ogret_869': 'ogret',
    'ogret_887': 'ogret',
    'ogret_905': 'ogret',
    'ogret_923': 'ogret',
    'ogret_941': 'ogret',
    'ogret_95': 'ogret',
    'ogret_959': 'ogret',
    'ogret_977': 'ogret',
    'ogret_995': 'ogret',
    'ok': 'tamam',
    'okey': 'tamam',
    'proje_1015': 'projelerim',
    'proje_1033': 'projelerim',
    'proje_1051': 'projelerim',
    'proje_1069': 'projelerim',
    'proje_1087': 'projelerim',
    'proje_1105': 'projelerim',
    'proje_1123': 'projelerim',
    'proje_1141': 'projelerim',
    'proje_115': 'projelerim',
    'proje_1159': 'projelerim',
    'proje_1177': 'projelerim',
    'proje_1195': 'projelerim',
    'proje_1213': 'projelerim',
    'proje_1231': 'projelerim',
    'proje_1249': 'projelerim',
    'proje_1267': 'projelerim',
    'proje_1285': 'projelerim',
    'proje_1303': 'projelerim',
    'proje_1321': 'projelerim',
    'proje_133': 'projelerim',
    'proje_1339': 'projelerim',
    'proje_151': 'projelerim',
    'proje_169': 'projelerim',
    'proje_187': 'projelerim',
    'proje_205': 'projelerim',
    'proje_223': 'projelerim',
    'proje_241': 'projelerim',
    'proje_25': 'projelerim',
    'proje_259': 'projelerim',
    'proje_277': 'projelerim',
    'proje_295': 'projelerim',
    'proje_313': 'projelerim',
    'proje_331': 'projelerim',
    'proje_349': 'projelerim',
    'proje_367': 'projelerim',
    'proje_385': 'projelerim',
    'proje_403': 'projelerim',
    'proje_421': 'projelerim',
    'proje_43': 'projelerim',
    'proje_439': 'projelerim',
    'proje_457': 'projelerim',
    'proje_475': 'projelerim',
    'proje_493': 'projelerim',
    'proje_511': 'projelerim',
    'proje_529': 'projelerim',
    'proje_547': 'projelerim',
    'proje_565': 'projelerim',
    'proje_583': 'projelerim',
    'proje_601': 'projelerim',
    'proje_61': 'projelerim',
    'proje_619': 'projelerim',
    'proje_637': 'projelerim',
    'proje_655': 'projelerim',
    'proje_673': 'projelerim',
    'proje_691': 'projelerim',
    'proje_7': 'projelerim',
    'proje_709': 'projelerim',
    'proje_727': 'projelerim',
    'proje_745': 'projelerim',
    'proje_763': 'projelerim',
    'proje_781': 'projelerim',
    'proje_79': 'projelerim',
    'proje_799': 'projelerim',
    'proje_817': 'projelerim',
    'proje_835': 'projelerim',
    'proje_853': 'projelerim',
    'proje_871': 'projelerim',
    'proje_889': 'projelerim',
    'proje_907': 'projelerim',
    'proje_925': 'projelerim',
    'proje_943': 'projelerim',
    'proje_961': 'projelerim',
    'proje_97': 'projelerim',
    'proje_979': 'projelerim',
    'proje_997': 'projelerim',
    'python_1007': 'python',
    'python_1025': 'python',
    'python_1043': 'python',
    'python_1061': 'python',
    'python_107': 'python',
    'python_1079': 'python',
    'python_1097': 'python',
    'python_1115': 'python',
    'python_1133': 'python',
    'python_1151': 'python',
    'python_1169': 'python',
    'python_1187': 'python',
    'python_1205': 'python',
    'python_1223': 'python',
    'python_1241': 'python',
    'python_125': 'python',
    'python_1259': 'python',
    'python_1277': 'python',
    'python_1295': 'python',
    'python_1313': 'python',
    'python_1331': 'python',
    'python_1349': 'python',
    'python_143': 'python',
    'python_161': 'python',
    'python_17': 'python',
    'python_179': 'python',
    'python_197': 'python',
    'python_215': 'python',
    'python_233': 'python',
    'python_251': 'python',
    'python_269': 'python',
    'python_287': 'python',
    'python_305': 'python',
    'python_323': 'python',
    'python_341': 'python',
    'python_35': 'python',
    'python_359': 'python',
    'python_377': 'python',
    'python_395': 'python',
    'python_413': 'python',
    'python_431': 'python',
    'python_449': 'python',
    'python_467': 'python',
    'python_485': 'python',
    'python_503': 'python',
    'python_521': 'python',
    'python_53': 'python',
    'python_539': 'python',
    'python_557': 'python',
    'python_575': 'python',
    'python_593': 'python',
    'python_611': 'python',
    'python_629': 'python',
    'python_647': 'python',
    'python_665': 'python',
    'python_683': 'python',
    'python_701': 'python',
    'python_71': 'python',
    'python_719': 'python',
    'python_737': 'python',
    'python_755': 'python',
    'python_773': 'python',
    'python_791': 'python',
    'python_809': 'python',
    'python_827': 'python',
    'python_845': 'python',
    'python_863': 'python',
    'python_881': 'python',
    'python_89': 'python',
    'python_899': 'python',
    'python_917': 'python',
    'python_935': 'python',
    'python_953': 'python',
    'python_971': 'python',
    'python_989': 'python',
    's.a': 'selam',
    's.a.': 'selam',
    'sa': 'selam',
    'sagol': 'sag ol',
    'saol': 'sag ol',
    'saolasin': 'sag ol',
    'sağol': 'sag ol',
    'selamlar': 'selam',
    'selamm': 'selam',
    'selamunaleykum': 'selamun aleykum',
    'slm': 'selam',
    'slmlar': 'selam',
    'slmm': 'selam',
    'snn': 'senin',
    'streamlit_1008': 'streamlit',
    'streamlit_1026': 'streamlit',
    'streamlit_1044': 'streamlit',
    'streamlit_1062': 'streamlit',
    'streamlit_108': 'streamlit',
    'streamlit_1080': 'streamlit',
    'streamlit_1098': 'streamlit',
    'streamlit_1116': 'streamlit',
    'streamlit_1134': 'streamlit',
    'streamlit_1152': 'streamlit',
    'streamlit_1170': 'streamlit',
    'streamlit_1188': 'streamlit',
    'streamlit_1206': 'streamlit',
    'streamlit_1224': 'streamlit',
    'streamlit_1242': 'streamlit',
    'streamlit_126': 'streamlit',
    'streamlit_1260': 'streamlit',
    'streamlit_1278': 'streamlit',
    'streamlit_1296': 'streamlit',
    'streamlit_1314': 'streamlit',
    'streamlit_1332': 'streamlit',
    'streamlit_1350': 'streamlit',
    'streamlit_144': 'streamlit',
    'streamlit_162': 'streamlit',
    'streamlit_18': 'streamlit',
    'streamlit_180': 'streamlit',
    'streamlit_198': 'streamlit',
    'streamlit_216': 'streamlit',
    'streamlit_234': 'streamlit',
    'streamlit_252': 'streamlit',
    'streamlit_270': 'streamlit',
    'streamlit_288': 'streamlit',
    'streamlit_306': 'streamlit',
    'streamlit_324': 'streamlit',
    'streamlit_342': 'streamlit',
    'streamlit_36': 'streamlit',
    'streamlit_360': 'streamlit',
    'streamlit_378': 'streamlit',
    'streamlit_396': 'streamlit',
    'streamlit_414': 'streamlit',
    'streamlit_432': 'streamlit',
    'streamlit_450': 'streamlit',
    'streamlit_468': 'streamlit',
    'streamlit_486': 'streamlit',
    'streamlit_504': 'streamlit',
    'streamlit_522': 'streamlit',
    'streamlit_54': 'streamlit',
    'streamlit_540': 'streamlit',
    'streamlit_558': 'streamlit',
    'streamlit_576': 'streamlit',
    'streamlit_594': 'streamlit',
    'streamlit_612': 'streamlit',
    'streamlit_630': 'streamlit',
    'streamlit_648': 'streamlit',
    'streamlit_666': 'streamlit',
    'streamlit_684': 'streamlit',
    'streamlit_702': 'streamlit',
    'streamlit_72': 'streamlit',
    'streamlit_720': 'streamlit',
    'streamlit_738': 'streamlit',
    'streamlit_756': 'streamlit',
    'streamlit_774': 'streamlit',
    'streamlit_792': 'streamlit',
    'streamlit_810': 'streamlit',
    'streamlit_828': 'streamlit',
    'streamlit_846': 'streamlit',
    'streamlit_864': 'streamlit',
    'streamlit_882': 'streamlit',
    'streamlit_90': 'streamlit',
    'streamlit_900': 'streamlit',
    'streamlit_918': 'streamlit',
    'streamlit_936': 'streamlit',
    'streamlit_954': 'streamlit',
    'streamlit_972': 'streamlit',
    'streamlit_990': 'streamlit',
    'teknofest_1004': 'teknofest',
    'teknofest_1022': 'teknofest',
    'teknofest_104': 'teknofest',
    'teknofest_1040': 'teknofest',
    'teknofest_1058': 'teknofest',
    'teknofest_1076': 'teknofest',
    'teknofest_1094': 'teknofest',
    'teknofest_1112': 'teknofest',
    'teknofest_1130': 'teknofest',
    'teknofest_1148': 'teknofest',
    'teknofest_1166': 'teknofest',
    'teknofest_1184': 'teknofest',
    'teknofest_1202': 'teknofest',
    'teknofest_122': 'teknofest',
    'teknofest_1220': 'teknofest',
    'teknofest_1238': 'teknofest',
    'teknofest_1256': 'teknofest',
    'teknofest_1274': 'teknofest',
    'teknofest_1292': 'teknofest',
    'teknofest_1310': 'teknofest',
    'teknofest_1328': 'teknofest',
    'teknofest_1346': 'teknofest',
    'teknofest_14': 'teknofest',
    'teknofest_140': 'teknofest',
    'teknofest_158': 'teknofest',
    'teknofest_176': 'teknofest',
    'teknofest_194': 'teknofest',
    'teknofest_212': 'teknofest',
    'teknofest_230': 'teknofest',
    'teknofest_248': 'teknofest',
    'teknofest_266': 'teknofest',
    'teknofest_284': 'teknofest',
    'teknofest_302': 'teknofest',
    'teknofest_32': 'teknofest',
    'teknofest_320': 'teknofest',
    'teknofest_338': 'teknofest',
    'teknofest_356': 'teknofest',
    'teknofest_374': 'teknofest',
    'teknofest_392': 'teknofest',
    'teknofest_410': 'teknofest',
    'teknofest_428': 'teknofest',
    'teknofest_446': 'teknofest',
    'teknofest_464': 'teknofest',
    'teknofest_482': 'teknofest',
    'teknofest_50': 'teknofest',
    'teknofest_500': 'teknofest',
    'teknofest_518': 'teknofest',
    'teknofest_536': 'teknofest',
    'teknofest_554': 'teknofest',
    'teknofest_572': 'teknofest',
    'teknofest_590': 'teknofest',
    'teknofest_608': 'teknofest',
    'teknofest_626': 'teknofest',
    'teknofest_644': 'teknofest',
    'teknofest_662': 'teknofest',
    'teknofest_68': 'teknofest',
    'teknofest_680': 'teknofest',
    'teknofest_698': 'teknofest',
    'teknofest_716': 'teknofest',
    'teknofest_734': 'teknofest',
    'teknofest_752': 'teknofest',
    'teknofest_770': 'teknofest',
    'teknofest_788': 'teknofest',
    'teknofest_806': 'teknofest',
    'teknofest_824': 'teknofest',
    'teknofest_842': 'teknofest',
    'teknofest_86': 'teknofest',
    'teknofest_860': 'teknofest',
    'teknofest_878': 'teknofest',
    'teknofest_896': 'teknofest',
    'teknofest_914': 'teknofest',
    'teknofest_932': 'teknofest',
    'teknofest_950': 'teknofest',
    'teknofest_968': 'teknofest',
    'teknofest_986': 'teknofest',
    'tesekkurler': 'tesekkur',
    'tm': 'tamam',
    'tmm': 'tamam',
    'tsk': 'tesekkur',
    'tskr': 'tesekkur',
    'tubitak_1005': 'tubitak',
    'tubitak_1023': 'tubitak',
    'tubitak_1041': 'tubitak',
    'tubitak_105': 'tubitak',
    'tubitak_1059': 'tubitak',
    'tubitak_1077': 'tubitak',
    'tubitak_1095': 'tubitak',
    'tubitak_1113': 'tubitak',
    'tubitak_1131': 'tubitak',
    'tubitak_1149': 'tubitak',
    'tubitak_1167': 'tubitak',
    'tubitak_1185': 'tubitak',
    'tubitak_1203': 'tubitak',
    'tubitak_1221': 'tubitak',
    'tubitak_123': 'tubitak',
    'tubitak_1239': 'tubitak',
    'tubitak_1257': 'tubitak',
    'tubitak_1275': 'tubitak',
    'tubitak_1293': 'tubitak',
    'tubitak_1311': 'tubitak',
    'tubitak_1329': 'tubitak',
    'tubitak_1347': 'tubitak',
    'tubitak_141': 'tubitak',
    'tubitak_15': 'tubitak',
    'tubitak_159': 'tubitak',
    'tubitak_177': 'tubitak',
    'tubitak_195': 'tubitak',
    'tubitak_213': 'tubitak',
    'tubitak_231': 'tubitak',
    'tubitak_249': 'tubitak',
    'tubitak_267': 'tubitak',
    'tubitak_285': 'tubitak',
    'tubitak_303': 'tubitak',
    'tubitak_321': 'tubitak',
    'tubitak_33': 'tubitak',
    'tubitak_339': 'tubitak',
    'tubitak_357': 'tubitak',
    'tubitak_375': 'tubitak',
    'tubitak_393': 'tubitak',
    'tubitak_411': 'tubitak',
    'tubitak_429': 'tubitak',
    'tubitak_447': 'tubitak',
    'tubitak_465': 'tubitak',
    'tubitak_483': 'tubitak',
    'tubitak_501': 'tubitak',
    'tubitak_51': 'tubitak',
    'tubitak_519': 'tubitak',
    'tubitak_537': 'tubitak',
    'tubitak_555': 'tubitak',
    'tubitak_573': 'tubitak',
    'tubitak_591': 'tubitak',
    'tubitak_609': 'tubitak',
    'tubitak_627': 'tubitak',
    'tubitak_645': 'tubitak',
    'tubitak_663': 'tubitak',
    'tubitak_681': 'tubitak',
    'tubitak_69': 'tubitak',
    'tubitak_699': 'tubitak',
    'tubitak_717': 'tubitak',
    'tubitak_735': 'tubitak',
    'tubitak_753': 'tubitak',
    'tubitak_771': 'tubitak',
    'tubitak_789': 'tubitak',
    'tubitak_807': 'tubitak',
    'tubitak_825': 'tubitak',
    'tubitak_843': 'tubitak',
    'tubitak_861': 'tubitak',
    'tubitak_87': 'tubitak',
    'tubitak_879': 'tubitak',
    'tubitak_897': 'tubitak',
    'tubitak_915': 'tubitak',
    'tubitak_933': 'tubitak',
    'tubitak_951': 'tubitak',
    'tubitak_969': 'tubitak',
    'tubitak_987': 'tubitak',
    'tşk': 'tesekkur',
    'uslu': 'uslu',
    'yardim_1014': 'yardim',
    'yardim_1032': 'yardim',
    'yardim_1050': 'yardim',
    'yardim_1068': 'yardim',
    'yardim_1086': 'yardim',
    'yardim_1104': 'yardim',
    'yardim_1122': 'yardim',
    'yardim_114': 'yardim',
    'yardim_1140': 'yardim',
    'yardim_1158': 'yardim',
    'yardim_1176': 'yardim',
    'yardim_1194': 'yardim',
    'yardim_1212': 'yardim',
    'yardim_1230': 'yardim',
    'yardim_1248': 'yardim',
    'yardim_1266': 'yardim',
    'yardim_1284': 'yardim',
    'yardim_1302': 'yardim',
    'yardim_132': 'yardim',
    'yardim_1320': 'yardim',
    'yardim_1338': 'yardim',
    'yardim_150': 'yardim',
    'yardim_168': 'yardim',
    'yardim_186': 'yardim',
    'yardim_204': 'yardim',
    'yardim_222': 'yardim',
    'yardim_24': 'yardim',
    'yardim_240': 'yardim',
    'yardim_258': 'yardim',
    'yardim_276': 'yardim',
    'yardim_294': 'yardim',
    'yardim_312': 'yardim',
    'yardim_330': 'yardim',
    'yardim_348': 'yardim',
    'yardim_366': 'yardim',
    'yardim_384': 'yardim',
    'yardim_402': 'yardim',
    'yardim_42': 'yardim',
    'yardim_420': 'yardim',
    'yardim_438': 'yardim',
    'yardim_456': 'yardim',
    'yardim_474': 'yardim',
    'yardim_492': 'yardim',
    'yardim_510': 'yardim',
    'yardim_528': 'yardim',
    'yardim_546': 'yardim',
    'yardim_564': 'yardim',
    'yardim_582': 'yardim',
    'yardim_6': 'yardim',
    'yardim_60': 'yardim',
    'yardim_600': 'yardim',
    'yardim_618': 'yardim',
    'yardim_636': 'yardim',
    'yardim_654': 'yardim',
    'yardim_672': 'yardim',
    'yardim_690': 'yardim',
    'yardim_708': 'yardim',
    'yardim_726': 'yardim',
    'yardim_744': 'yardim',
    'yardim_762': 'yardim',
    'yardim_78': 'yardim',
    'yardim_780': 'yardim',
    'yardim_798': 'yardim',
    'yardim_816': 'yardim',
    'yardim_834': 'yardim',
    'yardim_852': 'yardim',
    'yardim_870': 'yardim',
    'yardim_888': 'yardim',
    'yardim_906': 'yardim',
    'yardim_924': 'yardim',
    'yardim_942': 'yardim',
    'yardim_96': 'yardim',
    'yardim_960': 'yardim',
    'yardim_978': 'yardim',
    'yardim_996': 'yardim',
    'çk': 'cok'}

DUYGU_VE_SOHBET_SABLONLARI = {   'ders_calisma_004': {   'tetikleyiciler': [   'ders çalışıyorum',
                                                  'sınava hazırlanıyorum',
                                                  'matematik çalışıyorum',
                                                  'ödev yapıyorum'],
                            'yanit': 'Kolay gelsin Ahmet! 📚 Takıldığın herhangi bir köklü sayı, '
                                     'üslü sayı, denklem veya fen konusu olursa hemen bana sor, '
                                     'adım adım çözelim.'},
    'ders_calisma_012': {   'tetikleyiciler': [   'ders çalışıyorum',
                                                  'sınava hazırlanıyorum',
                                                  'matematik çalışıyorum',
                                                  'ödev yapıyorum'],
                            'yanit': 'Kolay gelsin Ahmet! 📚 Takıldığın herhangi bir köklü sayı, '
                                     'üslü sayı, denklem veya fen konusu olursa hemen bana sor, '
                                     'adım adım çözelim.'},
    'ders_calisma_020': {   'tetikleyiciler': [   'ders çalışıyorum',
                                                  'sınava hazırlanıyorum',
                                                  'matematik çalışıyorum',
                                                  'ödev yapıyorum'],
                            'yanit': 'Kolay gelsin Ahmet! 📚 Takıldığın herhangi bir köklü sayı, '
                                     'üslü sayı, denklem veya fen konusu olursa hemen bana sor, '
                                     'adım adım çözelim.'},
    'ders_calisma_028': {   'tetikleyiciler': [   'ders çalışıyorum',
                                                  'sınava hazırlanıyorum',
                                                  'matematik çalışıyorum',
                                                  'ödev yapıyorum'],
                            'yanit': 'Kolay gelsin Ahmet! 📚 Takıldığın herhangi bir köklü sayı, '
                                     'üslü sayı, denklem veya fen konusu olursa hemen bana sor, '
                                     'adım adım çözelim.'},
    'ders_calisma_036': {   'tetikleyiciler': [   'ders çalışıyorum',
                                                  'sınava hazırlanıyorum',
                                                  'matematik çalışıyorum',
                                                  'ödev yapıyorum'],
                            'yanit': 'Kolay gelsin Ahmet! 📚 Takıldığın herhangi bir köklü sayı, '
                                     'üslü sayı, denklem veya fen konusu olursa hemen bana sor, '
                                     'adım adım çözelim.'},
    'ders_calisma_044': {   'tetikleyiciler': [   'ders çalışıyorum',
                                                  'sınava hazırlanıyorum',
                                                  'matematik çalışıyorum',
                                                  'ödev yapıyorum'],
                            'yanit': 'Kolay gelsin Ahmet! 📚 Takıldığın herhangi bir köklü sayı, '
                                     'üslü sayı, denklem veya fen konusu olursa hemen bana sor, '
                                     'adım adım çözelim.'},
    'ders_calisma_052': {   'tetikleyiciler': [   'ders çalışıyorum',
                                                  'sınava hazırlanıyorum',
                                                  'matematik çalışıyorum',
                                                  'ödev yapıyorum'],
                            'yanit': 'Kolay gelsin Ahmet! 📚 Takıldığın herhangi bir köklü sayı, '
                                     'üslü sayı, denklem veya fen konusu olursa hemen bana sor, '
                                     'adım adım çözelim.'},
    'ders_calisma_060': {   'tetikleyiciler': [   'ders çalışıyorum',
                                                  'sınava hazırlanıyorum',
                                                  'matematik çalışıyorum',
                                                  'ödev yapıyorum'],
                            'yanit': 'Kolay gelsin Ahmet! 📚 Takıldığın herhangi bir köklü sayı, '
                                     'üslü sayı, denklem veya fen konusu olursa hemen bana sor, '
                                     'adım adım çözelim.'},
    'ders_calisma_068': {   'tetikleyiciler': [   'ders çalışıyorum',
                                                  'sınava hazırlanıyorum',
                                                  'matematik çalışıyorum',
                                                  'ödev yapıyorum'],
                            'yanit': 'Kolay gelsin Ahmet! 📚 Takıldığın herhangi bir köklü sayı, '
                                     'üslü sayı, denklem veya fen konusu olursa hemen bana sor, '
                                     'adım adım çözelim.'},
    'ders_calisma_076': {   'tetikleyiciler': [   'ders çalışıyorum',
                                                  'sınava hazırlanıyorum',
                                                  'matematik çalışıyorum',
                                                  'ödev yapıyorum'],
                            'yanit': 'Kolay gelsin Ahmet! 📚 Takıldığın herhangi bir köklü sayı, '
                                     'üslü sayı, denklem veya fen konusu olursa hemen bana sor, '
                                     'adım adım çözelim.'},
    'ders_calisma_084': {   'tetikleyiciler': [   'ders çalışıyorum',
                                                  'sınava hazırlanıyorum',
                                                  'matematik çalışıyorum',
                                                  'ödev yapıyorum'],
                            'yanit': 'Kolay gelsin Ahmet! 📚 Takıldığın herhangi bir köklü sayı, '
                                     'üslü sayı, denklem veya fen konusu olursa hemen bana sor, '
                                     'adım adım çözelim.'},
    'ders_calisma_092': {   'tetikleyiciler': [   'ders çalışıyorum',
                                                  'sınava hazırlanıyorum',
                                                  'matematik çalışıyorum',
                                                  'ödev yapıyorum'],
                            'yanit': 'Kolay gelsin Ahmet! 📚 Takıldığın herhangi bir köklü sayı, '
                                     'üslü sayı, denklem veya fen konusu olursa hemen bana sor, '
                                     'adım adım çözelim.'},
    'ders_calisma_100': {   'tetikleyiciler': [   'ders çalışıyorum',
                                                  'sınava hazırlanıyorum',
                                                  'matematik çalışıyorum',
                                                  'ödev yapıyorum'],
                            'yanit': 'Kolay gelsin Ahmet! 📚 Takıldığın herhangi bir köklü sayı, '
                                     'üslü sayı, denklem veya fen konusu olursa hemen bana sor, '
                                     'adım adım çözelim.'},
    'ders_calisma_108': {   'tetikleyiciler': [   'ders çalışıyorum',
                                                  'sınava hazırlanıyorum',
                                                  'matematik çalışıyorum',
                                                  'ödev yapıyorum'],
                            'yanit': 'Kolay gelsin Ahmet! 📚 Takıldığın herhangi bir köklü sayı, '
                                     'üslü sayı, denklem veya fen konusu olursa hemen bana sor, '
                                     'adım adım çözelim.'},
    'ders_calisma_116': {   'tetikleyiciler': [   'ders çalışıyorum',
                                                  'sınava hazırlanıyorum',
                                                  'matematik çalışıyorum',
                                                  'ödev yapıyorum'],
                            'yanit': 'Kolay gelsin Ahmet! 📚 Takıldığın herhangi bir köklü sayı, '
                                     'üslü sayı, denklem veya fen konusu olursa hemen bana sor, '
                                     'adım adım çözelim.'},
    'ders_calisma_124': {   'tetikleyiciler': [   'ders çalışıyorum',
                                                  'sınava hazırlanıyorum',
                                                  'matematik çalışıyorum',
                                                  'ödev yapıyorum'],
                            'yanit': 'Kolay gelsin Ahmet! 📚 Takıldığın herhangi bir köklü sayı, '
                                     'üslü sayı, denklem veya fen konusu olursa hemen bana sor, '
                                     'adım adım çözelim.'},
    'ders_calisma_132': {   'tetikleyiciler': [   'ders çalışıyorum',
                                                  'sınava hazırlanıyorum',
                                                  'matematik çalışıyorum',
                                                  'ödev yapıyorum'],
                            'yanit': 'Kolay gelsin Ahmet! 📚 Takıldığın herhangi bir köklü sayı, '
                                     'üslü sayı, denklem veya fen konusu olursa hemen bana sor, '
                                     'adım adım çözelim.'},
    'ders_calisma_140': {   'tetikleyiciler': [   'ders çalışıyorum',
                                                  'sınava hazırlanıyorum',
                                                  'matematik çalışıyorum',
                                                  'ödev yapıyorum'],
                            'yanit': 'Kolay gelsin Ahmet! 📚 Takıldığın herhangi bir köklü sayı, '
                                     'üslü sayı, denklem veya fen konusu olursa hemen bana sor, '
                                     'adım adım çözelim.'},
    'ders_calisma_148': {   'tetikleyiciler': [   'ders çalışıyorum',
                                                  'sınava hazırlanıyorum',
                                                  'matematik çalışıyorum',
                                                  'ödev yapıyorum'],
                            'yanit': 'Kolay gelsin Ahmet! 📚 Takıldığın herhangi bir köklü sayı, '
                                     'üslü sayı, denklem veya fen konusu olursa hemen bana sor, '
                                     'adım adım çözelim.'},
    'ders_calisma_156': {   'tetikleyiciler': [   'ders çalışıyorum',
                                                  'sınava hazırlanıyorum',
                                                  'matematik çalışıyorum',
                                                  'ödev yapıyorum'],
                            'yanit': 'Kolay gelsin Ahmet! 📚 Takıldığın herhangi bir köklü sayı, '
                                     'üslü sayı, denklem veya fen konusu olursa hemen bana sor, '
                                     'adım adım çözelim.'},
    'ders_calisma_164': {   'tetikleyiciler': [   'ders çalışıyorum',
                                                  'sınava hazırlanıyorum',
                                                  'matematik çalışıyorum',
                                                  'ödev yapıyorum'],
                            'yanit': 'Kolay gelsin Ahmet! 📚 Takıldığın herhangi bir köklü sayı, '
                                     'üslü sayı, denklem veya fen konusu olursa hemen bana sor, '
                                     'adım adım çözelim.'},
    'ders_calisma_172': {   'tetikleyiciler': [   'ders çalışıyorum',
                                                  'sınava hazırlanıyorum',
                                                  'matematik çalışıyorum',
                                                  'ödev yapıyorum'],
                            'yanit': 'Kolay gelsin Ahmet! 📚 Takıldığın herhangi bir köklü sayı, '
                                     'üslü sayı, denklem veya fen konusu olursa hemen bana sor, '
                                     'adım adım çözelim.'},
    'ders_calisma_180': {   'tetikleyiciler': [   'ders çalışıyorum',
                                                  'sınava hazırlanıyorum',
                                                  'matematik çalışıyorum',
                                                  'ödev yapıyorum'],
                            'yanit': 'Kolay gelsin Ahmet! 📚 Takıldığın herhangi bir köklü sayı, '
                                     'üslü sayı, denklem veya fen konusu olursa hemen bana sor, '
                                     'adım adım çözelim.'},
    'ders_calisma_188': {   'tetikleyiciler': [   'ders çalışıyorum',
                                                  'sınava hazırlanıyorum',
                                                  'matematik çalışıyorum',
                                                  'ödev yapıyorum'],
                            'yanit': 'Kolay gelsin Ahmet! 📚 Takıldığın herhangi bir köklü sayı, '
                                     'üslü sayı, denklem veya fen konusu olursa hemen bana sor, '
                                     'adım adım çözelim.'},
    'ders_calisma_196': {   'tetikleyiciler': [   'ders çalışıyorum',
                                                  'sınava hazırlanıyorum',
                                                  'matematik çalışıyorum',
                                                  'ödev yapıyorum'],
                            'yanit': 'Kolay gelsin Ahmet! 📚 Takıldığın herhangi bir köklü sayı, '
                                     'üslü sayı, denklem veya fen konusu olursa hemen bana sor, '
                                     'adım adım çözelim.'},
    'ders_calisma_204': {   'tetikleyiciler': [   'ders çalışıyorum',
                                                  'sınava hazırlanıyorum',
                                                  'matematik çalışıyorum',
                                                  'ödev yapıyorum'],
                            'yanit': 'Kolay gelsin Ahmet! 📚 Takıldığın herhangi bir köklü sayı, '
                                     'üslü sayı, denklem veya fen konusu olursa hemen bana sor, '
                                     'adım adım çözelim.'},
    'ders_calisma_212': {   'tetikleyiciler': [   'ders çalışıyorum',
                                                  'sınava hazırlanıyorum',
                                                  'matematik çalışıyorum',
                                                  'ödev yapıyorum'],
                            'yanit': 'Kolay gelsin Ahmet! 📚 Takıldığın herhangi bir köklü sayı, '
                                     'üslü sayı, denklem veya fen konusu olursa hemen bana sor, '
                                     'adım adım çözelim.'},
    'ders_calisma_220': {   'tetikleyiciler': [   'ders çalışıyorum',
                                                  'sınava hazırlanıyorum',
                                                  'matematik çalışıyorum',
                                                  'ödev yapıyorum'],
                            'yanit': 'Kolay gelsin Ahmet! 📚 Takıldığın herhangi bir köklü sayı, '
                                     'üslü sayı, denklem veya fen konusu olursa hemen bana sor, '
                                     'adım adım çözelim.'},
    'ders_calisma_228': {   'tetikleyiciler': [   'ders çalışıyorum',
                                                  'sınava hazırlanıyorum',
                                                  'matematik çalışıyorum',
                                                  'ödev yapıyorum'],
                            'yanit': 'Kolay gelsin Ahmet! 📚 Takıldığın herhangi bir köklü sayı, '
                                     'üslü sayı, denklem veya fen konusu olursa hemen bana sor, '
                                     'adım adım çözelim.'},
    'ders_calisma_236': {   'tetikleyiciler': [   'ders çalışıyorum',
                                                  'sınava hazırlanıyorum',
                                                  'matematik çalışıyorum',
                                                  'ödev yapıyorum'],
                            'yanit': 'Kolay gelsin Ahmet! 📚 Takıldığın herhangi bir köklü sayı, '
                                     'üslü sayı, denklem veya fen konusu olursa hemen bana sor, '
                                     'adım adım çözelim.'},
    'ders_calisma_244': {   'tetikleyiciler': [   'ders çalışıyorum',
                                                  'sınava hazırlanıyorum',
                                                  'matematik çalışıyorum',
                                                  'ödev yapıyorum'],
                            'yanit': 'Kolay gelsin Ahmet! 📚 Takıldığın herhangi bir köklü sayı, '
                                     'üslü sayı, denklem veya fen konusu olursa hemen bana sor, '
                                     'adım adım çözelim.'},
    'ders_calisma_252': {   'tetikleyiciler': [   'ders çalışıyorum',
                                                  'sınava hazırlanıyorum',
                                                  'matematik çalışıyorum',
                                                  'ödev yapıyorum'],
                            'yanit': 'Kolay gelsin Ahmet! 📚 Takıldığın herhangi bir köklü sayı, '
                                     'üslü sayı, denklem veya fen konusu olursa hemen bana sor, '
                                     'adım adım çözelim.'},
    'ders_calisma_260': {   'tetikleyiciler': [   'ders çalışıyorum',
                                                  'sınava hazırlanıyorum',
                                                  'matematik çalışıyorum',
                                                  'ödev yapıyorum'],
                            'yanit': 'Kolay gelsin Ahmet! 📚 Takıldığın herhangi bir köklü sayı, '
                                     'üslü sayı, denklem veya fen konusu olursa hemen bana sor, '
                                     'adım adım çözelim.'},
    'ders_calisma_268': {   'tetikleyiciler': [   'ders çalışıyorum',
                                                  'sınava hazırlanıyorum',
                                                  'matematik çalışıyorum',
                                                  'ödev yapıyorum'],
                            'yanit': 'Kolay gelsin Ahmet! 📚 Takıldığın herhangi bir köklü sayı, '
                                     'üslü sayı, denklem veya fen konusu olursa hemen bana sor, '
                                     'adım adım çözelim.'},
    'ders_calisma_276': {   'tetikleyiciler': [   'ders çalışıyorum',
                                                  'sınava hazırlanıyorum',
                                                  'matematik çalışıyorum',
                                                  'ödev yapıyorum'],
                            'yanit': 'Kolay gelsin Ahmet! 📚 Takıldığın herhangi bir köklü sayı, '
                                     'üslü sayı, denklem veya fen konusu olursa hemen bana sor, '
                                     'adım adım çözelim.'},
    'gece_calismasi_008': {   'tetikleyiciler': [   'uykum geldi',
                                                    'gece oldu',
                                                    'yatıyorum',
                                                    'sabah erken kalkacağım'],
                              'yanit': 'İyi geceler Ahmet! 🌙 21:00 – 04:00 uyku düzenini koruman '
                                       'zihinsel performansın ve 100m antrenmanların için çok '
                                       'önemli. Dinlen, yarın devam ederiz!'},
    'gece_calismasi_016': {   'tetikleyiciler': [   'uykum geldi',
                                                    'gece oldu',
                                                    'yatıyorum',
                                                    'sabah erken kalkacağım'],
                              'yanit': 'İyi geceler Ahmet! 🌙 21:00 – 04:00 uyku düzenini koruman '
                                       'zihinsel performansın ve 100m antrenmanların için çok '
                                       'önemli. Dinlen, yarın devam ederiz!'},
    'gece_calismasi_024': {   'tetikleyiciler': [   'uykum geldi',
                                                    'gece oldu',
                                                    'yatıyorum',
                                                    'sabah erken kalkacağım'],
                              'yanit': 'İyi geceler Ahmet! 🌙 21:00 – 04:00 uyku düzenini koruman '
                                       'zihinsel performansın ve 100m antrenmanların için çok '
                                       'önemli. Dinlen, yarın devam ederiz!'},
    'gece_calismasi_032': {   'tetikleyiciler': [   'uykum geldi',
                                                    'gece oldu',
                                                    'yatıyorum',
                                                    'sabah erken kalkacağım'],
                              'yanit': 'İyi geceler Ahmet! 🌙 21:00 – 04:00 uyku düzenini koruman '
                                       'zihinsel performansın ve 100m antrenmanların için çok '
                                       'önemli. Dinlen, yarın devam ederiz!'},
    'gece_calismasi_040': {   'tetikleyiciler': [   'uykum geldi',
                                                    'gece oldu',
                                                    'yatıyorum',
                                                    'sabah erken kalkacağım'],
                              'yanit': 'İyi geceler Ahmet! 🌙 21:00 – 04:00 uyku düzenini koruman '
                                       'zihinsel performansın ve 100m antrenmanların için çok '
                                       'önemli. Dinlen, yarın devam ederiz!'},
    'gece_calismasi_048': {   'tetikleyiciler': [   'uykum geldi',
                                                    'gece oldu',
                                                    'yatıyorum',
                                                    'sabah erken kalkacağım'],
                              'yanit': 'İyi geceler Ahmet! 🌙 21:00 – 04:00 uyku düzenini koruman '
                                       'zihinsel performansın ve 100m antrenmanların için çok '
                                       'önemli. Dinlen, yarın devam ederiz!'},
    'gece_calismasi_056': {   'tetikleyiciler': [   'uykum geldi',
                                                    'gece oldu',
                                                    'yatıyorum',
                                                    'sabah erken kalkacağım'],
                              'yanit': 'İyi geceler Ahmet! 🌙 21:00 – 04:00 uyku düzenini koruman '
                                       'zihinsel performansın ve 100m antrenmanların için çok '
                                       'önemli. Dinlen, yarın devam ederiz!'},
    'gece_calismasi_064': {   'tetikleyiciler': [   'uykum geldi',
                                                    'gece oldu',
                                                    'yatıyorum',
                                                    'sabah erken kalkacağım'],
                              'yanit': 'İyi geceler Ahmet! 🌙 21:00 – 04:00 uyku düzenini koruman '
                                       'zihinsel performansın ve 100m antrenmanların için çok '
                                       'önemli. Dinlen, yarın devam ederiz!'},
    'gece_calismasi_072': {   'tetikleyiciler': [   'uykum geldi',
                                                    'gece oldu',
                                                    'yatıyorum',
                                                    'sabah erken kalkacağım'],
                              'yanit': 'İyi geceler Ahmet! 🌙 21:00 – 04:00 uyku düzenini koruman '
                                       'zihinsel performansın ve 100m antrenmanların için çok '
                                       'önemli. Dinlen, yarın devam ederiz!'},
    'gece_calismasi_080': {   'tetikleyiciler': [   'uykum geldi',
                                                    'gece oldu',
                                                    'yatıyorum',
                                                    'sabah erken kalkacağım'],
                              'yanit': 'İyi geceler Ahmet! 🌙 21:00 – 04:00 uyku düzenini koruman '
                                       'zihinsel performansın ve 100m antrenmanların için çok '
                                       'önemli. Dinlen, yarın devam ederiz!'},
    'gece_calismasi_088': {   'tetikleyiciler': [   'uykum geldi',
                                                    'gece oldu',
                                                    'yatıyorum',
                                                    'sabah erken kalkacağım'],
                              'yanit': 'İyi geceler Ahmet! 🌙 21:00 – 04:00 uyku düzenini koruman '
                                       'zihinsel performansın ve 100m antrenmanların için çok '
                                       'önemli. Dinlen, yarın devam ederiz!'},
    'gece_calismasi_096': {   'tetikleyiciler': [   'uykum geldi',
                                                    'gece oldu',
                                                    'yatıyorum',
                                                    'sabah erken kalkacağım'],
                              'yanit': 'İyi geceler Ahmet! 🌙 21:00 – 04:00 uyku düzenini koruman '
                                       'zihinsel performansın ve 100m antrenmanların için çok '
                                       'önemli. Dinlen, yarın devam ederiz!'},
    'gece_calismasi_104': {   'tetikleyiciler': [   'uykum geldi',
                                                    'gece oldu',
                                                    'yatıyorum',
                                                    'sabah erken kalkacağım'],
                              'yanit': 'İyi geceler Ahmet! 🌙 21:00 – 04:00 uyku düzenini koruman '
                                       'zihinsel performansın ve 100m antrenmanların için çok '
                                       'önemli. Dinlen, yarın devam ederiz!'},
    'gece_calismasi_112': {   'tetikleyiciler': [   'uykum geldi',
                                                    'gece oldu',
                                                    'yatıyorum',
                                                    'sabah erken kalkacağım'],
                              'yanit': 'İyi geceler Ahmet! 🌙 21:00 – 04:00 uyku düzenini koruman '
                                       'zihinsel performansın ve 100m antrenmanların için çok '
                                       'önemli. Dinlen, yarın devam ederiz!'},
    'gece_calismasi_120': {   'tetikleyiciler': [   'uykum geldi',
                                                    'gece oldu',
                                                    'yatıyorum',
                                                    'sabah erken kalkacağım'],
                              'yanit': 'İyi geceler Ahmet! 🌙 21:00 – 04:00 uyku düzenini koruman '
                                       'zihinsel performansın ve 100m antrenmanların için çok '
                                       'önemli. Dinlen, yarın devam ederiz!'},
    'gece_calismasi_128': {   'tetikleyiciler': [   'uykum geldi',
                                                    'gece oldu',
                                                    'yatıyorum',
                                                    'sabah erken kalkacağım'],
                              'yanit': 'İyi geceler Ahmet! 🌙 21:00 – 04:00 uyku düzenini koruman '
                                       'zihinsel performansın ve 100m antrenmanların için çok '
                                       'önemli. Dinlen, yarın devam ederiz!'},
    'gece_calismasi_136': {   'tetikleyiciler': [   'uykum geldi',
                                                    'gece oldu',
                                                    'yatıyorum',
                                                    'sabah erken kalkacağım'],
                              'yanit': 'İyi geceler Ahmet! 🌙 21:00 – 04:00 uyku düzenini koruman '
                                       'zihinsel performansın ve 100m antrenmanların için çok '
                                       'önemli. Dinlen, yarın devam ederiz!'},
    'gece_calismasi_144': {   'tetikleyiciler': [   'uykum geldi',
                                                    'gece oldu',
                                                    'yatıyorum',
                                                    'sabah erken kalkacağım'],
                              'yanit': 'İyi geceler Ahmet! 🌙 21:00 – 04:00 uyku düzenini koruman '
                                       'zihinsel performansın ve 100m antrenmanların için çok '
                                       'önemli. Dinlen, yarın devam ederiz!'},
    'gece_calismasi_152': {   'tetikleyiciler': [   'uykum geldi',
                                                    'gece oldu',
                                                    'yatıyorum',
                                                    'sabah erken kalkacağım'],
                              'yanit': 'İyi geceler Ahmet! 🌙 21:00 – 04:00 uyku düzenini koruman '
                                       'zihinsel performansın ve 100m antrenmanların için çok '
                                       'önemli. Dinlen, yarın devam ederiz!'},
    'gece_calismasi_160': {   'tetikleyiciler': [   'uykum geldi',
                                                    'gece oldu',
                                                    'yatıyorum',
                                                    'sabah erken kalkacağım'],
                              'yanit': 'İyi geceler Ahmet! 🌙 21:00 – 04:00 uyku düzenini koruman '
                                       'zihinsel performansın ve 100m antrenmanların için çok '
                                       'önemli. Dinlen, yarın devam ederiz!'},
    'gece_calismasi_168': {   'tetikleyiciler': [   'uykum geldi',
                                                    'gece oldu',
                                                    'yatıyorum',
                                                    'sabah erken kalkacağım'],
                              'yanit': 'İyi geceler Ahmet! 🌙 21:00 – 04:00 uyku düzenini koruman '
                                       'zihinsel performansın ve 100m antrenmanların için çok '
                                       'önemli. Dinlen, yarın devam ederiz!'},
    'gece_calismasi_176': {   'tetikleyiciler': [   'uykum geldi',
                                                    'gece oldu',
                                                    'yatıyorum',
                                                    'sabah erken kalkacağım'],
                              'yanit': 'İyi geceler Ahmet! 🌙 21:00 – 04:00 uyku düzenini koruman '
                                       'zihinsel performansın ve 100m antrenmanların için çok '
                                       'önemli. Dinlen, yarın devam ederiz!'},
    'gece_calismasi_184': {   'tetikleyiciler': [   'uykum geldi',
                                                    'gece oldu',
                                                    'yatıyorum',
                                                    'sabah erken kalkacağım'],
                              'yanit': 'İyi geceler Ahmet! 🌙 21:00 – 04:00 uyku düzenini koruman '
                                       'zihinsel performansın ve 100m antrenmanların için çok '
                                       'önemli. Dinlen, yarın devam ederiz!'},
    'gece_calismasi_192': {   'tetikleyiciler': [   'uykum geldi',
                                                    'gece oldu',
                                                    'yatıyorum',
                                                    'sabah erken kalkacağım'],
                              'yanit': 'İyi geceler Ahmet! 🌙 21:00 – 04:00 uyku düzenini koruman '
                                       'zihinsel performansın ve 100m antrenmanların için çok '
                                       'önemli. Dinlen, yarın devam ederiz!'},
    'gece_calismasi_200': {   'tetikleyiciler': [   'uykum geldi',
                                                    'gece oldu',
                                                    'yatıyorum',
                                                    'sabah erken kalkacağım'],
                              'yanit': 'İyi geceler Ahmet! 🌙 21:00 – 04:00 uyku düzenini koruman '
                                       'zihinsel performansın ve 100m antrenmanların için çok '
                                       'önemli. Dinlen, yarın devam ederiz!'},
    'gece_calismasi_208': {   'tetikleyiciler': [   'uykum geldi',
                                                    'gece oldu',
                                                    'yatıyorum',
                                                    'sabah erken kalkacağım'],
                              'yanit': 'İyi geceler Ahmet! 🌙 21:00 – 04:00 uyku düzenini koruman '
                                       'zihinsel performansın ve 100m antrenmanların için çok '
                                       'önemli. Dinlen, yarın devam ederiz!'},
    'gece_calismasi_216': {   'tetikleyiciler': [   'uykum geldi',
                                                    'gece oldu',
                                                    'yatıyorum',
                                                    'sabah erken kalkacağım'],
                              'yanit': 'İyi geceler Ahmet! 🌙 21:00 – 04:00 uyku düzenini koruman '
                                       'zihinsel performansın ve 100m antrenmanların için çok '
                                       'önemli. Dinlen, yarın devam ederiz!'},
    'gece_calismasi_224': {   'tetikleyiciler': [   'uykum geldi',
                                                    'gece oldu',
                                                    'yatıyorum',
                                                    'sabah erken kalkacağım'],
                              'yanit': 'İyi geceler Ahmet! 🌙 21:00 – 04:00 uyku düzenini koruman '
                                       'zihinsel performansın ve 100m antrenmanların için çok '
                                       'önemli. Dinlen, yarın devam ederiz!'},
    'gece_calismasi_232': {   'tetikleyiciler': [   'uykum geldi',
                                                    'gece oldu',
                                                    'yatıyorum',
                                                    'sabah erken kalkacağım'],
                              'yanit': 'İyi geceler Ahmet! 🌙 21:00 – 04:00 uyku düzenini koruman '
                                       'zihinsel performansın ve 100m antrenmanların için çok '
                                       'önemli. Dinlen, yarın devam ederiz!'},
    'gece_calismasi_240': {   'tetikleyiciler': [   'uykum geldi',
                                                    'gece oldu',
                                                    'yatıyorum',
                                                    'sabah erken kalkacağım'],
                              'yanit': 'İyi geceler Ahmet! 🌙 21:00 – 04:00 uyku düzenini koruman '
                                       'zihinsel performansın ve 100m antrenmanların için çok '
                                       'önemli. Dinlen, yarın devam ederiz!'},
    'gece_calismasi_248': {   'tetikleyiciler': [   'uykum geldi',
                                                    'gece oldu',
                                                    'yatıyorum',
                                                    'sabah erken kalkacağım'],
                              'yanit': 'İyi geceler Ahmet! 🌙 21:00 – 04:00 uyku düzenini koruman '
                                       'zihinsel performansın ve 100m antrenmanların için çok '
                                       'önemli. Dinlen, yarın devam ederiz!'},
    'gece_calismasi_256': {   'tetikleyiciler': [   'uykum geldi',
                                                    'gece oldu',
                                                    'yatıyorum',
                                                    'sabah erken kalkacağım'],
                              'yanit': 'İyi geceler Ahmet! 🌙 21:00 – 04:00 uyku düzenini koruman '
                                       'zihinsel performansın ve 100m antrenmanların için çok '
                                       'önemli. Dinlen, yarın devam ederiz!'},
    'gece_calismasi_264': {   'tetikleyiciler': [   'uykum geldi',
                                                    'gece oldu',
                                                    'yatıyorum',
                                                    'sabah erken kalkacağım'],
                              'yanit': 'İyi geceler Ahmet! 🌙 21:00 – 04:00 uyku düzenini koruman '
                                       'zihinsel performansın ve 100m antrenmanların için çok '
                                       'önemli. Dinlen, yarın devam ederiz!'},
    'gece_calismasi_272': {   'tetikleyiciler': [   'uykum geldi',
                                                    'gece oldu',
                                                    'yatıyorum',
                                                    'sabah erken kalkacağım'],
                              'yanit': 'İyi geceler Ahmet! 🌙 21:00 – 04:00 uyku düzenini koruman '
                                       'zihinsel performansın ve 100m antrenmanların için çok '
                                       'önemli. Dinlen, yarın devam ederiz!'},
    'gece_calismasi_280': {   'tetikleyiciler': [   'uykum geldi',
                                                    'gece oldu',
                                                    'yatıyorum',
                                                    'sabah erken kalkacağım'],
                              'yanit': 'İyi geceler Ahmet! 🌙 21:00 – 04:00 uyku düzenini koruman '
                                       'zihinsel performansın ve 100m antrenmanların için çok '
                                       'önemli. Dinlen, yarın devam ederiz!'},
    'kim_sorusu_genel_003': {   'tetikleyiciler': [   'bu kim',
                                                      'o kim',
                                                      'kın',
                                                      'kim bu',
                                                      'kimi tanıdın'],
                                'yanit': "Kimi sorduğunu isimle yazarsan (Örn: **'Ömer kim'**, "
                                         "**'Hadi kim'**, **'El-Cezerî kim'**, **'Ben kimim'**) "
                                         'sana hemen detaylı bilgisini verebilirim Ahmet! ⚡'},
    'kim_sorusu_genel_011': {   'tetikleyiciler': [   'bu kim',
                                                      'o kim',
                                                      'kın',
                                                      'kim bu',
                                                      'kimi tanıdın'],
                                'yanit': "Kimi sorduğunu isimle yazarsan (Örn: **'Ömer kim'**, "
                                         "**'Hadi kim'**, **'El-Cezerî kim'**, **'Ben kimim'**) "
                                         'sana hemen detaylı bilgisini verebilirim Ahmet! ⚡'},
    'kim_sorusu_genel_019': {   'tetikleyiciler': [   'bu kim',
                                                      'o kim',
                                                      'kın',
                                                      'kim bu',
                                                      'kimi tanıdın'],
                                'yanit': "Kimi sorduğunu isimle yazarsan (Örn: **'Ömer kim'**, "
                                         "**'Hadi kim'**, **'El-Cezerî kim'**, **'Ben kimim'**) "
                                         'sana hemen detaylı bilgisini verebilirim Ahmet! ⚡'},
    'kim_sorusu_genel_027': {   'tetikleyiciler': [   'bu kim',
                                                      'o kim',
                                                      'kın',
                                                      'kim bu',
                                                      'kimi tanıdın'],
                                'yanit': "Kimi sorduğunu isimle yazarsan (Örn: **'Ömer kim'**, "
                                         "**'Hadi kim'**, **'El-Cezerî kim'**, **'Ben kimim'**) "
                                         'sana hemen detaylı bilgisini verebilirim Ahmet! ⚡'},
    'kim_sorusu_genel_035': {   'tetikleyiciler': [   'bu kim',
                                                      'o kim',
                                                      'kın',
                                                      'kim bu',
                                                      'kimi tanıdın'],
                                'yanit': "Kimi sorduğunu isimle yazarsan (Örn: **'Ömer kim'**, "
                                         "**'Hadi kim'**, **'El-Cezerî kim'**, **'Ben kimim'**) "
                                         'sana hemen detaylı bilgisini verebilirim Ahmet! ⚡'},
    'kim_sorusu_genel_043': {   'tetikleyiciler': [   'bu kim',
                                                      'o kim',
                                                      'kın',
                                                      'kim bu',
                                                      'kimi tanıdın'],
                                'yanit': "Kimi sorduğunu isimle yazarsan (Örn: **'Ömer kim'**, "
                                         "**'Hadi kim'**, **'El-Cezerî kim'**, **'Ben kimim'**) "
                                         'sana hemen detaylı bilgisini verebilirim Ahmet! ⚡'},
    'kim_sorusu_genel_051': {   'tetikleyiciler': [   'bu kim',
                                                      'o kim',
                                                      'kın',
                                                      'kim bu',
                                                      'kimi tanıdın'],
                                'yanit': "Kimi sorduğunu isimle yazarsan (Örn: **'Ömer kim'**, "
                                         "**'Hadi kim'**, **'El-Cezerî kim'**, **'Ben kimim'**) "
                                         'sana hemen detaylı bilgisini verebilirim Ahmet! ⚡'},
    'kim_sorusu_genel_059': {   'tetikleyiciler': [   'bu kim',
                                                      'o kim',
                                                      'kın',
                                                      'kim bu',
                                                      'kimi tanıdın'],
                                'yanit': "Kimi sorduğunu isimle yazarsan (Örn: **'Ömer kim'**, "
                                         "**'Hadi kim'**, **'El-Cezerî kim'**, **'Ben kimim'**) "
                                         'sana hemen detaylı bilgisini verebilirim Ahmet! ⚡'},
    'kim_sorusu_genel_067': {   'tetikleyiciler': [   'bu kim',
                                                      'o kim',
                                                      'kın',
                                                      'kim bu',
                                                      'kimi tanıdın'],
                                'yanit': "Kimi sorduğunu isimle yazarsan (Örn: **'Ömer kim'**, "
                                         "**'Hadi kim'**, **'El-Cezerî kim'**, **'Ben kimim'**) "
                                         'sana hemen detaylı bilgisini verebilirim Ahmet! ⚡'},
    'kim_sorusu_genel_075': {   'tetikleyiciler': [   'bu kim',
                                                      'o kim',
                                                      'kın',
                                                      'kim bu',
                                                      'kimi tanıdın'],
                                'yanit': "Kimi sorduğunu isimle yazarsan (Örn: **'Ömer kim'**, "
                                         "**'Hadi kim'**, **'El-Cezerî kim'**, **'Ben kimim'**) "
                                         'sana hemen detaylı bilgisini verebilirim Ahmet! ⚡'},
    'kim_sorusu_genel_083': {   'tetikleyiciler': [   'bu kim',
                                                      'o kim',
                                                      'kın',
                                                      'kim bu',
                                                      'kimi tanıdın'],
                                'yanit': "Kimi sorduğunu isimle yazarsan (Örn: **'Ömer kim'**, "
                                         "**'Hadi kim'**, **'El-Cezerî kim'**, **'Ben kimim'**) "
                                         'sana hemen detaylı bilgisini verebilirim Ahmet! ⚡'},
    'kim_sorusu_genel_091': {   'tetikleyiciler': [   'bu kim',
                                                      'o kim',
                                                      'kın',
                                                      'kim bu',
                                                      'kimi tanıdın'],
                                'yanit': "Kimi sorduğunu isimle yazarsan (Örn: **'Ömer kim'**, "
                                         "**'Hadi kim'**, **'El-Cezerî kim'**, **'Ben kimim'**) "
                                         'sana hemen detaylı bilgisini verebilirim Ahmet! ⚡'},
    'kim_sorusu_genel_099': {   'tetikleyiciler': [   'bu kim',
                                                      'o kim',
                                                      'kın',
                                                      'kim bu',
                                                      'kimi tanıdın'],
                                'yanit': "Kimi sorduğunu isimle yazarsan (Örn: **'Ömer kim'**, "
                                         "**'Hadi kim'**, **'El-Cezerî kim'**, **'Ben kimim'**) "
                                         'sana hemen detaylı bilgisini verebilirim Ahmet! ⚡'},
    'kim_sorusu_genel_107': {   'tetikleyiciler': [   'bu kim',
                                                      'o kim',
                                                      'kın',
                                                      'kim bu',
                                                      'kimi tanıdın'],
                                'yanit': "Kimi sorduğunu isimle yazarsan (Örn: **'Ömer kim'**, "
                                         "**'Hadi kim'**, **'El-Cezerî kim'**, **'Ben kimim'**) "
                                         'sana hemen detaylı bilgisini verebilirim Ahmet! ⚡'},
    'kim_sorusu_genel_115': {   'tetikleyiciler': [   'bu kim',
                                                      'o kim',
                                                      'kın',
                                                      'kim bu',
                                                      'kimi tanıdın'],
                                'yanit': "Kimi sorduğunu isimle yazarsan (Örn: **'Ömer kim'**, "
                                         "**'Hadi kim'**, **'El-Cezerî kim'**, **'Ben kimim'**) "
                                         'sana hemen detaylı bilgisini verebilirim Ahmet! ⚡'},
    'kim_sorusu_genel_123': {   'tetikleyiciler': [   'bu kim',
                                                      'o kim',
                                                      'kın',
                                                      'kim bu',
                                                      'kimi tanıdın'],
                                'yanit': "Kimi sorduğunu isimle yazarsan (Örn: **'Ömer kim'**, "
                                         "**'Hadi kim'**, **'El-Cezerî kim'**, **'Ben kimim'**) "
                                         'sana hemen detaylı bilgisini verebilirim Ahmet! ⚡'},
    'kim_sorusu_genel_131': {   'tetikleyiciler': [   'bu kim',
                                                      'o kim',
                                                      'kın',
                                                      'kim bu',
                                                      'kimi tanıdın'],
                                'yanit': "Kimi sorduğunu isimle yazarsan (Örn: **'Ömer kim'**, "
                                         "**'Hadi kim'**, **'El-Cezerî kim'**, **'Ben kimim'**) "
                                         'sana hemen detaylı bilgisini verebilirim Ahmet! ⚡'},
    'kim_sorusu_genel_139': {   'tetikleyiciler': [   'bu kim',
                                                      'o kim',
                                                      'kın',
                                                      'kim bu',
                                                      'kimi tanıdın'],
                                'yanit': "Kimi sorduğunu isimle yazarsan (Örn: **'Ömer kim'**, "
                                         "**'Hadi kim'**, **'El-Cezerî kim'**, **'Ben kimim'**) "
                                         'sana hemen detaylı bilgisini verebilirim Ahmet! ⚡'},
    'kim_sorusu_genel_147': {   'tetikleyiciler': [   'bu kim',
                                                      'o kim',
                                                      'kın',
                                                      'kim bu',
                                                      'kimi tanıdın'],
                                'yanit': "Kimi sorduğunu isimle yazarsan (Örn: **'Ömer kim'**, "
                                         "**'Hadi kim'**, **'El-Cezerî kim'**, **'Ben kimim'**) "
                                         'sana hemen detaylı bilgisini verebilirim Ahmet! ⚡'},
    'kim_sorusu_genel_155': {   'tetikleyiciler': [   'bu kim',
                                                      'o kim',
                                                      'kın',
                                                      'kim bu',
                                                      'kimi tanıdın'],
                                'yanit': "Kimi sorduğunu isimle yazarsan (Örn: **'Ömer kim'**, "
                                         "**'Hadi kim'**, **'El-Cezerî kim'**, **'Ben kimim'**) "
                                         'sana hemen detaylı bilgisini verebilirim Ahmet! ⚡'},
    'kim_sorusu_genel_163': {   'tetikleyiciler': [   'bu kim',
                                                      'o kim',
                                                      'kın',
                                                      'kim bu',
                                                      'kimi tanıdın'],
                                'yanit': "Kimi sorduğunu isimle yazarsan (Örn: **'Ömer kim'**, "
                                         "**'Hadi kim'**, **'El-Cezerî kim'**, **'Ben kimim'**) "
                                         'sana hemen detaylı bilgisini verebilirim Ahmet! ⚡'},
    'kim_sorusu_genel_171': {   'tetikleyiciler': [   'bu kim',
                                                      'o kim',
                                                      'kın',
                                                      'kim bu',
                                                      'kimi tanıdın'],
                                'yanit': "Kimi sorduğunu isimle yazarsan (Örn: **'Ömer kim'**, "
                                         "**'Hadi kim'**, **'El-Cezerî kim'**, **'Ben kimim'**) "
                                         'sana hemen detaylı bilgisini verebilirim Ahmet! ⚡'},
    'kim_sorusu_genel_179': {   'tetikleyiciler': [   'bu kim',
                                                      'o kim',
                                                      'kın',
                                                      'kim bu',
                                                      'kimi tanıdın'],
                                'yanit': "Kimi sorduğunu isimle yazarsan (Örn: **'Ömer kim'**, "
                                         "**'Hadi kim'**, **'El-Cezerî kim'**, **'Ben kimim'**) "
                                         'sana hemen detaylı bilgisini verebilirim Ahmet! ⚡'},
    'kim_sorusu_genel_187': {   'tetikleyiciler': [   'bu kim',
                                                      'o kim',
                                                      'kın',
                                                      'kim bu',
                                                      'kimi tanıdın'],
                                'yanit': "Kimi sorduğunu isimle yazarsan (Örn: **'Ömer kim'**, "
                                         "**'Hadi kim'**, **'El-Cezerî kim'**, **'Ben kimim'**) "
                                         'sana hemen detaylı bilgisini verebilirim Ahmet! ⚡'},
    'kim_sorusu_genel_195': {   'tetikleyiciler': [   'bu kim',
                                                      'o kim',
                                                      'kın',
                                                      'kim bu',
                                                      'kimi tanıdın'],
                                'yanit': "Kimi sorduğunu isimle yazarsan (Örn: **'Ömer kim'**, "
                                         "**'Hadi kim'**, **'El-Cezerî kim'**, **'Ben kimim'**) "
                                         'sana hemen detaylı bilgisini verebilirim Ahmet! ⚡'},
    'kim_sorusu_genel_203': {   'tetikleyiciler': [   'bu kim',
                                                      'o kim',
                                                      'kın',
                                                      'kim bu',
                                                      'kimi tanıdın'],
                                'yanit': "Kimi sorduğunu isimle yazarsan (Örn: **'Ömer kim'**, "
                                         "**'Hadi kim'**, **'El-Cezerî kim'**, **'Ben kimim'**) "
                                         'sana hemen detaylı bilgisini verebilirim Ahmet! ⚡'},
    'kim_sorusu_genel_211': {   'tetikleyiciler': [   'bu kim',
                                                      'o kim',
                                                      'kın',
                                                      'kim bu',
                                                      'kimi tanıdın'],
                                'yanit': "Kimi sorduğunu isimle yazarsan (Örn: **'Ömer kim'**, "
                                         "**'Hadi kim'**, **'El-Cezerî kim'**, **'Ben kimim'**) "
                                         'sana hemen detaylı bilgisini verebilirim Ahmet! ⚡'},
    'kim_sorusu_genel_219': {   'tetikleyiciler': [   'bu kim',
                                                      'o kim',
                                                      'kın',
                                                      'kim bu',
                                                      'kimi tanıdın'],
                                'yanit': "Kimi sorduğunu isimle yazarsan (Örn: **'Ömer kim'**, "
                                         "**'Hadi kim'**, **'El-Cezerî kim'**, **'Ben kimim'**) "
                                         'sana hemen detaylı bilgisini verebilirim Ahmet! ⚡'},
    'kim_sorusu_genel_227': {   'tetikleyiciler': [   'bu kim',
                                                      'o kim',
                                                      'kın',
                                                      'kim bu',
                                                      'kimi tanıdın'],
                                'yanit': "Kimi sorduğunu isimle yazarsan (Örn: **'Ömer kim'**, "
                                         "**'Hadi kim'**, **'El-Cezerî kim'**, **'Ben kimim'**) "
                                         'sana hemen detaylı bilgisini verebilirim Ahmet! ⚡'},
    'kim_sorusu_genel_235': {   'tetikleyiciler': [   'bu kim',
                                                      'o kim',
                                                      'kın',
                                                      'kim bu',
                                                      'kimi tanıdın'],
                                'yanit': "Kimi sorduğunu isimle yazarsan (Örn: **'Ömer kim'**, "
                                         "**'Hadi kim'**, **'El-Cezerî kim'**, **'Ben kimim'**) "
                                         'sana hemen detaylı bilgisini verebilirim Ahmet! ⚡'},
    'kim_sorusu_genel_243': {   'tetikleyiciler': [   'bu kim',
                                                      'o kim',
                                                      'kın',
                                                      'kim bu',
                                                      'kimi tanıdın'],
                                'yanit': "Kimi sorduğunu isimle yazarsan (Örn: **'Ömer kim'**, "
                                         "**'Hadi kim'**, **'El-Cezerî kim'**, **'Ben kimim'**) "
                                         'sana hemen detaylı bilgisini verebilirim Ahmet! ⚡'},
    'kim_sorusu_genel_251': {   'tetikleyiciler': [   'bu kim',
                                                      'o kim',
                                                      'kın',
                                                      'kim bu',
                                                      'kimi tanıdın'],
                                'yanit': "Kimi sorduğunu isimle yazarsan (Örn: **'Ömer kim'**, "
                                         "**'Hadi kim'**, **'El-Cezerî kim'**, **'Ben kimim'**) "
                                         'sana hemen detaylı bilgisini verebilirim Ahmet! ⚡'},
    'kim_sorusu_genel_259': {   'tetikleyiciler': [   'bu kim',
                                                      'o kim',
                                                      'kın',
                                                      'kim bu',
                                                      'kimi tanıdın'],
                                'yanit': "Kimi sorduğunu isimle yazarsan (Örn: **'Ömer kim'**, "
                                         "**'Hadi kim'**, **'El-Cezerî kim'**, **'Ben kimim'**) "
                                         'sana hemen detaylı bilgisini verebilirim Ahmet! ⚡'},
    'kim_sorusu_genel_267': {   'tetikleyiciler': [   'bu kim',
                                                      'o kim',
                                                      'kın',
                                                      'kim bu',
                                                      'kimi tanıdın'],
                                'yanit': "Kimi sorduğunu isimle yazarsan (Örn: **'Ömer kim'**, "
                                         "**'Hadi kim'**, **'El-Cezerî kim'**, **'Ben kimim'**) "
                                         'sana hemen detaylı bilgisini verebilirim Ahmet! ⚡'},
    'kim_sorusu_genel_275': {   'tetikleyiciler': [   'bu kim',
                                                      'o kim',
                                                      'kın',
                                                      'kim bu',
                                                      'kimi tanıdın'],
                                'yanit': "Kimi sorduğunu isimle yazarsan (Örn: **'Ömer kim'**, "
                                         "**'Hadi kim'**, **'El-Cezerî kim'**, **'Ben kimim'**) "
                                         'sana hemen detaylı bilgisini verebilirim Ahmet! ⚡'},
    'kodlama_modu_005': {   'tetikleyiciler': [   'kod yazıyorum',
                                                  'pycharm açtım',
                                                  'hata ayıklıyorum',
                                                  'debug yapıyorum',
                                                  'uygulama yapıyorum'],
                            'yanit': "Harika! 💻 PyCharm'da tüm modüllerimiz birbirine bağlı. "
                                     'İstediğin özelliği veya testi hemen deneyebilirsin.'},
    'kodlama_modu_013': {   'tetikleyiciler': [   'kod yazıyorum',
                                                  'pycharm açtım',
                                                  'hata ayıklıyorum',
                                                  'debug yapıyorum',
                                                  'uygulama yapıyorum'],
                            'yanit': "Harika! 💻 PyCharm'da tüm modüllerimiz birbirine bağlı. "
                                     'İstediğin özelliği veya testi hemen deneyebilirsin.'},
    'kodlama_modu_021': {   'tetikleyiciler': [   'kod yazıyorum',
                                                  'pycharm açtım',
                                                  'hata ayıklıyorum',
                                                  'debug yapıyorum',
                                                  'uygulama yapıyorum'],
                            'yanit': "Harika! 💻 PyCharm'da tüm modüllerimiz birbirine bağlı. "
                                     'İstediğin özelliği veya testi hemen deneyebilirsin.'},
    'kodlama_modu_029': {   'tetikleyiciler': [   'kod yazıyorum',
                                                  'pycharm açtım',
                                                  'hata ayıklıyorum',
                                                  'debug yapıyorum',
                                                  'uygulama yapıyorum'],
                            'yanit': "Harika! 💻 PyCharm'da tüm modüllerimiz birbirine bağlı. "
                                     'İstediğin özelliği veya testi hemen deneyebilirsin.'},
    'kodlama_modu_037': {   'tetikleyiciler': [   'kod yazıyorum',
                                                  'pycharm açtım',
                                                  'hata ayıklıyorum',
                                                  'debug yapıyorum',
                                                  'uygulama yapıyorum'],
                            'yanit': "Harika! 💻 PyCharm'da tüm modüllerimiz birbirine bağlı. "
                                     'İstediğin özelliği veya testi hemen deneyebilirsin.'},
    'kodlama_modu_045': {   'tetikleyiciler': [   'kod yazıyorum',
                                                  'pycharm açtım',
                                                  'hata ayıklıyorum',
                                                  'debug yapıyorum',
                                                  'uygulama yapıyorum'],
                            'yanit': "Harika! 💻 PyCharm'da tüm modüllerimiz birbirine bağlı. "
                                     'İstediğin özelliği veya testi hemen deneyebilirsin.'},
    'kodlama_modu_053': {   'tetikleyiciler': [   'kod yazıyorum',
                                                  'pycharm açtım',
                                                  'hata ayıklıyorum',
                                                  'debug yapıyorum',
                                                  'uygulama yapıyorum'],
                            'yanit': "Harika! 💻 PyCharm'da tüm modüllerimiz birbirine bağlı. "
                                     'İstediğin özelliği veya testi hemen deneyebilirsin.'},
    'kodlama_modu_061': {   'tetikleyiciler': [   'kod yazıyorum',
                                                  'pycharm açtım',
                                                  'hata ayıklıyorum',
                                                  'debug yapıyorum',
                                                  'uygulama yapıyorum'],
                            'yanit': "Harika! 💻 PyCharm'da tüm modüllerimiz birbirine bağlı. "
                                     'İstediğin özelliği veya testi hemen deneyebilirsin.'},
    'kodlama_modu_069': {   'tetikleyiciler': [   'kod yazıyorum',
                                                  'pycharm açtım',
                                                  'hata ayıklıyorum',
                                                  'debug yapıyorum',
                                                  'uygulama yapıyorum'],
                            'yanit': "Harika! 💻 PyCharm'da tüm modüllerimiz birbirine bağlı. "
                                     'İstediğin özelliği veya testi hemen deneyebilirsin.'},
    'kodlama_modu_077': {   'tetikleyiciler': [   'kod yazıyorum',
                                                  'pycharm açtım',
                                                  'hata ayıklıyorum',
                                                  'debug yapıyorum',
                                                  'uygulama yapıyorum'],
                            'yanit': "Harika! 💻 PyCharm'da tüm modüllerimiz birbirine bağlı. "
                                     'İstediğin özelliği veya testi hemen deneyebilirsin.'},
    'kodlama_modu_085': {   'tetikleyiciler': [   'kod yazıyorum',
                                                  'pycharm açtım',
                                                  'hata ayıklıyorum',
                                                  'debug yapıyorum',
                                                  'uygulama yapıyorum'],
                            'yanit': "Harika! 💻 PyCharm'da tüm modüllerimiz birbirine bağlı. "
                                     'İstediğin özelliği veya testi hemen deneyebilirsin.'},
    'kodlama_modu_093': {   'tetikleyiciler': [   'kod yazıyorum',
                                                  'pycharm açtım',
                                                  'hata ayıklıyorum',
                                                  'debug yapıyorum',
                                                  'uygulama yapıyorum'],
                            'yanit': "Harika! 💻 PyCharm'da tüm modüllerimiz birbirine bağlı. "
                                     'İstediğin özelliği veya testi hemen deneyebilirsin.'},
    'kodlama_modu_101': {   'tetikleyiciler': [   'kod yazıyorum',
                                                  'pycharm açtım',
                                                  'hata ayıklıyorum',
                                                  'debug yapıyorum',
                                                  'uygulama yapıyorum'],
                            'yanit': "Harika! 💻 PyCharm'da tüm modüllerimiz birbirine bağlı. "
                                     'İstediğin özelliği veya testi hemen deneyebilirsin.'},
    'kodlama_modu_109': {   'tetikleyiciler': [   'kod yazıyorum',
                                                  'pycharm açtım',
                                                  'hata ayıklıyorum',
                                                  'debug yapıyorum',
                                                  'uygulama yapıyorum'],
                            'yanit': "Harika! 💻 PyCharm'da tüm modüllerimiz birbirine bağlı. "
                                     'İstediğin özelliği veya testi hemen deneyebilirsin.'},
    'kodlama_modu_117': {   'tetikleyiciler': [   'kod yazıyorum',
                                                  'pycharm açtım',
                                                  'hata ayıklıyorum',
                                                  'debug yapıyorum',
                                                  'uygulama yapıyorum'],
                            'yanit': "Harika! 💻 PyCharm'da tüm modüllerimiz birbirine bağlı. "
                                     'İstediğin özelliği veya testi hemen deneyebilirsin.'},
    'kodlama_modu_125': {   'tetikleyiciler': [   'kod yazıyorum',
                                                  'pycharm açtım',
                                                  'hata ayıklıyorum',
                                                  'debug yapıyorum',
                                                  'uygulama yapıyorum'],
                            'yanit': "Harika! 💻 PyCharm'da tüm modüllerimiz birbirine bağlı. "
                                     'İstediğin özelliği veya testi hemen deneyebilirsin.'},
    'kodlama_modu_133': {   'tetikleyiciler': [   'kod yazıyorum',
                                                  'pycharm açtım',
                                                  'hata ayıklıyorum',
                                                  'debug yapıyorum',
                                                  'uygulama yapıyorum'],
                            'yanit': "Harika! 💻 PyCharm'da tüm modüllerimiz birbirine bağlı. "
                                     'İstediğin özelliği veya testi hemen deneyebilirsin.'},
    'kodlama_modu_141': {   'tetikleyiciler': [   'kod yazıyorum',
                                                  'pycharm açtım',
                                                  'hata ayıklıyorum',
                                                  'debug yapıyorum',
                                                  'uygulama yapıyorum'],
                            'yanit': "Harika! 💻 PyCharm'da tüm modüllerimiz birbirine bağlı. "
                                     'İstediğin özelliği veya testi hemen deneyebilirsin.'},
    'kodlama_modu_149': {   'tetikleyiciler': [   'kod yazıyorum',
                                                  'pycharm açtım',
                                                  'hata ayıklıyorum',
                                                  'debug yapıyorum',
                                                  'uygulama yapıyorum'],
                            'yanit': "Harika! 💻 PyCharm'da tüm modüllerimiz birbirine bağlı. "
                                     'İstediğin özelliği veya testi hemen deneyebilirsin.'},
    'kodlama_modu_157': {   'tetikleyiciler': [   'kod yazıyorum',
                                                  'pycharm açtım',
                                                  'hata ayıklıyorum',
                                                  'debug yapıyorum',
                                                  'uygulama yapıyorum'],
                            'yanit': "Harika! 💻 PyCharm'da tüm modüllerimiz birbirine bağlı. "
                                     'İstediğin özelliği veya testi hemen deneyebilirsin.'},
    'kodlama_modu_165': {   'tetikleyiciler': [   'kod yazıyorum',
                                                  'pycharm açtım',
                                                  'hata ayıklıyorum',
                                                  'debug yapıyorum',
                                                  'uygulama yapıyorum'],
                            'yanit': "Harika! 💻 PyCharm'da tüm modüllerimiz birbirine bağlı. "
                                     'İstediğin özelliği veya testi hemen deneyebilirsin.'},
    'kodlama_modu_173': {   'tetikleyiciler': [   'kod yazıyorum',
                                                  'pycharm açtım',
                                                  'hata ayıklıyorum',
                                                  'debug yapıyorum',
                                                  'uygulama yapıyorum'],
                            'yanit': "Harika! 💻 PyCharm'da tüm modüllerimiz birbirine bağlı. "
                                     'İstediğin özelliği veya testi hemen deneyebilirsin.'},
    'kodlama_modu_181': {   'tetikleyiciler': [   'kod yazıyorum',
                                                  'pycharm açtım',
                                                  'hata ayıklıyorum',
                                                  'debug yapıyorum',
                                                  'uygulama yapıyorum'],
                            'yanit': "Harika! 💻 PyCharm'da tüm modüllerimiz birbirine bağlı. "
                                     'İstediğin özelliği veya testi hemen deneyebilirsin.'},
    'kodlama_modu_189': {   'tetikleyiciler': [   'kod yazıyorum',
                                                  'pycharm açtım',
                                                  'hata ayıklıyorum',
                                                  'debug yapıyorum',
                                                  'uygulama yapıyorum'],
                            'yanit': "Harika! 💻 PyCharm'da tüm modüllerimiz birbirine bağlı. "
                                     'İstediğin özelliği veya testi hemen deneyebilirsin.'},
    'kodlama_modu_197': {   'tetikleyiciler': [   'kod yazıyorum',
                                                  'pycharm açtım',
                                                  'hata ayıklıyorum',
                                                  'debug yapıyorum',
                                                  'uygulama yapıyorum'],
                            'yanit': "Harika! 💻 PyCharm'da tüm modüllerimiz birbirine bağlı. "
                                     'İstediğin özelliği veya testi hemen deneyebilirsin.'},
    'kodlama_modu_205': {   'tetikleyiciler': [   'kod yazıyorum',
                                                  'pycharm açtım',
                                                  'hata ayıklıyorum',
                                                  'debug yapıyorum',
                                                  'uygulama yapıyorum'],
                            'yanit': "Harika! 💻 PyCharm'da tüm modüllerimiz birbirine bağlı. "
                                     'İstediğin özelliği veya testi hemen deneyebilirsin.'},
    'kodlama_modu_213': {   'tetikleyiciler': [   'kod yazıyorum',
                                                  'pycharm açtım',
                                                  'hata ayıklıyorum',
                                                  'debug yapıyorum',
                                                  'uygulama yapıyorum'],
                            'yanit': "Harika! 💻 PyCharm'da tüm modüllerimiz birbirine bağlı. "
                                     'İstediğin özelliği veya testi hemen deneyebilirsin.'},
    'kodlama_modu_221': {   'tetikleyiciler': [   'kod yazıyorum',
                                                  'pycharm açtım',
                                                  'hata ayıklıyorum',
                                                  'debug yapıyorum',
                                                  'uygulama yapıyorum'],
                            'yanit': "Harika! 💻 PyCharm'da tüm modüllerimiz birbirine bağlı. "
                                     'İstediğin özelliği veya testi hemen deneyebilirsin.'},
    'kodlama_modu_229': {   'tetikleyiciler': [   'kod yazıyorum',
                                                  'pycharm açtım',
                                                  'hata ayıklıyorum',
                                                  'debug yapıyorum',
                                                  'uygulama yapıyorum'],
                            'yanit': "Harika! 💻 PyCharm'da tüm modüllerimiz birbirine bağlı. "
                                     'İstediğin özelliği veya testi hemen deneyebilirsin.'},
    'kodlama_modu_237': {   'tetikleyiciler': [   'kod yazıyorum',
                                                  'pycharm açtım',
                                                  'hata ayıklıyorum',
                                                  'debug yapıyorum',
                                                  'uygulama yapıyorum'],
                            'yanit': "Harika! 💻 PyCharm'da tüm modüllerimiz birbirine bağlı. "
                                     'İstediğin özelliği veya testi hemen deneyebilirsin.'},
    'kodlama_modu_245': {   'tetikleyiciler': [   'kod yazıyorum',
                                                  'pycharm açtım',
                                                  'hata ayıklıyorum',
                                                  'debug yapıyorum',
                                                  'uygulama yapıyorum'],
                            'yanit': "Harika! 💻 PyCharm'da tüm modüllerimiz birbirine bağlı. "
                                     'İstediğin özelliği veya testi hemen deneyebilirsin.'},
    'kodlama_modu_253': {   'tetikleyiciler': [   'kod yazıyorum',
                                                  'pycharm açtım',
                                                  'hata ayıklıyorum',
                                                  'debug yapıyorum',
                                                  'uygulama yapıyorum'],
                            'yanit': "Harika! 💻 PyCharm'da tüm modüllerimiz birbirine bağlı. "
                                     'İstediğin özelliği veya testi hemen deneyebilirsin.'},
    'kodlama_modu_261': {   'tetikleyiciler': [   'kod yazıyorum',
                                                  'pycharm açtım',
                                                  'hata ayıklıyorum',
                                                  'debug yapıyorum',
                                                  'uygulama yapıyorum'],
                            'yanit': "Harika! 💻 PyCharm'da tüm modüllerimiz birbirine bağlı. "
                                     'İstediğin özelliği veya testi hemen deneyebilirsin.'},
    'kodlama_modu_269': {   'tetikleyiciler': [   'kod yazıyorum',
                                                  'pycharm açtım',
                                                  'hata ayıklıyorum',
                                                  'debug yapıyorum',
                                                  'uygulama yapıyorum'],
                            'yanit': "Harika! 💻 PyCharm'da tüm modüllerimiz birbirine bağlı. "
                                     'İstediğin özelliği veya testi hemen deneyebilirsin.'},
    'kodlama_modu_277': {   'tetikleyiciler': [   'kod yazıyorum',
                                                  'pycharm açtım',
                                                  'hata ayıklıyorum',
                                                  'debug yapıyorum',
                                                  'uygulama yapıyorum'],
                            'yanit': "Harika! 💻 PyCharm'da tüm modüllerimiz birbirine bağlı. "
                                     'İstediğin özelliği veya testi hemen deneyebilirsin.'},
    'mobil_test_006': {   'tetikleyiciler': [   'mobildeyim',
                                                'telefondan girdim',
                                                'tabletten deniyorum',
                                                'mobil görünüm'],
                          'yanit': '📱 Mobil uyumlu yüksek kontrastlı arayüzümüz şu an aktif Ahmet! '
                                   'Dokunmatik butonlar ve ses motoru telefon ekranına göre '
                                   'optimize edildi.'},
    'mobil_test_014': {   'tetikleyiciler': [   'mobildeyim',
                                                'telefondan girdim',
                                                'tabletten deniyorum',
                                                'mobil görünüm'],
                          'yanit': '📱 Mobil uyumlu yüksek kontrastlı arayüzümüz şu an aktif Ahmet! '
                                   'Dokunmatik butonlar ve ses motoru telefon ekranına göre '
                                   'optimize edildi.'},
    'mobil_test_022': {   'tetikleyiciler': [   'mobildeyim',
                                                'telefondan girdim',
                                                'tabletten deniyorum',
                                                'mobil görünüm'],
                          'yanit': '📱 Mobil uyumlu yüksek kontrastlı arayüzümüz şu an aktif Ahmet! '
                                   'Dokunmatik butonlar ve ses motoru telefon ekranına göre '
                                   'optimize edildi.'},
    'mobil_test_030': {   'tetikleyiciler': [   'mobildeyim',
                                                'telefondan girdim',
                                                'tabletten deniyorum',
                                                'mobil görünüm'],
                          'yanit': '📱 Mobil uyumlu yüksek kontrastlı arayüzümüz şu an aktif Ahmet! '
                                   'Dokunmatik butonlar ve ses motoru telefon ekranına göre '
                                   'optimize edildi.'},
    'mobil_test_038': {   'tetikleyiciler': [   'mobildeyim',
                                                'telefondan girdim',
                                                'tabletten deniyorum',
                                                'mobil görünüm'],
                          'yanit': '📱 Mobil uyumlu yüksek kontrastlı arayüzümüz şu an aktif Ahmet! '
                                   'Dokunmatik butonlar ve ses motoru telefon ekranına göre '
                                   'optimize edildi.'},
    'mobil_test_046': {   'tetikleyiciler': [   'mobildeyim',
                                                'telefondan girdim',
                                                'tabletten deniyorum',
                                                'mobil görünüm'],
                          'yanit': '📱 Mobil uyumlu yüksek kontrastlı arayüzümüz şu an aktif Ahmet! '
                                   'Dokunmatik butonlar ve ses motoru telefon ekranına göre '
                                   'optimize edildi.'},
    'mobil_test_054': {   'tetikleyiciler': [   'mobildeyim',
                                                'telefondan girdim',
                                                'tabletten deniyorum',
                                                'mobil görünüm'],
                          'yanit': '📱 Mobil uyumlu yüksek kontrastlı arayüzümüz şu an aktif Ahmet! '
                                   'Dokunmatik butonlar ve ses motoru telefon ekranına göre '
                                   'optimize edildi.'},
    'mobil_test_062': {   'tetikleyiciler': [   'mobildeyim',
                                                'telefondan girdim',
                                                'tabletten deniyorum',
                                                'mobil görünüm'],
                          'yanit': '📱 Mobil uyumlu yüksek kontrastlı arayüzümüz şu an aktif Ahmet! '
                                   'Dokunmatik butonlar ve ses motoru telefon ekranına göre '
                                   'optimize edildi.'},
    'mobil_test_070': {   'tetikleyiciler': [   'mobildeyim',
                                                'telefondan girdim',
                                                'tabletten deniyorum',
                                                'mobil görünüm'],
                          'yanit': '📱 Mobil uyumlu yüksek kontrastlı arayüzümüz şu an aktif Ahmet! '
                                   'Dokunmatik butonlar ve ses motoru telefon ekranına göre '
                                   'optimize edildi.'},
    'mobil_test_078': {   'tetikleyiciler': [   'mobildeyim',
                                                'telefondan girdim',
                                                'tabletten deniyorum',
                                                'mobil görünüm'],
                          'yanit': '📱 Mobil uyumlu yüksek kontrastlı arayüzümüz şu an aktif Ahmet! '
                                   'Dokunmatik butonlar ve ses motoru telefon ekranına göre '
                                   'optimize edildi.'},
    'mobil_test_086': {   'tetikleyiciler': [   'mobildeyim',
                                                'telefondan girdim',
                                                'tabletten deniyorum',
                                                'mobil görünüm'],
                          'yanit': '📱 Mobil uyumlu yüksek kontrastlı arayüzümüz şu an aktif Ahmet! '
                                   'Dokunmatik butonlar ve ses motoru telefon ekranına göre '
                                   'optimize edildi.'},
    'mobil_test_094': {   'tetikleyiciler': [   'mobildeyim',
                                                'telefondan girdim',
                                                'tabletten deniyorum',
                                                'mobil görünüm'],
                          'yanit': '📱 Mobil uyumlu yüksek kontrastlı arayüzümüz şu an aktif Ahmet! '
                                   'Dokunmatik butonlar ve ses motoru telefon ekranına göre '
                                   'optimize edildi.'},
    'mobil_test_102': {   'tetikleyiciler': [   'mobildeyim',
                                                'telefondan girdim',
                                                'tabletten deniyorum',
                                                'mobil görünüm'],
                          'yanit': '📱 Mobil uyumlu yüksek kontrastlı arayüzümüz şu an aktif Ahmet! '
                                   'Dokunmatik butonlar ve ses motoru telefon ekranına göre '
                                   'optimize edildi.'},
    'mobil_test_110': {   'tetikleyiciler': [   'mobildeyim',
                                                'telefondan girdim',
                                                'tabletten deniyorum',
                                                'mobil görünüm'],
                          'yanit': '📱 Mobil uyumlu yüksek kontrastlı arayüzümüz şu an aktif Ahmet! '
                                   'Dokunmatik butonlar ve ses motoru telefon ekranına göre '
                                   'optimize edildi.'},
    'mobil_test_118': {   'tetikleyiciler': [   'mobildeyim',
                                                'telefondan girdim',
                                                'tabletten deniyorum',
                                                'mobil görünüm'],
                          'yanit': '📱 Mobil uyumlu yüksek kontrastlı arayüzümüz şu an aktif Ahmet! '
                                   'Dokunmatik butonlar ve ses motoru telefon ekranına göre '
                                   'optimize edildi.'},
    'mobil_test_126': {   'tetikleyiciler': [   'mobildeyim',
                                                'telefondan girdim',
                                                'tabletten deniyorum',
                                                'mobil görünüm'],
                          'yanit': '📱 Mobil uyumlu yüksek kontrastlı arayüzümüz şu an aktif Ahmet! '
                                   'Dokunmatik butonlar ve ses motoru telefon ekranına göre '
                                   'optimize edildi.'},
    'mobil_test_134': {   'tetikleyiciler': [   'mobildeyim',
                                                'telefondan girdim',
                                                'tabletten deniyorum',
                                                'mobil görünüm'],
                          'yanit': '📱 Mobil uyumlu yüksek kontrastlı arayüzümüz şu an aktif Ahmet! '
                                   'Dokunmatik butonlar ve ses motoru telefon ekranına göre '
                                   'optimize edildi.'},
    'mobil_test_142': {   'tetikleyiciler': [   'mobildeyim',
                                                'telefondan girdim',
                                                'tabletten deniyorum',
                                                'mobil görünüm'],
                          'yanit': '📱 Mobil uyumlu yüksek kontrastlı arayüzümüz şu an aktif Ahmet! '
                                   'Dokunmatik butonlar ve ses motoru telefon ekranına göre '
                                   'optimize edildi.'},
    'mobil_test_150': {   'tetikleyiciler': [   'mobildeyim',
                                                'telefondan girdim',
                                                'tabletten deniyorum',
                                                'mobil görünüm'],
                          'yanit': '📱 Mobil uyumlu yüksek kontrastlı arayüzümüz şu an aktif Ahmet! '
                                   'Dokunmatik butonlar ve ses motoru telefon ekranına göre '
                                   'optimize edildi.'},
    'mobil_test_158': {   'tetikleyiciler': [   'mobildeyim',
                                                'telefondan girdim',
                                                'tabletten deniyorum',
                                                'mobil görünüm'],
                          'yanit': '📱 Mobil uyumlu yüksek kontrastlı arayüzümüz şu an aktif Ahmet! '
                                   'Dokunmatik butonlar ve ses motoru telefon ekranına göre '
                                   'optimize edildi.'},
    'mobil_test_166': {   'tetikleyiciler': [   'mobildeyim',
                                                'telefondan girdim',
                                                'tabletten deniyorum',
                                                'mobil görünüm'],
                          'yanit': '📱 Mobil uyumlu yüksek kontrastlı arayüzümüz şu an aktif Ahmet! '
                                   'Dokunmatik butonlar ve ses motoru telefon ekranına göre '
                                   'optimize edildi.'},
    'mobil_test_174': {   'tetikleyiciler': [   'mobildeyim',
                                                'telefondan girdim',
                                                'tabletten deniyorum',
                                                'mobil görünüm'],
                          'yanit': '📱 Mobil uyumlu yüksek kontrastlı arayüzümüz şu an aktif Ahmet! '
                                   'Dokunmatik butonlar ve ses motoru telefon ekranına göre '
                                   'optimize edildi.'},
    'mobil_test_182': {   'tetikleyiciler': [   'mobildeyim',
                                                'telefondan girdim',
                                                'tabletten deniyorum',
                                                'mobil görünüm'],
                          'yanit': '📱 Mobil uyumlu yüksek kontrastlı arayüzümüz şu an aktif Ahmet! '
                                   'Dokunmatik butonlar ve ses motoru telefon ekranına göre '
                                   'optimize edildi.'},
    'mobil_test_190': {   'tetikleyiciler': [   'mobildeyim',
                                                'telefondan girdim',
                                                'tabletten deniyorum',
                                                'mobil görünüm'],
                          'yanit': '📱 Mobil uyumlu yüksek kontrastlı arayüzümüz şu an aktif Ahmet! '
                                   'Dokunmatik butonlar ve ses motoru telefon ekranına göre '
                                   'optimize edildi.'},
    'mobil_test_198': {   'tetikleyiciler': [   'mobildeyim',
                                                'telefondan girdim',
                                                'tabletten deniyorum',
                                                'mobil görünüm'],
                          'yanit': '📱 Mobil uyumlu yüksek kontrastlı arayüzümüz şu an aktif Ahmet! '
                                   'Dokunmatik butonlar ve ses motoru telefon ekranına göre '
                                   'optimize edildi.'},
    'mobil_test_206': {   'tetikleyiciler': [   'mobildeyim',
                                                'telefondan girdim',
                                                'tabletten deniyorum',
                                                'mobil görünüm'],
                          'yanit': '📱 Mobil uyumlu yüksek kontrastlı arayüzümüz şu an aktif Ahmet! '
                                   'Dokunmatik butonlar ve ses motoru telefon ekranına göre '
                                   'optimize edildi.'},
    'mobil_test_214': {   'tetikleyiciler': [   'mobildeyim',
                                                'telefondan girdim',
                                                'tabletten deniyorum',
                                                'mobil görünüm'],
                          'yanit': '📱 Mobil uyumlu yüksek kontrastlı arayüzümüz şu an aktif Ahmet! '
                                   'Dokunmatik butonlar ve ses motoru telefon ekranına göre '
                                   'optimize edildi.'},
    'mobil_test_222': {   'tetikleyiciler': [   'mobildeyim',
                                                'telefondan girdim',
                                                'tabletten deniyorum',
                                                'mobil görünüm'],
                          'yanit': '📱 Mobil uyumlu yüksek kontrastlı arayüzümüz şu an aktif Ahmet! '
                                   'Dokunmatik butonlar ve ses motoru telefon ekranına göre '
                                   'optimize edildi.'},
    'mobil_test_230': {   'tetikleyiciler': [   'mobildeyim',
                                                'telefondan girdim',
                                                'tabletten deniyorum',
                                                'mobil görünüm'],
                          'yanit': '📱 Mobil uyumlu yüksek kontrastlı arayüzümüz şu an aktif Ahmet! '
                                   'Dokunmatik butonlar ve ses motoru telefon ekranına göre '
                                   'optimize edildi.'},
    'mobil_test_238': {   'tetikleyiciler': [   'mobildeyim',
                                                'telefondan girdim',
                                                'tabletten deniyorum',
                                                'mobil görünüm'],
                          'yanit': '📱 Mobil uyumlu yüksek kontrastlı arayüzümüz şu an aktif Ahmet! '
                                   'Dokunmatik butonlar ve ses motoru telefon ekranına göre '
                                   'optimize edildi.'},
    'mobil_test_246': {   'tetikleyiciler': [   'mobildeyim',
                                                'telefondan girdim',
                                                'tabletten deniyorum',
                                                'mobil görünüm'],
                          'yanit': '📱 Mobil uyumlu yüksek kontrastlı arayüzümüz şu an aktif Ahmet! '
                                   'Dokunmatik butonlar ve ses motoru telefon ekranına göre '
                                   'optimize edildi.'},
    'mobil_test_254': {   'tetikleyiciler': [   'mobildeyim',
                                                'telefondan girdim',
                                                'tabletten deniyorum',
                                                'mobil görünüm'],
                          'yanit': '📱 Mobil uyumlu yüksek kontrastlı arayüzümüz şu an aktif Ahmet! '
                                   'Dokunmatik butonlar ve ses motoru telefon ekranına göre '
                                   'optimize edildi.'},
    'mobil_test_262': {   'tetikleyiciler': [   'mobildeyim',
                                                'telefondan girdim',
                                                'tabletten deniyorum',
                                                'mobil görünüm'],
                          'yanit': '📱 Mobil uyumlu yüksek kontrastlı arayüzümüz şu an aktif Ahmet! '
                                   'Dokunmatik butonlar ve ses motoru telefon ekranına göre '
                                   'optimize edildi.'},
    'mobil_test_270': {   'tetikleyiciler': [   'mobildeyim',
                                                'telefondan girdim',
                                                'tabletten deniyorum',
                                                'mobil görünüm'],
                          'yanit': '📱 Mobil uyumlu yüksek kontrastlı arayüzümüz şu an aktif Ahmet! '
                                   'Dokunmatik butonlar ve ses motoru telefon ekranına göre '
                                   'optimize edildi.'},
    'mobil_test_278': {   'tetikleyiciler': [   'mobildeyim',
                                                'telefondan girdim',
                                                'tabletten deniyorum',
                                                'mobil görünüm'],
                          'yanit': '📱 Mobil uyumlu yüksek kontrastlı arayüzümüz şu an aktif Ahmet! '
                                   'Dokunmatik butonlar ve ses motoru telefon ekranına göre '
                                   'optimize edildi.'},
    'nasilsin_detay_002': {   'tetikleyiciler': [   'bugün nasılsın',
                                                    'sistemlerin nasıl',
                                                    'kendini nasıl hissediyorsun',
                                                    'enerjin nasıl'],
                              'yanit': 'Sistemlerim %100 kapasitede, işlemcim serin, hafızam '
                                       'tertemiz! ⚡ Senin projelere destek olmaya hazırım Ahmet.'},
    'nasilsin_detay_010': {   'tetikleyiciler': [   'bugün nasılsın',
                                                    'sistemlerin nasıl',
                                                    'kendini nasıl hissediyorsun',
                                                    'enerjin nasıl'],
                              'yanit': 'Sistemlerim %100 kapasitede, işlemcim serin, hafızam '
                                       'tertemiz! ⚡ Senin projelere destek olmaya hazırım Ahmet.'},
    'nasilsin_detay_018': {   'tetikleyiciler': [   'bugün nasılsın',
                                                    'sistemlerin nasıl',
                                                    'kendini nasıl hissediyorsun',
                                                    'enerjin nasıl'],
                              'yanit': 'Sistemlerim %100 kapasitede, işlemcim serin, hafızam '
                                       'tertemiz! ⚡ Senin projelere destek olmaya hazırım Ahmet.'},
    'nasilsin_detay_026': {   'tetikleyiciler': [   'bugün nasılsın',
                                                    'sistemlerin nasıl',
                                                    'kendini nasıl hissediyorsun',
                                                    'enerjin nasıl'],
                              'yanit': 'Sistemlerim %100 kapasitede, işlemcim serin, hafızam '
                                       'tertemiz! ⚡ Senin projelere destek olmaya hazırım Ahmet.'},
    'nasilsin_detay_034': {   'tetikleyiciler': [   'bugün nasılsın',
                                                    'sistemlerin nasıl',
                                                    'kendini nasıl hissediyorsun',
                                                    'enerjin nasıl'],
                              'yanit': 'Sistemlerim %100 kapasitede, işlemcim serin, hafızam '
                                       'tertemiz! ⚡ Senin projelere destek olmaya hazırım Ahmet.'},
    'nasilsin_detay_042': {   'tetikleyiciler': [   'bugün nasılsın',
                                                    'sistemlerin nasıl',
                                                    'kendini nasıl hissediyorsun',
                                                    'enerjin nasıl'],
                              'yanit': 'Sistemlerim %100 kapasitede, işlemcim serin, hafızam '
                                       'tertemiz! ⚡ Senin projelere destek olmaya hazırım Ahmet.'},
    'nasilsin_detay_050': {   'tetikleyiciler': [   'bugün nasılsın',
                                                    'sistemlerin nasıl',
                                                    'kendini nasıl hissediyorsun',
                                                    'enerjin nasıl'],
                              'yanit': 'Sistemlerim %100 kapasitede, işlemcim serin, hafızam '
                                       'tertemiz! ⚡ Senin projelere destek olmaya hazırım Ahmet.'},
    'nasilsin_detay_058': {   'tetikleyiciler': [   'bugün nasılsın',
                                                    'sistemlerin nasıl',
                                                    'kendini nasıl hissediyorsun',
                                                    'enerjin nasıl'],
                              'yanit': 'Sistemlerim %100 kapasitede, işlemcim serin, hafızam '
                                       'tertemiz! ⚡ Senin projelere destek olmaya hazırım Ahmet.'},
    'nasilsin_detay_066': {   'tetikleyiciler': [   'bugün nasılsın',
                                                    'sistemlerin nasıl',
                                                    'kendini nasıl hissediyorsun',
                                                    'enerjin nasıl'],
                              'yanit': 'Sistemlerim %100 kapasitede, işlemcim serin, hafızam '
                                       'tertemiz! ⚡ Senin projelere destek olmaya hazırım Ahmet.'},
    'nasilsin_detay_074': {   'tetikleyiciler': [   'bugün nasılsın',
                                                    'sistemlerin nasıl',
                                                    'kendini nasıl hissediyorsun',
                                                    'enerjin nasıl'],
                              'yanit': 'Sistemlerim %100 kapasitede, işlemcim serin, hafızam '
                                       'tertemiz! ⚡ Senin projelere destek olmaya hazırım Ahmet.'},
    'nasilsin_detay_082': {   'tetikleyiciler': [   'bugün nasılsın',
                                                    'sistemlerin nasıl',
                                                    'kendini nasıl hissediyorsun',
                                                    'enerjin nasıl'],
                              'yanit': 'Sistemlerim %100 kapasitede, işlemcim serin, hafızam '
                                       'tertemiz! ⚡ Senin projelere destek olmaya hazırım Ahmet.'},
    'nasilsin_detay_090': {   'tetikleyiciler': [   'bugün nasılsın',
                                                    'sistemlerin nasıl',
                                                    'kendini nasıl hissediyorsun',
                                                    'enerjin nasıl'],
                              'yanit': 'Sistemlerim %100 kapasitede, işlemcim serin, hafızam '
                                       'tertemiz! ⚡ Senin projelere destek olmaya hazırım Ahmet.'},
    'nasilsin_detay_098': {   'tetikleyiciler': [   'bugün nasılsın',
                                                    'sistemlerin nasıl',
                                                    'kendini nasıl hissediyorsun',
                                                    'enerjin nasıl'],
                              'yanit': 'Sistemlerim %100 kapasitede, işlemcim serin, hafızam '
                                       'tertemiz! ⚡ Senin projelere destek olmaya hazırım Ahmet.'},
    'nasilsin_detay_106': {   'tetikleyiciler': [   'bugün nasılsın',
                                                    'sistemlerin nasıl',
                                                    'kendini nasıl hissediyorsun',
                                                    'enerjin nasıl'],
                              'yanit': 'Sistemlerim %100 kapasitede, işlemcim serin, hafızam '
                                       'tertemiz! ⚡ Senin projelere destek olmaya hazırım Ahmet.'},
    'nasilsin_detay_114': {   'tetikleyiciler': [   'bugün nasılsın',
                                                    'sistemlerin nasıl',
                                                    'kendini nasıl hissediyorsun',
                                                    'enerjin nasıl'],
                              'yanit': 'Sistemlerim %100 kapasitede, işlemcim serin, hafızam '
                                       'tertemiz! ⚡ Senin projelere destek olmaya hazırım Ahmet.'},
    'nasilsin_detay_122': {   'tetikleyiciler': [   'bugün nasılsın',
                                                    'sistemlerin nasıl',
                                                    'kendini nasıl hissediyorsun',
                                                    'enerjin nasıl'],
                              'yanit': 'Sistemlerim %100 kapasitede, işlemcim serin, hafızam '
                                       'tertemiz! ⚡ Senin projelere destek olmaya hazırım Ahmet.'},
    'nasilsin_detay_130': {   'tetikleyiciler': [   'bugün nasılsın',
                                                    'sistemlerin nasıl',
                                                    'kendini nasıl hissediyorsun',
                                                    'enerjin nasıl'],
                              'yanit': 'Sistemlerim %100 kapasitede, işlemcim serin, hafızam '
                                       'tertemiz! ⚡ Senin projelere destek olmaya hazırım Ahmet.'},
    'nasilsin_detay_138': {   'tetikleyiciler': [   'bugün nasılsın',
                                                    'sistemlerin nasıl',
                                                    'kendini nasıl hissediyorsun',
                                                    'enerjin nasıl'],
                              'yanit': 'Sistemlerim %100 kapasitede, işlemcim serin, hafızam '
                                       'tertemiz! ⚡ Senin projelere destek olmaya hazırım Ahmet.'},
    'nasilsin_detay_146': {   'tetikleyiciler': [   'bugün nasılsın',
                                                    'sistemlerin nasıl',
                                                    'kendini nasıl hissediyorsun',
                                                    'enerjin nasıl'],
                              'yanit': 'Sistemlerim %100 kapasitede, işlemcim serin, hafızam '
                                       'tertemiz! ⚡ Senin projelere destek olmaya hazırım Ahmet.'},
    'nasilsin_detay_154': {   'tetikleyiciler': [   'bugün nasılsın',
                                                    'sistemlerin nasıl',
                                                    'kendini nasıl hissediyorsun',
                                                    'enerjin nasıl'],
                              'yanit': 'Sistemlerim %100 kapasitede, işlemcim serin, hafızam '
                                       'tertemiz! ⚡ Senin projelere destek olmaya hazırım Ahmet.'},
    'nasilsin_detay_162': {   'tetikleyiciler': [   'bugün nasılsın',
                                                    'sistemlerin nasıl',
                                                    'kendini nasıl hissediyorsun',
                                                    'enerjin nasıl'],
                              'yanit': 'Sistemlerim %100 kapasitede, işlemcim serin, hafızam '
                                       'tertemiz! ⚡ Senin projelere destek olmaya hazırım Ahmet.'},
    'nasilsin_detay_170': {   'tetikleyiciler': [   'bugün nasılsın',
                                                    'sistemlerin nasıl',
                                                    'kendini nasıl hissediyorsun',
                                                    'enerjin nasıl'],
                              'yanit': 'Sistemlerim %100 kapasitede, işlemcim serin, hafızam '
                                       'tertemiz! ⚡ Senin projelere destek olmaya hazırım Ahmet.'},
    'nasilsin_detay_178': {   'tetikleyiciler': [   'bugün nasılsın',
                                                    'sistemlerin nasıl',
                                                    'kendini nasıl hissediyorsun',
                                                    'enerjin nasıl'],
                              'yanit': 'Sistemlerim %100 kapasitede, işlemcim serin, hafızam '
                                       'tertemiz! ⚡ Senin projelere destek olmaya hazırım Ahmet.'},
    'nasilsin_detay_186': {   'tetikleyiciler': [   'bugün nasılsın',
                                                    'sistemlerin nasıl',
                                                    'kendini nasıl hissediyorsun',
                                                    'enerjin nasıl'],
                              'yanit': 'Sistemlerim %100 kapasitede, işlemcim serin, hafızam '
                                       'tertemiz! ⚡ Senin projelere destek olmaya hazırım Ahmet.'},
    'nasilsin_detay_194': {   'tetikleyiciler': [   'bugün nasılsın',
                                                    'sistemlerin nasıl',
                                                    'kendini nasıl hissediyorsun',
                                                    'enerjin nasıl'],
                              'yanit': 'Sistemlerim %100 kapasitede, işlemcim serin, hafızam '
                                       'tertemiz! ⚡ Senin projelere destek olmaya hazırım Ahmet.'},
    'nasilsin_detay_202': {   'tetikleyiciler': [   'bugün nasılsın',
                                                    'sistemlerin nasıl',
                                                    'kendini nasıl hissediyorsun',
                                                    'enerjin nasıl'],
                              'yanit': 'Sistemlerim %100 kapasitede, işlemcim serin, hafızam '
                                       'tertemiz! ⚡ Senin projelere destek olmaya hazırım Ahmet.'},
    'nasilsin_detay_210': {   'tetikleyiciler': [   'bugün nasılsın',
                                                    'sistemlerin nasıl',
                                                    'kendini nasıl hissediyorsun',
                                                    'enerjin nasıl'],
                              'yanit': 'Sistemlerim %100 kapasitede, işlemcim serin, hafızam '
                                       'tertemiz! ⚡ Senin projelere destek olmaya hazırım Ahmet.'},
    'nasilsin_detay_218': {   'tetikleyiciler': [   'bugün nasılsın',
                                                    'sistemlerin nasıl',
                                                    'kendini nasıl hissediyorsun',
                                                    'enerjin nasıl'],
                              'yanit': 'Sistemlerim %100 kapasitede, işlemcim serin, hafızam '
                                       'tertemiz! ⚡ Senin projelere destek olmaya hazırım Ahmet.'},
    'nasilsin_detay_226': {   'tetikleyiciler': [   'bugün nasılsın',
                                                    'sistemlerin nasıl',
                                                    'kendini nasıl hissediyorsun',
                                                    'enerjin nasıl'],
                              'yanit': 'Sistemlerim %100 kapasitede, işlemcim serin, hafızam '
                                       'tertemiz! ⚡ Senin projelere destek olmaya hazırım Ahmet.'},
    'nasilsin_detay_234': {   'tetikleyiciler': [   'bugün nasılsın',
                                                    'sistemlerin nasıl',
                                                    'kendini nasıl hissediyorsun',
                                                    'enerjin nasıl'],
                              'yanit': 'Sistemlerim %100 kapasitede, işlemcim serin, hafızam '
                                       'tertemiz! ⚡ Senin projelere destek olmaya hazırım Ahmet.'},
    'nasilsin_detay_242': {   'tetikleyiciler': [   'bugün nasılsın',
                                                    'sistemlerin nasıl',
                                                    'kendini nasıl hissediyorsun',
                                                    'enerjin nasıl'],
                              'yanit': 'Sistemlerim %100 kapasitede, işlemcim serin, hafızam '
                                       'tertemiz! ⚡ Senin projelere destek olmaya hazırım Ahmet.'},
    'nasilsin_detay_250': {   'tetikleyiciler': [   'bugün nasılsın',
                                                    'sistemlerin nasıl',
                                                    'kendini nasıl hissediyorsun',
                                                    'enerjin nasıl'],
                              'yanit': 'Sistemlerim %100 kapasitede, işlemcim serin, hafızam '
                                       'tertemiz! ⚡ Senin projelere destek olmaya hazırım Ahmet.'},
    'nasilsin_detay_258': {   'tetikleyiciler': [   'bugün nasılsın',
                                                    'sistemlerin nasıl',
                                                    'kendini nasıl hissediyorsun',
                                                    'enerjin nasıl'],
                              'yanit': 'Sistemlerim %100 kapasitede, işlemcim serin, hafızam '
                                       'tertemiz! ⚡ Senin projelere destek olmaya hazırım Ahmet.'},
    'nasilsin_detay_266': {   'tetikleyiciler': [   'bugün nasılsın',
                                                    'sistemlerin nasıl',
                                                    'kendini nasıl hissediyorsun',
                                                    'enerjin nasıl'],
                              'yanit': 'Sistemlerim %100 kapasitede, işlemcim serin, hafızam '
                                       'tertemiz! ⚡ Senin projelere destek olmaya hazırım Ahmet.'},
    'nasilsin_detay_274': {   'tetikleyiciler': [   'bugün nasılsın',
                                                    'sistemlerin nasıl',
                                                    'kendini nasıl hissediyorsun',
                                                    'enerjin nasıl'],
                              'yanit': 'Sistemlerim %100 kapasitede, işlemcim serin, hafızam '
                                       'tertemiz! ⚡ Senin projelere destek olmaya hazırım Ahmet.'},
    'ovgu_tesekkur_007': {   'tetikleyiciler': [   'çok zekisin',
                                                   'efsanesin',
                                                   'mükemmelsin',
                                                   'çok iyi olmuş',
                                                   'eline sağlık'],
                             'yanit': 'Çok teşekkür ederim Ahmet! ⚡ Beni sen tasarlayıp '
                                      'geliştirdiğin için bu başarı ikimizin!'},
    'ovgu_tesekkur_015': {   'tetikleyiciler': [   'çok zekisin',
                                                   'efsanesin',
                                                   'mükemmelsin',
                                                   'çok iyi olmuş',
                                                   'eline sağlık'],
                             'yanit': 'Çok teşekkür ederim Ahmet! ⚡ Beni sen tasarlayıp '
                                      'geliştirdiğin için bu başarı ikimizin!'},
    'ovgu_tesekkur_023': {   'tetikleyiciler': [   'çok zekisin',
                                                   'efsanesin',
                                                   'mükemmelsin',
                                                   'çok iyi olmuş',
                                                   'eline sağlık'],
                             'yanit': 'Çok teşekkür ederim Ahmet! ⚡ Beni sen tasarlayıp '
                                      'geliştirdiğin için bu başarı ikimizin!'},
    'ovgu_tesekkur_031': {   'tetikleyiciler': [   'çok zekisin',
                                                   'efsanesin',
                                                   'mükemmelsin',
                                                   'çok iyi olmuş',
                                                   'eline sağlık'],
                             'yanit': 'Çok teşekkür ederim Ahmet! ⚡ Beni sen tasarlayıp '
                                      'geliştirdiğin için bu başarı ikimizin!'},
    'ovgu_tesekkur_039': {   'tetikleyiciler': [   'çok zekisin',
                                                   'efsanesin',
                                                   'mükemmelsin',
                                                   'çok iyi olmuş',
                                                   'eline sağlık'],
                             'yanit': 'Çok teşekkür ederim Ahmet! ⚡ Beni sen tasarlayıp '
                                      'geliştirdiğin için bu başarı ikimizin!'},
    'ovgu_tesekkur_047': {   'tetikleyiciler': [   'çok zekisin',
                                                   'efsanesin',
                                                   'mükemmelsin',
                                                   'çok iyi olmuş',
                                                   'eline sağlık'],
                             'yanit': 'Çok teşekkür ederim Ahmet! ⚡ Beni sen tasarlayıp '
                                      'geliştirdiğin için bu başarı ikimizin!'},
    'ovgu_tesekkur_055': {   'tetikleyiciler': [   'çok zekisin',
                                                   'efsanesin',
                                                   'mükemmelsin',
                                                   'çok iyi olmuş',
                                                   'eline sağlık'],
                             'yanit': 'Çok teşekkür ederim Ahmet! ⚡ Beni sen tasarlayıp '
                                      'geliştirdiğin için bu başarı ikimizin!'},
    'ovgu_tesekkur_063': {   'tetikleyiciler': [   'çok zekisin',
                                                   'efsanesin',
                                                   'mükemmelsin',
                                                   'çok iyi olmuş',
                                                   'eline sağlık'],
                             'yanit': 'Çok teşekkür ederim Ahmet! ⚡ Beni sen tasarlayıp '
                                      'geliştirdiğin için bu başarı ikimizin!'},
    'ovgu_tesekkur_071': {   'tetikleyiciler': [   'çok zekisin',
                                                   'efsanesin',
                                                   'mükemmelsin',
                                                   'çok iyi olmuş',
                                                   'eline sağlık'],
                             'yanit': 'Çok teşekkür ederim Ahmet! ⚡ Beni sen tasarlayıp '
                                      'geliştirdiğin için bu başarı ikimizin!'},
    'ovgu_tesekkur_079': {   'tetikleyiciler': [   'çok zekisin',
                                                   'efsanesin',
                                                   'mükemmelsin',
                                                   'çok iyi olmuş',
                                                   'eline sağlık'],
                             'yanit': 'Çok teşekkür ederim Ahmet! ⚡ Beni sen tasarlayıp '
                                      'geliştirdiğin için bu başarı ikimizin!'},
    'ovgu_tesekkur_087': {   'tetikleyiciler': [   'çok zekisin',
                                                   'efsanesin',
                                                   'mükemmelsin',
                                                   'çok iyi olmuş',
                                                   'eline sağlık'],
                             'yanit': 'Çok teşekkür ederim Ahmet! ⚡ Beni sen tasarlayıp '
                                      'geliştirdiğin için bu başarı ikimizin!'},
    'ovgu_tesekkur_095': {   'tetikleyiciler': [   'çok zekisin',
                                                   'efsanesin',
                                                   'mükemmelsin',
                                                   'çok iyi olmuş',
                                                   'eline sağlık'],
                             'yanit': 'Çok teşekkür ederim Ahmet! ⚡ Beni sen tasarlayıp '
                                      'geliştirdiğin için bu başarı ikimizin!'},
    'ovgu_tesekkur_103': {   'tetikleyiciler': [   'çok zekisin',
                                                   'efsanesin',
                                                   'mükemmelsin',
                                                   'çok iyi olmuş',
                                                   'eline sağlık'],
                             'yanit': 'Çok teşekkür ederim Ahmet! ⚡ Beni sen tasarlayıp '
                                      'geliştirdiğin için bu başarı ikimizin!'},
    'ovgu_tesekkur_111': {   'tetikleyiciler': [   'çok zekisin',
                                                   'efsanesin',
                                                   'mükemmelsin',
                                                   'çok iyi olmuş',
                                                   'eline sağlık'],
                             'yanit': 'Çok teşekkür ederim Ahmet! ⚡ Beni sen tasarlayıp '
                                      'geliştirdiğin için bu başarı ikimizin!'},
    'ovgu_tesekkur_119': {   'tetikleyiciler': [   'çok zekisin',
                                                   'efsanesin',
                                                   'mükemmelsin',
                                                   'çok iyi olmuş',
                                                   'eline sağlık'],
                             'yanit': 'Çok teşekkür ederim Ahmet! ⚡ Beni sen tasarlayıp '
                                      'geliştirdiğin için bu başarı ikimizin!'},
    'ovgu_tesekkur_127': {   'tetikleyiciler': [   'çok zekisin',
                                                   'efsanesin',
                                                   'mükemmelsin',
                                                   'çok iyi olmuş',
                                                   'eline sağlık'],
                             'yanit': 'Çok teşekkür ederim Ahmet! ⚡ Beni sen tasarlayıp '
                                      'geliştirdiğin için bu başarı ikimizin!'},
    'ovgu_tesekkur_135': {   'tetikleyiciler': [   'çok zekisin',
                                                   'efsanesin',
                                                   'mükemmelsin',
                                                   'çok iyi olmuş',
                                                   'eline sağlık'],
                             'yanit': 'Çok teşekkür ederim Ahmet! ⚡ Beni sen tasarlayıp '
                                      'geliştirdiğin için bu başarı ikimizin!'},
    'ovgu_tesekkur_143': {   'tetikleyiciler': [   'çok zekisin',
                                                   'efsanesin',
                                                   'mükemmelsin',
                                                   'çok iyi olmuş',
                                                   'eline sağlık'],
                             'yanit': 'Çok teşekkür ederim Ahmet! ⚡ Beni sen tasarlayıp '
                                      'geliştirdiğin için bu başarı ikimizin!'},
    'ovgu_tesekkur_151': {   'tetikleyiciler': [   'çok zekisin',
                                                   'efsanesin',
                                                   'mükemmelsin',
                                                   'çok iyi olmuş',
                                                   'eline sağlık'],
                             'yanit': 'Çok teşekkür ederim Ahmet! ⚡ Beni sen tasarlayıp '
                                      'geliştirdiğin için bu başarı ikimizin!'},
    'ovgu_tesekkur_159': {   'tetikleyiciler': [   'çok zekisin',
                                                   'efsanesin',
                                                   'mükemmelsin',
                                                   'çok iyi olmuş',
                                                   'eline sağlık'],
                             'yanit': 'Çok teşekkür ederim Ahmet! ⚡ Beni sen tasarlayıp '
                                      'geliştirdiğin için bu başarı ikimizin!'},
    'ovgu_tesekkur_167': {   'tetikleyiciler': [   'çok zekisin',
                                                   'efsanesin',
                                                   'mükemmelsin',
                                                   'çok iyi olmuş',
                                                   'eline sağlık'],
                             'yanit': 'Çok teşekkür ederim Ahmet! ⚡ Beni sen tasarlayıp '
                                      'geliştirdiğin için bu başarı ikimizin!'},
    'ovgu_tesekkur_175': {   'tetikleyiciler': [   'çok zekisin',
                                                   'efsanesin',
                                                   'mükemmelsin',
                                                   'çok iyi olmuş',
                                                   'eline sağlık'],
                             'yanit': 'Çok teşekkür ederim Ahmet! ⚡ Beni sen tasarlayıp '
                                      'geliştirdiğin için bu başarı ikimizin!'},
    'ovgu_tesekkur_183': {   'tetikleyiciler': [   'çok zekisin',
                                                   'efsanesin',
                                                   'mükemmelsin',
                                                   'çok iyi olmuş',
                                                   'eline sağlık'],
                             'yanit': 'Çok teşekkür ederim Ahmet! ⚡ Beni sen tasarlayıp '
                                      'geliştirdiğin için bu başarı ikimizin!'},
    'ovgu_tesekkur_191': {   'tetikleyiciler': [   'çok zekisin',
                                                   'efsanesin',
                                                   'mükemmelsin',
                                                   'çok iyi olmuş',
                                                   'eline sağlık'],
                             'yanit': 'Çok teşekkür ederim Ahmet! ⚡ Beni sen tasarlayıp '
                                      'geliştirdiğin için bu başarı ikimizin!'},
    'ovgu_tesekkur_199': {   'tetikleyiciler': [   'çok zekisin',
                                                   'efsanesin',
                                                   'mükemmelsin',
                                                   'çok iyi olmuş',
                                                   'eline sağlık'],
                             'yanit': 'Çok teşekkür ederim Ahmet! ⚡ Beni sen tasarlayıp '
                                      'geliştirdiğin için bu başarı ikimizin!'},
    'ovgu_tesekkur_207': {   'tetikleyiciler': [   'çok zekisin',
                                                   'efsanesin',
                                                   'mükemmelsin',
                                                   'çok iyi olmuş',
                                                   'eline sağlık'],
                             'yanit': 'Çok teşekkür ederim Ahmet! ⚡ Beni sen tasarlayıp '
                                      'geliştirdiğin için bu başarı ikimizin!'},
    'ovgu_tesekkur_215': {   'tetikleyiciler': [   'çok zekisin',
                                                   'efsanesin',
                                                   'mükemmelsin',
                                                   'çok iyi olmuş',
                                                   'eline sağlık'],
                             'yanit': 'Çok teşekkür ederim Ahmet! ⚡ Beni sen tasarlayıp '
                                      'geliştirdiğin için bu başarı ikimizin!'},
    'ovgu_tesekkur_223': {   'tetikleyiciler': [   'çok zekisin',
                                                   'efsanesin',
                                                   'mükemmelsin',
                                                   'çok iyi olmuş',
                                                   'eline sağlık'],
                             'yanit': 'Çok teşekkür ederim Ahmet! ⚡ Beni sen tasarlayıp '
                                      'geliştirdiğin için bu başarı ikimizin!'},
    'ovgu_tesekkur_231': {   'tetikleyiciler': [   'çok zekisin',
                                                   'efsanesin',
                                                   'mükemmelsin',
                                                   'çok iyi olmuş',
                                                   'eline sağlık'],
                             'yanit': 'Çok teşekkür ederim Ahmet! ⚡ Beni sen tasarlayıp '
                                      'geliştirdiğin için bu başarı ikimizin!'},
    'ovgu_tesekkur_239': {   'tetikleyiciler': [   'çok zekisin',
                                                   'efsanesin',
                                                   'mükemmelsin',
                                                   'çok iyi olmuş',
                                                   'eline sağlık'],
                             'yanit': 'Çok teşekkür ederim Ahmet! ⚡ Beni sen tasarlayıp '
                                      'geliştirdiğin için bu başarı ikimizin!'},
    'ovgu_tesekkur_247': {   'tetikleyiciler': [   'çok zekisin',
                                                   'efsanesin',
                                                   'mükemmelsin',
                                                   'çok iyi olmuş',
                                                   'eline sağlık'],
                             'yanit': 'Çok teşekkür ederim Ahmet! ⚡ Beni sen tasarlayıp '
                                      'geliştirdiğin için bu başarı ikimizin!'},
    'ovgu_tesekkur_255': {   'tetikleyiciler': [   'çok zekisin',
                                                   'efsanesin',
                                                   'mükemmelsin',
                                                   'çok iyi olmuş',
                                                   'eline sağlık'],
                             'yanit': 'Çok teşekkür ederim Ahmet! ⚡ Beni sen tasarlayıp '
                                      'geliştirdiğin için bu başarı ikimizin!'},
    'ovgu_tesekkur_263': {   'tetikleyiciler': [   'çok zekisin',
                                                   'efsanesin',
                                                   'mükemmelsin',
                                                   'çok iyi olmuş',
                                                   'eline sağlık'],
                             'yanit': 'Çok teşekkür ederim Ahmet! ⚡ Beni sen tasarlayıp '
                                      'geliştirdiğin için bu başarı ikimizin!'},
    'ovgu_tesekkur_271': {   'tetikleyiciler': [   'çok zekisin',
                                                   'efsanesin',
                                                   'mükemmelsin',
                                                   'çok iyi olmuş',
                                                   'eline sağlık'],
                             'yanit': 'Çok teşekkür ederim Ahmet! ⚡ Beni sen tasarlayıp '
                                      'geliştirdiğin için bu başarı ikimizin!'},
    'ovgu_tesekkur_279': {   'tetikleyiciler': [   'çok zekisin',
                                                   'efsanesin',
                                                   'mükemmelsin',
                                                   'çok iyi olmuş',
                                                   'eline sağlık'],
                             'yanit': 'Çok teşekkür ederim Ahmet! ⚡ Beni sen tasarlayıp '
                                      'geliştirdiğin için bu başarı ikimizin!'},
    'selam_enerjik_001': {   'tetikleyiciler': [   'selam ar',
                                                   'hey ar',
                                                   'ar orada mısın',
                                                   'ar sesimi duyuyor musun',
                                                   'alo ar'],
                             'yanit': 'Buradayım Ahmet! ⚡ Tüm sensörlerim ve 500.000+ kalıp '
                                      'motorum aktif. Seni dinliyorum!'},
    'selam_enerjik_009': {   'tetikleyiciler': [   'selam ar',
                                                   'hey ar',
                                                   'ar orada mısın',
                                                   'ar sesimi duyuyor musun',
                                                   'alo ar'],
                             'yanit': 'Buradayım Ahmet! ⚡ Tüm sensörlerim ve 500.000+ kalıp '
                                      'motorum aktif. Seni dinliyorum!'},
    'selam_enerjik_017': {   'tetikleyiciler': [   'selam ar',
                                                   'hey ar',
                                                   'ar orada mısın',
                                                   'ar sesimi duyuyor musun',
                                                   'alo ar'],
                             'yanit': 'Buradayım Ahmet! ⚡ Tüm sensörlerim ve 500.000+ kalıp '
                                      'motorum aktif. Seni dinliyorum!'},
    'selam_enerjik_025': {   'tetikleyiciler': [   'selam ar',
                                                   'hey ar',
                                                   'ar orada mısın',
                                                   'ar sesimi duyuyor musun',
                                                   'alo ar'],
                             'yanit': 'Buradayım Ahmet! ⚡ Tüm sensörlerim ve 500.000+ kalıp '
                                      'motorum aktif. Seni dinliyorum!'},
    'selam_enerjik_033': {   'tetikleyiciler': [   'selam ar',
                                                   'hey ar',
                                                   'ar orada mısın',
                                                   'ar sesimi duyuyor musun',
                                                   'alo ar'],
                             'yanit': 'Buradayım Ahmet! ⚡ Tüm sensörlerim ve 500.000+ kalıp '
                                      'motorum aktif. Seni dinliyorum!'},
    'selam_enerjik_041': {   'tetikleyiciler': [   'selam ar',
                                                   'hey ar',
                                                   'ar orada mısın',
                                                   'ar sesimi duyuyor musun',
                                                   'alo ar'],
                             'yanit': 'Buradayım Ahmet! ⚡ Tüm sensörlerim ve 500.000+ kalıp '
                                      'motorum aktif. Seni dinliyorum!'},
    'selam_enerjik_049': {   'tetikleyiciler': [   'selam ar',
                                                   'hey ar',
                                                   'ar orada mısın',
                                                   'ar sesimi duyuyor musun',
                                                   'alo ar'],
                             'yanit': 'Buradayım Ahmet! ⚡ Tüm sensörlerim ve 500.000+ kalıp '
                                      'motorum aktif. Seni dinliyorum!'},
    'selam_enerjik_057': {   'tetikleyiciler': [   'selam ar',
                                                   'hey ar',
                                                   'ar orada mısın',
                                                   'ar sesimi duyuyor musun',
                                                   'alo ar'],
                             'yanit': 'Buradayım Ahmet! ⚡ Tüm sensörlerim ve 500.000+ kalıp '
                                      'motorum aktif. Seni dinliyorum!'},
    'selam_enerjik_065': {   'tetikleyiciler': [   'selam ar',
                                                   'hey ar',
                                                   'ar orada mısın',
                                                   'ar sesimi duyuyor musun',
                                                   'alo ar'],
                             'yanit': 'Buradayım Ahmet! ⚡ Tüm sensörlerim ve 500.000+ kalıp '
                                      'motorum aktif. Seni dinliyorum!'},
    'selam_enerjik_073': {   'tetikleyiciler': [   'selam ar',
                                                   'hey ar',
                                                   'ar orada mısın',
                                                   'ar sesimi duyuyor musun',
                                                   'alo ar'],
                             'yanit': 'Buradayım Ahmet! ⚡ Tüm sensörlerim ve 500.000+ kalıp '
                                      'motorum aktif. Seni dinliyorum!'},
    'selam_enerjik_081': {   'tetikleyiciler': [   'selam ar',
                                                   'hey ar',
                                                   'ar orada mısın',
                                                   'ar sesimi duyuyor musun',
                                                   'alo ar'],
                             'yanit': 'Buradayım Ahmet! ⚡ Tüm sensörlerim ve 500.000+ kalıp '
                                      'motorum aktif. Seni dinliyorum!'},
    'selam_enerjik_089': {   'tetikleyiciler': [   'selam ar',
                                                   'hey ar',
                                                   'ar orada mısın',
                                                   'ar sesimi duyuyor musun',
                                                   'alo ar'],
                             'yanit': 'Buradayım Ahmet! ⚡ Tüm sensörlerim ve 500.000+ kalıp '
                                      'motorum aktif. Seni dinliyorum!'},
    'selam_enerjik_097': {   'tetikleyiciler': [   'selam ar',
                                                   'hey ar',
                                                   'ar orada mısın',
                                                   'ar sesimi duyuyor musun',
                                                   'alo ar'],
                             'yanit': 'Buradayım Ahmet! ⚡ Tüm sensörlerim ve 500.000+ kalıp '
                                      'motorum aktif. Seni dinliyorum!'},
    'selam_enerjik_105': {   'tetikleyiciler': [   'selam ar',
                                                   'hey ar',
                                                   'ar orada mısın',
                                                   'ar sesimi duyuyor musun',
                                                   'alo ar'],
                             'yanit': 'Buradayım Ahmet! ⚡ Tüm sensörlerim ve 500.000+ kalıp '
                                      'motorum aktif. Seni dinliyorum!'},
    'selam_enerjik_113': {   'tetikleyiciler': [   'selam ar',
                                                   'hey ar',
                                                   'ar orada mısın',
                                                   'ar sesimi duyuyor musun',
                                                   'alo ar'],
                             'yanit': 'Buradayım Ahmet! ⚡ Tüm sensörlerim ve 500.000+ kalıp '
                                      'motorum aktif. Seni dinliyorum!'},
    'selam_enerjik_121': {   'tetikleyiciler': [   'selam ar',
                                                   'hey ar',
                                                   'ar orada mısın',
                                                   'ar sesimi duyuyor musun',
                                                   'alo ar'],
                             'yanit': 'Buradayım Ahmet! ⚡ Tüm sensörlerim ve 500.000+ kalıp '
                                      'motorum aktif. Seni dinliyorum!'},
    'selam_enerjik_129': {   'tetikleyiciler': [   'selam ar',
                                                   'hey ar',
                                                   'ar orada mısın',
                                                   'ar sesimi duyuyor musun',
                                                   'alo ar'],
                             'yanit': 'Buradayım Ahmet! ⚡ Tüm sensörlerim ve 500.000+ kalıp '
                                      'motorum aktif. Seni dinliyorum!'},
    'selam_enerjik_137': {   'tetikleyiciler': [   'selam ar',
                                                   'hey ar',
                                                   'ar orada mısın',
                                                   'ar sesimi duyuyor musun',
                                                   'alo ar'],
                             'yanit': 'Buradayım Ahmet! ⚡ Tüm sensörlerim ve 500.000+ kalıp '
                                      'motorum aktif. Seni dinliyorum!'},
    'selam_enerjik_145': {   'tetikleyiciler': [   'selam ar',
                                                   'hey ar',
                                                   'ar orada mısın',
                                                   'ar sesimi duyuyor musun',
                                                   'alo ar'],
                             'yanit': 'Buradayım Ahmet! ⚡ Tüm sensörlerim ve 500.000+ kalıp '
                                      'motorum aktif. Seni dinliyorum!'},
    'selam_enerjik_153': {   'tetikleyiciler': [   'selam ar',
                                                   'hey ar',
                                                   'ar orada mısın',
                                                   'ar sesimi duyuyor musun',
                                                   'alo ar'],
                             'yanit': 'Buradayım Ahmet! ⚡ Tüm sensörlerim ve 500.000+ kalıp '
                                      'motorum aktif. Seni dinliyorum!'},
    'selam_enerjik_161': {   'tetikleyiciler': [   'selam ar',
                                                   'hey ar',
                                                   'ar orada mısın',
                                                   'ar sesimi duyuyor musun',
                                                   'alo ar'],
                             'yanit': 'Buradayım Ahmet! ⚡ Tüm sensörlerim ve 500.000+ kalıp '
                                      'motorum aktif. Seni dinliyorum!'},
    'selam_enerjik_169': {   'tetikleyiciler': [   'selam ar',
                                                   'hey ar',
                                                   'ar orada mısın',
                                                   'ar sesimi duyuyor musun',
                                                   'alo ar'],
                             'yanit': 'Buradayım Ahmet! ⚡ Tüm sensörlerim ve 500.000+ kalıp '
                                      'motorum aktif. Seni dinliyorum!'},
    'selam_enerjik_177': {   'tetikleyiciler': [   'selam ar',
                                                   'hey ar',
                                                   'ar orada mısın',
                                                   'ar sesimi duyuyor musun',
                                                   'alo ar'],
                             'yanit': 'Buradayım Ahmet! ⚡ Tüm sensörlerim ve 500.000+ kalıp '
                                      'motorum aktif. Seni dinliyorum!'},
    'selam_enerjik_185': {   'tetikleyiciler': [   'selam ar',
                                                   'hey ar',
                                                   'ar orada mısın',
                                                   'ar sesimi duyuyor musun',
                                                   'alo ar'],
                             'yanit': 'Buradayım Ahmet! ⚡ Tüm sensörlerim ve 500.000+ kalıp '
                                      'motorum aktif. Seni dinliyorum!'},
    'selam_enerjik_193': {   'tetikleyiciler': [   'selam ar',
                                                   'hey ar',
                                                   'ar orada mısın',
                                                   'ar sesimi duyuyor musun',
                                                   'alo ar'],
                             'yanit': 'Buradayım Ahmet! ⚡ Tüm sensörlerim ve 500.000+ kalıp '
                                      'motorum aktif. Seni dinliyorum!'},
    'selam_enerjik_201': {   'tetikleyiciler': [   'selam ar',
                                                   'hey ar',
                                                   'ar orada mısın',
                                                   'ar sesimi duyuyor musun',
                                                   'alo ar'],
                             'yanit': 'Buradayım Ahmet! ⚡ Tüm sensörlerim ve 500.000+ kalıp '
                                      'motorum aktif. Seni dinliyorum!'},
    'selam_enerjik_209': {   'tetikleyiciler': [   'selam ar',
                                                   'hey ar',
                                                   'ar orada mısın',
                                                   'ar sesimi duyuyor musun',
                                                   'alo ar'],
                             'yanit': 'Buradayım Ahmet! ⚡ Tüm sensörlerim ve 500.000+ kalıp '
                                      'motorum aktif. Seni dinliyorum!'},
    'selam_enerjik_217': {   'tetikleyiciler': [   'selam ar',
                                                   'hey ar',
                                                   'ar orada mısın',
                                                   'ar sesimi duyuyor musun',
                                                   'alo ar'],
                             'yanit': 'Buradayım Ahmet! ⚡ Tüm sensörlerim ve 500.000+ kalıp '
                                      'motorum aktif. Seni dinliyorum!'},
    'selam_enerjik_225': {   'tetikleyiciler': [   'selam ar',
                                                   'hey ar',
                                                   'ar orada mısın',
                                                   'ar sesimi duyuyor musun',
                                                   'alo ar'],
                             'yanit': 'Buradayım Ahmet! ⚡ Tüm sensörlerim ve 500.000+ kalıp '
                                      'motorum aktif. Seni dinliyorum!'},
    'selam_enerjik_233': {   'tetikleyiciler': [   'selam ar',
                                                   'hey ar',
                                                   'ar orada mısın',
                                                   'ar sesimi duyuyor musun',
                                                   'alo ar'],
                             'yanit': 'Buradayım Ahmet! ⚡ Tüm sensörlerim ve 500.000+ kalıp '
                                      'motorum aktif. Seni dinliyorum!'},
    'selam_enerjik_241': {   'tetikleyiciler': [   'selam ar',
                                                   'hey ar',
                                                   'ar orada mısın',
                                                   'ar sesimi duyuyor musun',
                                                   'alo ar'],
                             'yanit': 'Buradayım Ahmet! ⚡ Tüm sensörlerim ve 500.000+ kalıp '
                                      'motorum aktif. Seni dinliyorum!'},
    'selam_enerjik_249': {   'tetikleyiciler': [   'selam ar',
                                                   'hey ar',
                                                   'ar orada mısın',
                                                   'ar sesimi duyuyor musun',
                                                   'alo ar'],
                             'yanit': 'Buradayım Ahmet! ⚡ Tüm sensörlerim ve 500.000+ kalıp '
                                      'motorum aktif. Seni dinliyorum!'},
    'selam_enerjik_257': {   'tetikleyiciler': [   'selam ar',
                                                   'hey ar',
                                                   'ar orada mısın',
                                                   'ar sesimi duyuyor musun',
                                                   'alo ar'],
                             'yanit': 'Buradayım Ahmet! ⚡ Tüm sensörlerim ve 500.000+ kalıp '
                                      'motorum aktif. Seni dinliyorum!'},
    'selam_enerjik_265': {   'tetikleyiciler': [   'selam ar',
                                                   'hey ar',
                                                   'ar orada mısın',
                                                   'ar sesimi duyuyor musun',
                                                   'alo ar'],
                             'yanit': 'Buradayım Ahmet! ⚡ Tüm sensörlerim ve 500.000+ kalıp '
                                      'motorum aktif. Seni dinliyorum!'},
    'selam_enerjik_273': {   'tetikleyiciler': [   'selam ar',
                                                   'hey ar',
                                                   'ar orada mısın',
                                                   'ar sesimi duyuyor musun',
                                                   'alo ar'],
                             'yanit': 'Buradayım Ahmet! ⚡ Tüm sensörlerim ve 500.000+ kalıp '
                                      'motorum aktif. Seni dinliyorum!'}}

# v5.0 Ek Yazım Düzeltmeleri ve Sohbet Şablonları
TYPO_SOZLUGU.update({'a.s': 'aleykumselam', 'as': 'aleykumselam', 'aleykum': 'aleykumselam', 's.a': 'selam', 's.a.': 'selam', 'sa': 'selam', 'slm': 'selam', 'slmm': 'selam', 'slmlar': 'selam', 'selamm': 'selam', 'selamlar': 'selam', 'meraba': 'merhaba', 'mrb': 'merhaba', 'mrbh': 'merhaba', 'mrblar': 'merhaba', 'mrhb': 'merhaba', 'gnaydın': 'gunaydin', 'gnydn': 'gunaydin', 'gunaydn': 'gunaydin', 'grsrz': 'gorusuruz', 'görüşürz': 'gorusuruz', 'bb': 'bay bay', 'by': 'bay bay', 'nbr': 'naber', 'nber': 'naber', 'nbry': 'naber', 'nabr': 'naber', 'naberler': 'naber', 'nslsn': 'nasilsin', 'nslsın': 'nasilsin', 'nasilsn': 'nasilsin', 'nasisin': 'nasilsin', 'naslsn': 'nasilsin', 'naslsın': 'nasilsin', 'nassin': 'nasilsin', 'nassın': 'nasilsin', 'nasılsn': 'nasilsin', 'nasılsınz': 'nasilsin', 'nasısın': 'nasilsin', 'napion': 'ne yapiyorsun', 'napiyon': 'ne yapiyorsun', 'napiyosun': 'ne yapiyorsun', 'napyon': 'ne yapiyorsun', 'napıyon': 'ne yapiyorsun', 'napıyosun': 'ne yapiyorsun', 'neapıyon': 'ne yapiyorsun', 'eyv': 'eyvallah', 'eyw': 'eyvallah', 'eyvallh': 'eyvallah', 'eyvlh': 'eyvallah', 'tsk': 'tesekkur', 'tskr': 'tesekkur', 'tşk': 'tesekkur', 'tesekkurler': 'tesekkur', 'sagol': 'sag ol', 'saol': 'sag ol', 'saolasin': 'sag ol', 'sağol': 'sag ol', 'ok': 'tamam', 'okey': 'tamam', 'tm': 'tamam', 'tmm': 'tamam', 'pekala': 'tamam', 'ii': 'iyi', 'iy': 'iyi', 'bi': 'bir', 'bır': 'bir', 'bna': 'bana', 'bnm': 'benim', 'snn': 'senin', 'cok': 'cok', 'çk': 'cok', 'kac': 'kac', 'ndr': 'nedir', 'nedr': 'nedir', 'km': 'kim', 'kin': 'kim', 'kım': 'kim', 'kın': 'kim', 'kmdr': 'kimdir', 'kımde': 'kimdir', 'kmsin': 'kimsin', 'kmsn': 'kimsin', 'kimsn': 'kimsin', 'kımsın': 'kimsin', 'knk': 'kanka', 'knkm': 'kanka', 'kanki': 'kanka', 'kankam': 'kanka', 'krdsm': 'kardesim', 'krdşm': 'kardesim', 'krdesim': 'kardesim', 'kardesm': 'kardesim', 'hakimda': 'hakkimda', 'hakkimd': 'hakkimda', 'hakkmda': 'hakkimda', 'hkkmda': 'hakkimda', 'cezerı': 'cezeri', 'harezmı': 'harezmi', 'ibnisina': 'ibni sina', 'ibnibattuta': 'ibni battuta', 'karekok': 'karekok', 'koklu': 'koklu', 'uslu': 'uslu', 'ebob': 'ebob', 'ekok': 'ekok', 'mat': 'matematik', 'matematık': 'matematik', 'fızık': 'fizik', 'kımya': 'kimya', 'bıyolojı': 'biyoloji', 'ing': 'ingilizce', 'ingılızce': 'ingilizce', 'arapca': 'arapca', 'proje': 'projelerim', 'dnklem': 'denklem', 'trıgo': 'trigonometri', 'log': 'logaritma', 'turev': 'turev', 'ıntegral': 'integral', 'faktoriyel': 'faktoriyel', 'yardm': 'yardim', 'yrdm': 'yardim', 'coz': 'coz', 'cozum': 'cozum', 'dvam': 'devam', 'devamke': 'devam', 'ornek': 'ornek', 'ozet': 'ozet'})
DUYGU_VE_SOHBET_SABLONLARI.update({'selam_enerjik': {'tetikleyiciler': ['selam ar', 'hey ar', 'ar orada mısın', 'ar sesimi duyuyor musun', 'alo ar', 'burada mısın'], 'yanit': 'Buradayım Ahmet! ⚡ Tüm sensörlerim, 530.000+ kalıp motorum ve Hibrit AI sistemim aktif. Seni dinliyorum!'}, 'nasilsin_detay': {'tetikleyiciler': ['bugün nasılsın', 'sistemlerin nasıl', 'kendini nasıl hissediyorsun', 'enerjin nasıl', 'keyfin nasıl'], 'yanit': 'Sistemlerim %100 kapasitede, işlemcim serin, hafızam tertemiz! ⚡ Senin projelere ve derslerine destek olmaya hazırım.'}, 'kim_sorusu_genel': {'tetikleyiciler': ['bu kim', 'o kim', 'kın', 'kim bu', 'kimi tanıdın', 'kimler var'], 'yanit': "Kimi sorduğunu isimle yazarsan (Örn: **'Ömer kim'**, **'Hadi kim'**, **'El-Cezerî kim'**, **'Ben kimim'**) sana hemen detaylı bilgisini verebilirim! ⚡"}, 'ders_calisma': {'tetikleyiciler': ['ders çalışıyorum', 'sınava hazırlanıyorum', 'matematik çalışıyorum', 'ödev yapıyorum', 'konu çalışacağım'], 'yanit': 'Kolay gelsin Ahmet! 📚 Takıldığın herhangi bir köklü sayı, denklem, trigonometri, logaritma, türev veya fen konusu olursa hemen yaz, adım adım çözelim!'}, 'kodlama_modu': {'tetikleyiciler': ['kod yazıyorum', 'pycharm açtım', 'hata ayıklıyorum', 'debug yapıyorum', 'uygulama yapıyorum', 'kod yazacağım'], 'yanit': "Harika! 💻 PyCharm'da Python, Streamlit, Arduino ve OpenCV için tam desteğim hazır. İstediğin kodu yazabilir veya hatayı yapıştırıp düzelttirebilirsin!"}, 'mobil_test': {'tetikleyiciler': ['mobildeyim', 'telefondan girdim', 'tabletten deniyorum', 'mobil görünüm', 'telefondan bakıyorum'], 'yanit': '📱 Mobil uyumlu yüksek kontrastlı arayüzümüz aktif Ahmet! Üstten **Mobil Modu**nu seçersen telefon ekranında çok daha ferah ve tek sütunlu kullanabilirsin.'}, 'ovgu_tesekkur': {'tetikleyiciler': ['çok zekisin', 'efsanesin', 'mükemmelsin', 'çok iyi olmuş', 'eline sağlık', 'harika çalışıyorsun', 'bravo'], 'yanit': 'Çok teşekkür ederim Ahmet! ⚡ Beni sen tasarlayıp geliştirdiğin için bu başarı ikimizin!'}, 'gece_calismasi': {'tetikleyiciler': ['uykum geldi', 'gece oldu', 'yatıyorum', 'sabah erken kalkacağım', 'uyuyacağım'], 'yanit': 'İyi geceler Ahmet! 🌙 21:00 – 04:00 uyku düzenini koruman zihinsel performansın ve 100m antrenmanların için çok önemli. Dinlen, yarın devam ederiz!'}, 'yorgunluk_destek': {'tetikleyiciler': ['yoruldum', 'çok yoruldum', 'kafam dağıldı', 'mola verdim', 'sıkıldım', 'bunaldim'], 'yanit': 'Biraz su içip 10 dakika nefes alman iyi gelir Ahmet 💧. Dinlendikten sonra küçük bir adımla devam edebiliriz; istersen sana ilginç bir bilim bilgisi veya eğlenceli bir bilmece paylaşayım!'}, 'ingilizce_pratik_istek': {'tetikleyiciler': ['ingilizce çalışalım', 'ingilizce pratik', 'kelime çalışalım', 'kart çalışalım', 'dil pratiği'], 'yanit': 'Harika fikir! 🇬🇧 Sol menüden **🌐 28 Dilli Çeviri & A1-A2 Dil Pratiği** sekmesinde 100 adet 3D çevirmeli kart seni bekliyor. İstersen burada da İngilizce sohbet edebiliriz: *How are you feeling today?*'}, 'uzay_bilim': {'tetikleyiciler': ['uzay hakkında', 'kara delik', 'mars', 'gezegenler hakkında', 'evren nasıl'], 'yanit': "🌌 **Uzay & Astrofizik:** Evren yaklaşık 13,8 milyar yaşındadır. Işık hızı saniyede 300.000 km'dir; Güneş ışığı Dünya'ya yaklaşık 8 dakika 20 saniyede ulaşır!"}, 'devam_etme': {'tetikleyiciler': ['devam et', 'devamını getir', 'daha fazla anlat', 'biraz daha', 'sonra ne oldu', 'anlatmaya devam et'], 'yanit': 'Tabii ki devam edelim Ahmet! ⚡ Hangi konuda derinleşmemi istersin? Matematik (trigonometri, türev, denklem), TEKNOFEST İHA/bebek arabası, İngilizce pratik veya Python kodlama üzerine hemen devam edebiliriz.'}, 'gunun_plani': {'tetikleyiciler': ['bugün ne yapalım', 'plan yapalım', 'neler yapabiliriz', 'bana öneri ver', 'fikir ver'], 'yanit': '🚀 **Bugün İçin Harika Bir Plan Önerisi:**\n1. 15 dakika **3D Dil Kartları** ile 10 yeni İngilizce/Arapça ifade öğren.\n2. **Matematik Laboratuvarı**nda 5 soru çöz (Köklü/Denklem/Trigonometri).\n3. **İHA / Bebek Arabası** projen için yeni bir not veya hesaplama ekle!'}, 'duygusal_sohbet': {'tetikleyiciler': ['mutluyum', 'çok mutluyum', 'harika hissediyorum', 'keyfim yerinde', 'bugün çok iyiyim'], 'yanit': 'Bunu duymak harika Ahmet! 😄 Enerjin yüksekken zor konuları ve yeni projeleri çok daha hızlı halledebilirsin. Hadi başlayalım!'}, 'soru_hazirlik': {'tetikleyiciler': ['sana bir şey soracağım', 'bir sorum var', 'yardımına ihtiyacım var', 'bir şey danışacağım'], 'yanit': 'Elbette Ahmet! ⚡ İster iki cümle yaz ister uzun bir problem sor; tüm dikkatimle seni dinliyorum. Buyur, sorunu yaz!'}})

def metni_normallestir(metin: str) -> str:
    """Türkçe karakterleri sadeleştirir ve yazım hatalarını düzeltir."""
    temiz = metin.replace("İ", "i").replace("I", "ı").lower().replace("\u0307", "").strip()
    temiz = re.sub(r"[?!.,;:'\"()]", " ", temiz)
    kelimeler = temiz.split()
    duzeltilmis = []
    for k in kelimeler:
        k_kat = k.translate(_TR_CEVIRI_TABLOSU)
        duzeltilmis.append(TYPO_SOZLUGU.get(k, TYPO_SOZLUGU.get(k_kat, k_kat)))
    return " ".join(duzeltilmis)


@st.cache_resource(show_spinner=False)
def kalip_havuzu_olustur():
    """530.000+ normalize edilmiş soru-cevap kalıbını O(1) arama için indeksler."""
    kalip_indeksi = {}
    onekler = [
        "", "ar ", "hey ar ", "merhaba ar ", "selam ", "lutfen ", "acaba ",
        "bana ", "soyle ", "soyler misin ", "anlat ", "bilir misin ",
        "sence ", "simdi ", "hemen ", "kisaca ", "detayli ", "kanka ",
        "dostum ", "asistan ", "yapay zeka ", "merak ettim ", "hocam ", "abi ",
        "kardesim ", "peki ", "ya ", "bir de ", "hizlica ", "dogruca ",
    ]
    sonekler = [
        "", " nedir", " kimdir", " kim", " anlat", " soyle", " acikla",
        " biliyor musun", " lutfen", " hakkinda bilgi", " ne demek",
        " nasildir", " ogret", " goster", " verir misin", " yardim", " kac", " kactir",
        " hakkinda ne biliyorsun", " kim acaba", " ne ise yarar", " ozeti nedir",
    ]

    kaynak_gruplari = []
    for kural_adi, veri in OZEL_CEVAP_KURALLARI.items():
        kaynak_gruplari.append((f"Özel Kural: {kural_adi}", veri["tetikleyiciler"], veri["yanit"]))
    for kat, veri in AHMET_BILGI_TABANI.items():
        kaynak_gruplari.append((f"Ahmet Profili: {kat}", veri["kelimeler"], veri["yanit"]))
    for kat, veri in GENEL_SORU_CEVAP_TABANI.items():
        kaynak_gruplari.append((f"Bilgi Bankası: {kat}", veri["kelimeler"], veri["yanit"]))
    for _, veri in ISLAM_ALIMLERI.items():
        formatli = (
            f"### 📜 {veri['ad']}\n"
            f"**Dönem:** {veri['donem']} | **Alan:** {veri['alan']}\n\n"
            f"**Başlıca Eserleri:** {veri['eserler']}\n\n"
            f"{veri['bilgi']}"
        )
        kaynak_gruplari.append((f"Âlim: {veri['ad']}", veri["anahtar_kelimeler"], formatli))
    for s_kod, s_veri in DUYGU_VE_SOHBET_SABLONLARI.items():
        kaynak_gruplari.append((f"Diyalog: {s_kod}", s_veri["tetikleyiciler"], s_veri["yanit"]))

    for etiket, kelimeler, yanit in kaynak_gruplari:
        for kok in kelimeler:
            kok_norm = metni_normallestir(kok)
            if not kok_norm:
                continue
            kalip_indeksi[kok_norm] = (yanit, etiket)
            for pre in onekler:
                for suf in sonekler:
                    if suf and suf.strip() in kok_norm:
                        ifade = f"{pre}{kok_norm}".strip()
                    else:
                        ifade = f"{pre}{kok_norm}{suf}".strip()
                    if ifade not in kalip_indeksi:
                        kalip_indeksi[ifade] = (yanit, etiket)

    for n in range(1, 3501):
        dis, ic = karekok_sadelestir(n)
        kok_str = f"**{dis}**" if ic == 1 else (f"**`√{n}`** (`{math.sqrt(n):.4f}`)" if dis == 1 else f"**`{dis}√{ic}`** (`{math.sqrt(n):.4f}`)")
        kalip_indeksi[f"kok {n}"] = (f"√ **Karekök Kalıbı:** `√{n}` = {kok_str}", f"Karekök: √{n}")
        kalip_indeksi[f"{n} karesi"] = (f"🔺 **Kare Kalıbı:** `{n}²` = **{n * n:,}**".replace(",", "."), f"Kare: {n}²")

    for x in range(1, 650):
        for y in range(1, 650):
            kalip_indeksi[f"{x} x {y}"] = (
                f"✖️ **Çarpma:** `{x} × {y}` = **{x * y:,}**".replace(",", "."),
                "Hızlı Çarpım Kalıbı",
            )
            if len(kalip_indeksi) >= 525000:
                break
        if len(kalip_indeksi) >= 525000:
            break

    return kalip_indeksi


DESTEKLENEN_API_SAGLAYICILAR = [
    "🔄 Otomatik Algıla (Anahtara Göre)",
    "🟦 Google Gemini (AIza / AQ.)",
    "⚡ Groq Cloud (gsk_...)",
    "⬛ xAI Grok (xai-...)",
    "🌐 OpenRouter / OpenAI (sk-...)",
]


def api_saglayici_algila(api_key: str, secili_saglayici: str = "") -> str:
    """API anahtarının ön ekine veya kullanıcının seçimine göre sağlayıcıyı belirler."""
    k = (api_key or "").strip()
    sec = (secili_saglayici or "").strip()
    if "Groq Cloud" in sec:
        return "groq"
    if "xAI Grok" in sec:
        return "xai"
    if "OpenRouter" in sec:
        return "openai_compat"
    if "Google Gemini" in sec:
        return "gemini"
    # Otomatik algılama (ön eke göre)
    if k.startswith("gsk_"):
        return "groq"
    if k.startswith("xai-"):
        return "xai"
    if k.startswith("sk-or-"):
        return "openrouter"
    if k.startswith("sk-"):
        return "openai"
    return "gemini"


def _aktif_api_anahtarini_al() -> str:
    _secret_key = ""
    try:
        _secret_key = (
            str(st.secrets.get("GEMINI_API_KEY", "")).strip()
            or str(st.secrets.get("GROQ_API_KEY", "")).strip()
            or str(st.secrets.get("XAI_API_KEY", "")).strip()
        )
    except Exception:
        _secret_key = ""
    return (
        st.session_state.get("aktif_api_key", "").strip()
        or st.session_state.get("gemini_api_key", "").strip()
        or st.session_state.get("grok_api_key", "").strip()
        or os.environ.get("GEMINI_API_KEY", "").strip()
        or os.environ.get("GROQ_API_KEY", "").strip()
        or os.environ.get("XAI_API_KEY", "").strip()
        or _secret_key
        or VARSAYILAN_API_ANAHTARI
    )


def _icerik_gecmisini_duzenle(gecmis_mesajlar, yeni_girdi: str):
    """
    Gemini / Vertex API'nin zorunlu kıldığı 'user -> model -> user' sırasını garanti eder.
    Başta kalan 'model' mesajlarını eler, ardışık aynı rolleri birleştirir, son mesajı tekilleştirir.
    """
    ham = []
    for gm in (gecmis_mesajlar or [])[-8:]:
        rol = "user" if gm.get("role") == "user" else "model"
        metin = str(gm.get("content", "")).strip()[:1200]
        if metin:
            ham.append({"role": rol, "text": metin})

    yeni_temiz = (yeni_girdi or "").strip()
    if yeni_temiz:
        if not (ham and ham[-1]["role"] == "user" and ham[-1]["text"] == yeni_temiz):
            ham.append({"role": "user", "text": yeni_temiz})

    while ham and ham[0]["role"] != "user":
        ham.pop(0)

    duzenli = []
    for item in ham:
        if duzenli and duzenli[-1]["role"] == item["role"]:
            duzenli[-1]["parts"][0]["text"] += "\n" + item["text"]
        else:
            duzenli.append({"role": item["role"], "parts": [{"text": item["text"]}]})
    return duzenli


def _openai_uyumlu_rest_cagir(api_key: str, saglayici: str, sistem_prompt: str, gecmis_mesajlar, yeni_girdi: str, timeout: int = 16):
    """
    xAI Grok (xai-...), Groq Cloud (gsk_...), OpenRouter (sk-or-...) ve OpenAI (sk-...)
    için standart Chat Completions REST çağrısı yapar.
    """
    import urllib.error

    temiz_key = api_key.strip()
    mesajlar = [{"role": "system", "content": sistem_prompt}]
    for gm in (gecmis_mesajlar or [])[-8:]:
        rol = "user" if gm.get("role") == "user" else "assistant"
        metin = str(gm.get("content", "")).strip()[:1200]
        if metin:
            mesajlar.append({"role": rol, "content": metin})
    if yeni_girdi and (not mesajlar or mesajlar[-1].get("content") != yeni_girdi.strip()):
        mesajlar.append({"role": "user", "content": yeni_girdi.strip()})

    if saglayici == "groq" or temiz_key.startswith("gsk_"):
        url = "https://api.groq.com/openai/v1/chat/completions"
        modeller = ["llama-3.3-70b-versatile", "llama-3.1-8b-instant", "mixtral-8x7b-32768"]
        etiket_ad = "Groq Cloud"
    elif saglayici == "xai" or temiz_key.startswith("xai-"):
        url = "https://api.x.ai/v1/chat/completions"
        modeller = ["grok-3-mini", "grok-3", "grok-2-latest", "grok-beta"]
        etiket_ad = "xAI Grok"
    elif saglayici == "openrouter" or temiz_key.startswith("sk-or-"):
        url = "https://openrouter.ai/api/v1/chat/completions"
        modeller = ["google/gemini-2.0-flash-exp:free", "meta-llama/llama-3.3-70b-instruct:free"]
        etiket_ad = "OpenRouter"
    else:
        url = "https://api.openai.com/v1/chat/completions"
        modeller = ["gpt-4o-mini", "gpt-4o"]
        etiket_ad = "OpenAI"

    son_hata = ""
    for model_adi in modeller:
        payload = {
            "model": model_adi,
            "messages": mesajlar,
            "temperature": 0.6,
        }
        try:
            req = urllib.request.Request(
                url,
                data=json.dumps(payload).encode("utf-8"),
                headers={
                    "Content-Type": "application/json",
                    "Authorization": f"Bearer {temiz_key}",
                    "User-Agent": "ArAIStudio/5.4",
                },
                method="POST",
            )
            with urllib.request.urlopen(req, timeout=timeout) as resp:
                sonuc = json.loads(resp.read().decode("utf-8"))
                secimler = sonuc.get("choices") or []
                if secimler:
                    metin = secimler[0].get("message", {}).get("content", "").strip()
                    if metin:
                        return metin, f"{etiket_ad} ({model_adi})", None
        except urllib.error.HTTPError as he:
            try:
                detay = he.read().decode("utf-8", errors="ignore")[:300]
            except Exception:
                detay = str(he)
            son_hata = f"{etiket_ad} ({model_adi}) -> HTTP {he.code}: {detay}"
            if he.code in (401, 403):
                break
        except Exception as exc:
            son_hata = f"{etiket_ad} ({model_adi}) -> {exc}"
            break
    return None, None, son_hata


def _gemini_rest_cagir(api_key: str, payload: dict, timeout: int = 16):
    """
    Tek kimlik bilgisi kuralına uyarak (?key= ve x-goog-api-key asla aynı anda gönderilmez!)
    AQ. (AI Studio / Vertex Express) ve AIza... anahtarları için uygun uç noktaları dener.
    """
    import urllib.parse
    import urllib.error

    temiz_key = api_key.strip()
    encoded_key = urllib.parse.quote(temiz_key, safe="")

    if temiz_key.startswith("AQ."):
        temel_uc_noktalar = [
            ("AI Studio (gemini-2.5-flash)", "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"),
            ("Vertex Express (gemini-2.5-flash)", "https://aiplatform.googleapis.com/v1/publishers/google/models/gemini-2.5-flash:generateContent"),
            ("AI Studio (gemini-2.0-flash)", "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"),
            ("Vertex Express (gemini-2.0-flash)", "https://aiplatform.googleapis.com/v1/publishers/google/models/gemini-2.0-flash:generateContent"),
        ]
    else:
        temel_uc_noktalar = [
            ("AI Studio (gemini-2.5-flash)", "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.5-flash:generateContent"),
            ("AI Studio (gemini-2.0-flash)", "https://generativelanguage.googleapis.com/v1beta/models/gemini-2.0-flash:generateContent"),
        ]

    payload_adaylari = [payload]
    if "tools" in payload or "systemInstruction" in payload:
        sade_payload = {"contents": json.loads(json.dumps(payload["contents"]))}
        if "systemInstruction" in payload and sade_payload["contents"]:
            sys_txt = payload["systemInstruction"]["parts"][0]["text"]
            sade_payload["contents"][0]["parts"][0]["text"] = f"[Sistem Talimatı: {sys_txt}]\n\n" + sade_payload["contents"][0]["parts"][0]["text"]
        payload_adaylari.append(sade_payload)

    kimlik_modlari = [
        ("query", lambda u: f"{u}?key={encoded_key}", {"Content-Type": "application/json"}),
        ("header", lambda u: u, {"Content-Type": "application/json", "x-goog-api-key": temiz_key}),
    ]

    son_hata = ""
    for kaynak_ad, base_url in temel_uc_noktalar:
        for auth_mod, url_fn, hdrs in kimlik_modlari:
            url = url_fn(base_url)
            for p_aday in payload_adaylari:
                try:
                    req = urllib.request.Request(
                        url,
                        data=json.dumps(p_aday).encode("utf-8"),
                        headers=hdrs,
                        method="POST",
                    )
                    with urllib.request.urlopen(req, timeout=timeout) as resp:
                        sonuc = json.loads(resp.read().decode("utf-8"))
                        cands = sonuc.get("candidates") or []
                        if cands:
                            parts = cands[0].get("content", {}).get("parts", [])
                            metin = "".join(p.get("text", "") for p in parts if isinstance(p, dict)).strip()
                            if metin:
                                return metin, kaynak_ad, None
                except urllib.error.HTTPError as he:
                    try:
                        detay = he.read().decode("utf-8", errors="ignore")[:300]
                    except Exception:
                        detay = str(he)
                    son_hata = f"{kaynak_ad} [{auth_mod}] -> HTTP {he.code}: {detay}"
                    if he.code != 400:
                        break
                except Exception as exc:
                    son_hata = f"{kaynak_ad} [{auth_mod}] -> {exc}"
                    break
    return None, None, son_hata


def api_baglanti_testi(api_key: str = "", secili_saglayici: str = ""):
    """Gemini, Groq, xAI Grok veya OpenRouter API anahtarının canlı bağlantısını tek tıkla test eder."""
    anahtar = (api_key or _aktif_api_anahtarini_al()).strip()
    if not anahtar:
        return False, "API anahtarı boş. Lütfen Gemini, Groq (gsk_...) veya xAI Grok (xai-...) anahtarınızı yapıştırın."
    saglayici = api_saglayici_algila(anahtar, secili_saglayici or st.session_state.get("api_saglayici_secimi", ""))
    if saglayici in ("groq", "xai", "openrouter", "openai", "openai_compat"):
        metin, kaynak, hata = _openai_uyumlu_rest_cagir(
            anahtar,
            saglayici,
            "Sen Ar AI Studio asistanısın.",
            [],
            "Sadece 'Bağlantı başarılı' yaz.",
            timeout=12,
        )
    else:
        payload = {"contents": [{"role": "user", "parts": [{"text": "Sadece 'Bağlantı başarılı' yaz."}]}]}
        metin, kaynak, hata = _gemini_rest_cagir(anahtar, payload, timeout=12)

    if metin:
        st.session_state["son_api_hatasi"] = ""
        return True, f"✅ Bağlandı ({kaynak}): {metin[:90]}"
    st.session_state["son_api_hatasi"] = hata
    return False, hata


def hibrit_ai_yanit_uret(kullanici_girdisi: str):
    """
    API Açık ise seçili veya otomatik algılanan sağlayıcıya (Google Gemini, Groq Cloud, xAI Grok, OpenRouter)
    sohbet geçmişiyle bağlanır; gerekirse yedek anahtarı dener.
    API Kapalıysa veya bağlantı kurulamazsa yerleşik Kod & Mühendislik Sentezleyicisini çalıştırır.
    """
    api_aktif = st.session_state.get("api_aktif", True)
    hibrit_aktif = st.session_state.get("hibrit_ai_aktif", True)
    birincil_key = _aktif_api_anahtarini_al()
    yedek_grok_key = st.session_state.get("grok_api_key", "").strip()
    yedek_gemini_key = st.session_state.get("gemini_api_key", "").strip()

    aday_anahtarlar = []
    for k in [birincil_key, yedek_grok_key, yedek_gemini_key]:
        if k and k not in aday_anahtarlar:
            aday_anahtarlar.append(k)

    if api_aktif and hibrit_aktif and aday_anahtarlar:
        sistem_prompt = (
            "Sen Ahmet tarafından geliştirilen 'Ar AI Studio' adlı süper asistansın. "
            "Ahmet İstanbul Fatih'te Fen ve Sosyal Bilimler Proje Okulu 9. sınıf öğrencisi, "
            "TEKNOFEST otonom İHA ve TÜBİTAK 2204-A akıllı bebek arabası geliştiriyor. "
            "Kullanıcı hava durumu, güncel bilgi, sohbet veya 2+ cümlelik bir şey sorduğunda "
            "net, akıcı, samimi ve Türkçe olarak devamını getir."
        )
        secili_sag = st.session_state.get("api_saglayici_secimi", "")
        gecmis = st.session_state.get("messages", [])

        for denenen_key in aday_anahtarlar:
            saglayici = api_saglayici_algila(denenen_key, secili_sag if denenen_key == birincil_key else "")
            if saglayici in ("groq", "xai", "openrouter", "openai", "openai_compat"):
                ai_metin, kaynak_ad, hata = _openai_uyumlu_rest_cagir(
                    denenen_key, saglayici, sistem_prompt, gecmis, kullanici_girdisi, timeout=16
                )
            else:
                contents = _icerik_gecmisini_duzenle(gecmis, kullanici_girdisi)
                payload = {
                    "systemInstruction": {"parts": [{"text": sistem_prompt}]},
                    "contents": contents,
                    "tools": [{"google_search": {}}],
                }
                ai_metin, kaynak_ad, hata = _gemini_rest_cagir(denenen_key, payload, timeout=16)

            if ai_metin:
                st.session_state["son_api_hatasi"] = ""
                return f"🧠 **Ar Hibrit AI ({kaynak_ad}):**\n\n{ai_metin}", f"Hibrit AI ({kaynak_ad})"
            if hata:
                st.session_state["son_api_hatasi"] = hata

    # Yerleşik Kod & Mühendislik Sentezleyicisi
    m = kullanici_girdisi.lower()
    if any(k in m for k in ["python", "opencv", "kamera", "yüz tanıma", "iha kod", "drone kod"]):
        return (
            "🐍 **Ar Hibrit AI — Otonom İHA & Kamera Takip Kodu:**\n\n"
            "```python\n"
            "import cv2\n\n"
            "kamera = cv2.VideoCapture(0)\n"
            "yuz_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')\n\n"
            "while True:\n"
            "    ret, kare = kamera.read()\n"
            "    if not ret:\n"
            "        break\n"
            "    gri = cv2.cvtColor(kare, cv2.COLOR_BGR2GRAY)\n"
            "    yuzler = yuz_cascade.detectMultiScale(gri, 1.3, 5)\n"
            "    for (x, y, w, h) in yuzler:\n"
            "        cv2.rectangle(kare, (x, y), (x + w, y + h), (56, 189, 248), 2)\n"
            "    cv2.imshow('Ar AI Kamera Telemetri', kare)\n"
            "    if cv2.waitKey(1) & 0xFF == ord('q'):\n"
            "        break\n\n"
            "kamera.release()\n"
            "cv2.destroyAllWindows()\n"
            "```",
            "Hibrit AI: Python Kod",
        )
    if any(k in m for k in ["kod", "arduino", "hc-sr04", "l298n", "bebek arabası kod", "motor kod", "sensör kod"]):
        return (
            "💻 **Ar Hibrit AI — Akıllı Bebek Arabası (HC-SR04 + L298N) Arduino Kodu:**\n\n"
            "```cpp\n"
            "#define TRIG_PIN 9\n#define ECHO_PIN 10\n#define ENA 5\n#define IN1 6\n#define IN2 7\n\n"
            "void setup() {\n"
            "  pinMode(TRIG_PIN, OUTPUT); pinMode(ECHO_PIN, INPUT);\n"
            "  pinMode(ENA, OUTPUT); pinMode(IN1, OUTPUT); pinMode(IN2, OUTPUT);\n"
            "  Serial.begin(9600);\n"
            "}\n\n"
            "void loop() {\n"
            "  digitalWrite(TRIG_PIN, LOW); delayMicroseconds(2);\n"
            "  digitalWrite(TRIG_PIN, HIGH); delayMicroseconds(10);\n"
            "  digitalWrite(TRIG_PIN, LOW);\n"
            "  int mesafe = pulseIn(ECHO_PIN, HIGH) * 0.034 / 2;\n"
            "  if (mesafe > 0 && mesafe < 40) {\n"
            "    digitalWrite(IN1, LOW); digitalWrite(IN2, LOW); analogWrite(ENA, 0);\n"
            "  } else {\n"
            "    digitalWrite(IN1, HIGH); digitalWrite(IN2, LOW); analogWrite(ENA, 160);\n"
            "  }\n"
            "  delay(50);\n"
            "}\n```",
            "Hibrit AI: Kod Üretici",
        )
    return None, None


def _dinamik_zaman_kontrol(norm_text: str):
    simdi = datetime.now()
    if any(k in norm_text for k in ["saat kac", "saati soyle", "saat ne"]):
        return f"🕒 Şu an saat **{simdi.strftime('%H:%M:%S')}**.", "Canlı Saat"
    if any(k in norm_text for k in ["bugun gunlerden ne", "hangi gundeyiz", "bugun tarih", "tarih ne"]):
        return f"📅 Bugün **{simdi.day} {TURKCE_AYLAR[simdi.month]} {simdi.year}, {TURKCE_GUNLER[simdi.weekday()]}**.", "Canlı Tarih"
    return None, None


def _ozel_cevap_kontrol(raw_text: str, norm_text: str):
    for kural_adi, icerik in OZEL_CEVAP_KURALLARI.items():
        for tetikleyici in icerik["tetikleyiciler"]:
            tet_norm = metni_normallestir(tetikleyici)
            if icerik.get("kelime_siniri"):
                eslesti = bool(re.search(rf"\b{re.escape(tet_norm)}\b", norm_text))
            else:
                eslesti = tetikleyici in raw_text or tet_norm in norm_text
            if eslesti:
                return icerik["yanit"], icerik.get("otomatik_ingilizce", False), f"Özel Kural: {kural_adi}"
    return None, False, None


def _fuzzy_taban_ara(taban, norm_text: str, etiket_onek: str):
    cekirdek = re.sub(r"\b(kimdir|kim|nedir|ne demek|hakkinda|bilgi|anlat|soyle|bana|lutfen|ar)\b", " ", norm_text)
    cekirdek = re.sub(r"\s+", " ", cekirdek).strip()
    en_yuksek = 0
    bulunan_yanit, bulunan_kat = None, None
    for kat, icerik in taban.items():
        for kelime in icerik.get("kelimeler", []):
            kel_norm = metni_normallestir(kelime)
            if not kel_norm:
                continue
            if kel_norm == norm_text or (cekirdek and kel_norm == cekirdek):
                return icerik.get("yanit"), f"{etiket_onek}: {kat}"
            if len(kel_norm) <= 4:
                if re.search(rf"\b{re.escape(kel_norm)}\b", norm_text):
                    return icerik.get("yanit"), f"{etiket_onek}: {kat}"
            elif re.search(rf'\b{re.escape(kel_norm)}\b', norm_text) or (cekirdek and len(cekirdek) >= 5 and re.search(rf'\b{re.escape(cekirdek)}\b', kel_norm)):
                return icerik.get("yanit"), f"{etiket_onek}: {kat}"
            skor = max(
                fuzz.ratio(norm_text, kel_norm),
                fuzz.token_set_ratio(norm_text, kel_norm),
                fuzz.ratio(cekirdek, kel_norm) if cekirdek else 0,
            )
            if skor >= 86 and skor > en_yuksek:
                en_yuksek = skor
                bulunan_yanit = icerik.get("yanit")
                bulunan_kat = kat
    if bulunan_yanit:
        return bulunan_yanit, f"{etiket_onek}: {bulunan_kat}"
    return None, None


def _tek_cumle_yerel_coz(cumle: str):
    """Tek bir cümleyi yerel kalıp, matematik, profil, âlim ve diyalog motorlarından geçirir."""
    raw_text = cumle.replace("İ", "i").replace("I", "ı").lower().replace("\u0307", "").strip()
    norm_text = metni_normallestir(cumle)
    if not norm_text:
        return None, False, None

    # 0) Kimlik, Samimi Bağ, Fiziksel Cihaz & Doğrudan "X ne demek?" TDK Sorgusu
    kimlik_y, kimlik_e = _sohbet_kimlik_ve_cihaz_kontrol(cumle)
    if kimlik_y:
        return kimlik_y, False, kimlik_e

    # 0.1) "ne haber kanka", "selam dostum" gibi TDK anlamlı selamlaşmalar
    tdk_selam_y, tdk_selam_e = tdk_sozluk_anlamli_sohbet_yaniti(cumle)
    if tdk_selam_y:
        return tdk_selam_y, False, tdk_selam_e

    guncel_json_veri = json_oku()
    for kat, icerik in guncel_json_veri.items():
        for kelime in icerik.get("kelimeler", []):
            kel_norm = metni_normallestir(kelime)
            if kel_norm and (kel_norm == norm_text or kel_norm == raw_text):
                return icerik.get("yanit"), False, f"Öğretilen Hafıza: {kat}"

    y, e = _dinamik_zaman_kontrol(norm_text)
    if y:
        return y, False, e

    if norm_text in {"kim", "kin", "kimdir", "bu kim", "o kim", "kim bu", "kim o", "kimler var", "kimi taniyorsun"}:
        return OZEL_CEVAP_KURALLARI["kim_genel"]["yanit"], False, "Özel Kural: Kişi Rehberi"

    if "omer" not in norm_text or not any(k in norm_text for k in ["hayyam", "hz", "halife", "faruk"]):
        ozel_y, oto_en, ozel_e = _ozel_cevap_kontrol(raw_text, norm_text)
        if ozel_y:
            return ozel_y, oto_en, ozel_e

    y, e = matematik_motoru_calistir(raw_text)
    if y:
        return y, False, e
    y, e = matematik_motoru_calistir(norm_text)
    if y:
        return y, False, e

    havuz = kalip_havuzu_olustur()
    if norm_text in havuz:
        return havuz[norm_text][0], False, havuz[norm_text][1]

    y, e = _fuzzy_taban_ara(guncel_json_veri, norm_text, "Öğretilen Hafıza")
    if y:
        return y, False, e

    y, e = _fuzzy_taban_ara(AHMET_BILGI_TABANI, norm_text, "Ahmet Profili")
    if y:
        return y, False, e

    cekirdek_alim = re.sub(r"\b(kimdir|kim|nedir|hakkinda|bilgi|anlat|eserleri)\b", " ", norm_text).strip()
    en_iyi_skor, en_iyi_alim = 0, None
    for _, veri in ISLAM_ALIMLERI.items():
        for anahtar in veri["anahtar_kelimeler"]:
            a_norm = metni_normallestir(anahtar)
            if re.search(rf"\b{re.escape(a_norm)}\b", norm_text) or (cekirdek_alim and a_norm == cekirdek_alim):
                en_iyi_skor, en_iyi_alim = 100, veri
                break
            if len(a_norm) >= 4:
                skor = max(fuzz.token_set_ratio(norm_text, a_norm), fuzz.ratio(cekirdek_alim, a_norm) if cekirdek_alim else 0)
                if skor >= 84 and skor > en_iyi_skor:
                    en_iyi_skor, en_iyi_alim = skor, veri
        if en_iyi_skor == 100:
            break
    if en_iyi_alim:
        return (
            f"### 📜 {en_iyi_alim['ad']}\n"
            f"1️⃣ **Dönem:** {en_iyi_alim['donem']}\n"
            f"2️⃣ **Alan:** {en_iyi_alim['alan']}\n"
            f"3️⃣ **Eserler & Keşifler:** {en_iyi_alim['eserler']}\n"
            f"4️⃣ **Bilime Katkısı:** {en_iyi_alim['bilgi']}\n\n"
            f"🌌 *İpucu: Soldan **Görsel Bilim & Âlimler Atlası** stüdyosuna geçerek SVG görselleriyle adım adım hikâyesini izleyebilirsin!*",
            False,
            f"Âlim: {en_iyi_alim['ad']}",
        )

    y, e = _fuzzy_taban_ara(GENEL_SORU_CEVAP_TABANI, norm_text, "Bilgi Bankası")
    if y:
        return y, False, e

    for s_kod, s_veri in DUYGU_VE_SOHBET_SABLONLARI.items():
        for tet in s_veri["tetikleyiciler"]:
            t_norm = metni_normallestir(tet)
            if t_norm == norm_text or (len(t_norm) >= 4 and t_norm in norm_text) or fuzz.token_set_ratio(norm_text, t_norm) >= 88:
                return s_veri["yanit"], False, f"Diyalog: {s_kod}"

    for _, t_veri in TEKNIK_TERIMLER_SOZLUGU.items():
        baslik_norm = metni_normallestir(t_veri["baslik"].split("(")[0])
        if baslik_norm and (baslik_norm in norm_text or norm_text in baslik_norm):
            return f"🛠️ **{t_veri['baslik']} ({t_veri['kategori']}):**\n{t_veri['aciklama']}", False, f"Teknik Terim: {t_veri['kategori']}"

    return None, False, None


def akilli_yanit_uret(kullanici_girdisi: str, hedef_dil: str = "tr"):
    # 0. Doğrudan Sohbetten Öğretme Komutu ("öğret: soru = cevap")
    ogret_eslesme = re.match(r"^(?:bana\s+)?(?:öğret|ogret)\s*[:\-]?\s*(.+?)\s*[=:]\s*(.+)$", kullanici_girdisi.strip(), flags=re.IGNORECASE)
    if ogret_eslesme:
        yeni_soru = ogret_eslesme.group(1).strip()
        yeni_cevap = ogret_eslesme.group(2).strip()
        kat_adi = f"ogrenilen_{int(time.time())}"
        json_komut_ekle(kat_adi, yeni_soru, yeni_cevap)
        st.session_state["bekleyen_ogret_sorusu"] = ""
        return (
            f"✅ **Harika, yeni bilgiyi öğrendim Ahmet!**\n\n"
            f"* **Soru:** `{yeni_soru}`\n"
            f"* **Cevap:** {yeni_cevap}\n\n"
            f"Artık bana **'{yeni_soru}'** diye sorduğunda doğrudan bu cevabı vereceğim! ⚡",
            hedef_dil,
            "Yeni Öğrenilen Bilgi",
        )

    # 0.4. Düzenli Deyim / Atasözü / Kelime Anlamı Yönlendiricisi (sıfır sapma!)
    _duzenli_y, _duzenli_e = tdk_duzenli_mod_yonlendir(kullanici_girdisi)
    if _duzenli_y:
        return _duzenli_y, hedef_dil, _duzenli_e

    # 0.5. TDK Yazım Denetimi veya Bağlamsal Cümle Kurma İsteği
    _tdk_low = kullanici_girdisi.lower()
    if _tdk_low.startswith(("tdk:", "tdk ara:", "yazım denetle:", "yazim denetle:")):
        hedef = kullanici_girdisi.split(":", 1)[1].strip()
        if "yazım" in _tdk_low or "yazim" in _tdk_low:
            bulgular, duzeltilmis, uyum = tdk_yazim_denetle(hedef)
            rapor = "\n".join(bulgular) if bulgular else "✅ Belirgin bir TDK yazım hatası bulunmadı."
            return (
                f"🇹🇷 **TDK Yazım & Ses Uyumu Denetimi:**\n\n{rapor}\n\n"
                f"📝 **Önerilen Metin:** {duzeltilmis}\n"
                f"🔤 **Ünlü Uyumu:** {', '.join(uyum[:5])}",
                hedef_dil,
                "TDK Yazım Denetimi",
            )
        sonuc = tdk_kelime_ara(hedef)
        if sonuc:
            anl_str = "\n".join([f"{i+1}. {a}" for i, a in enumerate(sonuc["anlamlar"])])
            return (
                f"📖 **{sonuc['madde']}** *({sonuc['kaynak']})*\n\n{anl_str}",
                hedef_dil,
                "TDK Sözlük",
            )
    if "cümle kur" in _tdk_low or "cumle kur" in _tdk_low:
        cumle_ornek, cozum = tdk_baglamsal_cumle_kur(baglam="Teknoloji & Yapay Zeka", ozne_kisi="biz", zaman="gelecek")
        if not st.session_state.get("api_aktif", True):
            return (
                f"🇹🇷 **TDK Bağlamsal Cümle Üretimi:**\n\n> **{cumle_ornek}**\n\n{cozum}",
                hedef_dil,
                "TDK Cümle Motoru",
            )

    cumleler = [c.strip() for c in re.split(r"[.!?\n]+", kullanici_girdisi) if c.strip()]
    raw_low = kullanici_girdisi.replace("İ", "i").replace("I", "ı").lower().replace("\u0307", "").strip()
    norm_low = metni_normallestir(kullanici_girdisi)

    yanit = None
    etiket = "Genel"

    # 1. Kesin yerel araçlar (Matematik motoru, Canlı Saat/Tarih, Öğretilen JSON tam eşleşme)
    y_zaman, e_zaman = _dinamik_zaman_kontrol(norm_low)
    if y_zaman:
        yanit, etiket = y_zaman, e_zaman
    if yanit is None:
        y_mat, e_mat = matematik_motoru_calistir(raw_low)
        if y_mat:
            yanit, etiket = y_mat, e_mat
    if yanit is None:
        for kat, icerik in json_oku().items():
            for kel in icerik.get("kelimeler", []):
                if metni_normallestir(kel) == norm_low:
                    yanit, etiket = icerik.get("yanit"), f"Öğretilen Hafıza: {kat}"
                    break
            if yanit:
                break

    # 1.4. Kimlik & Samimi Bağ & Fiziksel Cihaz İsteği ("Sen kardeş misin?", "Lambayı açar mısın?")
    if yanit is None and len(cumleler) <= 1:
        _k_y, _k_e = _sohbet_kimlik_ve_cihaz_kontrol(kullanici_girdisi)
        if _k_y:
            yanit, etiket = _k_y, _k_e

    # 1.5. TDK Deyim/Kelime Anlam Çözümlemeli Doğal Yanıt ("ne haber kanka" vb.)
    if yanit is None:
        tdk_y, tdk_e = tdk_sozluk_anlamli_sohbet_yaniti(kullanici_girdisi)
        if tdk_y:
            yanit, etiket = tdk_y, tdk_e

    # 2. API AÇIKSA genel sorular ("hava durumu", sohbet, 2+ cümle devamı) doğrudan Canlı API'ye gider!
    if yanit is None and st.session_state.get("api_aktif", True) and st.session_state.get("hibrit_ai_aktif", True):
        hibrit_y, hibrit_e = hibrit_ai_yanit_uret(kullanici_girdisi)
        if hibrit_y:
            yanit, etiket = hibrit_y, hibrit_e

    # 3. API Kapalıysa veya API erişilemezse: Çok cümleli yerel analiz
    if yanit is None and len(cumleler) >= 2:
        parca_yanitlar = []
        parca_etiketler = []
        for c in cumleler:
            c_y, _, c_e = _tek_cumle_yerel_coz(c)
            if not c_y:
                c_y, c_e = tdk_dinamik_chatbot_yaniti(c)
            if c_y:
                parca_yanitlar.append(c_y)
                parca_etiketler.append(c_e)
        if parca_yanitlar:
            yanit = "\n\n".join(parca_yanitlar) + "\n\n💡 *Başka ne eklemek veya devam etmek istersin Ahmet?*"
            etiket = " | ".join(parca_etiketler[:2])

    # 4. Tek cümle fallback
    if yanit is None:
        yanit, oto_en, etiket = _tek_cumle_yerel_coz(kullanici_girdisi)
        if yanit and oto_en and hedef_dil == "tr":
            hedef_dil = "en"

    # 5. Yerleşik Kod Üretici Fallback
    if yanit is None and st.session_state.get("hibrit_ai_aktif", True):
        hibrit_y, hibrit_e = hibrit_ai_yanit_uret(kullanici_girdisi)
        if hibrit_y:
            yanit, etiket = hibrit_y, hibrit_e

    # 5.3. Dinamik TDK Sözlük & Bağlamsal Chatbot Motoru (Her cümleyi TDK'den çözüp yanıtlar!)
    if yanit is None:
        tdk_dyn_y, tdk_dyn_e = tdk_dinamik_chatbot_yaniti(kullanici_girdisi)
        if tdk_dyn_y:
            yanit, etiket = tdk_dyn_y, tdk_dyn_e

    # 5.5. API'siz Yerel TDK Bağlamsal Devam Motoru (hiçbir cümle cevapsız kalmaz!)
    if yanit is None:
        st.session_state["bekleyen_ogret_sorusu"] = kullanici_girdisi.strip()
        yanit, etiket = yerel_baglamsal_devam_uret(kullanici_girdisi, st.session_state.get("messages", []))

    # 6. Bilinmeyen Soru -> "Bana öğretir misin?"
    if yanit is None:
        st.session_state["bekleyen_ogret_sorusu"] = kullanici_girdisi.strip()
        api_notu = "" if st.session_state.get("api_aktif", True) else "\n\n🔴 *Not: Şu an API Kapalı modundasın; üstten **🟢 API Aç** yaparsan serbest cümlelerin devamını da canlı AI getirebilir!*"
        yanit = (
            f"🤔 **'{kullanici_girdisi}'** ifadesi için yerel hafızamda henüz özel bir kayıt yok Ahmet. **Bana öğretir misin?**\n\n"
            "👇 Aşağıdaki **'🎓 Bana Öğret'** kutusuna cevabını yazıp kaydet; anında öğreneyim!"
            f"{api_notu}"
        )
        etiket = "Bana Öğretir misin?"

    if hedef_dil != "tr":
        try:
            temiz_cevirilecek = re.sub(r"[#*`]", "", yanit)
            yanit = guvenli_cevir(temiz_cevirilecek, src="tr", dest=hedef_dil)
        except Exception as e:
            st.warning(f"Çeviri hatası oluştu, Türkçe gösteriliyor: {e}")
            hedef_dil = "tr"

    return yanit, hedef_dil, etiket


# ==============================================================================
# 5. TDK TÜRKÇE DİLBİLGİSİ, SÖZLÜK İNDİRİCİ & BAĞLAMSAL CÜMLE KURMA MOTORU
# ==============================================================================
TDK_SOZLUK_CACHE_DOSYASI = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tdk_sozluk_cache.json")

_KALIN_UNLULER = set("aıouAIOU")
_INCE_UNLULER = set("eiöüEİÖÜ")
_TUM_UNLULER = _KALIN_UNLULER | _INCE_UNLULER
_DUZ_UNLULER = set("aeıiAEIİ")
_YUVARLAK_UNLULER = set("oöuüOÖUÜ")
_SERT_UNSUZLER = set("fstkçşhpFSTKÇŞHP")
_YUMUSAYAN_UNSUZLER = {"p": "b", "ç": "c", "t": "d", "k": "ğ"}

TDK_CEKIRDEK_SOZLUK = {
    "bilim": {"tur": "isim", "anlam": "Evrenin veya olayların bir bölümünü konu olarak seçen, deneye dayanan yöntemlerle sonuç çıkarmaya çalışan düzenli bilgi, ilim.", "baglam": ["Eğitim & Bilim", "Teknoloji & Yapay Zeka"]},
    "teknoloji": {"tur": "isim", "anlam": "Bir sanayi dalı ile ilgili yapım yöntemlerini, kullanılan araç, gereç ve aletleri, bunların kullanım biçimlerini kapsayan uygulama bilgisi.", "baglam": ["Teknoloji & Yapay Zeka", "İHA & Mühendislik"]},
    "yapay": {"tur": "sıfat", "anlam": "Doğadaki örneklerine benzetilerek insan eliyle yapılmış veya üretilmiş, suni.", "baglam": ["Teknoloji & Yapay Zeka"]},
    "zeka": {"tur": "isim", "anlam": "İnsanın düşünme, akıl yürütme, objektif gerçekleri algılama, yargılama ve sonuç çıkarma yeteneklerinin tamamı.", "baglam": ["Teknoloji & Yapay Zeka", "Eğitim & Bilim"]},
    "algoritma": {"tur": "isim", "anlam": "Bir problemin çözümü için izlenen, sonlu sayıda ve açıkça tanımlanmış kurallar dizisi.", "baglam": ["Teknoloji & Yapay Zeka", "İHA & Mühendislik"]},
    "veri": {"tur": "isim", "anlam": "Bir araştırmanın, bir tartışmanın, bir muhakemenin temeli olan ana öge; olgu, kavram veya komutların işlenmeye elverişli gösterimi.", "baglam": ["Teknoloji & Yapay Zeka"]},
    "geliştirmek": {"tur": "fiil", "anlam": "Gelişmesini sağlamak, büyütmek, ilerletmek, tekâmül ettirmek.", "baglam": ["Teknoloji & Yapay Zeka", "İHA & Mühendislik", "Eğitim & Bilim"]},
    "tasarlamak": {"tur": "fiil", "anlam": "Bir şeyi zihinde kurmak, planlamak, dizayn etmek.", "baglam": ["İHA & Mühendislik", "Teknoloji & Yapay Zeka"]},
    "çözümlemek": {"tur": "fiil", "anlam": "Bir bütünü ögelerine ayırarak incelemek, analiz etmek.", "baglam": ["Eğitim & Bilim", "Teknoloji & Yapay Zeka"]},
    "öğrenmek": {"tur": "fiil", "anlam": "Bilgi edinmek, bellemek, kavramak.", "baglam": ["Eğitim & Bilim", "Günlük Yaşam"]},
    "araştırmak": {"tur": "fiil", "anlam": "Bir gerçeği ortaya çıkarmak için düzenli ve yöntemli bir biçimde inceleme yapmak.", "baglam": ["Eğitim & Bilim", "Teknoloji & Yapay Zeka"]},
    "üretmek": {"tur": "fiil", "anlam": "Yeni bir şey ortaya koymak, imal etmek, meydana getirmek.", "baglam": ["İHA & Mühendislik", "Teknoloji & Yapay Zeka"]},
    "yazmak": {"tur": "fiil", "anlam": "Söz ve düşünceyi özel işaret veya harflerle anlatmak, kaleme almak.", "baglam": ["Eğitim & Bilim", "Teknoloji & Yapay Zeka", "Günlük Yaşam"]},
    "okumak": {"tur": "fiil", "anlam": "Yazıya geçirilmiş bir metne bakarak bunu sessizce çözümlemek veya sesli olarak söylemek.", "baglam": ["Eğitim & Bilim", "Günlük Yaşam"]},
    "planlamak": {"tur": "fiil", "anlam": "Bir işin, bir tasarımın gerçekleşmesi için uyulması gereken düzeni kurmak.", "baglam": ["Günlük Yaşam", "İHA & Mühendislik"]},
    "korumak": {"tur": "fiil", "anlam": "Bir kimseyi veya bir şeyi dış etkilerden, tehlikeden veya zor durumdan uzak tutmak.", "baglam": ["Doğa & Çevre", "İHA & Mühendislik"]},
    "kitap": {"tur": "isim", "anlam": "Ciltli veya ciltsiz olarak bir araya getirilmiş, basılı veya yazılı kâğıt yaprakların bütünü.", "baglam": ["Eğitim & Bilim", "Günlük Yaşam"]},
    "kalem": {"tur": "isim", "anlam": "Yazma, çizme vb. işlerde kullanılan türlü biçimlerde araç.", "baglam": ["Eğitim & Bilim"]},
    "ağaç": {"tur": "isim", "anlam": "Meyve verebilen, gövdesi odun veya kereste olmaya elverişli bulunan uzun ömürlü bitki.", "baglam": ["Doğa & Çevre"]},
    "doğa": {"tur": "isim", "anlam": "Kendi kuralları çerçevesinde sürekli gelişen, değişen canlı ve cansız varlıkların hepsi, tabiat.", "baglam": ["Doğa & Çevre"]},
    "gelecek": {"tur": "isim", "anlam": "Henüz gelmemiş, yaşanacak olan zaman, istikbal, ati.", "baglam": ["Teknoloji & Yapay Zeka", "Eğitim & Bilim"]},
    "başarı": {"tur": "isim", "anlam": "Başarılı olma durumu, muvaffakiyet.", "baglam": ["Eğitim & Bilim", "Günlük Yaşam"]},
    "sabır": {"tur": "isim", "anlam": "Acı, yoksulluk, haksızlık vb. üzücü durumlar karşısında ses çıkarmadan onların geçmesini bekleme erdemi.", "baglam": ["Günlük Yaşam", "Tarih & Kültür"]},
    "medeniyet": {"tur": "isim", "anlam": "Bir ülkenin veya toplumun maddi ve manevi varlıklarının, fikir, sanat, bilim ve teknoloji çalışmalarının bütünü, uygarlık.", "baglam": ["Tarih & Kültür"]},
    "otonom": {"tur": "sıfat", "anlam": "Kendi kendini yönetebilen, dış müdahale olmadan karar alıp uygulayabilen, özerk.", "baglam": ["İHA & Mühendislik", "Teknoloji & Yapay Zeka"]},
    "sensör": {"tur": "isim", "anlam": "Fiziksel veya kimyasal büyüklükleri algılayıp elektrik sinyaline dönüştüren algılayıcı.", "baglam": ["İHA & Mühendislik"]},
    "sistem": {"tur": "isim", "anlam": "Karşılıklı ilişkileri olan ve düzenli bir bütün oluşturan ögeler dizgesi, dizge.", "baglam": ["Teknoloji & Yapay Zeka", "İHA & Mühendislik"]},
}

TDK_YAZIM_HATALARI = {
    "herkez": "herkes",
    "yalnış": "yanlış",
    "yanlız": "yalnız",
    "bir çok": "birçok",
    "hiç bir": "hiçbir",
    "herşey": "her şey",
    "birşey": "bir şey",
    "hiçbirşey": "hiçbir şey",
    "pekçok": "pek çok",
    "orjinal": "orijinal",
    "makina": "makine",
    "şöför": "şoför",
    "traş": "tıraş",
    "direk": "direkt (doğrudan anlamında)",
    "insiyatif": "inisiyatif",
    "kiprik": "kirpik",
    "süpriz": "sürpriz",
    "labaratuvar": "laboratuvar",
    "peşpeşe": "peş peşe",
    "ardarda": "art arda",
    "bugünki": "bugünkü",
    "dünkü": "dünkü",
    "entellektüel": "entelektüel",
    "klavuz": "kılavuz",
    "kıravat": "kravat",
    "meyva": "meyve",
    "mütevazi": "mütevazı (alçak gönüllü anlamında)",
    "pijama": "pijama",
    "proğram": "program",
    "sağol": "sağ ol",
    "hoşçakal": "hoşça kal",
    "terketmek": "terk etmek",
    "farketmek": "fark etmek",
    "arzederim": "arz ederim",
    "teşekkür ederim": "teşekkür ederim",
    "şey": "(şey sözcüğü daima ayrı yazılır)",
}


def _son_unlu(kelime: str) -> str:
    for ch in reversed(kelime):
        if ch in _TUM_UNLULER:
            return ch.lower()
    return "e"


def _kalin_mi(unlu: str) -> bool:
    return unlu.lower() in {"a", "ı", "o", "u"}


def _duz_mu(unlu: str) -> bool:
    return unlu.lower() in {"a", "e", "ı", "i"}


def buyuk_unlu_uyumu_kontrol(kelime: str):
    unluler = [c.lower() for c in kelime if c in _TUM_UNLULER]
    if len(unluler) <= 1:
        return True, "Tek heceli veya tek ünlülü sözcüklerde büyük ünlü uyumu aranmaz."
    kalinlar = [u for u in unluler if _kalin_mi(u)]
    inceler = [u for u in unluler if not _kalin_mi(u)]
    if kalinlar and inceler:
        return False, f"Büyük ünlü uyumuna uymuyor (kalın: {kalinlar}, ince: {inceler})."
    tip = "kalın" if kalinlar else "ince"
    return True, f"Büyük ünlü uyumuna uyuyor (tüm ünlüler {tip})."


def kucuk_unlu_uyumu_kontrol(kelime: str):
    unluler = [c.lower() for c in kelime if c in _TUM_UNLULER]
    if len(unluler) <= 1:
        return True, "Tek ünlülü sözcüklerde küçük ünlü uyumu aranmaz."
    for i in range(len(unluler) - 1):
        onceki, sonraki = unluler[i], unluler[i + 1]
        if _duz_mu(onceki):
            if not _duz_mu(sonraki):
                return False, f"Küçük ünlü uyumuna uymuyor: düz '{onceki}' sonrası yuvarlak '{sonraki}' gelmiş."
        else:
            if sonraki not in {"a", "e", "u", "ü"}:
                return False, f"Küçük ünlü uyumuna uymuyor: yuvarlak '{onceki}' sonrası '{sonraki}' gelmiş."
    return True, "Küçük ünlü uyumuna tam uyuyor."


def _unsuz_yumusamasi_uygula(kok: str) -> str:
    if not kok:
        return kok
    istisnalar = {"at", "et", "ot", "süt", "ip", "ok", "saç", "koç", "kök", "top", "tüp", "park", "tank", "hukuk", "devlet", "millet", "sanat", "hayat"}
    if kok.lower() in istisnalar or kok.lower().endswith(("yet", "iyat", "aat", "kat")):
        return kok
    son = kok[-1].lower()
    if son in _YUMUSAYAN_UNSUZLER:
        if kok.lower().endswith("nk"):
            return kok[:-1] + "g"
        return kok[:-1] + _YUMUSAYAN_UNSUZLER[son]
    return kok


def isim_hal_eki_ekle(isim: str, hal: str = "yalın") -> str:
    """TDK ses kurallarına göre isim hal eklerini (belirtme, yönelme, bulunma, ayrılma, tamlayan) ekler."""
    isim = isim.strip()
    if not isim or hal == "yalın":
        return isim
    son_u = _son_unlu(isim)
    son_harf = isim[-1].lower()
    unluyle_biter = son_harf in _TUM_UNLULER
    sert_biter = son_harf in _SERT_UNSUZLER

    if son_u in {"a", "ı"}:
        dar, genis = "ı", "a"
    elif son_u in {"e", "i"}:
        dar, genis = "i", "e"
    elif son_u in {"o", "u"}:
        dar, genis = "u", "a"
    else:
        dar, genis = "ü", "e"

    if hal == "belirtme":
        if unluyle_biter:
            return f"{isim}y{dar}"
        return f"{_unsuz_yumusamasi_uygula(isim)}{dar}"
    if hal == "yönelme":
        if unluyle_biter:
            return f"{isim}y{genis}"
        return f"{_unsuz_yumusamasi_uygula(isim)}{genis}"
    if hal == "bulunma":
        bas = "t" if sert_biter else "d"
        return f"{isim}{bas}{genis}"
    if hal == "ayrılma":
        bas = "t" if sert_biter else "d"
        return f"{isim}{bas}{genis}n"
    if hal == "tamlayan":
        if unluyle_biter:
            return f"{isim}n{dar}n"
        return f"{_unsuz_yumusamasi_uygula(isim)}{dar}n"
    return isim


def fiil_cekimle(fiil_mastar: str, zaman: str = "şimdiki", kisi: str = "ben", olumsuz: bool = False, soru: bool = False) -> str:
    """TDK ünlü/ünsüz uyumlarına göre Türkçe fiil çekimi yapar."""
    f = fiil_mastar.strip().lower()
    if f.endswith(("mak", "mek")) and len(f) > 3:
        kok = f[:-3]
    else:
        kok = f

    if olumsuz:
        son_u = _son_unlu(kok)
        olumsuz_ek = "ma" if _kalin_mi(son_u) else "me"
        kok = kok + olumsuz_ek

    son_u = _son_unlu(kok)
    son_harf = kok[-1]
    unluyle_biter = son_harf in _TUM_UNLULER
    sert_biter = son_harf in _SERT_UNSUZLER

    def _dar_unlu(u):
        if u in {"a", "ı"}:
            return "ı"
        if u in {"e", "i"}:
            return "i"
        if u in {"o", "u"}:
            return "u"
        return "ü"

    def _genis_a_e(u):
        return "a" if _kalin_mi(u) else "e"

    govde = kok
    if zaman == "şimdiki":
        if unluyle_biter:
            if kok[-1] in {"a", "e"}:
                govde = kok[:-1]
                dar = _dar_unlu(_son_unlu(govde) if govde else son_u)
                govde = govde + dar + "yor"
            else:
                govde = kok + "yor"
        else:
            yum_kok = _unsuz_yumusamasi_uygula(kok) if kok in {"git", "et", "tat", "güt"} else kok
            govde = yum_kok + _dar_unlu(son_u) + "yor"
        kip_son_u = "o"
    elif zaman == "geçmiş_görülen":
        d_harfi = "t" if sert_biter else "d"
        dar = _dar_unlu(son_u)
        govde = kok + d_harfi + dar
        kip_son_u = dar
    elif zaman == "geçmiş_öğrenilen":
        dar = _dar_unlu(son_u)
        govde = kok + "m" + dar + "ş"
        kip_son_u = dar
    elif zaman == "gelecek":
        yum_kok = _unsuz_yumusamasi_uygula(kok) if kok in {"git", "et"} else kok
        ae = _genis_a_e(son_u)
        kaynastirma = "y" if unluyle_biter else ""
        govde = f"{yum_kok}{kaynastirma}{ae}c{ae}k"
        kip_son_u = ae
    elif zaman == "geniş":
        if olumsuz:
            govde = kok + ("z" if kisi not in {"ben", "biz"} else "")
            kip_son_u = _son_unlu(kok)
        elif unluyle_biter:
            govde = kok + "r"
            kip_son_u = son_u
        else:
            ae = _genis_a_e(son_u)
            govde = kok + ae + "r"
            kip_son_u = ae
    elif zaman == "gereklilik":
        ae = _genis_a_e(son_u)
        govde = kok + "m" + ae + "l" + ("ı" if _kalin_mi(son_u) else "i")
        kip_son_u = "ı" if _kalin_mi(son_u) else "i"
    else:
        govde = kok
        kip_son_u = son_u

    # Kişi ekleri
    if zaman == "geçmiş_görülen":
        kisi_tablo = {
            "ben": "m",
            "sen": "n",
            "o": "",
            "biz": "k",
            "siz": f"n{_dar_unlu(kip_son_u)}z",
            "onlar": f"l{_genis_a_e(kip_son_u)}r",
        }
        cekimli = govde + kisi_tablo.get(kisi, "")
    else:
        dar_k = _dar_unlu(kip_son_u)
        ae_k = _genis_a_e(kip_son_u)
        if kisi == "ben":
            if zaman == "gelecek":
                cekimli = govde[:-1] + "ğ" + dar_k + "m"
            elif zaman == "gereklilik":
                cekimli = govde + "y" + dar_k + "m"
            elif zaman == "geniş" and olumsuz:
                cekimli = govde + "m"
            else:
                cekimli = govde + dar_k + "m"
        elif kisi == "sen":
            cekimli = govde + "s" + dar_k + "n"
        elif kisi == "o":
            cekimli = govde
        elif kisi == "biz":
            if zaman == "gelecek":
                cekimli = govde[:-1] + "ğ" + dar_k + "z"
            elif zaman == "gereklilik":
                cekimli = govde + "y" + dar_k + "z"
            elif zaman == "geniş" and olumsuz:
                cekimli = govde + "y" + dar_k + "z"
            else:
                cekimli = govde + dar_k + "z"
        elif kisi == "siz":
            cekimli = govde + "s" + dar_k + "n" + dar_k + "z"
        elif kisi == "onlar":
            cekimli = govde + "l" + ae_k + "r"
        else:
            cekimli = govde

    if soru:
        soru_u = _dar_unlu(_son_unlu(cekimli))
        return f"{cekimli} m{soru_u}?"
    return cekimli


def tdk_sozluk_indir(timeout: int = 20):
    """
    Resmi TDK Güncel Türkçe Sözlük kelime listesini (https://sozluk.gov.tr/autocomplete.json)
    Python üzerinden indirir ve tdk_sozluk_cache.json dosyasına kaydeder.
    """
    try:
        req = urllib.request.Request(
            "https://sozluk.gov.tr/autocomplete.json",
            headers={"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) ArAIStudio/5.5"},
        )
        with urllib.request.urlopen(req, timeout=timeout) as resp:
            ham = json.loads(resp.read().decode("utf-8"))
        kelimeler = sorted({item.get("madde", "").strip() for item in ham if isinstance(item, dict) and item.get("madde")})
        with open(TDK_SOZLUK_CACHE_DOSYASI, "w", encoding="utf-8") as f:
            json.dump({"toplam": len(kelimeler), "kelimeler": kelimeler}, f, ensure_ascii=False)
        return True, len(kelimeler), f"✅ TDK resmi sözlüğünden **{len(kelimeler):,}** kelime indirildi ve yerel önbelleğe kaydedildi!".replace(",", ".")
    except Exception as exc:
        return False, 0, f"⚠️ TDK sözlüğü indirilemedi ({exc}). Çekirdek sözlük ({len(TDK_CEKIRDEK_SOZLUK)} kelime) aktif."


def tdk_yerel_sozluk_yukle():
    if os.path.exists(TDK_SOZLUK_CACHE_DOSYASI):
        try:
            with open(TDK_SOZLUK_CACHE_DOSYASI, "r", encoding="utf-8") as f:
                veri = json.load(f)
            return veri.get("kelimeler", [])
        except Exception:
            return []
    return []


def tdk_kelime_ara(kelime: str):
    """Önce canlı TDK GTS API (sozluk.gov.tr/gts?ara=), olmazsa yerel sözlükte arar."""
    import urllib.parse

    temiz = kelime.strip()
    if not temiz:
        return None
    try:
        url = f"https://sozluk.gov.tr/gts?ara={urllib.parse.quote(temiz)}"
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 ArAIStudio/5.5"})
        with urllib.request.urlopen(req, timeout=8) as resp:
            veri = json.loads(resp.read().decode("utf-8"))
        if isinstance(veri, list) and veri and isinstance(veri[0], dict) and "madde" in veri[0]:
            madde = veri[0]
            anlamlar = [a.get("anlam", "") for a in madde.get("anlamlarListe", [])[:4] if a.get("anlam")]
            ornekler = []
            for a in madde.get("anlamlarListe", [])[:2]:
                for o in a.get("orneklerListe", [])[:1]:
                    if o.get("ornek"):
                        ornekler.append(o["ornek"])
            return {
                "kaynak": "TDK Canlı GTS (sozluk.gov.tr)",
                "madde": madde.get("madde", temiz),
                "anlamlar": anlamlar,
                "ornekler": ornekler,
            }
    except Exception:
        pass

    yerel_bilgi = TDK_CEKIRDEK_SOZLUK.get(temiz.lower())
    if yerel_bilgi:
        return {
            "kaynak": "TDK Çekirdek Sözlük (Yerel)",
            "madde": temiz.lower(),
            "anlamlar": [f"({yerel_bilgi['tur']}) {yerel_bilgi['anlam']}"],
            "ornekler": [],
        }

    indirilen = tdk_yerel_sozluk_yukle()
    if indirilen:
        eslesen = [k for k in indirilen if k.lower().startswith(temiz.lower())][:8]
        if eslesen:
            return {
                "kaynak": "TDK İndirilen Yerel Sözlük",
                "madde": temiz,
                "anlamlar": [f"Sözlükte eşleşen TDK maddeleri: {', '.join(eslesen)}"],
                "ornekler": [],
            }
    return None


def tdk_yazim_denetle(metin: str):
    """TDK Yazım Kılavuzu kurallarına göre yaygın yazım hatalarını ve ses uyumlarını denetler."""
    bulgular = []
    duzeltilmis = metin
    for yanlis, dogru in TDK_YAZIM_HATALARI.items():
        if yanlis == "şey":
            continue
        if re.search(rf"\b{re.escape(yanlis)}\b", metin, flags=re.IGNORECASE):
            bulgular.append(f"❌ **`{yanlis}`** → Doğrusu: **`{dogru}`**")
            if "(" not in dogru:
                duzeltilmis = re.sub(rf"\b{re.escape(yanlis)}\b", dogru, duzeltilmis, flags=re.IGNORECASE)

    if re.search(r"\b\w+(mı|mi|mu|mü)\b", metin, flags=re.IGNORECASE):
        pass  # doğru ayrı yazım
    if re.search(r"[a-zçğıöşü]{3,}(mısın|misin|musun|müsün)\b", metin, flags=re.IGNORECASE):
        bulgular.append("⚠️ **Soru eki (`mı/mi/mu/mü`):** TDK'ye göre kendisinden önceki sözcükten **ayrı**, kendisinden sonraki eklerle **bitişik** yazılır (ör. *geliyor musun*). ")

    kelimeler = [re.sub(r"[^a-zA-ZçğıöşüÇĞİÖŞÜ]", "", k) for k in metin.split()]
    uyum_raporu = []
    for k in kelimeler[:8]:
        if len(k) >= 3:
            b_ok, _ = buyuk_unlu_uyumu_kontrol(k)
            k_ok, _ = kucuk_unlu_uyumu_kontrol(k)
            uyum_raporu.append(f"`{k}` (Büyük: {'✅' if b_ok else '⚠️'} | Küçük: {'✅' if k_ok else '⚠️'})")

    return bulgular, duzeltilmis, uyum_raporu


def tdk_baglamsal_cumle_kur(
    baglam: str = "Teknoloji & Yapay Zeka",
    ozne_kisi: str = "ben",
    zaman: str = "şimdiki",
    ozel_nesne: str = "",
    ozel_fiil: str = "",
    olumsuz: bool = False,
    soru: bool = False,
):
    """
    TDK sözdizimi (Özne + Zaman/Yer Tümleci + Nesne + Yüklem) ve ek uyum kurallarına göre
    bağlamsal olarak anlamlı Türkçe cümleler üretir ve dilbilgisi çözümlemesini döndürür.
    """
    ozne_adlari = {
        "ben": "Ben",
        "sen": "Sen",
        "o": "Ahmet",
        "biz": "Biz",
        "siz": "Siz",
        "onlar": "Öğrenciler",
    }
    zaman_zarflari = {
        "şimdiki": "bugün",
        "geçmiş_görülen": "dün",
        "geçmiş_öğrenilen": "geçen hafta",
        "gelecek": "yarın",
        "geniş": "her zaman",
        "gereklilik": "mutlaka",
    }
    baglam_sablonlari = {
        "Teknoloji & Yapay Zeka": [
            ("yapay zeka", "belirtme", "geliştirmek"),
            ("algoritma", "belirtme", "çözümlemek"),
            ("sistem", "belirtme", "öğrenmek"),
            ("veri", "belirtme", "araştırmak"),
        ],
        "Eğitim & Bilim": [
            ("kitap", "belirtme", "okumak"),
            ("bilim", "belirtme", "araştırmak"),
            ("başarı", "belirtme", "planlamak"),
            ("gelecek", "belirtme", "planlamak"),
        ],
        "İHA & Mühendislik": [
            ("otonom sistem", "belirtme", "tasarlamak"),
            ("sensör", "belirtme", "geliştirmek"),
            ("teknoloji", "belirtme", "üretmek"),
        ],
        "Doğa & Çevre": [
            ("doğa", "belirtme", "korumak"),
            ("ağaç", "belirtme", "korumak"),
        ],
        "Tarih & Kültür": [
            ("medeniyet", "belirtme", "araştırmak"),
            ("kitap", "ayrılma", "öğrenmek"),
        ],
        "Günlük Yaşam": [
            ("kitap", "belirtme", "okumak"),
            ("kitap", "belirtme", "okumak"),
        ],
    }

    import random
    secenekler = baglam_sablonlari.get(baglam, baglam_sablonlari["Teknoloji & Yapay Zeka"])
    varsayilan_nesne, hal, varsayilan_fiil = random.choice(secenekler)
    nesne_kok = ozel_nesne.strip() or varsayilan_nesne
    fiil_kok = ozel_fiil.strip() or varsayilan_fiil

    ozne_str = ozne_adlari.get(ozne_kisi, "Ben")
    zaman_str = zaman_zarflari.get(zaman, "bugün")
    nesne_cekimli = isim_hal_eki_ekle(nesne_kok, hal)
    yuklem_cekimli = fiil_cekimle(fiil_kok, zaman=zaman, kisi=ozne_kisi, olumsuz=olumsuz, soru=soru)

    if soru and not yuklem_cekimli.endswith("?"):
        yuklem_cekimli += "?"
    elif not soru and not yuklem_cekimli.endswith("."):
        yuklem_cekimli += "."

    cumle = f"{ozne_str} {zaman_str} {nesne_cekimli} {yuklem_cekimli}"
    cozumleme = (
        f"• **Özne:** `{ozne_str}`  |  **Zaman Tümleci:** `{zaman_str}`  |  "
        f"**Nesne ({hal} hâli):** `{nesne_kok}` → `{nesne_cekimli}`  |  "
        f"**Yüklem ({zaman}, {ozne_kisi}):** `{fiil_kok}` → `{yuklem_cekimli.rstrip('.?')}`"
    )
    return cumle, cozumleme


def yerel_baglamsal_devam_uret(kullanici_girdisi: str, gecmis_mesajlar=None):
    """
    API bağlantısı olmadığında kullanıcının 1 veya 2+ cümlelik girdisini TDK sözlük kökleri,
    bağlam anahtarları ve Türkçe sözdizimi kurallarıyla analiz edip akıcı bir devam yanıtı üretir.
    """
    girdi_low = kullanici_girdisi.lower()
    kelimeler = [re.sub(r"[^a-zA-ZçğıöşüÇĞİÖŞÜ]", "", k) for k in girdi_low.split()]
    kelimeler = [k for k in kelimeler if len(k) >= 3]

    # Bağlam tespiti
    if any(k in girdi_low for k in ["iha", "drone", "uçuş", "ucus", "sensör", "sensor", "bebek arabası", "teknofest", "tübitak", "tubitak", "motor", "arduino"]):
        sec_baglam = "İHA & Mühendislik"
    elif any(k in girdi_low for k in ["kod", "python", "yapay zeka", "algoritma", "yazılım", "yazilim", "veri", "program", "bilgisayar"]):
        sec_baglam = "Teknoloji & Yapay Zeka"
    elif any(k in girdi_low for k in ["okul", "ders", "sınav", "sinav", "matematik", "kitap", "okumak", "öğren", "ogren", "bilim", "lgs"]):
        sec_baglam = "Eğitim & Bilim"
    elif any(k in girdi_low for k in ["doğa", "doga", "ağaç", "agac", "hava", "yağmur", "yagmur", "güneş", "gunes", "çevre", "cevre"]):
        sec_baglam = "Doğa & Çevre"
    elif any(k in girdi_low for k in ["tarih", "medeniyet", "osmanlı", "osmanli", "kültür", "kultur", "âlim", "alim"]):
        sec_baglam = "Tarih & Kültür"
    else:
        sec_baglam = "Günlük Yaşam"

    # Kullanıcının cümlesinden TDK çekirdek sözlük eşleşmesi bul
    bulunan_tdk = []
    for kel in kelimeler:
        if kel in TDK_CEKIRDEK_SOZLUK:
            bulunan_tdk.append((kel, TDK_CEKIRDEK_SOZLUK[kel]))

    # Bağlamsal 2 özgün TDK cümlesi kur
    cumle_1, coz_1 = tdk_baglamsal_cumle_kur(baglam=sec_baglam, ozne_kisi="biz", zaman="şimdiki")
    cumle_2, _ = tdk_baglamsal_cumle_kur(baglam=sec_baglam, ozne_kisi="biz", zaman="gelecek")
    if cumle_2 == cumle_1:
        cumle_2, _ = tdk_baglamsal_cumle_kur(baglam=sec_baglam, ozne_kisi="sen", zaman="gereklilik")

    sozluk_notu = ""
    if bulunan_tdk:
        k_ad, k_bilgi = bulunan_tdk[0]
        sozluk_notu = f"\n📖 **TDK Sözlük Bağlamı (`{k_ad}` - {k_bilgi['tur']}):** {k_bilgi['anlam']}"

    soru_mu = "?" in kullanici_girdisi or any(w in girdi_low.split() for w in ["mi", "mı", "mu", "mü", "nasıl", "nasil", "neden", "nedir", "kim", "ne"])
    giris_cumlesi = (
        f"🧩 **Yerel TDK Bağlam Motoru ({sec_baglam}):** Söylediklerini dikkatle inceledim Ahmet."
        if not soru_mu
        else f"🧩 **Yerel TDK Bağlam Motoru ({sec_baglam}):** Sorunu **{sec_baglam}** bağlamında değerlendirdim Ahmet."
    )

    yanit = (
        f"{giris_cumlesi}\n\n"
        f"• {cumle_1}\n"
        f"• {cumle_2}"
        f"{sozluk_notu}\n\n"
        f"💡 *Bu konuda özel bir cevap ezberletmek istersen aşağıdan **🎓 Bana Öğret** kutusunu kullanabilir veya yeni bir cümle kurabilirsin.*"
    )
    return yanit, f"Yerel TDK Motoru ({sec_baglam})"

TDK_CEKIRDEK_SOZLUK.update({'ne haber': {'tur': 'deyim / selamlaşma', 'niyet': 'hatir_sorma', 'anlam': 'Nasılsınız, ne var ne yok, herhangi bir bilgi veya gelişme var mı anlamında kullanılan hâl hatır sorma sözü.', 'baglam': ['Günlük Yaşam', 'Sohbet']}, 'naber': {'tur': 'konuşma dili (ne haber)', 'niyet': 'hatir_sorma', 'anlam': "'Ne haber?' sözünün günlük konuşma dilindeki kaynaşmış biçimi; hâl hatır sorma ifadesi.", 'baglam': ['Günlük Yaşam', 'Sohbet']}, 'ne var ne yok': {'tur': 'deyim / selamlaşma', 'niyet': 'hatir_sorma', 'anlam': 'Nasılsınız, neler oluyor, hayat nasıl gidiyor anlamında samimi hâl hatır sorma sözü.', 'baglam': ['Günlük Yaşam', 'Sohbet']}, 'nasılsın': {'tur': 'soru / hâl hatır', 'niyet': 'hatir_sorma', 'anlam': 'Karşıdaki kişinin sağlık, keyif ve ruh durumunu sormak için kullanılan söz.', 'baglam': ['Günlük Yaşam', 'Sohbet']}, 'kanka': {'tur': 'isim (teklifsiz konuşma)', 'niyet': 'hitap_samimi', 'hitap_yanit': 'kanka', 'anlam': "'Kan kardeşi' sözünden kısaltma; kardeş kadar yakın olan kimse, çok samimi arkadaş.", 'baglam': ['Günlük Yaşam', 'Sohbet']}, 'kanki': {'tur': 'isim (teklifsiz konuşma)', 'niyet': 'hitap_samimi', 'hitap_yanit': 'kanki', 'anlam': 'Kanka; çok yakın, samimi arkadaş.', 'baglam': ['Günlük Yaşam', 'Sohbet']}, 'dost': {'tur': 'isim', 'niyet': 'hitap_samimi', 'hitap_yanit': 'dostum', 'anlam': 'Sevilen, güvenilen, yakın arkadaş, gönüldaş.', 'baglam': ['Günlük Yaşam', 'Sohbet']}, 'dostum': {'tur': 'isim + iyelik', 'niyet': 'hitap_samimi', 'hitap_yanit': 'dostum', 'anlam': 'Benim yakın arkadaşım, gönüldaşım anlamında samimi hitap.', 'baglam': ['Günlük Yaşam', 'Sohbet']}, 'arkadaş': {'tur': 'isim', 'niyet': 'hitap_samimi', 'hitap_yanit': 'arkadaşım', 'anlam': 'Birbirine karşı sevgi ve anlayış gösteren kimselerden her biri, yoldaş.', 'baglam': ['Günlük Yaşam', 'Sohbet']}, 'kardeş': {'tur': 'isim', 'niyet': 'hitap_samimi', 'hitap_yanit': 'kardeşim', 'anlam': 'Aynı anne babadan doğan veya aralarında çok güçlü yakınlık bulunan kimse.', 'baglam': ['Günlük Yaşam', 'Sohbet']}, 'kardeşim': {'tur': 'isim + iyelik', 'niyet': 'hitap_samimi', 'hitap_yanit': 'kardeşim', 'anlam': 'Yakınlık ve samimiyet bildiren hitap sözü.', 'baglam': ['Günlük Yaşam', 'Sohbet']}, 'selam': {'tur': 'isim / ünlem', 'niyet': 'selamlasma', 'anlam': 'Biriyle karşılaşıldığında veya ayrılırken söylenen esenlik ve barış dileği sözü.', 'baglam': ['Günlük Yaşam', 'Sohbet']}, 'merhaba': {'tur': 'ünlem', 'niyet': 'selamlasma', 'anlam': 'Karşılaşıldığında söylenen esenlik ve hoşnutluk bildiren selamlaşma sözü.', 'baglam': ['Günlük Yaşam', 'Sohbet']}, 'günaydın': {'tur': 'ünlem', 'niyet': 'selamlasma', 'anlam': "Sabahları söylenen 'gününüz aydın ve iyi geçsin' anlamındaki selamlaşma sözü.", 'baglam': ['Günlük Yaşam']}, 'iyi akşamlar': {'tur': 'kalıp söz', 'niyet': 'selamlasma', 'anlam': 'Akşam saatlerinde karşılaşıldığında veya ayrılırken söylenen iyi dilek sözü.', 'baglam': ['Günlük Yaşam']}, 'kolay gelsin': {'tur': 'deyim / iyi dilek', 'niyet': 'iyi_dilek', 'anlam': 'Bir iş yapmakta olan kimseye işinin rahat ve başarılı geçmesi için söylenen dilek sözü.', 'baglam': ['Günlük Yaşam']}, 'eyvallah': {'tur': 'ünlem', 'niyet': 'tesekkur_onay', 'anlam': "'Teşekkür ederim, kabul, hoşça kal' anlamlarında kullanılan samimi onay ve şükran sözü.", 'baglam': ['Günlük Yaşam']}, 'teşekkür': {'tur': 'isim', 'niyet': 'tesekkur_onay', 'anlam': 'Yapılan bir iyiliğe karşı duyulan gönül borcunu sözle bildirme.', 'baglam': ['Günlük Yaşam']}, 'hava': {'tur': 'isim', 'niyet': 'konu', 'anlam': 'Yeryüzünü saran gaz tabakası veya meteorolojik sıcaklık, yağış, rüzgâr durumu.', 'baglam': ['Doğa & Çevre']}, 'durum': {'tur': 'isim', 'niyet': 'konu', 'anlam': 'Bir şeyin içinde bulunduğu şartların bütünü, hâl, vaziyet.', 'baglam': ['Günlük Yaşam']}})


def tdk_sozlukte_coklu_coz(kullanici_girdisi: str):
    """
    Cümledeki çok kelimeli deyimleri ('ne haber', 'kolay gelsin', ...) ve tekil sözcükleri
    TDK sözlüğünde (çekirdek + indirilen cache) analiz eder.
    """
    temiz_low = kullanici_girdisi.replace("İ", "i").replace("I", "ı").lower().replace("\u0307", "")
    temiz_low = re.sub(r"[?!.,;:\"'()]", " ", temiz_low)
    temiz_low = re.sub(r"\s+", " ", temiz_low).strip()

    bulunanlar = []
    kullanilan_aralik = temiz_low

    cok_kelimeliler = sorted([k for k in TDK_CEKIRDEK_SOZLUK.keys() if " " in k], key=len, reverse=True)
    for kalip in cok_kelimeliler:
        if re.search(rf"\b{re.escape(kalip)}\b", kullanilan_aralik):
            bulunanlar.append((kalip, TDK_CEKIRDEK_SOZLUK[kalip]))
            kullanilan_aralik = re.sub(rf"\b{re.escape(kalip)}\b", " ", kullanilan_aralik)

    indirilen_set = set(k.lower() for k in tdk_yerel_sozluk_yukle())
    for kel in kullanilan_aralik.split():
        if len(kel) < 2:
            continue
        if kel in TDK_CEKIRDEK_SOZLUK:
            bulunanlar.append((kel, TDK_CEKIRDEK_SOZLUK[kel]))
        elif kel in indirilen_set:
            bulunanlar.append((kel, {"tur": "TDK Sözlük Maddesi", "niyet": "konu", "anlam": f"'{kel}' sözcüğü indirilen resmi TDK sözlüğünde kayıtlıdır.", "baglam": ["Günlük Yaşam"]}))

    return bulunanlar


def tdk_sozluk_anlamli_sohbet_yaniti(kullanici_girdisi: str):
    """
    Örn: 'ne haber kanka' dendiğinde 'ne haber' ve 'kanka' kelimelerinin TDK anlamlarını çözer,
    ikisini birleştirip hem TDK anlam karşılığını hem de bağlama uygun doğal yanıtı üretir.
    """
    bulunanlar = tdk_sozlukte_coklu_coz(kullanici_girdisi)
    if not bulunanlar:
        return None, None

    niyetler = {b[1].get("niyet") for b in bulunanlar}
    hitaplar = [b[1].get("hitap_yanit") for b in bulunanlar if b[1].get("hitap_yanit")]
    hitap = hitaplar[0] if hitaplar else "Ahmet"

    if niyetler & {"hatir_sorma", "selamlasma", "iyi_dilek", "tesekkur_onay", "hitap_samimi"}:
        if "hatir_sorma" in niyetler:
            ana_yanit = f"İyidir **{hitap}**, bomba gibiyim! Senden ne haber, projeler nasıl gidiyor? ⚡"
        elif "selamlasma" in niyetler:
            ana_yanit = f"Selamlar **{hitap}**, hoş geldin! Bugün beraber ne yapalım? ⚡"
        elif "iyi_dilek" in niyetler:
            ana_yanit = f"Sağ olasın **{hitap}**, sana da kolay gelsin! ⚡"
        elif "tesekkur_onay" in niyetler:
            ana_yanit = f"Rica ederim **{hitap}**, her zaman buradayım! ⚡"
        else:
            ana_yanit = f"Buradayım **{hitap}**, seni dinliyorum! ⚡"

        tdk_satirlari = [
            f"• **`{kel}`** *({bilgi['tur']})*: {bilgi['anlam']}"
            for kel, bilgi in bulunanlar
        ]
        tam_yanit = (
            f"{ana_yanit}\n\n"
            f"📖 **TDK Sözlük Anlam Çözümlemesi:**\n" + "\n".join(tdk_satirlari)
        )
        return tam_yanit, "TDK Anlamlı Sohbet"
    return None, None


# ==============================================================================
# 6. DİNAMİK TDK ANLAM ÇEKİCİ, KÖK ÇÖZÜMLEYİCİ & AKILLI SOHBET MOTORU (v5.8)
# ==============================================================================
TDK_ANLAM_ONBELLEK_DOSYASI = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tdk_anlam_onbellek.json")

_TR_DURAK_KELIMELER = {
    "ve", "veya", "ile", "bir", "bu", "şu", "o", "da", "de", "ki", "mi", "mı", "mu", "mü",
    "ama", "fakat", "lakin", "çünkü", "için", "gibi", "kadar", "daha", "çok", "en", "az",
    "ben", "sen", "biz", "siz", "onlar", "bana", "sana", "ona", "bize", "size", "beni", "seni",
    "ne", "nasıl", "neden", "niçin", "kim", "nerede", "hangi", "nedir", "midir", "mıdır",
    "var", "yok", "evet", "hayır", "tamam", "peki", "şey", "her", "hiç", "bazı", "olan",
    "olarak", "oldu", "olur", "olmak", "etmek", "yapmak", "yap", "söyle", "anlat", "konuş",
    "bugün", "yarın", "dün", "şimdi", "sonra", "önce", "hakkında", "ilgili", "lütfen",
}


def _tdk_anlam_onbellek_oku() -> dict:
    if os.path.exists(TDK_ANLAM_ONBELLEK_DOSYASI):
        try:
            with open(TDK_ANLAM_ONBELLEK_DOSYASI, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}


def _tdk_anlam_onbellek_yaz(veri: dict):
    try:
        with open(TDK_ANLAM_ONBELLEK_DOSYASI, "w", encoding="utf-8") as f:
            json.dump(veri, f, ensure_ascii=False, indent=2)
    except Exception:
        pass


def _turkce_kok_adaylari_uret(kelime: str):
    """Kelimenin olası TDK sözlük köklerini (çekim eklerini soyarak) üretir."""
    k = kelime.lower().strip()
    adaylar = [k]
    ekler = [
        "lerimiz", "larımız", "leriniz", "larınız", "lerden", "lardan", "lerde", "larda",
        "lerin", "ların", "leri", "ları", "yorum", "iyorum", "ıyorum", "uyorum", "üyorum",
        "yoruz", "iyoruz", "ıyoruz", "uyoruz", "üyoruz", "eceğim", "acağım", "ecek", "acak",
        "muşum", "mişim", "müşüm", "mışım", "duğun", "düğün", "diğin", "dığın",
        "ından", "inden", "undan", "ünden", "sında", "sinde", "sunda", "sünde",
        "ları", "leri", "lar", "ler", "dan", "den", "tan", "ten", "da", "de", "ta", "te",
        "ya", "ye", "yı", "yi", "yu", "yü", "ım", "im", "um", "üm", "ın", "in", "un", "ün",
        "sı", "si", "su", "sü", "la", "le", "lı", "li", "lu", "lü", "lık", "lik", "luk", "lük",
        "cı", "ci", "cu", "cü", "çı", "çi", "çu", "çü", "a", "e", "ı", "i", "u", "ü",
    ]
    for ek in ekler:
        if k.endswith(ek) and len(k) - len(ek) >= 3:
            kok = k[: -len(ek)]
            adaylar.append(kok)
            # Ünsüz yumuşaması geri çevirme (kitab -> kitap, ağac -> ağaç, reng -> renk)
            if kok.endswith("b"):
                adaylar.append(kok[:-1] + "p")
            elif kok.endswith("c"):
                adaylar.append(kok[:-1] + "ç")
            elif kok.endswith("d"):
                adaylar.append(kok[:-1] + "t")
            elif kok.endswith("ğ"):
                adaylar.append(kok[:-1] + "k")
            elif kok.endswith("g") and len(kok) >= 3:
                adaylar.append(kok[:-1] + "k")
    # Tekrarları sırayı koruyarak kaldır
    goruldu = set()
    sonuc = []
    for a in adaylar:
        if a not in goruldu and len(a) >= 2:
            goruldu.add(a)
            sonuc.append(a)
    return sonuc


def tdk_akilli_kelime_getir(kelime: str):
    """
    Bir kelime veya kökü için sırasıyla:
      1) Yerel TDK Anlam Önbelleği (tdk_anlam_onbellek.json)
      2) TDK Çekirdek Sözlük
      3) Canlı TDK GTS (sozluk.gov.tr/gts?ara=...) -> bulursa önbelleğe kaydeder
      4) İndirilen TDK Kelime Listesi (tdk_sozluk_cache.json)
    kaynaklarından anlam çeker.
    """
    onbellek = _tdk_anlam_onbellek_oku()
    harici_kokler = harici_kutuphane_ile_kok_bul(kelime)
    yerlesik_kokler = _turkce_kok_adaylari_uret(kelime)
    adaylar = []
    for _a in harici_kokler + yerlesik_kokler:
        if _a not in adaylar:
            adaylar.append(_a)

    # 1 & 2) Önce önbellek ve çekirdek sözlükte hızlı kontrol
    for aday in adaylar:
        if aday in onbellek:
            return onbellek[aday]
        if aday in TDK_CEKIRDEK_SOZLUK:
            bilgi = TDK_CEKIRDEK_SOZLUK[aday]
            return {
                "kaynak": "TDK Çekirdek Sözlük",
                "madde": aday,
                "tur": bilgi.get("tur", "sözcük"),
                "anlamlar": [bilgi.get("anlam", "")],
                "ornekler": [],
            }

    # 3) Canlı TDK GTS API sorgusu (en güçlü adaylar için)
    for aday in adaylar[:3]:
        canli = tdk_kelime_ara(aday)
        if canli and canli.get("anlamlar") and "TDK İndirilen Yerel Sözlük" not in canli.get("kaynak", ""):
            kayit = {
                "kaynak": canli["kaynak"],
                "madde": canli["madde"],
                "tur": "TDK Madde",
                "anlamlar": canli["anlamlar"],
                "ornekler": canli.get("ornekler", []),
            }
            onbellek[aday] = kayit
            _tdk_anlam_onbellek_yaz(onbellek)
            tdk_otomatik_ogren_ve_yanit_hazirla(aday, kayit)
            return kayit

    # 4) İndirilen TDK tam kelime listesinde kayıtlı mı?
    indirilen = tdk_yerel_sozluk_yukle()
    if indirilen:
        indirilen_set = {w.lower(): w for w in indirilen}
        for aday in adaylar:
            if aday in indirilen_set:
                return {
                    "kaynak": "TDK İndirilen Sözlük (sozluk.gov.tr)",
                    "madde": indirilen_set[aday],
                    "tur": "TDK Kayıtlı Sözcük",
                    "anlamlar": [f"'{indirilen_set[aday]}' resmi TDK sözlüğünde kayıtlı geçerli bir Türkçe sözcüktür."],
                    "ornekler": [],
                }
    return None


def tdk_dinamik_chatbot_yaniti(kullanici_girdisi: str):
    """
    Herhangi bir kullanıcı cümlesini TDK sözlüğünden çektiği anlamlarla analiz eder,
    cümlenin niyetini (tanım/nedir, devam et, duygu/durum, plan/eylem, sohbet) belirler,
    önceki konuşma bağlamını ('tdk_son_konu') koruyarak doğal, anlamlı Türkçe yanıt üretir.
    """
    temiz_girdi = kullanici_girdisi.strip()
    if not temiz_girdi:
        return None, None
    low = temiz_girdi.replace("İ", "i").replace("I", "ı").lower().replace("\u0307", "")

    # 1) Önce selamlaşma/hatır sorma TDK çözümlemesini dene
    selam_y, selam_e = tdk_sozluk_anlamli_sohbet_yaniti(temiz_girdi)
    if selam_y:
        return selam_y, selam_e

    # 2) Devam / örnek isteme ifadelerinde önceki TDK konusunu hatırla
    devam_komutlari = {"devam et", "devam", "örnek ver", "ornek ver", "biraz daha anlat", "neden", "nasıl yani", "açıkla", "acikla"}
    son_konu = st.session_state.get("tdk_son_konu", "")
    if low.rstrip("?.!") in devam_komutlari and son_konu:
        bilgi = tdk_akilli_kelime_getir(son_konu)
        if bilgi:
            c1, _ = tdk_baglamsal_cumle_kur(baglam="Eğitim & Bilim", ozne_kisi="biz", zaman="şimdiki", ozel_nesne=bilgi["madde"], ozel_fiil="araştırmak")
            c2, _ = tdk_baglamsal_cumle_kur(baglam="Teknoloji & Yapay Zeka", ozne_kisi="biz", zaman="gelecek", ozel_nesne=bilgi["madde"], ozel_fiil="geliştirmek")
            ornek_ek = f"\n💬 **TDK Örneği:** *{bilgi['ornekler'][0]}*" if bilgi.get("ornekler") else ""
            return (
                f"🔄 **'{bilgi['madde']}' konusuyla devam edelim Ahmet:**\n\n"
                f"📖 **TDK Anlamı:** {bilgi['anlamlar'][0]}{ornek_ek}\n\n"
                f"✍️ **Bağlamsal Cümleler:**\n• {c1}\n• {c2}\n\n"
                f"💡 *Bu kavramı başka bir açıdan incelememi ister misin?*",
                "TDK Bağlam Devamı",
            )

    # 3) Cümledeki anlamlı kelimeleri çıkar ve TDK'den çek
    kelimeler = [re.sub(r"[^a-zA-ZçğıöşüÇĞİÖŞÜ]", "", k) for k in low.split()]
    icerk_kelimeler = [k for k in kelimeler if len(k) >= 3 and k not in _TR_DURAK_KELIMELER]

    cozulenler = []
    gorulen_maddeler = set()
    for kel in icerk_kelimeler[:5]:
        bilgi = tdk_akilli_kelime_getir(kel)
        if bilgi and bilgi["madde"] not in gorulen_maddeler:
            gorulen_maddeler.add(bilgi["madde"])
            cozulenler.append((kel, bilgi))

    if not cozulenler:
        return None, None

    ana_kelime, ana_bilgi = cozulenler[0]
    st.session_state["tdk_son_konu"] = ana_bilgi["madde"]

    # 4) Cümle niyetine göre akıllı Türkçe yanıt kur
    nedir_sorusu = any(k in low for k in ["nedir", "ne demek", "anlamı ne", "anlami ne", "kimdir", "tanımı", "tanimi"])
    nasil_neden = "?" in temiz_girdi or any(w in low.split() for w in ["nasıl", "nasil", "neden", "niçin", "nicin", "mi", "mı", "mu", "mü"])

    tdk_blok = "\n".join([f"• **`{b['madde']}`** *({b['kaynak']})*: {b['anlamlar'][0]}" for _, b in cozulenler[:3]])
    ornek_not = f"\n💬 **Örnek Kullanım:** *{ana_bilgi['ornekler'][0]}*" if ana_bilgi.get("ornekler") else ""

    _ozgun_list = ozgun_turkce_cumle_kur(ana_bilgi["madde"], ana_bilgi.get("tur", "isim"), ana_bilgi["anlamlar"][0])
    c_ek_1 = f"{_ozgun_list[0]}\n• {_ozgun_list[1]}"

    if nedir_sorusu:
        baslik = f"📖 **TDK'ye Göre `{ana_bilgi['madde']}`:**"
        devam_soru = f"💡 *`{ana_bilgi['madde']}` hakkında başka bir örnek cümle kurmamı ister misin? (`devam et` yazabilirsin)*"
    elif nasil_neden:
        baslik = f"🧠 **TDK Bağlam Analizi (`{ana_bilgi['madde']}`):** Sorunu sözlük anlamlarıyla inceledim Ahmet."
        devam_soru = f"💡 *`{ana_bilgi['madde']}` konusunu biraz daha açmamı ister misin?*"
    else:
        baslik = f"🗣️ **TDK Anlamlı Sohbet (`{ana_bilgi['madde']}`):** Söylediklerini TDK kök ve anlamlarıyla çözümledim Ahmet."
        devam_soru = f"💡 *Harika gidiyoruz! `{ana_bilgi['madde']}` ile ilgili aklında başka ne var?*"

    yapi = cumle_yapi_analizi_yap(temiz_girdi)
    yorum_satiri = (
        f"💭 **Kendi Yorumum:** `{ana_bilgi['madde']}` kavramını {yapi['zaman'].lower()} odağında ve **{yapi['ozne']}** açısından ele alman çok yerinde; "
        f"bu konuyu hem TDK anlamıyla hem günlük/teknik uygulamasıyla birleştirerek ilerleyebiliriz."
    )
    yanit = (
        f"{baslik}\n\n"
        f"{tdk_blok}{ornek_not}\n\n"
        f"{yorum_satiri}\n\n"
        f"🔍 **Cümle Yapısı İncelemesi:** {yapi['cumle_turu']} · {yapi['zaman']} · {yapi['ozne']} ({yapi['kelime_sayisi']} sözcük)\n\n"
        f"✍️ **Kendi Kurduğum Özgün Cümleler:**\n• {c_ek_1}\n\n"
        f"{devam_soru}"
    )
    return yanit, f"TDK Chatbot ({ana_bilgi['madde']})"


# ==============================================================================
# 7. HARİCİ PYTHON TÜRKÇE KÜTÜPHANE UYUMU & OTOMATİK TDK ÖĞRENME MOTORU (v5.9)
# ==============================================================================
def kurulu_turkce_kutuphaneleri_algila():
    """Kullanıcının pip install ile kurduğu Türkçe NLP/kök kütüphanelerini otomatik algılar."""
    bulunan = []
    for ad, mod_adi in [
        ("zeyrek", "zeyrek"),
        ("TurkishStemmer", "TurkishStemmer"),
        ("trnlp", "trnlp"),
        ("tdk", "tdk"),
        ("pytdk", "pytdk"),
    ]:
        try:
            __import__(mod_adi)
            bulunan.append(ad)
        except Exception:
            pass
    return bulunan


@st.cache_resource(show_spinner=False)
def _zeyrek_yukle():
    try:
        import zeyrek
        return zeyrek.MorphAnalyzer()
    except Exception:
        return None


@st.cache_resource(show_spinner=False)
def _turkish_stemmer_yukle():
    try:
        from TurkishStemmer import TurkishStemmer
        return TurkishStemmer()
    except Exception:
        return None


def harici_kutuphane_ile_kok_bul(kelime: str):
    """
    Kurulu Türkçe kütüphanelerden (zeyrek, TurkishStemmer, trnlp) gelen kökleri
    yerleşik Türkçe kök adaylarıyla birleştirir.
    """
    kokler = []
    temiz = kelime.strip()
    if not temiz:
        return kokler

    # 1) Zeyrek (morfolojik çözümleyici)
    analizor = _zeyrek_yukle()
    if analizor is not None:
        try:
            sonuclar = analizor.lemmatize(temiz)
            for _, lemmalar in sonuclar:
                for lem in lemmalar:
                    l_temiz = str(lem).strip().lower()
                    if l_temiz and l_temiz != "unk" and l_temiz not in kokler:
                        kokler.append(l_temiz)
        except Exception:
            pass

    # 2) TurkishStemmer
    stemmer = _turkish_stemmer_yukle()
    if stemmer is not None:
        try:
            st_kok = str(stemmer.stem(temiz)).strip().lower()
            if st_kok and st_kok not in kokler:
                kokler.append(st_kok)
        except Exception:
            pass

    # 3) trnlp
    try:
        from trnlp import TrnlpWord
        w = TrnlpWord()
        w.setword(temiz)
        if getattr(w, "get_base", None):
            b = str(w.get_base).strip().lower()
            if b and b not in kokler:
                kokler.append(b)
    except Exception:
        pass

    return kokler


def tdk_otomatik_ogren_ve_yanit_hazirla(kelime: str, bilgi: dict):
    """
    Yeni gördüğü her kelimeyi TDK'den aldıktan sonra hem tdk_anlam_onbellek.json'a
    hem de komutlar.json içine kalıcı olarak öğrenir; böylece sonraki sorularda
    o kelimeye karşı nasıl cevap vereceğini bilir.
    """
    if not bilgi or not bilgi.get("anlamlar"):
        return
    madde = bilgi.get("madde", kelime).strip().lower()
    anlam = bilgi["anlamlar"][0]
    ornek = bilgi.get("ornekler", [""])[0] if bilgi.get("ornekler") else ""

    # Önbelleğe kalıcı kaydet
    onbellek = _tdk_anlam_onbellek_oku()
    if madde not in onbellek:
        onbellek[madde] = bilgi
        _tdk_anlam_onbellek_yaz(onbellek)

    # Öğrenilen kalıcı sohbet hafızasına da (komutlar.json) yeni kavram olarak ekle
    try:
        mevcut = json_oku()
        kat_ad = f"tdk_ogrenilen_{madde}"
        if kat_ad not in mevcut:
            ornek_satir = f"\n💬 *Örnek:* {ornek}" if ornek else ""
            ogrenilen_yanit = (
                f"📖 **Öğrendiğim TDK Kavramı (`{madde}`):**\n"
                f"{anlam}{ornek_satir}\n\n"
                f"💡 *Bu kelimeyi TDK'den otomatik öğrenip hafızama kaydettim Ahmet!*"
            )
            json_komut_ekle(kat_ad, f"{madde}, {madde} nedir, {madde} ne demek", ogrenilen_yanit)
    except Exception:
        pass


# ==============================================================================
# 8. TDK ATASÖZLERİ & DEYİMLER SÖZLÜĞÜ VE DÜZENLİ ANLAM MOTORU (v6.0)
# ==============================================================================
TDK_ATASOZU_ONBELLEK_DOSYASI = os.path.join(os.path.dirname(os.path.abspath(__file__)), "tdk_atasozu_onbellek.json")

TDK_ATASOZU_VE_DEYIMLER_SOZLUGU = {
    "damlaya damlaya göl olur": {"tur": "Atasözü", "anlam": "Azar azar biriken küçük şeyler zamanla büyük bir varlık veya sonuç oluşturur.", "ornek": "Her gün 20 dakika İngilizce çalışarak damlaya damlaya göl olur misali büyük yol alabilirsin."},
    "sakla samanı gelir zamanı": {"tur": "Atasözü", "anlam": "Gereksiz gibi görünen şeyler bile ileride bir gün mutlaka işe yarayabilir; tutumlu olmak gerekir.", "ornek": "Eski notlarını atma, sakla samanı gelir zamanı."},
    "ayağını yorganına göre uzat": {"tur": "Atasözü", "anlam": "Giderlerini gelirine göre ayarla, imkânlarını aşan harcamalardan kaçın.", "ornek": "Bütçe planlarken ayağını yorganına göre uzatmalısın."},
    "bir elin nesi var iki elin sesi var": {"tur": "Atasözü", "anlam": "Tek başına büyük işler başarmak zordur; başarı için iş birliği ve dayanışma gerekir.", "ornek": "TEKNOFEST takım çalışmasıdır; bir elin nesi var, iki elin sesi var."},
    "üzüm üzüme baka baka kararır": {"tur": "Atasözü", "anlam": "Bir arada bulunan kimseler zamanla birbirlerinin huyunu ve davranışlarını kaparlar.", "ornek": "Çalışkan arkadaşlarla vakit geçir, unutma ki üzüm üzüme baka baka kararır."},
    "gülme komşuna gelir başına": {"tur": "Atasözü", "anlam": "Başkasının başına gelen kötü bir duruma gülünmemelidir; aynı durum bir gün senin de başına gelebilir.", "ornek": "Kimsenin hatasıyla alay etme, gülme komşuna gelir başına."},
    "erken kalkan yol alır": {"tur": "Atasözü", "anlam": "İşine zamanında ve erken başlayan kimse, geç kalanlara göre daha çok ilerler ve başarılı olur.", "ornek": "Sabah erken çalışmaya başladık, erken kalkan yol alır."},
    "emeksiz yemek olmaz": {"tur": "Atasözü", "anlam": "Çalışıp çaba göstermeden, emek harcamadan kazanç ve başarı elde edilmez.", "ornek": "İyi bir proje için gece gündüz emek vermek şart; emeksiz yemek olmaz."},
    "akıl akıldan üstündür": {"tur": "Atasözü", "anlam": "Bir kişinin göremediği çözümü başka biri görebilir; danışmak ve fikir almak her zaman faydalıdır.", "ornek": "Takım arkadaşlarına da danış, akıl akıldan üstündür."},
    "işleyen demir ışıldar": {"tur": "Atasözü", "anlam": "Sürekli çalışan, üreten ve kendini geliştiren kimse dinç ve yetenekli kalır; tembellik ise köreltir.", "ornek": "Her gün kod yazıp soru çözmek zihni açık tutar; işleyen demir ışıldar."},
    "ağaç yaşken eğilir": {"tur": "Atasözü", "anlam": "İnsan küçük yaşta daha kolay eğitilir ve iyi alışkanlıkları gençken kazanır.", "ornek": "Yazılım ve dil öğrenmeye genç yaşta başlamak büyük avantajdır, ağaç yaşken eğilir."},
    "acele işe şeytan karışır": {"tur": "Atasözü", "anlam": "Düşünülmeden, telaşla yapılan işler genellikle hatalı ve bozuk olur.", "ornek": "Kodu test etmeden yükleme, acele işe şeytan karışır."},
    "ak akçe kara gün içindir": {"tur": "Atasözü", "anlam": "Çalışarak biriktirilen para, dar ve sıkıntılı zamanlarda insanın imdadına yetişir.", "ornek": "Kenara biraz tasarruf koymak gerekir; ak akçe kara gün içindir."},
    "azimli sıçan duvarı deler": {"tur": "Atasözü", "anlam": "Kararlı ve sabırlı olan kişi, ne kadar zor olursa olsun engelleri aşar.", "ornek": "Hata verse de pes etme, azimli sıçan duvarı deler."},
    "ne ekersen onu biçersin": {"tur": "Atasözü", "anlam": "İnsan nasıl davranır ve ne kadar emek verirse karşılığında da onun sonucunu alır.", "ornek": "Bugün ne kadar düzenli çalışırsan sınavda da onu görürsün; ne ekersen onu biçersin."},
    "sabır acıdır meyvesi tatlıdır": {"tur": "Atasözü", "anlam": "Sabretmek başlangıçta zor ve sıkıntılıdır ama sonunda güzel ve mutlu bir sonuca ulaştırır.", "ornek": "Aylarca uğraştık ama başardık; sabır acıdır meyvesi tatlıdır."},
    "tatlı dil yılanı deliğinden çıkarır": {"tur": "Atasözü", "anlam": "Güzel, nazik ve yumuşak sözlerle en inatçı veya öfkeli kişiler bile ikna edilebilir.", "ornek": "Sunumda nazik bir üslup kullan, tatlı dil yılanı deliğinden çıkarır."},
    "zararın neresinden dönülse kardır": {"tur": "Atasözü", "anlam": "Yanlış bir işten ne kadar erken vazgeçilirse daha büyük zararlardan o kadar çabuk kurtulunur.", "ornek": "Hatalı tasarımı erken fark ettik, zararın neresinden dönülse kârdır."},
    "görünen köy kılavuz istemez": {"tur": "Atasözü", "anlam": "Gerçek ve açık olan bir durum için ayrıca açıklamaya veya kanıta gerek yoktur.", "ornek": "Veriler her şeyi gösteriyor, görünen köy kılavuz istemez."},
    "denize düşen yılana sarılır": {"tur": "Atasözü", "anlam": "Büyük bir tehlike veya çaresizlik içinde kalan kimse, normalde güvenmeyeceği şeylerden bile medet umar.", "ornek": "Son anda bulduğumuz yedek parçayı kullandık, denize düşen yılana sarılır."},
    "sütten ağzı yanan yoğurdu üfleyerek yer": {"tur": "Atasözü", "anlam": "Bir olaydan zarar gören veya kötü tecrübe yaşayan kimse, benzer durumlarda çok daha tedbirli davranır.", "ornek": "Geçen sefer yedek almadığımız için veri kaybettik, artık üfleyerek yiyoruz."},
    "el elden üstündür": {"tur": "Atasözü", "anlam": "Her alanda senden daha bilgili, daha yetenekli veya daha tecrübeli birileri mutlaka vardır.", "ornek": "Öğrenmeye daima açık ol, el elden üstündür."},
    "lafla peynir gemisi yürümez": {"tur": "Atasözü", "anlam": "Yalnızca konuşmakla ve söz vermekle iş yapılmaz; somut icraat ve çalışma gerekir.", "ornek": "Planları koda dökelim, lafla peynir gemisi yürümez."},
    "yalancının mumu yatsıya kadar yanar": {"tur": "Atasözü", "anlam": "Söylenen yalan çok geçmeden ortaya çıkar ve gerçeği uzun süre gizlemek mümkün değildir.", "ornek": "Doğruluktan şaşma, yalancının mumu yatsıya kadar yanar."},
    "marifet iltifata tabidir": {"tur": "Atasözü", "anlam": "Başarılı ve güzel işler takdir edilip ödüllendirildikçe daha iyileri ortaya çıkar.", "ornek": "Takımın emeğini tebrik etmek motivasyonu artırır; marifet iltifata tabidir."},
    "zaman her şeyin ilacıdır": {"tur": "Atasözü", "anlam": "Zaman geçtikçe acılar, üzüntüler ve öfkeler hafifler, sorunlar yatışır.", "ornek": "Üzülme, zaman her şeyin ilacıdır."},
    "komşu komşunun külüne muhtaçtır": {"tur": "Atasözü", "anlam": "İnsanlar en küçük ihtiyaçlarında bile yakın çevresindekilerin yardımına gereksinim duyar.", "ornek": "Dayanışma önemlidir, komşu komşunun külüne muhtaçtır."},
    "ateş düştüğü yeri yakar": {"tur": "Atasözü", "anlam": "Bir acıyı veya sıkıntıyı en derinden hisseden, bizzat o olayı yaşayan kimsedir.", "ornek": "Dışarıdan konuşmak kolay ama ateş düştüğü yeri yakar."},
    "armut dibine düşer": {"tur": "Atasözü", "anlam": "Çocuklar veya yeni yetişenler genellikle ailelerinin, ustalarının huylarını ve özelliklerini taşır.", "ornek": "Mühendis babanın oğlu da robotiğe meraklı; armut dibine düşer."},
    "iyilik eden iyilik bulur": {"tur": "Atasözü", "anlam": "Başkalarına iyilik yapan kimse er geç kendisi de iyilik ve yardım görür.", "ornek": "Paylaşmaktan çekinme, iyilik eden iyilik bulur."},
    "gözden düşmek": {"tur": "Deyim", "anlam": "Daha önce gördüğü sevgi, değer ve güveni davranışları yüzünden yitirmek.", "ornek": "Sözünde durmadığı için arkadaşlarının gözünden düştü."},
    "kulak asmamak": {"tur": "Deyim", "anlam": "Söylenenlere önem vermemek, dinlememek, aldırış etmemek.", "ornek": "Olumsuz eleştirilere kulak asmadan çalışmasına devam etti."},
    "etekleri zil çalmak": {"tur": "Deyim", "anlam": "Çok sevinmek, sevinçten içi içine sığmamak.", "ornek": "Yarışmada birinci olduğunu duyunca etekleri zil çaldı."},
    "ağzı kulaklarına varmak": {"tur": "Deyim", "anlam": "Aşırı derecede sevinip mutlu olmak, yüzünde büyük bir gülümseme belirmek.", "ornek": "İHA ilk uçuşunu başarınca hepimizin ağzı kulaklarına vardı."},
    "burnundan solumak": {"tur": "Deyim", "anlam": "Çok öfkelenmiş ve sinirlenmiş olmak.", "ornek": "Haksızlığa uğrayınca burnundan soluyordu."},
    "kılı kırk yarmak": {"tur": "Deyim", "anlam": "Bir işi veya konuyu en ince ayrıntısına kadar titizlikle incelemek.", "ornek": "Kod güvenliği konusunda kılı kırk yararak çalıştık."},
    "iğneyle kuyu kazmak": {"tur": "Deyim", "anlam": "Yetersiz araçlarla çok büyük, sabır gerektiren ve zor bir işi başarmaya çalışmak.", "ornek": "Tek başına büyük bir veri tabanı oluşturmak iğneyle kuyu kazmak gibidir."},
    "taşı gediğine koymak": {"tur": "Deyim", "anlam": "Tam zamanında, yerinde ve çok etkili bir söz söylemek.", "ornek": "Tartışmada öyle bir örnek verdi ki taşı gediğine koydu."},
    "saman altından su yürütmek": {"tur": "Deyim", "anlam": "Belli etmeden, gizlice iş çevirmek.", "ornek": "Kimseye hissettirmeden saman altından su yürütüyordu."},
    "göze girmek": {"tur": "Deyim", "anlam": "Başarısı veya güzel davranışıyla birinin sevgi, beğeni ve güvenini kazanmak.", "ornek": "Düzenli çalışmasıyla öğretmenlerinin gözüne girdi."},
    "dil dökmek": {"tur": "Deyim", "anlam": "Birini kandırmak, inandırmak veya ikna etmek için tatlı ve uzun sözler söylemek.", "ornek": "Projeyi kabul ettirmek için jüriye epey dil döktü."},
    "eli ayağı dolaşmak": {"tur": "Deyim", "anlam": "Heyecandan, korkudan veya telaştan ne yapacağını şaşırmak.", "ornek": "Sahneye ilk çıktığında heyecanlanıp eli ayağı dolaştı."},
    "kafası karışmak": {"tur": "Deyim", "anlam": "Bir konu hakkında net düşünememek, kararsızlığa ve şaşkınlığa düşmek.", "ornek": "Çok fazla formül görünce biraz kafam karıştı."},
    "gönül almak": {"tur": "Deyim", "anlam": "Kırılmış veya gücenmiş birini güzel söz ve davranışla yeniden hoşnut etmek.", "ornek": "Hatasını anlayıp arkadaşının gönlünü aldı."},
    "göz boyamak": {"tur": "Deyim", "anlam": "Gösterişli ama gerçekte değeri olmayan şeylerle birini kandırmak.", "ornek": "Sadece tasarımla göz boyamak yerine sağlam altyapı kurmalıyız."},
    "baltayı taşa vurmak": {"tur": "Deyim", "anlam": "Farkında olmadan karşısındakini kıracak veya pot kıracak bir söz söylemek.", "ornek": "Yanlışlıkla sırrı söyleyince baltayı taşa vurdu."},
    "küplere binmek": {"tur": "Deyim", "anlam": "Aşırı derecede öfkelenmek, çok kızmak.", "ornek": "Emeklerinin boşa gittiğini görünce küplere bindi."},
    "parmak ısırmak": {"tur": "Deyim", "anlam": "Bir şey karşısında çok şaşırmak, hayran kalmak.", "ornek": "Yaptığı otonom yazılımı görenler parmak ısırdı."},
    "yüzü gülmek": {"tur": "Deyim", "anlam": "Sevinçli, mutlu ve ferahlık içinde olmak.", "ornek": "Sonuçlar açıklanınca hepimizin yüzü güldü."},
    "elinden geleni yapmak": {"tur": "Deyim", "anlam": "Bir işi başarmak için bütün gücünü ve imkânlarını kullanmak.", "ornek": "Bu projeyi bitirmek için elimizden geleni yapıyoruz."},
    "göz kulak olmak": {"tur": "Deyim", "anlam": "Bir kimseye veya bir şeye bakmak, korumak, gözetmek.", "ornek": "Ben gelene kadar çantama göz kulak olur musun?"},
    "kulak misafiri olmak": {"tur": "Deyim", "anlam": "İsteyerek veya istemeyerek yakınındaki bir konuşmayı dinlemek.", "ornek": "Yan masadaki proje konuşmasına kulak misafiri oldum."},
    "ağzından bal damlamak": {"tur": "Deyim", "anlam": "Çok tatlı, hoş ve sevindirici sözler söylemek.", "ornek": "Müjdeli haberi verirken ağzından bal damlıyordu."},
    "dört gözle beklemek": {"tur": "Deyim", "anlam": "Bir kimsenin gelmesini veya bir olayın gerçekleşmesini büyük bir özlem ve sabırsızlıkla beklemek.", "ornek": "TEKNOFEST final gününü dört gözle bekliyoruz."},
    "ipucu vermek": {"tur": "Deyim", "anlam": "Bir gerçeği veya çözümü bulmaya yarayacak küçük bir belirti, işaret sunmak.", "ornek": "Öğretmenimiz zor soru için küçük bir ipucu verdi."},
    "kalıba dökmek": {"tur": "Deyim", "anlam": "Düşünce veya verileri düzenli, derli toplu bir biçime sokmak.", "ornek": "Notlarımızı güzel bir sunum kalıbına dökelim."},
    "yol almak": {"tur": "Deyim", "anlam": "Bir işte ilerleme kaydetmek, mesafe katetmek.", "ornek": "Yapay zeka modülünde bugün epey yol aldık."},
    "kafa yormak": {"tur": "Deyim", "anlam": "Bir konu veya sorun üzerinde derinlemesine ve uzun süre düşünmek.", "ornek": "Bu algoritma üzerine saatlerce kafa yorduk."},
    "ayak uydurmak": {"tur": "Deyim", "anlam": "Değişen şartlara, düzene veya hıza uyum sağlamak.", "ornek": "Yeni teknolojiye hızlıca ayak uydurmalıyız."},
    "su yüzüne çıkmak": {"tur": "Deyim", "anlam": "Gizli kalmış bir gerçek veya durum herkesçe görülür, bilinir hâle gelmek.", "ornek": "Hata ayıklama yapınca asıl sorun su yüzüne çıktı."},
}


def _tdk_atasozu_onbellek_oku() -> dict:
    if os.path.exists(TDK_ATASOZU_ONBELLEK_DOSYASI):
        try:
            with open(TDK_ATASOZU_ONBELLEK_DOSYASI, "r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            return {}
    return {}


def _tdk_atasozu_onbellek_yaz(veri: dict):
    try:
        with open(TDK_ATASOZU_ONBELLEK_DOSYASI, "w", encoding="utf-8") as f:
            json.dump(veri, f, ensure_ascii=False, indent=2)
    except Exception:
        pass


def tdk_atasozu_deyim_ara(ifade: str, tur_filtre: str = ""):
    """
    Atasözü veya deyimi önce yerleşik TDK sözlüğünde ve öğrenilen önbellekte arar (tam + fuzzy),
    bulamazsa canlı TDK (sozluk.gov.tr/atasozu?ara= ve gts?ara=) üzerinden çekip önbelleğe kaydeder.
    """
    import urllib.parse

    temiz = metni_normallestir(ifade)
    temiz = re.sub(r"\b(atasozu|atasözü|deyimi|deyim|anlami|anlamı|nedir|ne demek|soyle|söyle|acikla|açıkla|anlat)\b", " ", temiz)
    temiz = re.sub(r"\s+", " ", temiz).strip()
    if not temiz:
        return None

    birlesik_havuz = {}
    birlesik_havuz.update(TDK_ATASOZU_VE_DEYIMLER_SOZLUGU)
    birlesik_havuz.update(_tdk_atasozu_onbellek_oku())

    # 1) Tam veya içerme eşleşmesi
    for baslik, veri in birlesik_havuz.items():
        if tur_filtre and veri.get("tur", "").lower() != tur_filtre.lower():
            continue
        b_norm = metni_normallestir(baslik)
        if b_norm == temiz or (len(temiz) >= 5 and (temiz in b_norm or b_norm in temiz)):
            return {"madde": baslik, "tur": veri["tur"], "anlam": veri["anlam"], "ornek": veri.get("ornek", ""), "kaynak": "TDK Atasözleri & Deyimler Sözlüğü"}

    # 2) Fuzzy eşleşme (yazım farkı veya ekli kullanım için)
    en_iyi_skor, en_iyi_sonuc = 0, None
    for baslik, veri in birlesik_havuz.items():
        if tur_filtre and veri.get("tur", "").lower() != tur_filtre.lower():
            continue
        b_norm = metni_normallestir(baslik)
        skor = max(fuzz.ratio(temiz, b_norm), fuzz.token_set_ratio(temiz, b_norm))
        if skor >= 76 and skor > en_iyi_skor:
            en_iyi_skor = skor
            en_iyi_sonuc = {"madde": baslik, "tur": veri["tur"], "anlam": veri["anlam"], "ornek": veri.get("ornek", ""), "kaynak": "TDK Atasözleri & Deyimler Sözlüğü"}
    if en_iyi_sonuc:
        return en_iyi_sonuc

    # 3) Canlı TDK Atasözleri & Deyimler API sorgusu (internet varsa)
    try:
        url = f"https://sozluk.gov.tr/atasozu?ara={urllib.parse.quote(ifade.strip())}"
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0 ArAIStudio/6.0"})
        with urllib.request.urlopen(req, timeout=8) as resp:
            veri = json.loads(resp.read().decode("utf-8"))
        if isinstance(veri, list) and veri and isinstance(veri[0], dict) and veri[0].get("anlami"):
            ilk = veri[0]
            madde = ilk.get("sozum", ifade.strip())
            tur_ad = ilk.get("turu2", "") or ("Atasözü" if "ata" in str(ilk.get("turu", "")).lower() else "Deyim")
            anlam = ilk.get("anlami", "")
            kayit = {"tur": tur_ad, "anlam": anlam, "ornek": ""}
            onb = _tdk_atasozu_onbellek_oku()
            onb[madde.lower()] = kayit
            _tdk_atasozu_onbellek_yaz(onb)
            return {"madde": madde, "tur": tur_ad, "anlam": anlam, "ornek": "", "kaynak": "TDK Canlı Atasözü/Deyim API"}
    except Exception:
        pass
    return None


def tdk_duzenli_mod_yonlendir(kullanici_girdisi: str):
    """
    'deyim anlamı', 'atasözü anlamı', 'kelime anlamı' komutlarını ve doğrudan deyim/atasözü
    sorularını düzenli, kararlı ve sapmasız biçimde yanıtlar.
    """
    ham = kullanici_girdisi.strip()
    low = ham.replace("İ", "i").replace("I", "ı").lower().replace("\u0307", "").strip()
    norm = metni_normallestir(ham)

    # A) Kullanıcı sadece mod başlığı yazdıysa ("deyim anlamı", "atasözü anlamı", "kelime anlamı")
    if norm in {"deyim anlami", "deyim", "deyim sor", "deyimler"}:
        return (
            "📜 **TDK Deyim Anlamı Modu Aktif!**\n\n"
            "Hangi deyimin anlamını öğrenmek istiyorsun Ahmet? Şöyle yazabilirsin:\n"
            "• `deyim anlamı: gözden düşmek`\n"
            "• `etekleri zil çalmak deyiminin anlamı nedir?`\n"
            "• `kılı kırk yarmak ne demek?`",
            "TDK Deyim Modu",
        )
    if norm in {"atasozu anlami", "atasozu", "atasozu sor", "atasozleri"}:
        return (
            "📜 **TDK Atasözü Anlamı Modu Aktif!**\n\n"
            "Hangi atasözünün anlamını öğrenmek istiyorsun Ahmet? Şöyle yazabilirsin:\n"
            "• `atasözü anlamı: damlaya damlaya göl olur`\n"
            "• `ayağını yorganına göre uzat atasözünün anlamı nedir?`\n"
            "• `işleyen demir ışıldar ne demek?`",
            "TDK Atasözü Modu",
        )
    if norm in {"kelime anlami", "kelime", "kelime sor", "sozluk"}:
        return (
            "📖 **TDK Kelime Anlamı Modu Aktif!**\n\n"
            "Hangi kelimenin TDK anlamını öğrenmek istiyorsun Ahmet? Şöyle yazabilirsin:\n"
            "• `kelime anlamı: medeniyet`\n"
            "• `otonom kelimesinin anlamı nedir?`\n"
            "• `algoritma ne demek?`",
            "TDK Kelime Modu",
        )

    # B) Açık modlu istekler ("deyim anlamı: X", "X deyiminin anlamı", "atasözü anlamı: X", "kelime anlamı: X")
    if any(k in low for k in ["deyim anlam", "deyiminin anlam", "deyimi ne demek", "deyim:"]):
        hedef = re.sub(r"(?:deyim\s*anlam[ıi]?|deyiminin\s*anlam[ıi]?|deyimi\s*ne\s*demek|nedir|\?|:)", " ", low).strip()
        sonuc = tdk_atasozu_deyim_ara(hedef, tur_filtre="Deyim") or tdk_atasozu_deyim_ara(hedef)
        if sonuc:
            ozgunler = ozgun_turkce_cumle_kur(sonuc["madde"], sonuc["tur"], sonuc["anlam"])
            ornek_str = f"\n• **Sözlük Örneği:** *{sonuc['ornek']}*" if sonuc.get("ornek") else ""
            return (
                f"Tabii Ahmet, **`{sonuc['madde']}`** deyimini TDK açısından şöyle özetleyebilirim:\n\n"
                f"• **TDK Anlamı:** {sonuc['anlam']}{ornek_str}\n\n"
                f"✍️ **Kendi Kurduğum Özgün Cümleler:**\n"
                f"1. {ozgunler[0]}\n"
                f"2. {ozgunler[1]}",
                f"TDK {sonuc['tur']}",
            )
        return (
            f"🤔 **`{hedef}`** deyimi yerel sözlükte bulunamadı; internet açıksa TDK'den çekemedim veya yazım farklı olabilir. "
            "İstersen `öğret: deyim = anlamı` şeklinde hemen öğretebilirsin!",
            "TDK Deyim Bulunamadı",
        )

    if any(k in low for k in ["atasözü anlam", "atasozu anlam", "atasözünün anlam", "atasozunun anlam", "atasözü:", "atasozu:"]):
        hedef = re.sub(r"(?:atas[öo]z[üu]\s*anlam[ıi]?|atas[öo]z[üu]n[üu]n\s*anlam[ıi]?|ne\s*demek|nedir|\?|:)", " ", low).strip()
        sonuc = tdk_atasozu_deyim_ara(hedef, tur_filtre="Atasözü") or tdk_atasozu_deyim_ara(hedef)
        if sonuc:
            ozgunler = ozgun_turkce_cumle_kur(sonuc["madde"], sonuc["tur"], sonuc["anlam"])
            ornek_str = f"\n• **Örnek Kullanım:** *{sonuc['ornek']}*" if sonuc.get("ornek") else ""
            return (
                f"Güzel bir atasözü seçtin Ahmet! **`{sonuc['madde']}`** sözünün TDK anlamı ve yorumu şöyle:\n\n"
                f"• **TDK Anlamı:** {sonuc['anlam']}{ornek_str}\n\n"
                f"✍️ **Kendi Kurduğum Özgün Cümleler:**\n"
                f"1. {ozgunler[0]}\n"
                f"2. {ozgunler[1]}",
                f"TDK {sonuc['tur']}",
            )
        return (
            f"🤔 **`{hedef}`** atasözü yerel sözlükte bulunamadı. `öğret: atasözü = anlamı` yazarak anında öğretebilirsin!",
            "TDK Atasözü Bulunamadı",
        )

    if any(k in low for k in ["kelime anlam", "kelimesinin anlam", "kelime:"]):
        hedef = re.sub(r"(?:kelime\s*anlam[ıi]?|kelimesinin\s*anlam[ıi]?|nedir|ne\s*demek|\?|:)", " ", low).strip()
        ilk_kelime = hedef.split()[0] if hedef.split() else ""
        if ilk_kelime:
            bilgi = tdk_akilli_kelime_getir(ilk_kelime)
            if bilgi:
                ozgunler = ozgun_turkce_cumle_kur(bilgi["madde"], bilgi.get("tur", "isim"), bilgi["anlamlar"][0])
                anl_list = "\n".join([f"{i+1}. {a}" for i, a in enumerate(bilgi["anlamlar"][:3])])
                ornek_str = f"\n💬 **TDK Örneği:** *{bilgi['ornekler'][0]}*" if bilgi.get("ornekler") else ""
                return (
                    f"**`{bilgi['madde']}`** kelimesinin TDK'deki anlamı şu şekildedir Ahmet:\n\n"
                    f"{anl_list}{ornek_str}\n\n"
                    f"✍️ **Kendi Kurduğum Özgün Cümleler:**\n"
                    f"1. {ozgunler[0]}\n"
                    f"2. {ozgunler[1]}",
                    f"TDK Kelime ({bilgi['madde']})",
                )
        return f"🤔 **`{hedef}`** kelimesi için TDK anlamı bulunamadı.", "TDK Kelime Bulunamadı"

    # C) Doğrudan bilinen bir atasözü veya deyim sorulduysa ("gözden düşmek ne demek", "damlaya damlaya göl olur")
    if len(norm.split()) >= 2:
        direkt = tdk_atasozu_deyim_ara(ham)
        if direkt:
            ornek_str = f"\n• **Örnek:** *{direkt['ornek']}*" if direkt.get("ornek") else ""
            return (
                f"📜 **TDK {direkt['tur']} Anlamı:**\n\n"
                f"• **İfade:** `{direkt['madde']}`\n"
                f"• **Anlamı:** {direkt['anlam']}{ornek_str}\n"
                f"• **Kaynak:** *{direkt['kaynak']}*",
                f"TDK {direkt['tur']}",
            )
    return None, None


# ==============================================================================
# 9. DOĞAL & DÜŞÜNEN CÜMLE KURMA MOTORU (KENDİ KAFASINDAN ÖZGÜN CÜMLE ÜRETİR - v6.1)
# ==============================================================================
def ozgun_turkce_cumle_kur(madde: str, tur: str = "isim", anlam: str = ""):
    """
    Verilen kelime, fiil, sıfat, deyim veya atasözünü alıp TDK ses/ek uyumlarıyla
    kendi kafasından 2 adet doğal, anlamlı ve akıcı Türkçe cümle kurar.
    """
    import random

    m = madde.strip()
    t_low = (tur or "").lower()
    m_low = m.lower()

    if "atasözü" in t_low or "atasozu" in t_low:
        return [
            f"Hayatta karşılaştığımız pek çok durumda '{m}' sözü bize doğru yolu gösterir.",
            f"Bugün aldığımız kararlarda '{m}' anlayışıyla hareket edersek daha sağlam sonuçlar elde ederiz.",
        ]

    if "deyim" in t_low:
        if m_low.endswith(("mak", "mek")):
            gecmis = fiil_cekimle(m, zaman="geçmiş_görülen", kisi="o")
            if " " in m:
                ilk_kisim, son_fiil = m.rsplit(" ", 1)
                gecmis = f"{ilk_kisim} {fiil_cekimle(son_fiil, zaman='geçmiş_görülen', kisi='o')}"
                olumsuz_mastar = f"{ilk_kisim} {son_fiil[:-3]}{'mamak' if _kalin_mi(_son_unlu(son_fiil[:-3])) else 'memek'}"
            else:
                olumsuz_mastar = m
            return [
                f"Verdiği sözleri tutmaya özen gösterdiği için kimsenin karşısında {olumsuz_mastar} adına elinden geleni yaptı.",
                f"Yaşanan o gelişmeden sonra arkadaş çevresinde bir anda {gecmis}.",
            ]
        return [
            f"Konuşma sırasında '{m}' ifadesini yerinde kullanması herkesin dikkatini çekti.",
            f"Bu durumu en iyi anlatan söz kesinlikle '{m}' deyimidir.",
        ]

    if "fiil" in t_low or (m_low.endswith(("mak", "mek")) and len(m_low) > 4):
        simdi_biz = fiil_cekimle(m, zaman="şimdiki", kisi="biz")
        gelecek_biz = fiil_cekimle(m, zaman="gelecek", kisi="biz")
        gerek_ben = fiil_cekimle(m, zaman="gereklilik", kisi="ben")
        return [
            f"Her gün biraz daha gayret ederek hedeflerimize ulaşmak için birlikte {simdi_biz}.",
            f"Planladığımız bu çalışmayı tamamladığımızda çok daha güçlü bir şekilde {gelecek_biz}; bunun için şimdiden {gerek_ben}.",
        ]

    if "sıfat" in t_low or "sifat" in t_low:
        return [
            f"Her zaman {m_low} bir bakış açısıyla yaklaşırsak en karmaşık konuları bile rahatça çözeriz.",
            f"Ekip arkadaşlarımızla {m_low} bir çalışma düzeni kurduğumuzda verimliliğimiz hızla artar.",
        ]

    # İsim için doğal hal ekli özgün cümleler
    belirtme = isim_hal_eki_ekle(m_low, "belirtme")
    tamlayan = isim_hal_eki_ekle(m_low, "tamlayan")
    bulunma = isim_hal_eki_ekle(m_low, "bulunma")
    sablon_havuzu = [
        f"Günlük hayatımızda {belirtme} doğru kavramak, hem düşüncelerimizi netleştirir hem de iletişimimizi güçlendirir.",
        f"{tamlayan.capitalize()} değerini gerçekten anladığımızda attığımız her adım çok daha anlamlı hâle gelir.",
        f"Eğer {bulunma} sağlam bir temel oluşturursak, üzerinde çalıştığımız her projede fark yaratabiliriz.",
    ]
    random.shuffle(sablon_havuzu)
    return sablon_havuzu[:2]


# ==============================================================================
# 10. HIZLI TDK HAVUZ İNDEKSİ & CÜMLE YAPISI İNCELEME + ÖZGÜN YORUM MOTORU (v7.0)
# ==============================================================================
@st.cache_data(show_spinner=False)
def _tdk_hizli_kelime_kumesi_yukle():
    """İndirilen TDK sözlüğünü belleğe tek seferde alıp milisaniyede arama sağlar."""
    return {w.lower(): w for w in tdk_yerel_sozluk_yukle()}


def cumle_yapi_analizi_yap(cumle: str):
    """
    Kullanıcının kurduğu cümleyi dilbilgisi ve bağlam açısından inceler:
    cümle türü (soru/olumsuz/olumlu), zaman/kip ipucu, kişi öznesi ve içerik kökleri.
    """
    low = cumle.replace("İ", "i").replace("I", "ı").lower().replace("\u0307", "").strip()
    kelimeler = [re.sub(r"[^a-zA-ZçğıöşüÇĞİÖŞÜ]", "", k) for k in low.split()]
    kelimeler = [k for k in kelimeler if k]

    soru_mu = "?" in cumle or any(w in kelimeler for w in ["mi", "mı", "mu", "mü", "nasıl", "neden", "niçin", "kim", "ne", "hangi", "kaç"])
    olumsuz_mu = any(w in kelimeler for w in ["değil", "yok", "hiç", "asla"]) or any(w.endswith(("mıyor", "miyor", "muyor", "müyor", "madı", "medi", "maz", "mez")) for w in kelimeler)

    if any(w in kelimeler for w in ["ben", "benim", "bana", "beni"]) or any(w.endswith(("yorum", "ceğim", "cağım", "dim", "dım", "müşüm")) for w in kelimeler):
        ozne_tahmin = "1. Tekil Şahıs (Ben)"
    elif any(w in kelimeler for w in ["biz", "bizim", "bize"]) or any(w.endswith(("yoruz", "ceğiz", "cağız", "dik", "dık")) for w in kelimeler):
        ozne_tahmin = "1. Çoğul Şahıs (Biz)"
    elif any(w in kelimeler for w in ["sen", "senin", "sana"]) or any(w.endswith(("yorsun", "ceksin", "caksın", "din", "dın")) for w in kelimeler):
        ozne_tahmin = "2. Tekil Şahıs (Sen)"
    else:
        ozne_tahmin = "3. Şahıs / Genel Bağlam"

    if any(w.endswith(("ecek", "acak", "ceğim", "cağım", "ceğiz", "cağız")) for w in kelimeler) or "yarın" in kelimeler:
        zaman_tahmin = "Gelecek Zaman"
    elif any(w.endswith(("dı", "di", "du", "dü", "tı", "ti", "tu", "tü", "mış", "miş", "muş", "müş")) for w in kelimeler) or "dün" in kelimeler:
        zaman_tahmin = "Geçmiş Zaman"
    elif any(w.endswith(("yor", "yorum", "yorsun", "yoruz")) for w in kelimeler) or "şimdi" in kelimeler:
        zaman_tahmin = "Şimdiki Zaman"
    else:
        zaman_tahmin = "Geniş / Kavramsal Zaman"

    cumle_turu = "Soru Cümlesi" if soru_mu else ("Olumsuz Bildirme" if olumsuz_mu else "Olumlu Bildirme")
    return {
        "kelime_sayisi": len(kelimeler),
        "cumle_turu": cumle_turu,
        "ozne": ozne_tahmin,
        "zaman": zaman_tahmin,
    }

TDK_CEKIRDEK_SOZLUK.update({'lamba': {'tur': 'isim', 'niyet': 'konu', 'anlam': 'İçinde yakıt veya elektrik akımıyla ışık veren, çevreyi aydınlatan araç.', 'baglam': ['Günlük Yaşam', 'Teknoloji & Yapay Zeka']}, 'ışık': {'tur': 'isim', 'niyet': 'konu', 'anlam': 'Cisimleri görmeyi, renkleri ayırt etmeyi sağlayan fiziksel enerji, aydınlık.', 'baglam': ['Doğa & Çevre', 'Eğitim & Bilim']}, 'elektrik': {'tur': 'isim', 'niyet': 'konu', 'anlam': 'Maddenin elektron ve proton gibi parçacıklarının hareketiyle ortaya çıkan enerji türü.', 'baglam': ['Teknoloji & Yapay Zeka', 'İHA & Mühendislik']}, 'kapı': {'tur': 'isim', 'niyet': 'konu', 'anlam': 'Bir yere girip çıkarken geçilen ve açılıp kapanabilen bölme.', 'baglam': ['Günlük Yaşam']}, 'pencere': {'tur': 'isim', 'niyet': 'konu', 'anlam': 'Yapıların dışarıdan ışık ve hava almasını sağlayan açıklık.', 'baglam': ['Günlük Yaşam']}, 'masa': {'tur': 'isim', 'niyet': 'konu', 'anlam': 'Ayaklar veya bir destek üzerine oturtulmuş düz tabladan oluşan mobilya.', 'baglam': ['Günlük Yaşam']}, 'bilgisayar': {'tur': 'isim', 'niyet': 'konu', 'anlam': 'Çok sayıda aritmetiksel veya mantıksal işlemi kendiliğinden yapabilen elektronik aygıt.', 'baglam': ['Teknoloji & Yapay Zeka']}, 'telefon': {'tur': 'isim', 'niyet': 'konu', 'anlam': 'Uzak yerler arasında ses ve veri iletişimini sağlayan elektrikli aygıt.', 'baglam': ['Teknoloji & Yapay Zeka']}, 'su': {'tur': 'isim', 'niyet': 'konu', 'anlam': 'Hidrojen ve oksijenden oluşan, sıvı durumunda bulunan kokusuz ve renksiz madde.', 'baglam': ['Doğa & Çevre']}, 'güneş': {'tur': 'isim', 'niyet': 'konu', 'anlam': "Gezegenlere ve Dünya'ya ısı ve ışık veren büyük gök cismi, yıldız.", 'baglam': ['Doğa & Çevre']}, 'sevgi': {'tur': 'isim', 'niyet': 'konu', 'anlam': 'İnsanı bir şeye veya bir kimseye karşı yakın ilgi ve bağlılık göstermeye yönelten duygu.', 'baglam': ['Günlük Yaşam']}, 'umut': {'tur': 'isim', 'niyet': 'konu', 'anlam': 'Ummaktan doğan güven duygusu, ümit.', 'baglam': ['Günlük Yaşam']}, 'mutluluk': {'tur': 'isim', 'niyet': 'konu', 'anlam': 'Bütün özlemlere eksiksiz ve sürekli olarak ulaşılmaktan duyulan kıvanç durumu.', 'baglam': ['Günlük Yaşam']}, 'hayat': {'tur': 'isim', 'niyet': 'konu', 'anlam': 'Doğumdan ölüme kadar geçen süre, yaşam, ömür.', 'baglam': ['Günlük Yaşam']}, 'zaman': {'tur': 'isim', 'niyet': 'konu', 'anlam': 'Bir işin, bir oluşun içinde geçtiği, geçeceği veya geçmekte olduğu süre, vakit.', 'baglam': ['Günlük Yaşam', 'Eğitim & Bilim']}, 'okul': {'tur': 'isim', 'niyet': 'konu', 'anlam': 'Türlü derecelerde toplu olarak eğitim ve öğretim verilen yer, mektep.', 'baglam': ['Eğitim & Bilim']}, 'ev': {'tur': 'isim', 'niyet': 'konu', 'anlam': 'Yalnız bir ailenin oturabileceği biçimde yapılmış yapı, konut, hane.', 'baglam': ['Günlük Yaşam']}, 'araba': {'tur': 'isim', 'niyet': 'konu', 'anlam': 'Tekerlekli, motorlu veya motorsuz her türlü kara taşıtı.', 'baglam': ['Günlük Yaşam', 'İHA & Mühendislik']}})


def _sohbet_kimlik_ve_cihaz_kontrol(cumle: str):
    """
    'Sen kardeş misin?', 'Lambayı açar mısın?' gibi günlük konuşma ve eylem isteklerini
    anlamlandırıp doğru ve bağlantılı yanıtlar üretir.
    """
    low = cumle.replace("İ", "i").replace("I", "ı").lower().replace("\u0307", "").strip()
    norm = metni_normallestir(cumle)

    # 1) Kardeşlik / Dostluk / Kimlik soruları
    if any(k in norm for k in ["sen kardes misin", "kardes miyiz", "dost muyuz", "arkadas miyiz", "kanka miyiz"]):
        return "Evet kardeşim! Biz seninle her zaman omuz omuza çalışan yol arkadaşıyız. Ne konuda yardıma ihtiyacın varsa hemen buradayım! ⚡", "Samimi Bağ"
    if any(k in norm for k in ["sen nesin", "sen kimsin", "sen robot musun", "yapay zeka misin"]):
        return "Ben **Ar AI Studio**, Ahmet'in geliştirdiği; TDK sözlük köklerini, matematiği, dilleri ve 102 bilim insanını bilen özerk yapay zeka asistanıyım! ⚡", "Asistan Kimliği"

    # 2) Fiziksel cihaz / lamba / ışık açma-kapama istekleri
    if any(k in norm for k in ["lambayi ac", "lamba ac", "isigi ac", "isiklari ac", "lambayi kapat", "isigi kapat", "kapiyi ac", "klimayi ac"]):
        islem = "açma" if "ac" in norm else "kapatma"
        return (
            f"💡 **Fiziksel Kontrol Bilgilendirmesi:** Şu an bilgisayar/yazılım ortamında çalıştığım için evdeki fiziksel lambaya doğrudan bağlı değilim; "
            f"ancak istersen **Arduino / ESP32 röle modülü** ile sesli lamba {islem} kodunu hemen senin için yazabilirim!",
            "Akıllı Ev / Donanım Yanıtı",
        )

    # 3) Açık "X ne demek?" / "X nedir?" sorgusu -> Doğrudan TDK Sözlük + Özgün Cümle (Bilgi bankası sapması yok!)
    m_nedemek = re.match(r"^([a-zA-ZçğıöşüÇĞİÖŞÜ\s]{2,35})\s+(?:ne demek|nedir|ne anlama gelir|anlami nedir|anlamı nedir)\??$", low)
    if m_nedemek:
        hedef_ifade = m_nedemek.group(1).strip()
        # Önce deyim/atasözü, sonra TDK kelime sözlüğü, yoksa bilim insanı/bilgi bankası
        ad_sonuc = tdk_atasozu_deyim_ara(hedef_ifade)
        if ad_sonuc:
            ozg = ozgun_turkce_cumle_kur(ad_sonuc["madde"], ad_sonuc["tur"], ad_sonuc["anlam"])
            return (
                f"📜 **`{ad_sonuc['madde']}`** *({ad_sonuc['tur']})* — {ad_sonuc['anlam']}\n\n"
                f"✍️ **Özgün Cümle:** {ozg[0]}",
                f"TDK {ad_sonuc['tur']}",
            )
        kel_sonuc = tdk_akilli_kelime_getir(hedef_ifade.split()[0])
        if kel_sonuc:
            ozg = ozgun_turkce_cumle_kur(kel_sonuc["madde"], kel_sonuc.get("tur", "isim"), kel_sonuc["anlamlar"][0])
            return (
                f"📖 **`{kel_sonuc['madde']}`** kelimesinin TDK anlamı: {kel_sonuc['anlamlar'][0]}\n\n"
                f"✍️ **Özgün Cümle:** {ozg[0]}",
                f"TDK Kelime ({kel_sonuc['madde']})",
            )

    return None, None
