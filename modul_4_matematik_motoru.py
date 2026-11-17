# -*- coding: utf-8 -*-
"""
==============================================================================
AR AI STUDIO v5.0 — MODÜL 4: DERİNLEMESİNE MATEMATİK MOTORU
Dört İşlem, Köklü/Üslü Sayılar, 1. & 2. Derece Denklemler, Trigonometri,
Logaritma, Permütasyon/Kombinasyon, Polinom Türev & İntegral ve Soru Bankası
(modul_4_matematik_motoru.py)
==============================================================================
"""
import ast
import importlib.util
import math
import operator
import os
import random
import re
import sys
import streamlit as st

_MODUL_DIZINI = os.path.dirname(os.path.abspath(__file__))
if _MODUL_DIZINI not in sys.path:
    sys.path.insert(0, _MODUL_DIZINI)


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


_m1 = _guvenli_modul_yukle("modul_1_arayuz_ve_tema")
bilgi_karti_olustur = _m1.bilgi_karti_olustur

_IZINLI_OPERATORLER = {
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
}

# ==============================================================================
# 1. DERİNLEMESİNE MATEMATİK & FİZİK KONU ANLATIM ANSİKLOPEDİSİ
# ==============================================================================
MATEMATIK_KONU_REHBERI = {
    "➕ Toplama ve Çıkarma Teknikleri": {
        "alt_baslik": "Temel Aritmetik & Zihinden Hızlı İşlem",
        "icerik": "• **Değişme ve Birleşme:** Toplamada sayıların yeri değişse de sonuç değişmez (`a + b = b + a`).\n• **İşaret Kuralları:** İki eksi yan yana gelirse artıya dönüşür (`12 - (-8) = 12 + 8 = 20`).\n• **Zihinden Tamamlama:** `78 + 46` işleminde `78 + 2 = 80`, `80 + 44 = 124`.",
    },
    "✖️ Çarpma ve Bölme & Ahmet'in Tekniği": {
        "alt_baslik": "Hızlı Zihinden Çarpma & Bölünebilme",
        "icerik": "• **Ahmet'in 25 ile Çarpma Tekniği:** Sayıyı 4'e böl, yanına iki sıfır ekle (`76 × 25` → `76 / 4 = 19` → `1900`).\n• **Ahmet'in 24 ile Çarpma Tekniği:** `76 × 24 = (76 × 25) - 76 = 1900 - 76 = 1824`.\n• **11 ile Pratik Çarpma:** `43 × 11` → Rakamları topla ortasına yaz → `4 (4+3) 3 = 473`.\n• **Sıfır Kuralı:** `0 / a = 0`, fakat `a / 0` tanımsızdır!",
    },
    "√ Köklü Sayılar (Karekök & a√b)": {
        "alt_baslik": "9. Sınıf & LGS İleri Matematik",
        "icerik": "• **Tam Kare Sayılar:** `1, 4, 9, 16, 25, 36, 49, 64, 81, 100, 121, 144, 169, 196, 225, 256, 289, 324, 361, 400`.\n• **Kök Dışına Çıkarma (`a√b`):** `√72 = √(36 × 2) = 6√2` | `√128 = √(64 × 2) = 8√2`.\n• **Toplama / Çıkarma:** Kök içleri eşitse katsayılar toplanır (`5√3 + 2√3 = 7√3`).\n• **Paydayı Rasyonel Yapma:** `6 / √3 = (6√3) / 3 = 2√3`.",
    },
    "🔺 Üslü Sayılar ve Bilimsel Gösterim": {
        "alt_baslik": "Kuvvet Kuralları & Üslü Denklemler",
        "icerik": "• **Temel Kurallar:** `a⁰ = 1` (`a ≠ 0`), `a⁻ⁿ = 1 / aⁿ`.\n• **Çarpma ve Bölme:** Tabanlar aynıysa çarpmada üsler toplanır (`2⁵ × 2³ = 2⁸`), bölmede çıkarılır (`2⁵ / 2³ = 2²`).\n• **Üssün Üssü:** `(aⁿ)ᵐ = aⁿˣᵐ` (Örn: `(3²)⁴ = 3⁸`).",
    },
    "📐 1. ve 2. Dereceden Denklemler": {
        "alt_baslik": "Cebir, Kökler Toplamı & Diskriminant (Δ)",
        "icerik": "• **1. Derece (`ax + b = c`):** `x = (c - b) / a`.\n• **2. Derece (`ax² + bx + c = 0`):** Diskriminant `Δ = b² - 4ac`.\n• `Δ > 0` ise iki farklı reel kök: `x₁,₂ = (-b ± √Δ) / (2a)`.\n• **Vieta Formülleri:** Kökler toplamı `x₁ + x₂ = -b/a`, kökler çarpımı `x₁ · x₂ = c/a`.",
    },
    "🧩 Polinomlar, Çarpanlara Ayırma & Özdeşlikler": {
        "alt_baslik": "Tam Kare, İki Kare Farkı ve Küp Açılımları",
        "icerik": "• **İki Kare Farkı:** `a² - b² = (a - b)(a + b)`.\n• **Tam Kare:** `(a + b)² = a² + 2ab + b²`, `(a - b)² = a² - 2ab + b²`.\n• **Küp Açılımları:** `a³ - b³ = (a - b)(a² + ab + b²)`, `a³ + b³ = (a + b)(a² - ab + b²)`.\n• **Kalan Teoremi:** `P(x)` polinomunun `(x - a)` ile bölümünden kalan `P(a)` değeridir.",
    },
    "📊 Trigonometri & Birim Çember": {
        "alt_baslik": "Sinüs, Kosinüs, Tanjant, Kotanjant & Özdeşlikler",
        "icerik": "• **Temel Özdeşlik:** `sin²θ + cos²θ = 1`, `tan θ = sin θ / cos θ`, `tan θ · cot θ = 1`.\n• **Özel Açılar:** `sin 30° = 1/2`, `cos 30° = √3/2`, `sin 45° = cos 45° = √2/2`, `tan 45° = 1`, `sin 60° = √3/2`, `cos 60° = 1/2`.\n• **Kosinüs Teoremi:** `c² = a² + b² - 2ab·cos(C)`.",
    },
    "📉 Logaritma & Üstel Fonksiyonlar": {
        "alt_baslik": "Üstel Ters Fonksiyon, Doğal Logaritma (ln)",
        "icerik": "• **Tanım:** `aˣ = b ⇔ log_a(b) = x` (`a > 0, a ≠ 1, b > 0`).\n• **Çarpım & Bölüm:** `log_a(x·y) = log_a(x) + log_a(y)` | `log_a(x/y) = log_a(x) - log_a(y)`.\n• **Kuvvet Başa Düşer:** `log_a(xⁿ) = n · log_a(x)`.\n• **Doğal Logaritma:** `ln(x) = log_e(x)` (`e ≈ 2,71828`, `ln(e) = 1`).",
    },
    "🎲 Permütasyon, Kombinasyon & Olasılık": {
        "alt_baslik": "Sayma Kuralları, Seçim ve Olasılık",
        "icerik": "• **Permütasyon (Sıralama Önemli):** `P(n, r) = n! / (n - r)!`.\n• **Kombinasyon (Seçim, Sıra Önemsiz):** `C(n, r) = n! / (r! · (n - r)!)`.\n• **Olasılık:** `P(A) = İstenen Durum / Tüm Durumlar`, daima `0 ≤ P(A) ≤ 1`.",
    },
    "∫ Türev ve İntegral Temelleri": {
        "alt_baslik": "Değişim Hızı, Teğet Eğimi ve Alan Hesabı",
        "icerik": "• **Güç Kuralı (Türev):** `f(x) = a·xⁿ ⇒ f'(x) = a·n·xⁿ⁻¹` (Sabitin türevi `0`).\n• **Türevin Anlamı:** Eğrinin o noktadaki teğetinin eğimini ve anlık değişim hızını verir.\n• **Belirsiz İntegral:** `∫ a·xⁿ dx = (a / (n+1)) · xⁿ⁺¹ + C` (`n ≠ -1`).",
    },
    "🔢 EBOB, EKOK ve Asal Çarpanlar": {
        "alt_baslik": "Sayılar Teorisi & Problemler",
        "icerik": "• **EBOB:** İki sayıyı aynı anda bölen en büyük tam sayı.\n• **EKOK:** Sayıların ortak katlarının en küçüğü.\n• **Altın Özdeşlik:** `EBOB(a, b) × EKOK(a, b) = a × b`.",
    },
    "📏 Geometri, Pisagor ve Alan/Hacim": {
        "alt_baslik": "Üçgenler, Çember ve Katı Cisimler",
        "icerik": "• **Pisagor Teoremi:** Dik üçgende `a² + b² = c²` (`3-4-5`, `5-12-13`, `8-15-17`, `7-24-25`).\n• **Daire:** Alan = `πr²`, Çevre = `2πr`.\n• **Küre:** Hacim = `(4/3)πr³`, Yüzey Alanı = `4πr²`.",
    },
    "🚀 Fizik & İHA Mühendislik Hesapları": {
        "alt_baslik": "Hareket, Kuvvet, Enerji ve Elektrik",
        "icerik": "• **Newton'un 2. Yasası:** `F = m × a`.\n• **Kinetik Enerji:** `Ek = ½ m v²` | **Potansiyel Enerji:** `Ep = m g h`.\n• **Ohm Yasası:** `V = I × R` | **Güç:** `P = V × I`.",
    },
}

# ==============================================================================
# 2. ÖN HESAPLANMIŞ KAREKÖK, KARE, KÜP REFERANS TABLOSU (1..250)
# ==============================================================================
MATEMATIK_REFERANS_TABLOSU = {
    1: {
        "sayi": 1,
        "karesi": 1,
        "kupu": 1,
        "karekok_sade": "1",
        "karekok_ondalik": 1.0,
        "cift_mi": False,
    },
    2: {
        "sayi": 2,
        "karesi": 4,
        "kupu": 8,
        "karekok_sade": "√2",
        "karekok_ondalik": 1.4142,
        "cift_mi": True,
    },
    3: {
        "sayi": 3,
        "karesi": 9,
        "kupu": 27,
        "karekok_sade": "√3",
        "karekok_ondalik": 1.7321,
        "cift_mi": False,
    },
    4: {
        "sayi": 4,
        "karesi": 16,
        "kupu": 64,
        "karekok_sade": "2",
        "karekok_ondalik": 2.0,
        "cift_mi": True,
    },
    5: {
        "sayi": 5,
        "karesi": 25,
        "kupu": 125,
        "karekok_sade": "√5",
        "karekok_ondalik": 2.2361,
        "cift_mi": False,
    },
    6: {
        "sayi": 6,
        "karesi": 36,
        "kupu": 216,
        "karekok_sade": "√6",
        "karekok_ondalik": 2.4495,
        "cift_mi": True,
    },
    7: {
        "sayi": 7,
        "karesi": 49,
        "kupu": 343,
        "karekok_sade": "√7",
        "karekok_ondalik": 2.6458,
        "cift_mi": False,
    },
    8: {
        "sayi": 8,
        "karesi": 64,
        "kupu": 512,
        "karekok_sade": "2√2",
        "karekok_ondalik": 2.8284,
        "cift_mi": True,
    },
    9: {
        "sayi": 9,
        "karesi": 81,
        "kupu": 729,
        "karekok_sade": "3",
        "karekok_ondalik": 3.0,
        "cift_mi": False,
    },
    10: {
        "sayi": 10,
        "karesi": 100,
        "kupu": 1000,
        "karekok_sade": "√10",
        "karekok_ondalik": 3.1623,
        "cift_mi": True,
    },
    11: {
        "sayi": 11,
        "karesi": 121,
        "kupu": 1331,
        "karekok_sade": "√11",
        "karekok_ondalik": 3.3166,
        "cift_mi": False,
    },
    12: {
        "sayi": 12,
        "karesi": 144,
        "kupu": 1728,
        "karekok_sade": "2√3",
        "karekok_ondalik": 3.4641,
        "cift_mi": True,
    },
    13: {
        "sayi": 13,
        "karesi": 169,
        "kupu": 2197,
        "karekok_sade": "√13",
        "karekok_ondalik": 3.6056,
        "cift_mi": False,
    },
    14: {
        "sayi": 14,
        "karesi": 196,
        "kupu": 2744,
        "karekok_sade": "√14",
        "karekok_ondalik": 3.7417,
        "cift_mi": True,
    },
    15: {
        "sayi": 15,
        "karesi": 225,
        "kupu": 3375,
        "karekok_sade": "√15",
        "karekok_ondalik": 3.873,
        "cift_mi": False,
    },
    16: {
        "sayi": 16,
        "karesi": 256,
        "kupu": 4096,
        "karekok_sade": "4",
        "karekok_ondalik": 4.0,
        "cift_mi": True,
    },
    17: {
        "sayi": 17,
        "karesi": 289,
        "kupu": 4913,
        "karekok_sade": "√17",
        "karekok_ondalik": 4.1231,
        "cift_mi": False,
    },
    18: {
        "sayi": 18,
        "karesi": 324,
        "kupu": 5832,
        "karekok_sade": "3√2",
        "karekok_ondalik": 4.2426,
        "cift_mi": True,
    },
    19: {
        "sayi": 19,
        "karesi": 361,
        "kupu": 6859,
        "karekok_sade": "√19",
        "karekok_ondalik": 4.3589,
        "cift_mi": False,
    },
    20: {
        "sayi": 20,
        "karesi": 400,
        "kupu": 8000,
        "karekok_sade": "2√5",
        "karekok_ondalik": 4.4721,
        "cift_mi": True,
    },
    21: {
        "sayi": 21,
        "karesi": 441,
        "kupu": 9261,
        "karekok_sade": "√21",
        "karekok_ondalik": 4.5826,
        "cift_mi": False,
    },
    22: {
        "sayi": 22,
        "karesi": 484,
        "kupu": 10648,
        "karekok_sade": "√22",
        "karekok_ondalik": 4.6904,
        "cift_mi": True,
    },
    23: {
        "sayi": 23,
        "karesi": 529,
        "kupu": 12167,
        "karekok_sade": "√23",
        "karekok_ondalik": 4.7958,
        "cift_mi": False,
    },
    24: {
        "sayi": 24,
        "karesi": 576,
        "kupu": 13824,
        "karekok_sade": "2√6",
        "karekok_ondalik": 4.899,
        "cift_mi": True,
    },
    25: {
        "sayi": 25,
        "karesi": 625,
        "kupu": 15625,
        "karekok_sade": "5",
        "karekok_ondalik": 5.0,
        "cift_mi": False,
    },
    26: {
        "sayi": 26,
        "karesi": 676,
        "kupu": 17576,
        "karekok_sade": "√26",
        "karekok_ondalik": 5.099,
        "cift_mi": True,
    },
    27: {
        "sayi": 27,
        "karesi": 729,
        "kupu": 19683,
        "karekok_sade": "3√3",
        "karekok_ondalik": 5.1962,
        "cift_mi": False,
    },
    28: {
        "sayi": 28,
        "karesi": 784,
        "kupu": 21952,
        "karekok_sade": "2√7",
        "karekok_ondalik": 5.2915,
        "cift_mi": True,
    },
    29: {
        "sayi": 29,
        "karesi": 841,
        "kupu": 24389,
        "karekok_sade": "√29",
        "karekok_ondalik": 5.3852,
        "cift_mi": False,
    },
    30: {
        "sayi": 30,
        "karesi": 900,
        "kupu": 27000,
        "karekok_sade": "√30",
        "karekok_ondalik": 5.4772,
        "cift_mi": True,
    },
    31: {
        "sayi": 31,
        "karesi": 961,
        "kupu": 29791,
        "karekok_sade": "√31",
        "karekok_ondalik": 5.5678,
        "cift_mi": False,
    },
    32: {
        "sayi": 32,
        "karesi": 1024,
        "kupu": 32768,
        "karekok_sade": "4√2",
        "karekok_ondalik": 5.6569,
        "cift_mi": True,
    },
    33: {
        "sayi": 33,
        "karesi": 1089,
        "kupu": 35937,
        "karekok_sade": "√33",
        "karekok_ondalik": 5.7446,
        "cift_mi": False,
    },
    34: {
        "sayi": 34,
        "karesi": 1156,
        "kupu": 39304,
        "karekok_sade": "√34",
        "karekok_ondalik": 5.831,
        "cift_mi": True,
    },
    35: {
        "sayi": 35,
        "karesi": 1225,
        "kupu": 42875,
        "karekok_sade": "√35",
        "karekok_ondalik": 5.9161,
        "cift_mi": False,
    },
    36: {
        "sayi": 36,
        "karesi": 1296,
        "kupu": 46656,
        "karekok_sade": "6",
        "karekok_ondalik": 6.0,
        "cift_mi": True,
    },
    37: {
        "sayi": 37,
        "karesi": 1369,
        "kupu": 50653,
        "karekok_sade": "√37",
        "karekok_ondalik": 6.0828,
        "cift_mi": False,
    },
    38: {
        "sayi": 38,
        "karesi": 1444,
        "kupu": 54872,
        "karekok_sade": "√38",
        "karekok_ondalik": 6.1644,
        "cift_mi": True,
    },
    39: {
        "sayi": 39,
        "karesi": 1521,
        "kupu": 59319,
        "karekok_sade": "√39",
        "karekok_ondalik": 6.245,
        "cift_mi": False,
    },
    40: {
        "sayi": 40,
        "karesi": 1600,
        "kupu": 64000,
        "karekok_sade": "2√10",
        "karekok_ondalik": 6.3246,
        "cift_mi": True,
    },
    41: {
        "sayi": 41,
        "karesi": 1681,
        "kupu": 68921,
        "karekok_sade": "√41",
        "karekok_ondalik": 6.4031,
        "cift_mi": False,
    },
    42: {
        "sayi": 42,
        "karesi": 1764,
        "kupu": 74088,
        "karekok_sade": "√42",
        "karekok_ondalik": 6.4807,
        "cift_mi": True,
    },
    43: {
        "sayi": 43,
        "karesi": 1849,
        "kupu": 79507,
        "karekok_sade": "√43",
        "karekok_ondalik": 6.5574,
        "cift_mi": False,
    },
    44: {
        "sayi": 44,
        "karesi": 1936,
        "kupu": 85184,
        "karekok_sade": "2√11",
        "karekok_ondalik": 6.6332,
        "cift_mi": True,
    },
    45: {
        "sayi": 45,
        "karesi": 2025,
        "kupu": 91125,
        "karekok_sade": "3√5",
        "karekok_ondalik": 6.7082,
        "cift_mi": False,
    },
    46: {
        "sayi": 46,
        "karesi": 2116,
        "kupu": 97336,
        "karekok_sade": "√46",
        "karekok_ondalik": 6.7823,
        "cift_mi": True,
    },
    47: {
        "sayi": 47,
        "karesi": 2209,
        "kupu": 103823,
        "karekok_sade": "√47",
        "karekok_ondalik": 6.8557,
        "cift_mi": False,
    },
    48: {
        "sayi": 48,
        "karesi": 2304,
        "kupu": 110592,
        "karekok_sade": "4√3",
        "karekok_ondalik": 6.9282,
        "cift_mi": True,
    },
    49: {
        "sayi": 49,
        "karesi": 2401,
        "kupu": 117649,
        "karekok_sade": "7",
        "karekok_ondalik": 7.0,
        "cift_mi": False,
    },
    50: {
        "sayi": 50,
        "karesi": 2500,
        "kupu": 125000,
        "karekok_sade": "5√2",
        "karekok_ondalik": 7.0711,
        "cift_mi": True,
    },
    51: {
        "sayi": 51,
        "karesi": 2601,
        "kupu": 132651,
        "karekok_sade": "√51",
        "karekok_ondalik": 7.1414,
        "cift_mi": False,
    },
    52: {
        "sayi": 52,
        "karesi": 2704,
        "kupu": 140608,
        "karekok_sade": "2√13",
        "karekok_ondalik": 7.2111,
        "cift_mi": True,
    },
    53: {
        "sayi": 53,
        "karesi": 2809,
        "kupu": 148877,
        "karekok_sade": "√53",
        "karekok_ondalik": 7.2801,
        "cift_mi": False,
    },
    54: {
        "sayi": 54,
        "karesi": 2916,
        "kupu": 157464,
        "karekok_sade": "3√6",
        "karekok_ondalik": 7.3485,
        "cift_mi": True,
    },
    55: {
        "sayi": 55,
        "karesi": 3025,
        "kupu": 166375,
        "karekok_sade": "√55",
        "karekok_ondalik": 7.4162,
        "cift_mi": False,
    },
    56: {
        "sayi": 56,
        "karesi": 3136,
        "kupu": 175616,
        "karekok_sade": "2√14",
        "karekok_ondalik": 7.4833,
        "cift_mi": True,
    },
    57: {
        "sayi": 57,
        "karesi": 3249,
        "kupu": 185193,
        "karekok_sade": "√57",
        "karekok_ondalik": 7.5498,
        "cift_mi": False,
    },
    58: {
        "sayi": 58,
        "karesi": 3364,
        "kupu": 195112,
        "karekok_sade": "√58",
        "karekok_ondalik": 7.6158,
        "cift_mi": True,
    },
    59: {
        "sayi": 59,
        "karesi": 3481,
        "kupu": 205379,
        "karekok_sade": "√59",
        "karekok_ondalik": 7.6811,
        "cift_mi": False,
    },
    60: {
        "sayi": 60,
        "karesi": 3600,
        "kupu": 216000,
        "karekok_sade": "2√15",
        "karekok_ondalik": 7.746,
        "cift_mi": True,
    },
    61: {
        "sayi": 61,
        "karesi": 3721,
        "kupu": 226981,
        "karekok_sade": "√61",
        "karekok_ondalik": 7.8102,
        "cift_mi": False,
    },
    62: {
        "sayi": 62,
        "karesi": 3844,
        "kupu": 238328,
        "karekok_sade": "√62",
        "karekok_ondalik": 7.874,
        "cift_mi": True,
    },
    63: {
        "sayi": 63,
        "karesi": 3969,
        "kupu": 250047,
        "karekok_sade": "3√7",
        "karekok_ondalik": 7.9373,
        "cift_mi": False,
    },
    64: {
        "sayi": 64,
        "karesi": 4096,
        "kupu": 262144,
        "karekok_sade": "8",
        "karekok_ondalik": 8.0,
        "cift_mi": True,
    },
    65: {
        "sayi": 65,
        "karesi": 4225,
        "kupu": 274625,
        "karekok_sade": "√65",
        "karekok_ondalik": 8.0623,
        "cift_mi": False,
    },
    66: {
        "sayi": 66,
        "karesi": 4356,
        "kupu": 287496,
        "karekok_sade": "√66",
        "karekok_ondalik": 8.124,
        "cift_mi": True,
    },
    67: {
        "sayi": 67,
        "karesi": 4489,
        "kupu": 300763,
        "karekok_sade": "√67",
        "karekok_ondalik": 8.1854,
        "cift_mi": False,
    },
    68: {
        "sayi": 68,
        "karesi": 4624,
        "kupu": 314432,
        "karekok_sade": "2√17",
        "karekok_ondalik": 8.2462,
        "cift_mi": True,
    },
    69: {
        "sayi": 69,
        "karesi": 4761,
        "kupu": 328509,
        "karekok_sade": "√69",
        "karekok_ondalik": 8.3066,
        "cift_mi": False,
    },
    70: {
        "sayi": 70,
        "karesi": 4900,
        "kupu": 343000,
        "karekok_sade": "√70",
        "karekok_ondalik": 8.3666,
        "cift_mi": True,
    },
    71: {
        "sayi": 71,
        "karesi": 5041,
        "kupu": 357911,
        "karekok_sade": "√71",
        "karekok_ondalik": 8.4261,
        "cift_mi": False,
    },
    72: {
        "sayi": 72,
        "karesi": 5184,
        "kupu": 373248,
        "karekok_sade": "6√2",
        "karekok_ondalik": 8.4853,
        "cift_mi": True,
    },
    73: {
        "sayi": 73,
        "karesi": 5329,
        "kupu": 389017,
        "karekok_sade": "√73",
        "karekok_ondalik": 8.544,
        "cift_mi": False,
    },
    74: {
        "sayi": 74,
        "karesi": 5476,
        "kupu": 405224,
        "karekok_sade": "√74",
        "karekok_ondalik": 8.6023,
        "cift_mi": True,
    },
    75: {
        "sayi": 75,
        "karesi": 5625,
        "kupu": 421875,
        "karekok_sade": "5√3",
        "karekok_ondalik": 8.6603,
        "cift_mi": False,
    },
    76: {
        "sayi": 76,
        "karesi": 5776,
        "kupu": 438976,
        "karekok_sade": "2√19",
        "karekok_ondalik": 8.7178,
        "cift_mi": True,
    },
    77: {
        "sayi": 77,
        "karesi": 5929,
        "kupu": 456533,
        "karekok_sade": "√77",
        "karekok_ondalik": 8.775,
        "cift_mi": False,
    },
    78: {
        "sayi": 78,
        "karesi": 6084,
        "kupu": 474552,
        "karekok_sade": "√78",
        "karekok_ondalik": 8.8318,
        "cift_mi": True,
    },
    79: {
        "sayi": 79,
        "karesi": 6241,
        "kupu": 493039,
        "karekok_sade": "√79",
        "karekok_ondalik": 8.8882,
        "cift_mi": False,
    },
    80: {
        "sayi": 80,
        "karesi": 6400,
        "kupu": 512000,
        "karekok_sade": "4√5",
        "karekok_ondalik": 8.9443,
        "cift_mi": True,
    },
    81: {
        "sayi": 81,
        "karesi": 6561,
        "kupu": 531441,
        "karekok_sade": "9",
        "karekok_ondalik": 9.0,
        "cift_mi": False,
    },
    82: {
        "sayi": 82,
        "karesi": 6724,
        "kupu": 551368,
        "karekok_sade": "√82",
        "karekok_ondalik": 9.0554,
        "cift_mi": True,
    },
    83: {
        "sayi": 83,
        "karesi": 6889,
        "kupu": 571787,
        "karekok_sade": "√83",
        "karekok_ondalik": 9.1104,
        "cift_mi": False,
    },
    84: {
        "sayi": 84,
        "karesi": 7056,
        "kupu": 592704,
        "karekok_sade": "2√21",
        "karekok_ondalik": 9.1652,
        "cift_mi": True,
    },
    85: {
        "sayi": 85,
        "karesi": 7225,
        "kupu": 614125,
        "karekok_sade": "√85",
        "karekok_ondalik": 9.2195,
        "cift_mi": False,
    },
    86: {
        "sayi": 86,
        "karesi": 7396,
        "kupu": 636056,
        "karekok_sade": "√86",
        "karekok_ondalik": 9.2736,
        "cift_mi": True,
    },
    87: {
        "sayi": 87,
        "karesi": 7569,
        "kupu": 658503,
        "karekok_sade": "√87",
        "karekok_ondalik": 9.3274,
        "cift_mi": False,
    },
    88: {
        "sayi": 88,
        "karesi": 7744,
        "kupu": 681472,
        "karekok_sade": "2√22",
        "karekok_ondalik": 9.3808,
        "cift_mi": True,
    },
    89: {
        "sayi": 89,
        "karesi": 7921,
        "kupu": 704969,
        "karekok_sade": "√89",
        "karekok_ondalik": 9.434,
        "cift_mi": False,
    },
    90: {
        "sayi": 90,
        "karesi": 8100,
        "kupu": 729000,
        "karekok_sade": "3√10",
        "karekok_ondalik": 9.4868,
        "cift_mi": True,
    },
    91: {
        "sayi": 91,
        "karesi": 8281,
        "kupu": 753571,
        "karekok_sade": "√91",
        "karekok_ondalik": 9.5394,
        "cift_mi": False,
    },
    92: {
        "sayi": 92,
        "karesi": 8464,
        "kupu": 778688,
        "karekok_sade": "2√23",
        "karekok_ondalik": 9.5917,
        "cift_mi": True,
    },
    93: {
        "sayi": 93,
        "karesi": 8649,
        "kupu": 804357,
        "karekok_sade": "√93",
        "karekok_ondalik": 9.6437,
        "cift_mi": False,
    },
    94: {
        "sayi": 94,
        "karesi": 8836,
        "kupu": 830584,
        "karekok_sade": "√94",
        "karekok_ondalik": 9.6954,
        "cift_mi": True,
    },
    95: {
        "sayi": 95,
        "karesi": 9025,
        "kupu": 857375,
        "karekok_sade": "√95",
        "karekok_ondalik": 9.7468,
        "cift_mi": False,
    },
    96: {
        "sayi": 96,
        "karesi": 9216,
        "kupu": 884736,
        "karekok_sade": "4√6",
        "karekok_ondalik": 9.798,
        "cift_mi": True,
    },
    97: {
        "sayi": 97,
        "karesi": 9409,
        "kupu": 912673,
        "karekok_sade": "√97",
        "karekok_ondalik": 9.8489,
        "cift_mi": False,
    },
    98: {
        "sayi": 98,
        "karesi": 9604,
        "kupu": 941192,
        "karekok_sade": "7√2",
        "karekok_ondalik": 9.8995,
        "cift_mi": True,
    },
    99: {
        "sayi": 99,
        "karesi": 9801,
        "kupu": 970299,
        "karekok_sade": "3√11",
        "karekok_ondalik": 9.9499,
        "cift_mi": False,
    },
    100: {
        "sayi": 100,
        "karesi": 10000,
        "kupu": 1000000,
        "karekok_sade": "10",
        "karekok_ondalik": 10.0,
        "cift_mi": True,
    },
    101: {
        "sayi": 101,
        "karesi": 10201,
        "kupu": 1030301,
        "karekok_sade": "√101",
        "karekok_ondalik": 10.0499,
        "cift_mi": False,
    },
    102: {
        "sayi": 102,
        "karesi": 10404,
        "kupu": 1061208,
        "karekok_sade": "√102",
        "karekok_ondalik": 10.0995,
        "cift_mi": True,
    },
    103: {
        "sayi": 103,
        "karesi": 10609,
        "kupu": 1092727,
        "karekok_sade": "√103",
        "karekok_ondalik": 10.1489,
        "cift_mi": False,
    },
    104: {
        "sayi": 104,
        "karesi": 10816,
        "kupu": 1124864,
        "karekok_sade": "2√26",
        "karekok_ondalik": 10.198,
        "cift_mi": True,
    },
    105: {
        "sayi": 105,
        "karesi": 11025,
        "kupu": 1157625,
        "karekok_sade": "√105",
        "karekok_ondalik": 10.247,
        "cift_mi": False,
    },
    106: {
        "sayi": 106,
        "karesi": 11236,
        "kupu": 1191016,
        "karekok_sade": "√106",
        "karekok_ondalik": 10.2956,
        "cift_mi": True,
    },
    107: {
        "sayi": 107,
        "karesi": 11449,
        "kupu": 1225043,
        "karekok_sade": "√107",
        "karekok_ondalik": 10.3441,
        "cift_mi": False,
    },
    108: {
        "sayi": 108,
        "karesi": 11664,
        "kupu": 1259712,
        "karekok_sade": "6√3",
        "karekok_ondalik": 10.3923,
        "cift_mi": True,
    },
    109: {
        "sayi": 109,
        "karesi": 11881,
        "kupu": 1295029,
        "karekok_sade": "√109",
        "karekok_ondalik": 10.4403,
        "cift_mi": False,
    },
    110: {
        "sayi": 110,
        "karesi": 12100,
        "kupu": 1331000,
        "karekok_sade": "√110",
        "karekok_ondalik": 10.4881,
        "cift_mi": True,
    },
    111: {
        "sayi": 111,
        "karesi": 12321,
        "kupu": 1367631,
        "karekok_sade": "√111",
        "karekok_ondalik": 10.5357,
        "cift_mi": False,
    },
    112: {
        "sayi": 112,
        "karesi": 12544,
        "kupu": 1404928,
        "karekok_sade": "4√7",
        "karekok_ondalik": 10.583,
        "cift_mi": True,
    },
    113: {
        "sayi": 113,
        "karesi": 12769,
        "kupu": 1442897,
        "karekok_sade": "√113",
        "karekok_ondalik": 10.6301,
        "cift_mi": False,
    },
    114: {
        "sayi": 114,
        "karesi": 12996,
        "kupu": 1481544,
        "karekok_sade": "√114",
        "karekok_ondalik": 10.6771,
        "cift_mi": True,
    },
    115: {
        "sayi": 115,
        "karesi": 13225,
        "kupu": 1520875,
        "karekok_sade": "√115",
        "karekok_ondalik": 10.7238,
        "cift_mi": False,
    },
    116: {
        "sayi": 116,
        "karesi": 13456,
        "kupu": 1560896,
        "karekok_sade": "2√29",
        "karekok_ondalik": 10.7703,
        "cift_mi": True,
    },
    117: {
        "sayi": 117,
        "karesi": 13689,
        "kupu": 1601613,
        "karekok_sade": "3√13",
        "karekok_ondalik": 10.8167,
        "cift_mi": False,
    },
    118: {
        "sayi": 118,
        "karesi": 13924,
        "kupu": 1643032,
        "karekok_sade": "√118",
        "karekok_ondalik": 10.8628,
        "cift_mi": True,
    },
    119: {
        "sayi": 119,
        "karesi": 14161,
        "kupu": 1685159,
        "karekok_sade": "√119",
        "karekok_ondalik": 10.9087,
        "cift_mi": False,
    },
    120: {
        "sayi": 120,
        "karesi": 14400,
        "kupu": 1728000,
        "karekok_sade": "2√30",
        "karekok_ondalik": 10.9545,
        "cift_mi": True,
    },
    121: {
        "sayi": 121,
        "karesi": 14641,
        "kupu": 1771561,
        "karekok_sade": "11",
        "karekok_ondalik": 11.0,
        "cift_mi": False,
    },
    122: {
        "sayi": 122,
        "karesi": 14884,
        "kupu": 1815848,
        "karekok_sade": "√122",
        "karekok_ondalik": 11.0454,
        "cift_mi": True,
    },
    123: {
        "sayi": 123,
        "karesi": 15129,
        "kupu": 1860867,
        "karekok_sade": "√123",
        "karekok_ondalik": 11.0905,
        "cift_mi": False,
    },
    124: {
        "sayi": 124,
        "karesi": 15376,
        "kupu": 1906624,
        "karekok_sade": "2√31",
        "karekok_ondalik": 11.1355,
        "cift_mi": True,
    },
    125: {
        "sayi": 125,
        "karesi": 15625,
        "kupu": 1953125,
        "karekok_sade": "5√5",
        "karekok_ondalik": 11.1803,
        "cift_mi": False,
    },
    126: {
        "sayi": 126,
        "karesi": 15876,
        "kupu": 2000376,
        "karekok_sade": "3√14",
        "karekok_ondalik": 11.225,
        "cift_mi": True,
    },
    127: {
        "sayi": 127,
        "karesi": 16129,
        "kupu": 2048383,
        "karekok_sade": "√127",
        "karekok_ondalik": 11.2694,
        "cift_mi": False,
    },
    128: {
        "sayi": 128,
        "karesi": 16384,
        "kupu": 2097152,
        "karekok_sade": "8√2",
        "karekok_ondalik": 11.3137,
        "cift_mi": True,
    },
    129: {
        "sayi": 129,
        "karesi": 16641,
        "kupu": 2146689,
        "karekok_sade": "√129",
        "karekok_ondalik": 11.3578,
        "cift_mi": False,
    },
    130: {
        "sayi": 130,
        "karesi": 16900,
        "kupu": 2197000,
        "karekok_sade": "√130",
        "karekok_ondalik": 11.4018,
        "cift_mi": True,
    },
    131: {
        "sayi": 131,
        "karesi": 17161,
        "kupu": 2248091,
        "karekok_sade": "√131",
        "karekok_ondalik": 11.4455,
        "cift_mi": False,
    },
    132: {
        "sayi": 132,
        "karesi": 17424,
        "kupu": 2299968,
        "karekok_sade": "2√33",
        "karekok_ondalik": 11.4891,
        "cift_mi": True,
    },
    133: {
        "sayi": 133,
        "karesi": 17689,
        "kupu": 2352637,
        "karekok_sade": "√133",
        "karekok_ondalik": 11.5326,
        "cift_mi": False,
    },
    134: {
        "sayi": 134,
        "karesi": 17956,
        "kupu": 2406104,
        "karekok_sade": "√134",
        "karekok_ondalik": 11.5758,
        "cift_mi": True,
    },
    135: {
        "sayi": 135,
        "karesi": 18225,
        "kupu": 2460375,
        "karekok_sade": "3√15",
        "karekok_ondalik": 11.619,
        "cift_mi": False,
    },
    136: {
        "sayi": 136,
        "karesi": 18496,
        "kupu": 2515456,
        "karekok_sade": "2√34",
        "karekok_ondalik": 11.6619,
        "cift_mi": True,
    },
    137: {
        "sayi": 137,
        "karesi": 18769,
        "kupu": 2571353,
        "karekok_sade": "√137",
        "karekok_ondalik": 11.7047,
        "cift_mi": False,
    },
    138: {
        "sayi": 138,
        "karesi": 19044,
        "kupu": 2628072,
        "karekok_sade": "√138",
        "karekok_ondalik": 11.7473,
        "cift_mi": True,
    },
    139: {
        "sayi": 139,
        "karesi": 19321,
        "kupu": 2685619,
        "karekok_sade": "√139",
        "karekok_ondalik": 11.7898,
        "cift_mi": False,
    },
    140: {
        "sayi": 140,
        "karesi": 19600,
        "kupu": 2744000,
        "karekok_sade": "2√35",
        "karekok_ondalik": 11.8322,
        "cift_mi": True,
    },
    141: {
        "sayi": 141,
        "karesi": 19881,
        "kupu": 2803221,
        "karekok_sade": "√141",
        "karekok_ondalik": 11.8743,
        "cift_mi": False,
    },
    142: {
        "sayi": 142,
        "karesi": 20164,
        "kupu": 2863288,
        "karekok_sade": "√142",
        "karekok_ondalik": 11.9164,
        "cift_mi": True,
    },
    143: {
        "sayi": 143,
        "karesi": 20449,
        "kupu": 2924207,
        "karekok_sade": "√143",
        "karekok_ondalik": 11.9583,
        "cift_mi": False,
    },
    144: {
        "sayi": 144,
        "karesi": 20736,
        "kupu": 2985984,
        "karekok_sade": "12",
        "karekok_ondalik": 12.0,
        "cift_mi": True,
    },
    145: {
        "sayi": 145,
        "karesi": 21025,
        "kupu": 3048625,
        "karekok_sade": "√145",
        "karekok_ondalik": 12.0416,
        "cift_mi": False,
    },
    146: {
        "sayi": 146,
        "karesi": 21316,
        "kupu": 3112136,
        "karekok_sade": "√146",
        "karekok_ondalik": 12.083,
        "cift_mi": True,
    },
    147: {
        "sayi": 147,
        "karesi": 21609,
        "kupu": 3176523,
        "karekok_sade": "7√3",
        "karekok_ondalik": 12.1244,
        "cift_mi": False,
    },
    148: {
        "sayi": 148,
        "karesi": 21904,
        "kupu": 3241792,
        "karekok_sade": "2√37",
        "karekok_ondalik": 12.1655,
        "cift_mi": True,
    },
    149: {
        "sayi": 149,
        "karesi": 22201,
        "kupu": 3307949,
        "karekok_sade": "√149",
        "karekok_ondalik": 12.2066,
        "cift_mi": False,
    },
    150: {
        "sayi": 150,
        "karesi": 22500,
        "kupu": 3375000,
        "karekok_sade": "5√6",
        "karekok_ondalik": 12.2474,
        "cift_mi": True,
    },
    151: {
        "sayi": 151,
        "karesi": 22801,
        "kupu": 3442951,
        "karekok_sade": "√151",
        "karekok_ondalik": 12.2882,
        "cift_mi": False,
    },
    152: {
        "sayi": 152,
        "karesi": 23104,
        "kupu": 3511808,
        "karekok_sade": "2√38",
        "karekok_ondalik": 12.3288,
        "cift_mi": True,
    },
    153: {
        "sayi": 153,
        "karesi": 23409,
        "kupu": 3581577,
        "karekok_sade": "3√17",
        "karekok_ondalik": 12.3693,
        "cift_mi": False,
    },
    154: {
        "sayi": 154,
        "karesi": 23716,
        "kupu": 3652264,
        "karekok_sade": "√154",
        "karekok_ondalik": 12.4097,
        "cift_mi": True,
    },
    155: {
        "sayi": 155,
        "karesi": 24025,
        "kupu": 3723875,
        "karekok_sade": "√155",
        "karekok_ondalik": 12.4499,
        "cift_mi": False,
    },
    156: {
        "sayi": 156,
        "karesi": 24336,
        "kupu": 3796416,
        "karekok_sade": "2√39",
        "karekok_ondalik": 12.49,
        "cift_mi": True,
    },
    157: {
        "sayi": 157,
        "karesi": 24649,
        "kupu": 3869893,
        "karekok_sade": "√157",
        "karekok_ondalik": 12.53,
        "cift_mi": False,
    },
    158: {
        "sayi": 158,
        "karesi": 24964,
        "kupu": 3944312,
        "karekok_sade": "√158",
        "karekok_ondalik": 12.5698,
        "cift_mi": True,
    },
    159: {
        "sayi": 159,
        "karesi": 25281,
        "kupu": 4019679,
        "karekok_sade": "√159",
        "karekok_ondalik": 12.6095,
        "cift_mi": False,
    },
    160: {
        "sayi": 160,
        "karesi": 25600,
        "kupu": 4096000,
        "karekok_sade": "4√10",
        "karekok_ondalik": 12.6491,
        "cift_mi": True,
    },
    161: {
        "sayi": 161,
        "karesi": 25921,
        "kupu": 4173281,
        "karekok_sade": "√161",
        "karekok_ondalik": 12.6886,
        "cift_mi": False,
    },
    162: {
        "sayi": 162,
        "karesi": 26244,
        "kupu": 4251528,
        "karekok_sade": "9√2",
        "karekok_ondalik": 12.7279,
        "cift_mi": True,
    },
    163: {
        "sayi": 163,
        "karesi": 26569,
        "kupu": 4330747,
        "karekok_sade": "√163",
        "karekok_ondalik": 12.7671,
        "cift_mi": False,
    },
    164: {
        "sayi": 164,
        "karesi": 26896,
        "kupu": 4410944,
        "karekok_sade": "2√41",
        "karekok_ondalik": 12.8062,
        "cift_mi": True,
    },
    165: {
        "sayi": 165,
        "karesi": 27225,
        "kupu": 4492125,
        "karekok_sade": "√165",
        "karekok_ondalik": 12.8452,
        "cift_mi": False,
    },
    166: {
        "sayi": 166,
        "karesi": 27556,
        "kupu": 4574296,
        "karekok_sade": "√166",
        "karekok_ondalik": 12.8841,
        "cift_mi": True,
    },
    167: {
        "sayi": 167,
        "karesi": 27889,
        "kupu": 4657463,
        "karekok_sade": "√167",
        "karekok_ondalik": 12.9228,
        "cift_mi": False,
    },
    168: {
        "sayi": 168,
        "karesi": 28224,
        "kupu": 4741632,
        "karekok_sade": "2√42",
        "karekok_ondalik": 12.9615,
        "cift_mi": True,
    },
    169: {
        "sayi": 169,
        "karesi": 28561,
        "kupu": 4826809,
        "karekok_sade": "13",
        "karekok_ondalik": 13.0,
        "cift_mi": False,
    },
    170: {
        "sayi": 170,
        "karesi": 28900,
        "kupu": 4913000,
        "karekok_sade": "√170",
        "karekok_ondalik": 13.0384,
        "cift_mi": True,
    },
    171: {
        "sayi": 171,
        "karesi": 29241,
        "kupu": 5000211,
        "karekok_sade": "3√19",
        "karekok_ondalik": 13.0767,
        "cift_mi": False,
    },
    172: {
        "sayi": 172,
        "karesi": 29584,
        "kupu": 5088448,
        "karekok_sade": "2√43",
        "karekok_ondalik": 13.1149,
        "cift_mi": True,
    },
    173: {
        "sayi": 173,
        "karesi": 29929,
        "kupu": 5177717,
        "karekok_sade": "√173",
        "karekok_ondalik": 13.1529,
        "cift_mi": False,
    },
    174: {
        "sayi": 174,
        "karesi": 30276,
        "kupu": 5268024,
        "karekok_sade": "√174",
        "karekok_ondalik": 13.1909,
        "cift_mi": True,
    },
    175: {
        "sayi": 175,
        "karesi": 30625,
        "kupu": 5359375,
        "karekok_sade": "5√7",
        "karekok_ondalik": 13.2288,
        "cift_mi": False,
    },
    176: {
        "sayi": 176,
        "karesi": 30976,
        "kupu": 5451776,
        "karekok_sade": "4√11",
        "karekok_ondalik": 13.2665,
        "cift_mi": True,
    },
    177: {
        "sayi": 177,
        "karesi": 31329,
        "kupu": 5545233,
        "karekok_sade": "√177",
        "karekok_ondalik": 13.3041,
        "cift_mi": False,
    },
    178: {
        "sayi": 178,
        "karesi": 31684,
        "kupu": 5639752,
        "karekok_sade": "√178",
        "karekok_ondalik": 13.3417,
        "cift_mi": True,
    },
    179: {
        "sayi": 179,
        "karesi": 32041,
        "kupu": 5735339,
        "karekok_sade": "√179",
        "karekok_ondalik": 13.3791,
        "cift_mi": False,
    },
    180: {
        "sayi": 180,
        "karesi": 32400,
        "kupu": 5832000,
        "karekok_sade": "6√5",
        "karekok_ondalik": 13.4164,
        "cift_mi": True,
    },
    181: {
        "sayi": 181,
        "karesi": 32761,
        "kupu": 5929741,
        "karekok_sade": "√181",
        "karekok_ondalik": 13.4536,
        "cift_mi": False,
    },
    182: {
        "sayi": 182,
        "karesi": 33124,
        "kupu": 6028568,
        "karekok_sade": "√182",
        "karekok_ondalik": 13.4907,
        "cift_mi": True,
    },
    183: {
        "sayi": 183,
        "karesi": 33489,
        "kupu": 6128487,
        "karekok_sade": "√183",
        "karekok_ondalik": 13.5277,
        "cift_mi": False,
    },
    184: {
        "sayi": 184,
        "karesi": 33856,
        "kupu": 6229504,
        "karekok_sade": "2√46",
        "karekok_ondalik": 13.5647,
        "cift_mi": True,
    },
    185: {
        "sayi": 185,
        "karesi": 34225,
        "kupu": 6331625,
        "karekok_sade": "√185",
        "karekok_ondalik": 13.6015,
        "cift_mi": False,
    },
    186: {
        "sayi": 186,
        "karesi": 34596,
        "kupu": 6434856,
        "karekok_sade": "√186",
        "karekok_ondalik": 13.6382,
        "cift_mi": True,
    },
    187: {
        "sayi": 187,
        "karesi": 34969,
        "kupu": 6539203,
        "karekok_sade": "√187",
        "karekok_ondalik": 13.6748,
        "cift_mi": False,
    },
    188: {
        "sayi": 188,
        "karesi": 35344,
        "kupu": 6644672,
        "karekok_sade": "2√47",
        "karekok_ondalik": 13.7113,
        "cift_mi": True,
    },
    189: {
        "sayi": 189,
        "karesi": 35721,
        "kupu": 6751269,
        "karekok_sade": "3√21",
        "karekok_ondalik": 13.7477,
        "cift_mi": False,
    },
    190: {
        "sayi": 190,
        "karesi": 36100,
        "kupu": 6859000,
        "karekok_sade": "√190",
        "karekok_ondalik": 13.784,
        "cift_mi": True,
    },
    191: {
        "sayi": 191,
        "karesi": 36481,
        "kupu": 6967871,
        "karekok_sade": "√191",
        "karekok_ondalik": 13.8203,
        "cift_mi": False,
    },
    192: {
        "sayi": 192,
        "karesi": 36864,
        "kupu": 7077888,
        "karekok_sade": "8√3",
        "karekok_ondalik": 13.8564,
        "cift_mi": True,
    },
    193: {
        "sayi": 193,
        "karesi": 37249,
        "kupu": 7189057,
        "karekok_sade": "√193",
        "karekok_ondalik": 13.8924,
        "cift_mi": False,
    },
    194: {
        "sayi": 194,
        "karesi": 37636,
        "kupu": 7301384,
        "karekok_sade": "√194",
        "karekok_ondalik": 13.9284,
        "cift_mi": True,
    },
    195: {
        "sayi": 195,
        "karesi": 38025,
        "kupu": 7414875,
        "karekok_sade": "√195",
        "karekok_ondalik": 13.9642,
        "cift_mi": False,
    },
    196: {
        "sayi": 196,
        "karesi": 38416,
        "kupu": 7529536,
        "karekok_sade": "14",
        "karekok_ondalik": 14.0,
        "cift_mi": True,
    },
    197: {
        "sayi": 197,
        "karesi": 38809,
        "kupu": 7645373,
        "karekok_sade": "√197",
        "karekok_ondalik": 14.0357,
        "cift_mi": False,
    },
    198: {
        "sayi": 198,
        "karesi": 39204,
        "kupu": 7762392,
        "karekok_sade": "3√22",
        "karekok_ondalik": 14.0712,
        "cift_mi": True,
    },
    199: {
        "sayi": 199,
        "karesi": 39601,
        "kupu": 7880599,
        "karekok_sade": "√199",
        "karekok_ondalik": 14.1067,
        "cift_mi": False,
    },
    200: {
        "sayi": 200,
        "karesi": 40000,
        "kupu": 8000000,
        "karekok_sade": "10√2",
        "karekok_ondalik": 14.1421,
        "cift_mi": True,
    },
    201: {
        "sayi": 201,
        "karesi": 40401,
        "kupu": 8120601,
        "karekok_sade": "√201",
        "karekok_ondalik": 14.1774,
        "cift_mi": False,
    },
    202: {
        "sayi": 202,
        "karesi": 40804,
        "kupu": 8242408,
        "karekok_sade": "√202",
        "karekok_ondalik": 14.2127,
        "cift_mi": True,
    },
    203: {
        "sayi": 203,
        "karesi": 41209,
        "kupu": 8365427,
        "karekok_sade": "√203",
        "karekok_ondalik": 14.2478,
        "cift_mi": False,
    },
    204: {
        "sayi": 204,
        "karesi": 41616,
        "kupu": 8489664,
        "karekok_sade": "2√51",
        "karekok_ondalik": 14.2829,
        "cift_mi": True,
    },
    205: {
        "sayi": 205,
        "karesi": 42025,
        "kupu": 8615125,
        "karekok_sade": "√205",
        "karekok_ondalik": 14.3178,
        "cift_mi": False,
    },
    206: {
        "sayi": 206,
        "karesi": 42436,
        "kupu": 8741816,
        "karekok_sade": "√206",
        "karekok_ondalik": 14.3527,
        "cift_mi": True,
    },
    207: {
        "sayi": 207,
        "karesi": 42849,
        "kupu": 8869743,
        "karekok_sade": "3√23",
        "karekok_ondalik": 14.3875,
        "cift_mi": False,
    },
    208: {
        "sayi": 208,
        "karesi": 43264,
        "kupu": 8998912,
        "karekok_sade": "4√13",
        "karekok_ondalik": 14.4222,
        "cift_mi": True,
    },
    209: {
        "sayi": 209,
        "karesi": 43681,
        "kupu": 9129329,
        "karekok_sade": "√209",
        "karekok_ondalik": 14.4568,
        "cift_mi": False,
    },
    210: {
        "sayi": 210,
        "karesi": 44100,
        "kupu": 9261000,
        "karekok_sade": "√210",
        "karekok_ondalik": 14.4914,
        "cift_mi": True,
    },
    211: {
        "sayi": 211,
        "karesi": 44521,
        "kupu": 9393931,
        "karekok_sade": "√211",
        "karekok_ondalik": 14.5258,
        "cift_mi": False,
    },
    212: {
        "sayi": 212,
        "karesi": 44944,
        "kupu": 9528128,
        "karekok_sade": "2√53",
        "karekok_ondalik": 14.5602,
        "cift_mi": True,
    },
    213: {
        "sayi": 213,
        "karesi": 45369,
        "kupu": 9663597,
        "karekok_sade": "√213",
        "karekok_ondalik": 14.5945,
        "cift_mi": False,
    },
    214: {
        "sayi": 214,
        "karesi": 45796,
        "kupu": 9800344,
        "karekok_sade": "√214",
        "karekok_ondalik": 14.6287,
        "cift_mi": True,
    },
    215: {
        "sayi": 215,
        "karesi": 46225,
        "kupu": 9938375,
        "karekok_sade": "√215",
        "karekok_ondalik": 14.6629,
        "cift_mi": False,
    },
    216: {
        "sayi": 216,
        "karesi": 46656,
        "kupu": 10077696,
        "karekok_sade": "6√6",
        "karekok_ondalik": 14.6969,
        "cift_mi": True,
    },
    217: {
        "sayi": 217,
        "karesi": 47089,
        "kupu": 10218313,
        "karekok_sade": "√217",
        "karekok_ondalik": 14.7309,
        "cift_mi": False,
    },
    218: {
        "sayi": 218,
        "karesi": 47524,
        "kupu": 10360232,
        "karekok_sade": "√218",
        "karekok_ondalik": 14.7648,
        "cift_mi": True,
    },
    219: {
        "sayi": 219,
        "karesi": 47961,
        "kupu": 10503459,
        "karekok_sade": "√219",
        "karekok_ondalik": 14.7986,
        "cift_mi": False,
    },
    220: {
        "sayi": 220,
        "karesi": 48400,
        "kupu": 10648000,
        "karekok_sade": "2√55",
        "karekok_ondalik": 14.8324,
        "cift_mi": True,
    },
    221: {
        "sayi": 221,
        "karesi": 48841,
        "kupu": 10793861,
        "karekok_sade": "√221",
        "karekok_ondalik": 14.8661,
        "cift_mi": False,
    },
    222: {
        "sayi": 222,
        "karesi": 49284,
        "kupu": 10941048,
        "karekok_sade": "√222",
        "karekok_ondalik": 14.8997,
        "cift_mi": True,
    },
    223: {
        "sayi": 223,
        "karesi": 49729,
        "kupu": 11089567,
        "karekok_sade": "√223",
        "karekok_ondalik": 14.9332,
        "cift_mi": False,
    },
    224: {
        "sayi": 224,
        "karesi": 50176,
        "kupu": 11239424,
        "karekok_sade": "4√14",
        "karekok_ondalik": 14.9666,
        "cift_mi": True,
    },
}


# ==============================================================================
# 3. GÜVENLİ AST İFADE HESAPLAYICI VE YARDIMCI FONKSİYONLAR
# ==============================================================================
def guvenli_ifade_hesapla(ifade: str):
    """eval() kullanmadan AST ile güvenli matematiksel ifade hesaplar."""
    temiz = ifade.replace("^", "**").replace("×", "*").replace("÷", "/").replace(",", ".")
    agac = ast.parse(temiz, mode="eval")

    def _degerlendir(dugum):
        if isinstance(dugum, ast.Expression):
            return _degerlendir(dugum.body)
        if isinstance(dugum, ast.Constant) and isinstance(dugum.value, (int, float)):
            return dugum.value
        if isinstance(dugum, ast.UnaryOp) and type(dugum.op) in _IZINLI_OPERATORLER:
            return _IZINLI_OPERATORLER[type(dugum.op)](_degerlendir(dugum.operand))
        if isinstance(dugum, ast.BinOp) and type(dugum.op) in _IZINLI_OPERATORLER:
            sol = _degerlendir(dugum.left)
            sag = _degerlendir(dugum.right)
            if isinstance(dugum.op, ast.Pow) and abs(sag) > 1000:
                raise ValueError("Üs çok büyük.")
            return _IZINLI_OPERATORLER[type(dugum.op)](sol, sag)
        raise ValueError("Desteklenmeyen ifade")

    return _degerlendir(agac)


def sayi_formatla(val) -> str:
    if isinstance(val, float) and val.is_integer():
        val = int(val)
    if isinstance(val, int):
        return f"{val:,}".replace(",", ".")
    return f"{val:,.4f}".rstrip("0").rstrip(".").replace(",", "X").replace(".", ",").replace("X", ".")


def karekok_sadelestir(n: int):
    if n < 0:
        return None
    if n == 0:
        return 0, 1
    disari = 1
    iceri = n
    carpan = 2
    while carpan * carpan <= iceri:
        while iceri % (carpan * carpan) == 0:
            disari *= carpan
            iceri //= carpan * carpan
        carpan += 1
    return disari, iceri


def asal_carpanlara_ayir(n: int):
    carpanlar = {}
    d = 2
    kalan = n
    while d * d <= kalan:
        while kalan % d == 0:
            carpanlar[d] = carpanlar.get(d, 0) + 1
            kalan //= d
        d += 1
    if kalan > 1:
        carpanlar[kalan] = carpanlar.get(kalan, 0) + 1
    return carpanlar


def ikinci_derece_denklem_coz(a_katsayi: float, b_katsayi: float, c_katsayi: float) -> str:
    if a_katsayi == 0:
        if b_katsayi == 0:
            return "⚠️ Geçersiz denklem (a ve b aynı anda 0 olamaz)."
        x = -c_katsayi / b_katsayi
        return f"📐 **1. Derece Denklem Çözümü:** `x = {sayi_formatla(x)}`"
    delta = (b_katsayi ** 2) - (4 * a_katsayi * c_katsayi)
    adim1 = f"1. **Diskriminant (Δ):** `Δ = b² - 4ac = ({b_katsayi})² - 4·({a_katsayi})·({c_katsayi}) = {sayi_formatla(delta)}`"
    vieta = f"• **Kökler Toplamı (`-b/a`):** `{sayi_formatla(-b_katsayi / a_katsayi)}` | **Kökler Çarpımı (`c/a`):** `{sayi_formatla(c_katsayi / a_katsayi)}`"
    if delta < 0:
        reel = -b_katsayi / (2 * a_katsayi)
        sanal = math.sqrt(abs(delta)) / (2 * a_katsayi)
        return (
            f"📐 **2. Derece Denklem:**\n{adim1}\n"
            f"2. **Sonuç (`Δ < 0`):** Reel kök yoktur. Karmaşık kökler: **`{sayi_formatla(reel)} ± {sayi_formatla(sanal)}i`**\n{vieta}"
        )
    if delta == 0:
        x_tek = -b_katsayi / (2 * a_katsayi)
        return f"📐 **2. Derece Denklem:**\n{adim1}\n2. **Çakışık Kök (`Δ = 0`):** **`x₁ = x₂ = {sayi_formatla(x_tek)}`**\n{vieta}"
    kok_delta = math.sqrt(delta)
    x1 = (-b_katsayi + kok_delta) / (2 * a_katsayi)
    x2 = (-b_katsayi - kok_delta) / (2 * a_katsayi)
    return (
        f"📐 **2. Derece Denklem Çözümü:**\n"
        f"{adim1}\n"
        f"2. **Kökler (`x = (-b ± √Δ) / 2a`):** **`x₁ = {sayi_formatla(x1)}`** ve **`x₂ = {sayi_formatla(x2)}`**\n"
        f"{vieta}"
    )


def pisagor_hesapla(dik_kenar1: float, dik_kenar2: float) -> str:
    hipotenus = math.sqrt(dik_kenar1 ** 2 + dik_kenar2 ** 2)
    alan = (dik_kenar1 * dik_kenar2) / 2
    cevre = dik_kenar1 + dik_kenar2 + hipotenus
    return (
        f"📐 **Dik Üçgen & Pisagor Analizi:**\n"
        f"* **Hipotenüs (`c = √(a² + b²)`):** **`{sayi_formatla(hipotenus)}`**\n"
        f"* **Üçgenin Alanı:** **`{sayi_formatla(alan)}`** | **Çevresi:** **`{sayi_formatla(cevre)}`**"
    )


def polinom_turev_al(ifade: str) -> str:
    """Basit polinom ifadelerinin (ör: 3x^2 + 5x - 7) adım adım türevini alır."""
    temiz = ifade.replace(" ", "").replace("-", "+-")
    terimler = [t for t in temiz.split("+") if t]
    sonuc_terimler = []
    adimlar = []
    for t in terimler:
        m = re.fullmatch(r"([+-]?\d*(?:\.\d+)?)x(?:\^([+-]?\d+))?", t)
        if m:
            kats_str = m.group(1)
            kats = 1.0 if kats_str in ("", "+") else (-1.0 if kats_str == "-" else float(kats_str))
            us = int(m.group(2)) if m.group(2) else 1
            yeni_kats = kats * us
            yeni_us = us - 1
            adimlar.append(f"`({t})' = {sayi_formatla(kats)}·{us}·x^{yeni_us}`")
            if yeni_us == 0:
                sonuc_terimler.append(sayi_formatla(yeni_kats))
            elif yeni_us == 1:
                sonuc_terimler.append(f"{sayi_formatla(yeni_kats)}x")
            else:
                sonuc_terimler.append(f"{sayi_formatla(yeni_kats)}x^{yeni_us}")
        elif re.fullmatch(r"[+-]?\d+(?:\.\d+)?", t):
            adimlar.append(f"`({t})' = 0` (Sabit terim)")
    if not sonuc_terimler:
        return "∫ **Türev Sonucu:** `f'(x) = 0`"
    birlesik = " + ".join(sonuc_terimler).replace("+ -", "- ")
    return f"📈 **Türev Adımları:** {', '.join(adimlar)}\n**Sonuç:** **`f'(x) = {birlesik}`**"


def polinom_integral_al(ifade: str) -> str:
    """Basit polinom ifadelerinin (ör: 3x^2 + 2x - 5) adım adım belirsiz integralini alır."""
    temiz = ifade.replace(" ", "").replace("-", "+-")
    terimler = [t for t in temiz.split("+") if t]
    sonuc_terimler = []
    adimlar = []
    for t in terimler:
        m = re.fullmatch(r"([+-]?\d*(?:\.\d+)?)x(?:\^([+-]?\d+))?", t)
        if m:
            kats_str = m.group(1)
            kats = 1.0 if kats_str in ("", "+") else (-1.0 if kats_str == "-" else float(kats_str))
            us = int(m.group(2)) if m.group(2) else 1
            yeni_us = us + 1
            if yeni_us == 0:
                sonuc_terimler.append(f"{sayi_formatla(kats)}·ln|x|")
            else:
                yeni_kats = kats / yeni_us
                adimlar.append(f"`∫{t} dx = ({sayi_formatla(kats)}/{yeni_us})x^{yeni_us}`")
                sonuc_terimler.append(f"{sayi_formatla(yeni_kats)}x^{yeni_us}")
        elif re.fullmatch(r"[+-]?\d+(?:\.\d+)?", t):
            kats = float(t)
            adimlar.append(f"`∫{t} dx = {sayi_formatla(kats)}x`")
            sonuc_terimler.append(f"{sayi_formatla(kats)}x")
    if not sonuc_terimler:
        return "∫ **İntegral Sonucu:** `C`"
    birlesik = " + ".join(sonuc_terimler).replace("+ -", "- ")
    return f"∫ **İntegral Adımları:** {', '.join(adimlar)}\n**Sonuç:** **`{birlesik} + C`**"


# ==============================================================================
# 4. ANA DOĞAL DİL MATEMATİK MOTORU (DERİNLEMESİNE ÇÖZÜCÜ)
# ==============================================================================
_OZEL_TRIG_TABLO = {
    ("sin", 0): "0", ("sin", 30): "1/2", ("sin", 45): "√2/2", ("sin", 60): "√3/2", ("sin", 90): "1",
    ("sin", 180): "0", ("sin", 270): "-1", ("sin", 360): "0",
    ("cos", 0): "1", ("cos", 30): "√3/2", ("cos", 45): "√2/2", ("cos", 60): "1/2", ("cos", 90): "0",
    ("cos", 180): "-1", ("cos", 270): "0", ("cos", 360): "1",
    ("tan", 0): "0", ("tan", 30): "√3/3", ("tan", 45): "1", ("tan", 60): "√3", ("tan", 90): "Tanımsız",
    ("cot", 0): "Tanımsız", ("cot", 30): "√3", ("cot", 45): "1", ("cot", 60): "√3/3", ("cot", 90): "0",
}


def matematik_motoru_calistir(user_text: str):
    """Dört işlem, köklü/üslü, 1. & 2. derece denklem, trigonometri, logaritma, permütasyon/kombinasyon, türev/integral çözer."""
    user_text = user_text.strip()
    _ut_low = user_text.lower()
    user_text = _ut_low
    # 0) Türev & İntegral
    turev_eslesme = re.search(r"(?:türev|turev)\s*[:\-]?\s*([0-9xX+\-*/^.,\s]+)", user_text)
    if turev_eslesme:
        ifade = turev_eslesme.group(1).replace("X", "x").strip()
        if any(c.isdigit() or c == "x" for c in ifade):
            return polinom_turev_al(ifade), "Türev Çözümü"

    integral_eslesme = re.search(r"(?:integral)\s*[:\-]?\s*([0-9xX+\-*/^.,\s]+)", user_text)
    if integral_eslesme:
        ifade = integral_eslesme.group(1).replace("X", "x").strip()
        if any(c.isdigit() or c == "x" for c in ifade):
            return polinom_integral_al(ifade), "İntegral Çözümü"

    # 0.1) EBOB & EKOK Hesaplayıcı (ebob 24 36, ekok 12 18)
    ebob_eslesme = re.search(r"\b(ebob|ekok)\s*[:\(]?\s*(\d+)(?:\s*[,;\s]+\s*(\d+))+", user_text)
    if ebob_eslesme:
        sayilar = [int(x) for x in re.findall(r"\d+", user_text[ebob_eslesme.start():])]
        if len(sayilar) >= 2:
            tur = ebob_eslesme.group(1).lower()
            if tur == "ebob":
                sonuc = sayilar[0]
                for s in sayilar[1:]:
                    sonuc = math.gcd(sonuc, s)
                return f"🔢 **EBOB Çözümü:** `EBOB({', '.join(map(str, sayilar))})` = **{sonuc}**", "EBOB Hesaplama"
            sonuc = sayilar[0]
            for s in sayilar[1:]:
                sonuc = math.lcm(sonuc, s)
            return f"🔢 **EKOK Çözümü:** `EKOK({', '.join(map(str, sayilar))})` = **{sonuc}**", "EKOK Hesaplama"

    # 0.12) İstatistik Motoru (ortalama / medyan / standart sapma 10 20 30 40)
    if any(k in user_text for k in ["istatistik", "ortalama", "medyan", "standart sapma", "varyans"]):
        sayilar = [float(x.replace(",", ".")) for x in re.findall(r"-?\d+(?:[.,]\d+)?", user_text)]
        if len(sayilar) >= 2:
            n_s = len(sayilar)
            ort = sum(sayilar) / n_s
            sirali = sorted(sayilar)
            medyan = sirali[n_s // 2] if n_s % 2 == 1 else (sirali[n_s // 2 - 1] + sirali[n_s // 2]) / 2
            varyans = sum((x - ort) ** 2 for x in sayilar) / n_s
            std_sapma = math.sqrt(varyans)
            return (
                f"📊 **İstatistik Analizi ({n_s} Veri):**\n"
                f"• **Veriler:** `{', '.join(sayi_formatla(s) for s in sirali)}`\n"
                f"• **Aritmetik Ortalama:** `{sayi_formatla(ort)}`\n"
                f"• **Medyan (Ortanca):** `{sayi_formatla(medyan)}`\n"
                f"• **Varyans:** `{sayi_formatla(varyans)}` | **Standart Sapma (σ):** `{sayi_formatla(std_sapma)}`",
                "İstatistik Çözümü",
            )

    # 0.14) 2x2 Determinant Hesaplayıcı (determinant 1 2 3 4)
    if "determinant" in user_text or user_text.startswith("det "):
        sayilar = [float(x.replace(",", ".")) for x in re.findall(r"-?\d+(?:[.,]\d+)?", user_text)]
        if len(sayilar) == 4:
            a, b, c, d = sayilar
            det = a * d - b * c
            return (
                f"🧮 **2×2 Matris Determinantı:**\n"
                f"`| {sayi_formatla(a)}  {sayi_formatla(b)} |`\n"
                f"`| {sayi_formatla(c)}  {sayi_formatla(d)} |`\n"
                f"• Formül: `({sayi_formatla(a)}·{sayi_formatla(d)}) - ({sayi_formatla(b)}·{sayi_formatla(c)})` = **`{sayi_formatla(det)}`**",
                "Determinant 2×2",
            )

    # 0.16) Geometri Alan & Hacim Hesaplayıcı (daire alan 5, küre hacim 3, silindir hacim 4 10)
    if any(k in user_text for k in ["daire alan", "daire cevre", "daire çevre", "kure hacim", "küre hacim", "kure alan", "küre alan", "silindir hacim"]):
        sayilar = [float(x.replace(",", ".")) for x in re.findall(r"\d+(?:[.,]\d+)?", user_text)]
        if sayilar:
            r = sayilar[0]
            if "daire alan" in user_text:
                return f"📐 **Daire Alanı (`r = {sayi_formatla(r)}`):** `π · r²` ≈ **{sayi_formatla(math.pi * r * r)}** (`{sayi_formatla(r*r)}π`)", "Geometri: Daire Alanı"
            if "daire cevre" in user_text or "daire çevre" in user_text:
                return f"📐 **Daire Çevresi (`r = {sayi_formatla(r)}`):** `2 · π · r` ≈ **{sayi_formatla(2 * math.pi * r)}** (`{sayi_formatla(2*r)}π`)", "Geometri: Daire Çevresi"
            if "kure hacim" in user_text or "küre hacim" in user_text:
                return f"🌐 **Küre Hacmi (`r = {sayi_formatla(r)}`):** `(4/3) · π · r³` ≈ **{sayi_formatla((4/3) * math.pi * (r**3))}**", "Geometri: Küre Hacmi"
            if "kure alan" in user_text or "küre alan" in user_text:
                return f"🌐 **Küre Yüzey Alanı (`r = {sayi_formatla(r)}`):** `4 · π · r²` ≈ **{sayi_formatla(4 * math.pi * r * r)}**", "Geometri: Küre Alanı"
            if "silindir hacim" in user_text and len(sayilar) >= 2:
                h = sayilar[1]
                return f"🛢️ **Silindir Hacmi (`r = {sayi_formatla(r)}, h = {sayi_formatla(h)}`):** `π · r² · h` ≈ **{sayi_formatla(math.pi * r * r * h)}**", "Geometri: Silindir Hacmi"

    # 0.2) Trigonometri (sin 30, cos 60, tan 45, cot 30)
    trig_eslesme = re.search(r"\b(sin|cos|tan|cot)\s*\(?\s*(-?\d+(?:[.,]\d+)?)\s*°?\)?", user_text)
    if trig_eslesme:
        fonk = trig_eslesme.group(1)
        aci_deg = float(trig_eslesme.group(2).replace(",", "."))
        rad = math.radians(aci_deg)
        kesin = _OZEL_TRIG_TABLO.get((fonk, int(aci_deg) % 360)) if aci_deg.is_integer() else None
        if fonk == "sin":
            val = math.sin(rad)
        elif fonk == "cos":
            val = math.cos(rad)
        elif fonk == "tan":
            if abs(math.cos(rad)) < 1e-12:
                return f"📊 **Trigonometri:** `tan({sayi_formatla(aci_deg)}°)` = **Tanımsız** (`cos = 0`)", "Trigonometri"
            val = math.tan(rad)
        else:
            if abs(math.sin(rad)) < 1e-12:
                return f"📊 **Trigonometri:** `cot({sayi_formatla(aci_deg)}°)` = **Tanımsız** (`sin = 0`)", "Trigonometri"
            val = 1.0 / math.tan(rad)
        kesin_not = f" | Kesin Değer: **`{kesin}`**" if kesin else ""
        return (
            f"📊 **Trigonometri Çözümü:** `{fonk}({sayi_formatla(aci_deg)}°)` = **{val:.4f}**{kesin_not}\n"
            f"💡 *Radyan:* `{rad:.4f} rad`",
            f"Trigonometri: {fonk}",
        )

    # 0.3) Logaritma (log 100, log2 8, ln 10)
    log_taban_eslesme = re.search(r"\blog_?(\d+(?:[.,]\d+)?)\s*\(?\s*(\d+(?:[.,]\d+)?)\)?", user_text)
    if log_taban_eslesme:
        taban = float(log_taban_eslesme.group(1).replace(",", "."))
        sayi = float(log_taban_eslesme.group(2).replace(",", "."))
        if taban <= 0 or taban == 1 or sayi <= 0:
            return "⚠️ Logaritmada taban `> 0, ≠ 1` ve sayı `> 0` olmalıdır!", "Logaritma Hatası"
        sonuc = math.log(sayi, taban)
        return (
            f"📉 **Logaritma Çözümü:** `log_{sayi_formatla(taban)}({sayi_formatla(sayi)})` = **{sayi_formatla(sonuc)}**\n"
            f"💡 *Kontrol:* `{sayi_formatla(taban)}^{sayi_formatla(sonuc)} = {sayi_formatla(sayi)}`",
            "Logaritma",
        )
    log_on_eslesme = re.search(r"\b(log|ln)\s*\(?\s*(\d+(?:[.,]\d+)?)\)?", user_text)
    if log_on_eslesme:
        tur = log_on_eslesme.group(1)
        sayi = float(log_on_eslesme.group(2).replace(",", "."))
        if sayi <= 0:
            return "⚠️ Logaritması alınacak sayı pozitif olmalıdır!", "Logaritma Hatası"
        if tur == "log":
            return f"📉 **10 Tabanında Logaritma:** `log₁₀({sayi_formatla(sayi)})` = **{sayi_formatla(math.log10(sayi))}**", "Logaritma"
        return f"📉 **Doğal Logaritma:** `ln({sayi_formatla(sayi)})` = **{sayi_formatla(math.log(sayi))}**", "Doğal Logaritma"

    # 0.4) Permütasyon & Kombinasyon (C(6,2), P(5,2))
    pk_eslesme = re.search(r"\b([cp])\s*\(\s*(\d+)\s*[,;]\s*(\d+)\s*\)", user_text)
    if pk_eslesme:
        tur, n, r = pk_eslesme.group(1).upper(), int(pk_eslesme.group(2)), int(pk_eslesme.group(3))
        if r > n or n > 100:
            return "⚠️ Geçersiz aralık (`0 ≤ r ≤ n ≤ 100` olmalı).", "Sayma Hatası"
        if tur == "C":
            val = math.comb(n, r)
            return (
                f"🎲 **Kombinasyon `C({n}, {r})`:**\n"
                f"1. Formül: `{n}! / ({r}! · ({n}-{r})!)`\n"
                f"2. Sonuç: **`{sayi_formatla(val)}`**",
                f"Kombinasyon C({n},{r})",
            )
        val = math.perm(n, r)
        return (
            f"🎲 **Permütasyon `P({n}, {r})`:**\n"
            f"1. Formül: `{n}! / ({n}-{r})!`\n"
            f"2. Sonuç: **`{sayi_formatla(val)}`**",
            f"Permütasyon P({n},{r})",
        )

    # 0.5) 2. Dereceden Denklem ("x^2 - 5x + 6 = 0", "2x^2 + 3x - 2 = 0")
    ikinci_der = re.search(
        r"([+-]?\s*\d*)\s*x\^2\s*([+-]\s*\d*\s*x)?\s*([+-]\s*\d+)?\s*=\s*([+-]?\s*\d+)",
        user_text.replace(" ", ""),
    )
    if ikinci_der and "x^2" in user_text.replace(" ", ""):
        a_s = ikinci_der.group(1)
        a_v = 1.0 if a_s in ("", "+") else (-1.0 if a_s == "-" else float(a_s))
        b_v = 0.0
        if ikinci_der.group(2):
            b_s = ikinci_der.group(2).replace("x", "")
            b_v = 1.0 if b_s in ("", "+") else (-1.0 if b_s == "-" else float(b_s))
        c_sol = float(ikinci_der.group(3)) if ikinci_der.group(3) else 0.0
        c_sag = float(ikinci_der.group(4))
        return ikinci_derece_denklem_coz(a_v, b_v, c_sol - c_sag), "2. Derece Denklem"

    # 1) Karekök / Köklü Sayı
    kok_eslesme = re.search(r"(?:karekök|karekok|kök|kok|√)\s*(\d+)", user_text)
    if kok_eslesme:
        n = int(kok_eslesme.group(1))
        disari, iceri = karekok_sadelestir(n)
        yaklasik = math.sqrt(n)
        if iceri == 1:
            return (
                f"√ **Köklü Sayı Çözümü:** `√{n}` = **{disari}** (Tam kare sayı! Çünkü `{disari} × {disari} = {n}`)",
                f"Karekök: √{n}",
            )
        if disari == 1:
            return (
                f"√ **Köklü Sayı Çözümü:** `√{n}` kök dışına çıkmaz (`a√b` hali: **`√{n}`**), yaklaşık değeri **`{yaklasik:.4f}`**",
                f"Karekök: √{n}",
            )
        return (
            f"√ **Köklü Sayı Çözümü:** `√{n}` = `√({disari**2} × {iceri})` = **`{disari}√{iceri}`** (Yaklaşık: `{yaklasik:.4f}`)",
            f"Karekök: √{n}",
        )

    # 2) Faktöriyel
    fak_eslesme = re.search(r"(\d+)\s*(?:!|faktöriyel|faktoriyel)", user_text)
    if fak_eslesme:
        n = int(fak_eslesme.group(1))
        if n > 100:
            return "⚠️ Çok büyük faktöriyel! Lütfen 0 ile 100 arasında bir sayı gir.", "Matematik Sınırı"
        return f"❗ **Faktöriyel:** `{n}!` = **{sayi_formatla(math.factorial(n))}**", f"Faktöriyel: {n}!"

    # 3) EBOB / EKOK
    ebob_ekok = re.search(r"\b(ebob|ekok)\b[^\d]*(\d+)[^\d]+(\d+)", user_text)
    if ebob_ekok:
        tur, s1, s2 = ebob_ekok.group(1), int(ebob_ekok.group(2)), int(ebob_ekok.group(3))
        ebob_val = math.gcd(s1, s2)
        ekok_val = abs(s1 * s2) // ebob_val if s1 and s2 else 0
        if tur == "ebob":
            return f"🔢 **EBOB({s1}, {s2})** = **{ebob_val}** (EKOK: `{ekok_val}`)", f"EBOB({s1},{s2})"
        return f"🔢 **EKOK({s1}, {s2})** = **{ekok_val}** (EBOB: `{ebob_val}`)", f"EKOK({s1},{s2})"

    # 4) Asal Sayı / Asal Çarpanlar
    asal_eslesme = re.search(r"(\d+)\s*(?:asal mı|asal mi|asal çarpan|asal carpan)", user_text)
    if asal_eslesme:
        n = int(asal_eslesme.group(1))
        if n < 2:
            return f"ℹ️ `{n}` asal sayı değildir.", f"Asal Kontrolü: {n}"
        carpanlar = asal_carpanlara_ayir(n)
        if len(carpanlar) == 1 and list(carpanlar.values())[0] == 1:
            return f"✅ **`{n}` bir ASAL sayıdır!**", f"Asal: {n}"
        gosterim = " × ".join(f"{k}^{v}" if v > 1 else str(k) for k, v in carpanlar.items())
        return f"🧩 **`{n}` asal değildir.** Asal çarpanları: **`{gosterim}`**", f"Asal Çarpan: {n}"

    # 5) 1. Dereceden Denklem
    denklem_eslesme = re.search(r"([+-]?\s*\d*)\s*x\s*([+-]\s*\d+)?\s*=\s*([+-]?\s*\d+)", user_text.replace(" ", ""))
    if denklem_eslesme and "=" in user_text:
        a_str = denklem_eslesme.group(1)
        a_val = 1 if a_str in ("", "+") else (-1 if a_str == "-" else int(a_str))
        b_val = int(denklem_eslesme.group(2)) if denklem_eslesme.group(2) else 0
        c_val = int(denklem_eslesme.group(3))
        if a_val == 0:
            return "⚠️ `x` katsayısı 0 olamaz.", "Denklem Hatası"
        x_val = (c_val - b_val) / a_val
        return (
            f"📐 **Denklem Çözümü:** `{user_text}`\n"
            f"1. Adım: `{a_val}x = {c_val} - ({b_val})` → `{a_val}x = {c_val - b_val}`\n"
            f"2. Adım: `x = {c_val - b_val} / {a_val}` → **`x = {sayi_formatla(x_val)}`**",
            "Denklem Çözümü",
        )

    # 6) Yüzde Hesaplama
    yuzde1 = re.search(r"(\d+(?:[.,]\d+)?)\s*(?:'?[uüıi]n)?\s*%\s*(\d+(?:[.,]\d+)?)", user_text)
    yuzde2 = re.search(r"%\s*(\d+(?:[.,]\d+)?)\s*(?:si|sı|su|sü)?\s*(\d+(?:[.,]\d+)?)", user_text)
    if yuzde1:
        ana, oran = float(yuzde1.group(1).replace(",", ".")), float(yuzde1.group(2).replace(",", "."))
        return f"💯 **Yüzde Hesabı:** `{sayi_formatla(ana)}` sayısının `%{sayi_formatla(oran)}`'i = **{sayi_formatla(ana * oran / 100)}**", "Yüzde Hesabı"
    if yuzde2:
        oran, ana = float(yuzde2.group(1).replace(",", ".")), float(yuzde2.group(2).replace(",", "."))
        return f"💯 **Yüzde Hesabı:** `{sayi_formatla(ana)}` sayısının `%{sayi_formatla(oran)}`'i = **{sayi_formatla(ana * oran / 100)}**", "Yüzde Hesabı"

    # 7) Üslü Sayılar
    us_eslesme = re.search(r"(\d+(?:[.,]\d+)?)\s*(?:üzeri|uzeri|üssü|ussu|\^)\s*(-?\d+)", user_text)
    if us_eslesme:
        taban, us = float(us_eslesme.group(1).replace(",", ".")), int(us_eslesme.group(2))
        if abs(us) > 200:
            return "⚠️ Üs değeri çok büyük.", "Matematik Sınırı"
        return f"🔺 **Üslü Sayı:** `{sayi_formatla(taban)}^{us}` = **{sayi_formatla(taban ** us)}**", f"Üs: {taban}^{us}"

    kare_kup = re.search(r"(\d+(?:[.,]\d+)?)\s*(?:'?[ıiuü]n)?\s*(karesi|küpü|kupu)", user_text)
    if kare_kup:
        taban = float(kare_kup.group(1).replace(",", "."))
        us = 2 if "kare" in kare_kup.group(2) else 3
        return f"🔺 **Üslü Sayı:** `{sayi_formatla(taban)}^{us}` = **{sayi_formatla(taban ** us)}**", f"Üs: {taban}^{us}"

    # 8-A) Türkçe Sonda Fiilli Dört İşlem
    sonda_op = re.search(
        r"(-?\d+(?:[.,]\d+)?)(?:'?[a-zçğıöşü]+)?\s+(?:(?:ile|ve|den|dan|ten|tan)\s+)?(-?\d+(?:[.,]\d+)?)(?:'?[a-zçğıöşü]+)?\s+\b(çarp|carp|topla|böl|bol|çıkar|cikar)\b",
        user_text,
    )
    if sonda_op:
        s1 = float(sonda_op.group(1).replace(",", "."))
        s2 = float(sonda_op.group(2).replace(",", "."))
        fiil = sonda_op.group(3)
        if fiil in ("çarp", "carp"):
            return f"✖️ **Çarpma:** `{sayi_formatla(s1)} × {sayi_formatla(s2)}` = **{sayi_formatla(s1 * s2)}**", "Çarpma İşlemi"
        if fiil == "topla":
            return f"➕ **Toplama:** `{sayi_formatla(s1)} + {sayi_formatla(s2)}` = **{sayi_formatla(s1 + s2)}**", "Toplama İşlemi"
        if fiil in ("böl", "bol"):
            if s2 == 0:
                return "⚠️ Matematikte hiçbir sayı **0'a bölünemez** (Tanımsız)!", "Sıfıra Bölme"
            return f"➗ **Bölme:** `{sayi_formatla(s1)} ÷ {sayi_formatla(s2)}` = **{sayi_formatla(s1 / s2)}**", "Bölme İşlemi"
        if fiil in ("çıkar", "cikar"):
            return f"➖ **Çıkarma:** `{sayi_formatla(s1)} - {sayi_formatla(s2)}` = **{sayi_formatla(s1 - s2)}**", "Çıkarma İşlemi"

    # 8-B) Ortada Operatörlü Dört İşlem
    sozel_op = re.search(
        r"(-?\d+(?:[.,]\d+)?)\s*(?:ile)?\s*(çarpı|carpi|çarp|carp|kere|x|×|\*|bölü|bolu|böl|bol|/|÷|artı|arti|topla|\+|eksi|çıkar|cikar|-)\s*(-?\d+(?:[.,]\d+)?)",
        user_text,
    )
    if sozel_op:
        s1, op, s2 = float(sozel_op.group(1).replace(",", ".")), sozel_op.group(2), float(sozel_op.group(3).replace(",", "."))
        if op in ("çarpı", "carpi", "çarp", "carp", "kere", "x", "×", "*"):
            sonuc = s1 * s2
            ekstra = ""
            if s1.is_integer() and s2.is_integer() and 10 <= abs(s1) <= 999 and 10 <= abs(s2) <= 999:
                a_int, b_int = int(s1), int(s2)
                onluk, birlik = (b_int // 10) * 10, b_int % 10
                if birlik != 0:
                    ekstra = f"\n💡 *Zihinden Dağılma:* `({a_int} × {onluk}) + ({a_int} × {birlik}) = {sayi_formatla(a_int * onluk)} + {sayi_formatla(a_int * birlik)}`"
            return f"✖️ **Çarpma:** `{sayi_formatla(s1)} × {sayi_formatla(s2)}` = **{sayi_formatla(sonuc)}**{ekstra}", "Çarpma İşlemi"
        if op in ("böl", "bol", "bölü", "bolu", "/", "÷"):
            if s2 == 0:
                return "⚠️ Matematikte hiçbir sayı **0'a bölünemez** (Tanımsız)!", "Sıfıra Bölme"
            return f"➗ **Bölme:** `{sayi_formatla(s1)} ÷ {sayi_formatla(s2)}` = **{sayi_formatla(s1 / s2)}**", "Bölme İşlemi"
        if op in ("artı", "arti", "topla", "+"):
            return f"➕ **Toplama:** `{sayi_formatla(s1)} + {sayi_formatla(s2)}` = **{sayi_formatla(s1 + s2)}**", "Toplama İşlemi"
        if op in ("eksi", "çıkar", "cikar", "-"):
            return f"➖ **Çıkarma:** `{sayi_formatla(s1)} - {sayi_formatla(s2)}` = **{sayi_formatla(s1 - s2)}**", "Çıkarma İşlemi"

    # 9) Karmaşık İfade
    temiz_ifade = re.sub(r"\b(kaçtır|kactir|kaç|kac|eder|eşittir|esittir|sonucu|nedir)\b|[?=]", "", user_text).strip()
    if re.fullmatch(r"[\d\s+\-*/().^×÷,%]+", temiz_ifade) and any(op in temiz_ifade for op in "+-*/^×÷"):
        try:
            return f"⚡ **Hesap Motoru:** `{user_text}` = **{sayi_formatla(guvenli_ifade_hesapla(temiz_ifade))}**", "Karma İşlem"
        except ZeroDivisionError:
            return "⚠️ İşlemde sıfıra bölme hatası var!", "Sıfıra Bölme"
        except Exception:
            pass

    return None, None


# ==============================================================================
# 5. ÇEŞİTLİ KONULU ÇÖZÜMLÜ SORU BANKASI (40 ÖZGÜN PROBLEM)
# ==============================================================================
COZUMLU_SORU_BANKASI = [
    {
        "no": 1,
        "konu": 'Köklü Sayılar',
        "soru": '`√27 + √12` işleminin en sade sonucu nedir?',
        "cozum": '`√27 = 3√3` ve `√12 = 2√3` olduğundan `3√3 + 2√3 = 5√3` bulunur.',
        "cevap": '5√3',
    },
    {
        "no": 2,
        "konu": 'Köklü Sayılar',
        "soru": '`√72 - √18` işleminin sonucu kaçtır?',
        "cozum": '`√72 = 6√2` ve `√18 = 3√2` olduğundan `6√2 - 3√2 = 3√2`.',
        "cevap": '3√2',
    },
    {
        "no": 3,
        "konu": 'Köklü Sayılar',
        "soru": '`12 / √3` kesrinin rasyonel paydalı hali nedir?',
        "cozum": 'Pay ve payda `√3` ile çarpılır: `12√3 / 3 = 4√3`.',
        "cevap": '4√3',
    },
    {
        "no": 4,
        "konu": 'Köklü Sayılar',
        "soru": '`√128 + √50` işleminin sonucu nedir?',
        "cozum": '`√128 = 8√2` ve `√50 = 5√2` olduğundan `13√2` bulunur.',
        "cevap": '13√2',
    },
    {
        "no": 5,
        "konu": '1. Derece Denklemler',
        "soru": '`4x + 5 = 21` denkleminde `x` kaçtır?',
        "cozum": '`4x = 21 - 5 = 16` → `x = 4`.',
        "cevap": '4',
    },
    {
        "no": 6,
        "konu": '1. Derece Denklemler',
        "soru": '`3(x - 2) = 15` denkleminde `x` kaçtır?',
        "cozum": '`x - 2 = 5` → `x = 7`.',
        "cevap": '7',
    },
    {
        "no": 7,
        "konu": '1. Derece Denklemler',
        "soru": '`5x - 7 = 2x + 11` denkleminde `x` kaçtır?',
        "cozum": '`3x = 18` → `x = 6`.',
        "cevap": '6',
    },
    {
        "no": 8,
        "konu": '2. Derece Denklemler',
        "soru": '`x² - 5x + 6 = 0` denkleminin kökler toplamı kaçtır?',
        "cozum": 'Vieta formülü ile `-b/a = -(-5)/1 = 5` (Kökler 2 ve 3).',
        "cevap": '5',
    },
    {
        "no": 9,
        "konu": '2. Derece Denklemler',
        "soru": '`x² - 9 = 0` denkleminin pozitif kökü kaçtır?',
        "cozum": '`(x - 3)(x + 3) = 0` → Pozitif kök `3`.',
        "cevap": '3',
    },
    {
        "no": 10,
        "konu": '2. Derece Denklemler',
        "soru": '`x² - 6x + 9 = 0` denkleminin çakışık kökü kaçtır?',
        "cozum": '`(x - 3)² = 0` olduğundan `x = 3`.',
        "cevap": '3',
    },
    {
        "no": 11,
        "konu": 'Üslü Sayılar',
        "soru": '`2^5 × 2^3` işleminin değeri kaçtır?',
        "cozum": '`2^(5+3) = 2^8 = 256`.',
        "cevap": '256',
    },
    {
        "no": 12,
        "konu": 'Üslü Sayılar',
        "soru": '`(3^2)^2` işleminin sonucu kaçtır?',
        "cozum": 'Üssün üssü çarpılır: `3^(2×2) = 3^4 = 81`.',
        "cevap": '81',
    },
    {
        "no": 13,
        "konu": 'Üslü Sayılar',
        "soru": '`5^4 / 5^2` işleminin sonucu kaçtır?',
        "cozum": '`5^(4-2) = 5^2 = 25`.',
        "cevap": '25',
    },
    {
        "no": 14,
        "konu": 'EBOB - EKOK',
        "soru": "`24` ve `36` sayılarının EBOB'u kaçtır?",
        "cozum": 'En büyük ortak bölen `12` dir.',
        "cevap": '12',
    },
    {
        "no": 15,
        "konu": 'EBOB - EKOK',
        "soru": "`12` ve `15` sayılarının EKOK'u kaçtır?",
        "cozum": '`12 = 2²×3`, `15 = 3×5` → `EKOK = 4×3×5 = 60`.',
        "cevap": '60',
    },
    {
        "no": 16,
        "konu": 'Trigonometri',
        "soru": '`sin 30° + cos 60°` toplamı kaçtır?',
        "cozum": '`sin 30° = 1/2` ve `cos 60° = 1/2` olduğundan `1/2 + 1/2 = 1`.',
        "cevap": '1',
    },
    {
        "no": 17,
        "konu": 'Trigonometri',
        "soru": '`tan 45° + cot 45°` toplamı kaçtır?',
        "cozum": '`tan 45° = 1` ve `cot 45° = 1` olduğundan `1 + 1 = 2`.',
        "cevap": '2',
    },
    {
        "no": 18,
        "konu": 'Trigonometri',
        "soru": '`sin²(37°) + cos²(37°)` işleminin sonucu kaçtır?',
        "cozum": 'Temel trigonometrik özdeşlik gereği her `θ` için `sin²θ + cos²θ = 1` dir.',
        "cevap": '1',
    },
    {
        "no": 19,
        "konu": 'Logaritma',
        "soru": '`log₂(8)` değeri kaçtır?',
        "cozum": '`8 = 2³` olduğundan `log₂(2³) = 3`.',
        "cevap": '3',
    },
    {
        "no": 20,
        "konu": 'Logaritma',
        "soru": '`log₁₀(1000)` değeri kaçtır?',
        "cozum": '`1000 = 10³` olduğundan `log₁₀(10³) = 3`.',
        "cevap": '3',
    },
    {
        "no": 21,
        "konu": 'Logaritma',
        "soru": '`ln(e²)` değeri kaçtır?',
        "cozum": '`ln(e²) = 2 · ln(e) = 2 · 1 = 2`.',
        "cevap": '2',
    },
    {
        "no": 22,
        "konu": 'Permütasyon & Kombinasyon',
        "soru": '`C(5, 2)` kombinasyonunun değeri kaçtır?',
        "cozum": '`5! / (2! · 3!) = (5 × 4) / 2 = 10`.',
        "cevap": '10',
    },
    {
        "no": 23,
        "konu": 'Permütasyon & Kombinasyon',
        "soru": '`P(4, 2)` permütasyonunun değeri kaçtır?',
        "cozum": '`4! / (4 - 2)! = 4 × 3 = 12`.',
        "cevap": '12',
    },
    {
        "no": 24,
        "konu": 'Permütasyon & Kombinasyon',
        "soru": '`5!` (5 faktöriyel) kaçtır?',
        "cozum": '`5 × 4 × 3 × 2 × 1 = 120`.',
        "cevap": '120',
    },
    {
        "no": 25,
        "konu": 'Polinomlar & Özdeşlikler',
        "soru": '`P(x) = x² - 3x + 5` ise `P(2)` kaçtır?',
        "cozum": '`2² - 3(2) + 5 = 4 - 6 + 5 = 3`.',
        "cevap": '3',
    },
    {
        "no": 26,
        "konu": 'Polinomlar & Özdeşlikler',
        "soru": '`25² - 15²` işleminin iki kare farkıyla sonucu kaçtır?',
        "cozum": '`(25 - 15)(25 + 15) = 10 × 40 = 400`.',
        "cevap": '400',
    },
    {
        "no": 27,
        "konu": 'Türev & İntegral',
        "soru": "`f(x) = 3x² + 4x - 5` fonksiyonunun `x = 1` noktasındaki türevi `f'(1)` kaçtır?",
        "cozum": "`f'(x) = 6x + 4` olduğundan `f'(1) = 6(1) + 4 = 10`.",
        "cevap": '10',
    },
    {
        "no": 28,
        "konu": 'Türev & İntegral',
        "soru": '`f(x) = x³` fonksiyonunun `x = 2` noktasındaki türevi kaçtır?',
        "cozum": "`f'(x) = 3x²` → `f'(2) = 3 × 4 = 12`.",
        "cevap": '12',
    },
    {
        "no": 29,
        "konu": 'Geometri & Pisagor',
        "soru": "Dik kenarları `6 cm` ve `8 cm` olan dik üçgenin hipotenüsü kaç cm'dir?",
        "cozum": '`√(6² + 8²) = √(36 + 64) = √100 = 10` cm.',
        "cevap": '10',
    },
    {
        "no": 30,
        "konu": 'Geometri & Pisagor',
        "soru": "Dik kenarları `5 cm` ve `12 cm` olan dik üçgenin hipotenüsü kaç cm'dir?",
        "cozum": '`5-12-13` özel üçgeninden hipotenüs `13` cm.',
        "cevap": '13',
    },
    {
        "no": 31,
        "konu": 'Zihinden Matematik',
        "soru": '`76 × 25` işleminin sonucu kaçtır?',
        "cozum": '`76 / 4 = 19` → yanına iki sıfır: `1900`.',
        "cevap": '1900',
    },
    {
        "no": 32,
        "konu": 'Zihinden Matematik',
        "soru": '`43 × 11` işleminin sonucu kaçtır?',
        "cozum": '`4` ile `3` arasına `4+3=7` yazılır → `473`.',
        "cevap": '473',
    },
    {
        "no": 33,
        "konu": '2. Derece Denklem',
        "soru": '`x² - 3x + 2 = 0` denkleminin köklerini bulunuz.',
        "cozum": 'Çarpanlara ayırma: `(x - (1))(x - (2)) = 0`. Diskriminant `Δ = (-3)² - 4·1·(2) = 1`.',
        "cevap": 'x₁ = 1, x₂ = 2',
    },
    {
        "no": 34,
        "konu": '2. Derece Denklem',
        "soru": '`x² - 5x + 4 = 0` denkleminin köklerini bulunuz.',
        "cozum": 'Çarpanlara ayırma: `(x - (1))(x - (4)) = 0`. Diskriminant `Δ = (-5)² - 4·1·(4) = 9`.',
        "cevap": 'x₁ = 1, x₂ = 4',
    },
    {
        "no": 35,
        "konu": '2. Derece Denklem',
        "soru": '`x² - 6x + 8 = 0` denkleminin köklerini bulunuz.',
        "cozum": 'Çarpanlara ayırma: `(x - (2))(x - (4)) = 0`. Diskriminant `Δ = (-6)² - 4·1·(8) = 4`.',
        "cevap": 'x₁ = 2, x₂ = 4',
    },
    {
        "no": 36,
        "konu": '2. Derece Denklem',
        "soru": '`x² - 7x + 10 = 0` denkleminin köklerini bulunuz.',
        "cozum": 'Çarpanlara ayırma: `(x - (2))(x - (5)) = 0`. Diskriminant `Δ = (-7)² - 4·1·(10) = 9`.',
        "cevap": 'x₁ = 2, x₂ = 5',
    },
    {
        "no": 37,
        "konu": '2. Derece Denklem',
        "soru": '`x² - 7x + 12 = 0` denkleminin köklerini bulunuz.',
        "cozum": 'Çarpanlara ayırma: `(x - (3))(x - (4)) = 0`. Diskriminant `Δ = (-7)² - 4·1·(12) = 1`.',
        "cevap": 'x₁ = 3, x₂ = 4',
    },
    {
        "no": 38,
        "konu": '2. Derece Denklem',
        "soru": '`x² - 8x + 15 = 0` denkleminin köklerini bulunuz.',
        "cozum": 'Çarpanlara ayırma: `(x - (3))(x - (5)) = 0`. Diskriminant `Δ = (-8)² - 4·1·(15) = 4`.',
        "cevap": 'x₁ = 3, x₂ = 5',
    },
    {
        "no": 39,
        "konu": '2. Derece Denklem',
        "soru": '`x² - 9x + 20 = 0` denkleminin köklerini bulunuz.',
        "cozum": 'Çarpanlara ayırma: `(x - (4))(x - (5)) = 0`. Diskriminant `Δ = (-9)² - 4·1·(20) = 1`.',
        "cevap": 'x₁ = 4, x₂ = 5',
    },
    {
        "no": 40,
        "konu": '2. Derece Denklem',
        "soru": '`x² - 7x + 6 = 0` denkleminin köklerini bulunuz.',
        "cozum": 'Çarpanlara ayırma: `(x - (1))(x - (6)) = 0`. Diskriminant `Δ = (-7)² - 4·1·(6) = 25`.',
        "cevap": 'x₁ = 1, x₂ = 6',
    },
    {
        "no": 41,
        "konu": '2. Derece Denklem',
        "soru": '`x² - 8x + 12 = 0` denkleminin köklerini bulunuz.',
        "cozum": 'Çarpanlara ayırma: `(x - (2))(x - (6)) = 0`. Diskriminant `Δ = (-8)² - 4·1·(12) = 16`.',
        "cevap": 'x₁ = 2, x₂ = 6',
    },
    {
        "no": 42,
        "konu": '2. Derece Denklem',
        "soru": '`x² - 9x + 18 = 0` denkleminin köklerini bulunuz.',
        "cozum": 'Çarpanlara ayırma: `(x - (3))(x - (6)) = 0`. Diskriminant `Δ = (-9)² - 4·1·(18) = 9`.',
        "cevap": 'x₁ = 3, x₂ = 6',
    },
    {
        "no": 43,
        "konu": '2. Derece Denklem',
        "soru": '`x² - 1x - 2 = 0` denkleminin köklerini bulunuz.',
        "cozum": 'Çarpanlara ayırma: `(x - (-1))(x - (2)) = 0`. Diskriminant `Δ = (-1)² - 4·1·(-2) = 9`.',
        "cevap": 'x₁ = -1, x₂ = 2',
    },
    {
        "no": 44,
        "konu": '2. Derece Denklem',
        "soru": '`x² - 1x - 6 = 0` denkleminin köklerini bulunuz.',
        "cozum": 'Çarpanlara ayırma: `(x - (-2))(x - (3)) = 0`. Diskriminant `Δ = (-1)² - 4·1·(-6) = 25`.',
        "cevap": 'x₁ = -2, x₂ = 3',
    },
    {
        "no": 45,
        "konu": '2. Derece Denklem',
        "soru": '`x² - 1x - 12 = 0` denkleminin köklerini bulunuz.',
        "cozum": 'Çarpanlara ayırma: `(x - (-3))(x - (4)) = 0`. Diskriminant `Δ = (-1)² - 4·1·(-12) = 49`.',
        "cevap": 'x₁ = -3, x₂ = 4',
    },
    {
        "no": 46,
        "konu": '2. Derece Denklem',
        "soru": '`x² - 4x - 5 = 0` denkleminin köklerini bulunuz.',
        "cozum": 'Çarpanlara ayırma: `(x - (-1))(x - (5)) = 0`. Diskriminant `Δ = (-4)² - 4·1·(-5) = 36`.',
        "cevap": 'x₁ = -1, x₂ = 5',
    },
    {
        "no": 47,
        "konu": '2. Derece Denklem',
        "soru": '`x² - 3x - 10 = 0` denkleminin köklerini bulunuz.',
        "cozum": 'Çarpanlara ayırma: `(x - (-2))(x - (5)) = 0`. Diskriminant `Δ = (-3)² - 4·1·(-10) = 49`.',
        "cevap": 'x₁ = -2, x₂ = 5',
    },
    {
        "no": 48,
        "konu": '2. Derece Denklem',
        "soru": '`x² - 1x - 20 = 0` denkleminin köklerini bulunuz.',
        "cozum": 'Çarpanlara ayırma: `(x - (-4))(x - (5)) = 0`. Diskriminant `Δ = (-1)² - 4·1·(-20) = 81`.',
        "cevap": 'x₁ = -4, x₂ = 5',
    },
    {
        "no": 49,
        "konu": '2. Derece Denklem',
        "soru": '`x² + 5x + 6 = 0` denkleminin köklerini bulunuz.',
        "cozum": 'Çarpanlara ayırma: `(x - (-2))(x - (-3)) = 0`. Diskriminant `Δ = (5)² - 4·1·(6) = 1`.',
        "cevap": 'x₁ = -2, x₂ = -3',
    },
    {
        "no": 50,
        "konu": '2. Derece Denklem',
        "soru": '`x² + 5x + 4 = 0` denkleminin köklerini bulunuz.',
        "cozum": 'Çarpanlara ayırma: `(x - (-1))(x - (-4)) = 0`. Diskriminant `Δ = (5)² - 4·1·(4) = 9`.',
        "cevap": 'x₁ = -1, x₂ = -4',
    },
    {
        "no": 51,
        "konu": '2. Derece Denklem',
        "soru": '`x² - 9x + 14 = 0` denkleminin köklerini bulunuz.',
        "cozum": 'Çarpanlara ayırma: `(x - (2))(x - (7)) = 0`. Diskriminant `Δ = (-9)² - 4·1·(14) = 25`.',
        "cevap": 'x₁ = 2, x₂ = 7',
    },
    {
        "no": 52,
        "konu": '2. Derece Denklem',
        "soru": '`x² - 10x + 21 = 0` denkleminin köklerini bulunuz.',
        "cozum": 'Çarpanlara ayırma: `(x - (3))(x - (7)) = 0`. Diskriminant `Δ = (-10)² - 4·1·(21) = 16`.',
        "cevap": 'x₁ = 3, x₂ = 7',
    },
    {
        "no": 53,
        "konu": 'Trigonometri',
        "soru": '`sin(0°)` trigonometrik değerini bulunuz.',
        "cozum": 'Birim çember ve özel dik üçgen oranları kullanılarak `sin(0°) = 0` elde edilir.',
        "cevap": '0',
    },
    {
        "no": 54,
        "konu": 'Trigonometri',
        "soru": '`sin(30°)` trigonometrik değerini bulunuz.',
        "cozum": 'Birim çember ve özel dik üçgen oranları kullanılarak `sin(30°) = 1/2` elde edilir.',
        "cevap": '1/2',
    },
    {
        "no": 55,
        "konu": 'Trigonometri',
        "soru": '`sin(45°)` trigonometrik değerini bulunuz.',
        "cozum": 'Birim çember ve özel dik üçgen oranları kullanılarak `sin(45°) = √2/2` elde edilir.',
        "cevap": '√2/2',
    },
    {
        "no": 56,
        "konu": 'Trigonometri',
        "soru": '`sin(60°)` trigonometrik değerini bulunuz.',
        "cozum": 'Birim çember ve özel dik üçgen oranları kullanılarak `sin(60°) = √3/2` elde edilir.',
        "cevap": '√3/2',
    },
    {
        "no": 57,
        "konu": 'Trigonometri',
        "soru": '`sin(90°)` trigonometrik değerini bulunuz.',
        "cozum": 'Birim çember ve özel dik üçgen oranları kullanılarak `sin(90°) = 1` elde edilir.',
        "cevap": '1',
    },
    {
        "no": 58,
        "konu": 'Trigonometri',
        "soru": '`cos(0°)` trigonometrik değerini bulunuz.',
        "cozum": 'Birim çember ve özel dik üçgen oranları kullanılarak `cos(0°) = 1` elde edilir.',
        "cevap": '1',
    },
    {
        "no": 59,
        "konu": 'Trigonometri',
        "soru": '`cos(30°)` trigonometrik değerini bulunuz.',
        "cozum": 'Birim çember ve özel dik üçgen oranları kullanılarak `cos(30°) = √3/2` elde edilir.',
        "cevap": '√3/2',
    },
    {
        "no": 60,
        "konu": 'Trigonometri',
        "soru": '`cos(45°)` trigonometrik değerini bulunuz.',
        "cozum": 'Birim çember ve özel dik üçgen oranları kullanılarak `cos(45°) = √2/2` elde edilir.',
        "cevap": '√2/2',
    },
    {
        "no": 61,
        "konu": 'Trigonometri',
        "soru": '`cos(60°)` trigonometrik değerini bulunuz.',
        "cozum": 'Birim çember ve özel dik üçgen oranları kullanılarak `cos(60°) = 1/2` elde edilir.',
        "cevap": '1/2',
    },
    {
        "no": 62,
        "konu": 'Trigonometri',
        "soru": '`cos(90°)` trigonometrik değerini bulunuz.',
        "cozum": 'Birim çember ve özel dik üçgen oranları kullanılarak `cos(90°) = 0` elde edilir.',
        "cevap": '0',
    },
    {
        "no": 63,
        "konu": 'Trigonometri',
        "soru": '`tan(0°)` trigonometrik değerini bulunuz.',
        "cozum": 'Birim çember ve özel dik üçgen oranları kullanılarak `tan(0°) = 0` elde edilir.',
        "cevap": '0',
    },
    {
        "no": 64,
        "konu": 'Trigonometri',
        "soru": '`tan(30°)` trigonometrik değerini bulunuz.',
        "cozum": 'Birim çember ve özel dik üçgen oranları kullanılarak `tan(30°) = √3/3` elde edilir.',
        "cevap": '√3/3',
    },
    {
        "no": 65,
        "konu": 'Trigonometri',
        "soru": '`tan(45°)` trigonometrik değerini bulunuz.',
        "cozum": 'Birim çember ve özel dik üçgen oranları kullanılarak `tan(45°) = 1` elde edilir.',
        "cevap": '1',
    },
    {
        "no": 66,
        "konu": 'Trigonometri',
        "soru": '`tan(60°)` trigonometrik değerini bulunuz.',
        "cozum": 'Birim çember ve özel dik üçgen oranları kullanılarak `tan(60°) = √3` elde edilir.',
        "cevap": '√3',
    },
    {
        "no": 67,
        "konu": 'Trigonometri',
        "soru": '`cot(30°)` trigonometrik değerini bulunuz.',
        "cozum": 'Birim çember ve özel dik üçgen oranları kullanılarak `cot(30°) = √3` elde edilir.',
        "cevap": '√3',
    },
    {
        "no": 68,
        "konu": 'Trigonometri',
        "soru": '`cot(45°)` trigonometrik değerini bulunuz.',
        "cozum": 'Birim çember ve özel dik üçgen oranları kullanılarak `cot(45°) = 1` elde edilir.',
        "cevap": '1',
    },
    {
        "no": 69,
        "konu": 'Trigonometri',
        "soru": '`cot(60°)` trigonometrik değerini bulunuz.',
        "cozum": 'Birim çember ve özel dik üçgen oranları kullanılarak `cot(60°) = √3/3` elde edilir.',
        "cevap": '√3/3',
    },
    {
        "no": 70,
        "konu": 'Trigonometri',
        "soru": '`sin(120°)` trigonometrik değerini bulunuz.',
        "cozum": 'Birim çember ve özel dik üçgen oranları kullanılarak `sin(120°) = √3/2` elde edilir.',
        "cevap": '√3/2',
    },
    {
        "no": 71,
        "konu": 'Trigonometri',
        "soru": '`cos(135°)` trigonometrik değerini bulunuz.',
        "cozum": 'Birim çember ve özel dik üçgen oranları kullanılarak `cos(135°) = -√2/2` elde edilir.',
        "cevap": '-√2/2',
    },
    {
        "no": 72,
        "konu": 'Trigonometri',
        "soru": '`sin(150°)` trigonometrik değerini bulunuz.',
        "cozum": 'Birim çember ve özel dik üçgen oranları kullanılarak `sin(150°) = 1/2` elde edilir.',
        "cevap": '1/2',
    },
    {
        "no": 73,
        "konu": 'Logaritma',
        "soru": '`log_2(4)` ifadesinin değeri kaçtır?',
        "cozum": '`2^x = 4` eşitliğini sağlayan üs `2^2 = 4` olduğu için `x = 2`.',
        "cevap": '2',
    },
    {
        "no": 74,
        "konu": 'Logaritma',
        "soru": '`log_2(8)` ifadesinin değeri kaçtır?',
        "cozum": '`2^x = 8` eşitliğini sağlayan üs `2^3 = 8` olduğu için `x = 3`.',
        "cevap": '3',
    },
    {
        "no": 75,
        "konu": 'Logaritma',
        "soru": '`log_2(16)` ifadesinin değeri kaçtır?',
        "cozum": '`2^x = 16` eşitliğini sağlayan üs `2^4 = 16` olduğu için `x = 4`.',
        "cevap": '4',
    },
    {
        "no": 76,
        "konu": 'Logaritma',
        "soru": '`log_2(32)` ifadesinin değeri kaçtır?',
        "cozum": '`2^x = 32` eşitliğini sağlayan üs `2^5 = 32` olduğu için `x = 5`.',
        "cevap": '5',
    },
    {
        "no": 77,
        "konu": 'Logaritma',
        "soru": '`log_2(64)` ifadesinin değeri kaçtır?',
        "cozum": '`2^x = 64` eşitliğini sağlayan üs `2^6 = 64` olduğu için `x = 6`.',
        "cevap": '6',
    },
    {
        "no": 78,
        "konu": 'Logaritma',
        "soru": '`log_3(9)` ifadesinin değeri kaçtır?',
        "cozum": '`3^x = 9` eşitliğini sağlayan üs `3^2 = 9` olduğu için `x = 2`.',
        "cevap": '2',
    },
    {
        "no": 79,
        "konu": 'Logaritma',
        "soru": '`log_3(27)` ifadesinin değeri kaçtır?',
        "cozum": '`3^x = 27` eşitliğini sağlayan üs `3^3 = 27` olduğu için `x = 3`.',
        "cevap": '3',
    },
    {
        "no": 80,
        "konu": 'Logaritma',
        "soru": '`log_3(81)` ifadesinin değeri kaçtır?',
        "cozum": '`3^x = 81` eşitliğini sağlayan üs `3^4 = 81` olduğu için `x = 4`.',
        "cevap": '4',
    },
    {
        "no": 81,
        "konu": 'Logaritma',
        "soru": '`log_3(243)` ifadesinin değeri kaçtır?',
        "cozum": '`3^x = 243` eşitliğini sağlayan üs `3^5 = 243` olduğu için `x = 5`.',
        "cevap": '5',
    },
    {
        "no": 82,
        "konu": 'Logaritma',
        "soru": '`log_4(16)` ifadesinin değeri kaçtır?',
        "cozum": '`4^x = 16` eşitliğini sağlayan üs `4^2 = 16` olduğu için `x = 2`.',
        "cevap": '2',
    },
    {
        "no": 83,
        "konu": 'Logaritma',
        "soru": '`log_4(64)` ifadesinin değeri kaçtır?',
        "cozum": '`4^x = 64` eşitliğini sağlayan üs `4^3 = 64` olduğu için `x = 3`.',
        "cevap": '3',
    },
    {
        "no": 84,
        "konu": 'Logaritma',
        "soru": '`log_5(25)` ifadesinin değeri kaçtır?',
        "cozum": '`5^x = 25` eşitliğini sağlayan üs `5^2 = 25` olduğu için `x = 2`.',
        "cevap": '2',
    },
    {
        "no": 85,
        "konu": 'Logaritma',
        "soru": '`log_5(125)` ifadesinin değeri kaçtır?',
        "cozum": '`5^x = 125` eşitliğini sağlayan üs `5^3 = 125` olduğu için `x = 3`.',
        "cevap": '3',
    },
    {
        "no": 86,
        "konu": 'Logaritma',
        "soru": '`log_5(625)` ifadesinin değeri kaçtır?',
        "cozum": '`5^x = 625` eşitliğini sağlayan üs `5^4 = 625` olduğu için `x = 4`.',
        "cevap": '4',
    },
    {
        "no": 87,
        "konu": 'Logaritma',
        "soru": '`log_6(36)` ifadesinin değeri kaçtır?',
        "cozum": '`6^x = 36` eşitliğini sağlayan üs `6^2 = 36` olduğu için `x = 2`.',
        "cevap": '2',
    },
    {
        "no": 88,
        "konu": 'Logaritma',
        "soru": '`log_7(49)` ifadesinin değeri kaçtır?',
        "cozum": '`7^x = 49` eşitliğini sağlayan üs `7^2 = 49` olduğu için `x = 2`.',
        "cevap": '2',
    },
    {
        "no": 89,
        "konu": 'Logaritma',
        "soru": '`log_10(10)` ifadesinin değeri kaçtır?',
        "cozum": '`10^x = 10` eşitliğini sağlayan üs `10^1 = 10` olduğu için `x = 1`.',
        "cevap": '1',
    },
    {
        "no": 90,
        "konu": 'Logaritma',
        "soru": '`log_10(100)` ifadesinin değeri kaçtır?',
        "cozum": '`10^x = 100` eşitliğini sağlayan üs `10^2 = 100` olduğu için `x = 2`.',
        "cevap": '2',
    },
    {
        "no": 91,
        "konu": 'Logaritma',
        "soru": '`log_10(1000)` ifadesinin değeri kaçtır?',
        "cozum": '`10^x = 1000` eşitliğini sağlayan üs `10^3 = 1000` olduğu için `x = 3`.',
        "cevap": '3',
    },
    {
        "no": 92,
        "konu": 'Logaritma',
        "soru": '`log_10(10000)` ifadesinin değeri kaçtır?',
        "cozum": '`10^x = 10000` eşitliğini sağlayan üs `10^4 = 10000` olduğu için `x = 4`.',
        "cevap": '4',
    },
    {
        "no": 93,
        "konu": 'Permütasyon & Kombinasyon',
        "soru": '`C(4, 2)` kombinasyon değerini hesaplayınız.',
        "cozum": 'Formül: `4! / (2!·(4-2)!) = 6`.',
        "cevap": '6',
    },
    {
        "no": 94,
        "konu": 'Permütasyon & Kombinasyon',
        "soru": '`C(5, 3)` kombinasyon değerini hesaplayınız.',
        "cozum": 'Formül: `5! / (3!·(5-3)!) = 10`.',
        "cevap": '10',
    },
    {
        "no": 95,
        "konu": 'Permütasyon & Kombinasyon',
        "soru": '`C(6, 2)` kombinasyon değerini hesaplayınız.',
        "cozum": 'Formül: `6! / (2!·(6-2)!) = 15`.',
        "cevap": '15',
    },
    {
        "no": 96,
        "konu": 'Permütasyon & Kombinasyon',
        "soru": '`C(6, 3)` kombinasyon değerini hesaplayınız.',
        "cozum": 'Formül: `6! / (3!·(6-3)!) = 20`.',
        "cevap": '20',
    },
    {
        "no": 97,
        "konu": 'Permütasyon & Kombinasyon',
        "soru": '`C(7, 2)` kombinasyon değerini hesaplayınız.',
        "cozum": 'Formül: `7! / (2!·(7-2)!) = 21`.',
        "cevap": '21',
    },
    {
        "no": 98,
        "konu": 'Permütasyon & Kombinasyon',
        "soru": '`C(7, 3)` kombinasyon değerini hesaplayınız.',
        "cozum": 'Formül: `7! / (3!·(7-3)!) = 35`.',
        "cevap": '35',
    },
    {
        "no": 99,
        "konu": 'Permütasyon & Kombinasyon',
        "soru": '`C(8, 2)` kombinasyon değerini hesaplayınız.',
        "cozum": 'Formül: `8! / (2!·(8-2)!) = 28`.',
        "cevap": '28',
    },
    {
        "no": 100,
        "konu": 'Permütasyon & Kombinasyon',
        "soru": '`C(8, 3)` kombinasyon değerini hesaplayınız.',
        "cozum": 'Formül: `8! / (3!·(8-3)!) = 56`.',
        "cevap": '56',
    },
    {
        "no": 101,
        "konu": 'Permütasyon & Kombinasyon',
        "soru": '`C(9, 2)` kombinasyon değerini hesaplayınız.',
        "cozum": 'Formül: `9! / (2!·(9-2)!) = 36`.',
        "cevap": '36',
    },
    {
        "no": 102,
        "konu": 'Permütasyon & Kombinasyon',
        "soru": '`C(10, 2)` kombinasyon değerini hesaplayınız.',
        "cozum": 'Formül: `10! / (2!·(10-2)!) = 45`.',
        "cevap": '45',
    },
    {
        "no": 103,
        "konu": 'Permütasyon & Kombinasyon',
        "soru": '`P(3, 2)` permütasyon değerini hesaplayınız.',
        "cozum": 'Formül: `3! / (3-2)! = 6`.',
        "cevap": '6',
    },
    {
        "no": 104,
        "konu": 'Permütasyon & Kombinasyon',
        "soru": '`P(4, 3)` permütasyon değerini hesaplayınız.',
        "cozum": 'Formül: `4! / (4-3)! = 24`.',
        "cevap": '24',
    },
    {
        "no": 105,
        "konu": 'Permütasyon & Kombinasyon',
        "soru": '`P(5, 2)` permütasyon değerini hesaplayınız.',
        "cozum": 'Formül: `5! / (5-2)! = 20`.',
        "cevap": '20',
    },
    {
        "no": 106,
        "konu": 'Permütasyon & Kombinasyon',
        "soru": '`P(5, 3)` permütasyon değerini hesaplayınız.',
        "cozum": 'Formül: `5! / (5-3)! = 60`.',
        "cevap": '60',
    },
    {
        "no": 107,
        "konu": 'Permütasyon & Kombinasyon',
        "soru": '`P(6, 2)` permütasyon değerini hesaplayınız.',
        "cozum": 'Formül: `6! / (6-2)! = 30`.',
        "cevap": '30',
    },
    {
        "no": 108,
        "konu": 'Permütasyon & Kombinasyon',
        "soru": '`P(6, 3)` permütasyon değerini hesaplayınız.',
        "cozum": 'Formül: `6! / (6-3)! = 120`.',
        "cevap": '120',
    },
    {
        "no": 109,
        "konu": 'Permütasyon & Kombinasyon',
        "soru": '`P(7, 2)` permütasyon değerini hesaplayınız.',
        "cozum": 'Formül: `7! / (7-2)! = 42`.',
        "cevap": '42',
    },
    {
        "no": 110,
        "konu": 'Permütasyon & Kombinasyon',
        "soru": '`P(8, 2)` permütasyon değerini hesaplayınız.',
        "cozum": 'Formül: `8! / (8-2)! = 56`.',
        "cevap": '56',
    },
    {
        "no": 111,
        "konu": 'Permütasyon & Kombinasyon',
        "soru": '`C(10, 3)` kombinasyon değerini hesaplayınız.',
        "cozum": 'Formül: `10! / (3!·(10-3)!) = 120`.',
        "cevap": '120',
    },
    {
        "no": 112,
        "konu": 'Permütasyon & Kombinasyon',
        "soru": '`P(4, 4)` permütasyon değerini hesaplayınız.',
        "cozum": 'Formül: `4! / (4-4)! = 24`.',
        "cevap": '24',
    },
    {
        "no": 113,
        "konu": 'Türev',
        "soru": '`f(x) = 2x^2` fonksiyonunun türevini bulunuz.',
        "cozum": "Kuvvet kuralı: `f'(x) = 2·2·x^(2-1) = 4x^`.",
        "cevap": '4x',
    },
    {
        "no": 114,
        "konu": 'İntegral',
        "soru": '`∫ 6x^2 dx` belirsiz integralini bulunuz.',
        "cozum": 'Kuvveti 1 artırıp yeni kuvvete böleriz: `6/(2+1)·x^3 + C = 2x^3 + C`.',
        "cevap": '2x^3 + C',
    },
    {
        "no": 115,
        "konu": 'Türev',
        "soru": '`f(x) = 3x^2` fonksiyonunun türevini bulunuz.',
        "cozum": "Kuvvet kuralı: `f'(x) = 3·2·x^(2-1) = 6x^`.",
        "cevap": '6x',
    },
    {
        "no": 116,
        "konu": 'İntegral',
        "soru": '`∫ 9x^2 dx` belirsiz integralini bulunuz.',
        "cozum": 'Kuvveti 1 artırıp yeni kuvvete böleriz: `9/(2+1)·x^3 + C = 3x^3 + C`.',
        "cevap": '3x^3 + C',
    },
    {
        "no": 117,
        "konu": 'Türev',
        "soru": '`f(x) = 4x^2` fonksiyonunun türevini bulunuz.',
        "cozum": "Kuvvet kuralı: `f'(x) = 4·2·x^(2-1) = 8x^`.",
        "cevap": '8x',
    },
    {
        "no": 118,
        "konu": 'İntegral',
        "soru": '`∫ 12x^2 dx` belirsiz integralini bulunuz.',
        "cozum": 'Kuvveti 1 artırıp yeni kuvvete böleriz: `12/(2+1)·x^3 + C = 4x^3 + C`.',
        "cevap": '4x^3 + C',
    },
    {
        "no": 119,
        "konu": 'Türev',
        "soru": '`f(x) = 5x^2` fonksiyonunun türevini bulunuz.',
        "cozum": "Kuvvet kuralı: `f'(x) = 5·2·x^(2-1) = 10x^`.",
        "cevap": '10x',
    },
    {
        "no": 120,
        "konu": 'İntegral',
        "soru": '`∫ 15x^2 dx` belirsiz integralini bulunuz.',
        "cozum": 'Kuvveti 1 artırıp yeni kuvvete böleriz: `15/(2+1)·x^3 + C = 5x^3 + C`.',
        "cevap": '5x^3 + C',
    },
    {
        "no": 121,
        "konu": 'Türev',
        "soru": '`f(x) = 2x^3` fonksiyonunun türevini bulunuz.',
        "cozum": "Kuvvet kuralı: `f'(x) = 2·3·x^(3-1) = 6x^2`.",
        "cevap": '6x^2',
    },
    {
        "no": 122,
        "konu": 'İntegral',
        "soru": '`∫ 8x^3 dx` belirsiz integralini bulunuz.',
        "cozum": 'Kuvveti 1 artırıp yeni kuvvete böleriz: `8/(3+1)·x^4 + C = 2x^4 + C`.',
        "cevap": '2x^4 + C',
    },
    {
        "no": 123,
        "konu": 'Türev',
        "soru": '`f(x) = 3x^3` fonksiyonunun türevini bulunuz.',
        "cozum": "Kuvvet kuralı: `f'(x) = 3·3·x^(3-1) = 9x^2`.",
        "cevap": '9x^2',
    },
    {
        "no": 124,
        "konu": 'İntegral',
        "soru": '`∫ 12x^3 dx` belirsiz integralini bulunuz.',
        "cozum": 'Kuvveti 1 artırıp yeni kuvvete böleriz: `12/(3+1)·x^4 + C = 3x^4 + C`.',
        "cevap": '3x^4 + C',
    },
    {
        "no": 125,
        "konu": 'Türev',
        "soru": '`f(x) = 4x^3` fonksiyonunun türevini bulunuz.',
        "cozum": "Kuvvet kuralı: `f'(x) = 4·3·x^(3-1) = 12x^2`.",
        "cevap": '12x^2',
    },
    {
        "no": 126,
        "konu": 'İntegral',
        "soru": '`∫ 16x^3 dx` belirsiz integralini bulunuz.',
        "cozum": 'Kuvveti 1 artırıp yeni kuvvete böleriz: `16/(3+1)·x^4 + C = 4x^4 + C`.',
        "cevap": '4x^4 + C',
    },
    {
        "no": 127,
        "konu": 'Türev',
        "soru": '`f(x) = 5x^3` fonksiyonunun türevini bulunuz.',
        "cozum": "Kuvvet kuralı: `f'(x) = 5·3·x^(3-1) = 15x^2`.",
        "cevap": '15x^2',
    },
    {
        "no": 128,
        "konu": 'İntegral',
        "soru": '`∫ 20x^3 dx` belirsiz integralini bulunuz.',
        "cozum": 'Kuvveti 1 artırıp yeni kuvvete böleriz: `20/(3+1)·x^4 + C = 5x^4 + C`.',
        "cevap": '5x^4 + C',
    },
    {
        "no": 129,
        "konu": 'Türev',
        "soru": '`f(x) = 2x^4` fonksiyonunun türevini bulunuz.',
        "cozum": "Kuvvet kuralı: `f'(x) = 2·4·x^(4-1) = 8x^3`.",
        "cevap": '8x^3',
    },
    {
        "no": 130,
        "konu": 'İntegral',
        "soru": '`∫ 10x^4 dx` belirsiz integralini bulunuz.',
        "cozum": 'Kuvveti 1 artırıp yeni kuvvete böleriz: `10/(4+1)·x^5 + C = 2x^5 + C`.',
        "cevap": '2x^5 + C',
    },
    {
        "no": 131,
        "konu": 'Türev',
        "soru": '`f(x) = 3x^4` fonksiyonunun türevini bulunuz.',
        "cozum": "Kuvvet kuralı: `f'(x) = 3·4·x^(4-1) = 12x^3`.",
        "cevap": '12x^3',
    },
    {
        "no": 132,
        "konu": 'İntegral',
        "soru": '`∫ 15x^4 dx` belirsiz integralini bulunuz.',
        "cozum": 'Kuvveti 1 artırıp yeni kuvvete böleriz: `15/(4+1)·x^5 + C = 3x^5 + C`.',
        "cevap": '3x^5 + C',
    },
]


def matematik_studyosu_goster(sesli_soyle_fn):
    st.subheader("🧮 Derinlemesine Matematik, Cebir, Trigonometri, Analiz & Geometri Laboratuvarı")
    t1, t2, t3, t4 = st.tabs([
        "📚 Derin Konu Ansiklopedisi",
        "⚡ Gelişmiş Çözücü & Hesaplayıcı",
        "📖 Çözümlü Soru Bankası",
        "🎯 Canlı Test",
    ])

    with t1:
        secili_konu = st.selectbox("Öğrenmek İstediğin Konuyu Seç:", list(MATEMATIK_KONU_REHBERI.keys()), key="m4_secili_konu")
        k_veri = MATEMATIK_KONU_REHBERI[secili_konu]
        st.markdown(
            bilgi_karti_olustur(secili_konu, f"📘 {k_veri['alt_baslik']}", k_veri["icerik"].replace("\n", "<br>")),
            unsafe_allow_html=True,
        )
        if st.button("🔊 Bu Konuyu Sesli Anlat", key="m4_konu_sesli_btn"):
            sesli_soyle_fn(k_veri["icerik"], dil="tr")

    with t2:
        c_m1, c_m2, c_m3 = st.columns(3, gap="medium")
        with c_m1:
            st.markdown("#### √ Karekök & Asal Çarpan")
            kok_n = st.number_input("Sayı gir:", min_value=1, max_value=1000000, value=72, step=1, key="m4_kok_n")
            dis, ic = karekok_sadelestir(int(kok_n))
            if ic == 1:
                st.success(f"`√{kok_n}` = **{dis}** (Tam Kare)")
            else:
                st.success(f"`√{kok_n}` = **`{dis if dis > 1 else ''}√{ic}`** (`{math.sqrt(kok_n):.4f}`)")
            carpanlar = asal_carpanlara_ayir(int(kok_n))
            if carpanlar:
                c_str = " × ".join(f"{k}^{v}" if v > 1 else str(k) for k, v in carpanlar.items())
                st.info(f"**Asal Çarpanlar:** `{c_str}`")
            if int(kok_n) in MATEMATIK_REFERANS_TABLOSU:
                ref = MATEMATIK_REFERANS_TABLOSU[int(kok_n)]
                st.caption(f"Karesi: `{ref['karesi']}` | Küpü: `{ref['kupu']}`")

        with c_m2:
            st.markdown("#### 📐 2. Derece Denklem (`ax²+bx+c=0`)")
            da = st.number_input("a katsayısı:", value=1.0, step=1.0, key="m4_denk_a")
            db = st.number_input("b katsayısı:", value=-5.0, step=1.0, key="m4_denk_b")
            dc = st.number_input("c sabiti:", value=6.0, step=1.0, key="m4_denk_c")
            st.markdown(ikinci_derece_denklem_coz(da, db, dc))

        with c_m3:
            st.markdown("#### 📏 Pisagor & Dik Üçgen")
            k_a = st.number_input("1. Dik Kenar (a):", min_value=1.0, value=6.0, step=1.0, key="m4_pis_a")
            k_b = st.number_input("2. Dik Kenar (b):", min_value=1.0, value=8.0, step=1.0, key="m4_pis_b")
            st.markdown(pisagor_hesapla(k_a, k_b))

        st.markdown("---")
        c_d1, c_d2, c_d3 = st.columns(3, gap="medium")
        with c_d1:
            st.markdown("#### 📊 Trigonometri & Logaritma")
            aci_g = st.slider("Açı (Derece):", 0, 360, 30, step=15, key="m4_trig_aci")
            rad_g = math.radians(aci_g)
            st.success(f"`sin({aci_g}°)` = `{math.sin(rad_g):.4f}` | `cos({aci_g}°)` = `{math.cos(rad_g):.4f}`")
            log_n = st.number_input("Logaritma Sayısı (log₁₀ & ln):", min_value=0.1, value=100.0, step=10.0, key="m4_log_n")
            st.info(f"`log₁₀({log_n})` = `{math.log10(log_n):.4f}` | `ln({log_n})` = `{math.log(log_n):.4f}`")

        with c_d2:
            st.markdown("#### 🎲 Permütasyon & Kombinasyon")
            pk_n = st.number_input("Eleman Sayısı (n):", min_value=1, max_value=50, value=6, step=1, key="m4_pk_n")
            pk_r = st.number_input("Seçim / Sıralama (r):", min_value=0, max_value=50, value=2, step=1, key="m4_pk_r")
            if pk_r <= pk_n:
                st.success(f"`C({pk_n}, {pk_r})` = **{sayi_formatla(math.comb(int(pk_n), int(pk_r)))}**")
                st.info(f"`P({pk_n}, {pk_r})` = **{sayi_formatla(math.perm(int(pk_n), int(pk_r)))}**")
            else:
                st.warning("`r` değeri `n` değerinden büyük olamaz.")

        with c_d3:
            st.markdown("#### ∫ Polinom Türev & İntegral")
            pol_girdi = st.text_input("Polinom (Örn: `3x^2 + 4x - 5`):", value="3x^2 + 4x - 5", key="m4_polinom")
            if pol_girdi.strip():
                st.markdown(polinom_turev_al(pol_girdi))
                st.markdown(polinom_integral_al(pol_girdi))

    with t3:
        konular = ["Tümü"] + sorted(list({s["konu"] for s in COZUMLU_SORU_BANKASI}))
        sec_konu_filtre = st.selectbox("Konuya Göre Filtrele:", konular, key="m4_banka_konu")
        filtrelenmis = [s for s in COZUMLU_SORU_BANKASI if sec_konu_filtre == "Tümü" or s["konu"] == sec_konu_filtre]
        for s_obj in filtrelenmis:
            st.markdown(
                bilgi_karti_olustur(
                    f"Soru #{s_obj['no']} — {s_obj['konu']}",
                    f"Doğru Cevap: {s_obj['cevap']}",
                    f"**Soru:** {s_obj['soru']}<br><br>**Adım Adım Çözüm:** {s_obj['cozum']}",
                ),
                unsafe_allow_html=True,
            )

    with t4:
        st.caption(f"Toplam Doğru Puanın: **{st.session_state.quiz_puan}**")
        if st.button("🎲 Yeni Test Sorusu Getir", key="m4_yeni_quiz_btn") or st.session_state.quiz_soru is None:
            rast = random.choice(COZUMLU_SORU_BANKASI)
            st.session_state.quiz_soru = (rast["soru"], rast["cevap"], rast["cozum"])
        q_soru, q_cevap, q_cozum = st.session_state.quiz_soru
        st.info(f"**Soru:** {q_soru}")
        k_yanit = st.text_input("Cevabın:", key="canli_quiz_girdi")
        if st.button("✅ Cevabı Kontrol Et", key="m4_quiz_kontrol_btn"):
            if k_yanit.strip().replace(" ", "") == q_cevap.replace(" ", ""):
                st.session_state.quiz_puan += 10
                st.success(f"🎉 Harika Ahmet! Doğru cevap: **{q_cevap}** (+10 Puan)")
            else:
                st.error(f"❌ Doğru cevap: **{q_cevap}** | Çözüm: {q_cozum}")
