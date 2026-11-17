# -*- coding: utf-8 -*-
"""
==============================================================================
AR AI STUDIO v5.0 — MODÜL 5: 100 ADET ÖZGÜN A1-A2-B1 3D ÇEVİRMELİ DİL KARTI
(İNGİLİZCE • ARAPÇA • BENGALCE), 28 DİLLİ ÇEVİRİ, NEURAL SES VE MİKROFON STT MOTORU
(modul_5_dil_ve_cevirmeli_kartlar.py)
==============================================================================
"""
import asyncio
import importlib.util
import inspect
import io
import json
import os
import random
import re
import sys
import urllib.parse
import urllib.request
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
cevirmeli_dil_karti_goster = _m1.cevirmeli_dil_karti_goster

try:
    from googletrans import Translator as _GoogleTranslator
    _translator_nesnesi = _GoogleTranslator()
except Exception:
    _translator_nesnesi = None

try:
    from gtts import gTTS
    GTTS_MEVCUT = True
except Exception:
    gTTS = None
    GTTS_MEVCUT = False

try:
    import edge_tts
    EDGE_TTS_MEVCUT = True
except Exception:
    EDGE_TTS_MEVCUT = False

try:
    import pygame
    PYGAME_MEVCUT = True
except Exception:
    PYGAME_MEVCUT = False

try:
    import speech_recognition as sr
    SPEECH_RECOGNITION_MEVCUT = True
except Exception:
    sr = None
    SPEECH_RECOGNITION_MEVCUT = False

DESTEKLENEN_DILLER = {
    "tr": "🇹🇷 Türkçe (Ana Dil)",
    "en": "🇬🇧 İngilizce (English)",
    "ar": "🇸🇦 Arapça (العربية)",
    "bn": "🇧🇩 Bengalce (বাংলা)",
    "zh-cn": "🇨🇳 Çince (中文 - Basitleştirilmiş)",
    "de": "🇩🇪 Almanca (Deutsch)",
    "fr": "🇫🇷 Fransızca (Français)",
    "es": "🇪🇸 İspanyolca (Español)",
    "ru": "🇷🇺 Rusça (Русский)",
    "ja": "🇯🇵 Japonca (日本語)",
    "ko": "🇰🇷 Korece (한국어)",
    "it": "🇮🇹 İtalyanca (Italiano)",
    "pt": "🇵🇹 Portekizce (Português)",
    "az": "🇦🇿 Azerbaycanca (Azərbaycanca)",
    "fa": "🇮🇷 Farsça (فارسی)",
    "ur": "🇵🇰 Urduca (اردو)",
    "hi": "🇮🇳 Hintçe (हिन्दी)",
    "id": "🇮🇩 Endonezce (Bahasa Indonesia)",
    "ms": "🇲🇾 Malayca (Bahasa Melayu)",
    "nl": "🇳🇱 Hollandaca (Nederlands)",
    "pl": "🇵🇱 Lehçe (Polski)",
    "ro": "🇷🇴 Rumence (Română)",
    "sv": "🇸🇪 İsveççe (Svenska)",
    "cs": "🇨🇿 Çekçe (Čeština)",
    "el": "🇬🇷 Yunanca (Ελληνικά)",
    "uk": "🇺🇦 Ukraynaca (Українська)",
    "th": "🇹🇭 Tayca (ภาษาไทย)",
    "vi": "🇻🇳 Vietnamca (Tiếng Việt)",
}

EDGE_SESLER = {
    "ar": "ar-SA-HamedNeural", "az": "az-AZ-BabekNeural", "bn": "bn-BD-PradeepNeural",
    "cs": "cs-CZ-AntoninNeural", "de": "de-DE-ConradNeural", "el": "el-GR-NestorasNeural",
    "en": "en-US-AndrewNeural", "es": "es-ES-AlvaroNeural", "fa": "fa-IR-FaridNeural",
    "fr": "fr-FR-HenriNeural", "hi": "hi-IN-MadhurNeural", "id": "id-ID-ArdiNeural",
    "it": "it-IT-DiegoNeural", "ja": "ja-JP-KeitaNeural", "ko": "ko-KR-InJoonNeural",
    "ms": "ms-MY-OsmanNeural", "nl": "nl-NL-MaartenNeural", "pl": "pl-PL-MarekNeural",
    "pt": "pt-BR-AntonioNeural", "ro": "ro-RO-EmilNeural", "ru": "ru-RU-DmitryNeural",
    "sv": "sv-SE-MattiasNeural", "th": "th-TH-NiwatNeural", "tr": "tr-TR-AhmetNeural",
    "uk": "uk-UA-OstapNeural", "ur": "ur-PK-AsadNeural", "vi": "vi-VN-NamMinhNeural",
    "zh-cn": "zh-CN-YunxiNeural",
}

EDGE_KADIN_SESLER = {
    "ar": "ar-SA-ZariyahNeural", "az": "az-AZ-BanuNeural", "bn": "bn-BD-NabanitaNeural",
    "cs": "cs-CZ-VlastaNeural", "de": "de-DE-KatjaNeural", "el": "el-GR-AthinaNeural",
    "en": "en-US-AriaNeural", "es": "es-ES-ElviraNeural", "fa": "fa-IR-DilaraNeural",
    "fr": "fr-FR-DeniseNeural", "hi": "hi-IN-SwaraNeural", "id": "id-ID-GadisNeural",
    "it": "it-IT-ElsaNeural", "ja": "ja-JP-NanamiNeural", "ko": "ko-KR-SunHiNeural",
    "ms": "ms-MY-YasminNeural", "nl": "nl-NL-ColetteNeural", "pl": "pl-PL-ZofiaNeural",
    "pt": "pt-BR-FranciscaNeural", "ro": "ro-RO-AlinaNeural", "ru": "ru-RU-SvetlanaNeural",
    "sv": "sv-SE-SofieNeural", "th": "th-TH-PremwadeeNeural", "tr": "tr-TR-EmelNeural",
    "uk": "uk-UA-PolinaNeural", "ur": "ur-PK-UzmaNeural", "vi": "vi-VN-HoaiMyNeural",
    "zh-cn": "zh-CN-XiaoxiaoNeural",
}

GTTS_DIL_ESLESME = {k: ("zh-CN" if k == "zh-cn" else k) for k in DESTEKLENEN_DILLER}
TURKCE_AYLAR = ["", "Ocak", "Şubat", "Mart", "Nisan", "Mayıs", "Haziran", "Temmuz", "Ağustos", "Eylül", "Ekim", "Kasım", "Aralık"]
TURKCE_GUNLER = ["Pazartesi", "Salı", "Çarşamba", "Perşembe", "Cuma", "Cumartesi", "Pazar"]

# 100 ADET TAMAMI ÖZGÜN A1-A2-B1 DİL KARTI
A1_A2_DIL_PRATIK_KARTLARI = [
    {
        "id": 1,
        "seviye": 'A1 (Başlangıç)',
        "kategori": 'Selamlaşma & Tanışma',
        "turkce": 'Merhaba, nasılsın?',
        "ingilizce": 'Hello, how are you?',
        "ing_okunus": 'Helo, hav ar yu?',
        "ornek_en": 'Hello, how are you today?',
        "arapca": 'مَرْحَبًا، كَيْفَ حَالُكَ؟',
        "ara_okunus": 'Merhaben, keyfe hâluke?',
        "ornek_ar": 'مَرْحَبًا يَا صَدِيقِي، كَيْفَ حَالُكَ الْيَوْمَ؟',
        "bengalce": 'হ্যালো, আপনি কেমন আছেন?',
        "ben_okunus": 'Hyalo, apni kemon achen?',
        "ornek_bn": 'হ্যালো ভাই, আপনি আজ কেমন আছেন?',
    },
    {
        "id": 2,
        "seviye": 'A1 (Başlangıç)',
        "kategori": 'Selamlaşma & Tanışma',
        "turkce": 'İyiyim, teşekkür ederim.',
        "ingilizce": 'I am fine, thank you.',
        "ing_okunus": 'Ay em fayn, tenk yu.',
        "ornek_en": 'I am fine, thank you very much.',
        "arapca": 'أَنَا بِخَيْرٍ، شُكْرًا لَكَ.',
        "ara_okunus": 'Ene bi-hayrin, şükran leke.',
        "ornek_ar": 'أَنَا بِخَيْرٍ وَالْحَمْدُ لِلَّهِ.',
        "bengalce": 'আমি ভালো আছি, ধন্যবাদ।',
        "ben_okunus": 'Ami bhalo achi, dhonnobad.',
        "ornek_bn": 'আমি খুব ভালো আছি, আপনাকে ধন্যবাদ।',
    },
    {
        "id": 3,
        "seviye": 'A1 (Başlangıç)',
        "kategori": 'Tanışma & Kimlik',
        "turkce": 'Benim adım Ahmet.',
        "ingilizce": 'My name is Ahmet.',
        "ing_okunus": 'May neym iz Ahmet.',
        "ornek_en": 'My name is Ahmet and I am a student.',
        "arapca": 'اِسْمِي أَحْمَدُ.',
        "ara_okunus": 'İsmî Ahmed.',
        "ornek_ar": 'اِسْمِي أَحْمَدُ وَأَنَا طَالِبٌ.',
        "bengalce": 'আমার নাম আহমেদ।',
        "ben_okunus": 'Amar nam Ahmed.',
        "ornek_bn": 'আমার নাম আহমেদ এবং আমি একজন ছাত্র।',
    },
    {
        "id": 4,
        "seviye": 'A1 (Başlangıç)',
        "kategori": 'Tanışma & Kimlik',
        "turkce": 'Tanıştığımıza memnun oldum.',
        "ingilizce": 'Nice to meet you.',
        "ing_okunus": 'Nays tu mit yu.',
        "ornek_en": 'Welcome to Istanbul, nice to meet you!',
        "arapca": 'تَشَرَّفْتُ بِمَعْرِفَتِكَ.',
        "ara_okunus": "Teşerraftü bi-ma'rifetike.",
        "ornek_ar": 'أَهْلًا بِكَ فِي إِسْطَنْبُولَ!',
        "bengalce": 'আপনার সাথে দেখা করে ভালো লাগলো।',
        "ben_okunus": 'Apnar sathe dekha kore bhalo laglo.',
        "ornek_bn": 'ইস্তাম্বুলে স্বাগতম!',
    },
    {
        "id": 5,
        "seviye": 'A1 (Başlangıç)',
        "kategori": 'Günlük İfadeler',
        "turkce": 'Günaydın / İyi sabahlar',
        "ingilizce": 'Good morning',
        "ing_okunus": 'Gud morning',
        "ornek_en": 'Good morning, have a great day!',
        "arapca": 'صَبَاحُ الْخَيْرِ',
        "ara_okunus": "Sabâhu'l-hayr",
        "ornek_ar": 'صَبَاحُ الْخَيْرِ، أَتَمَنَّى لَكَ يَوْمًا جَمِيلًا!',
        "bengalce": 'শুভ সকাল',
        "ben_okunus": 'Shubho shokal',
        "ornek_bn": 'শুভ সকাল, আপনার দিনটি ভালো কাটুক!',
    },
    {
        "id": 6,
        "seviye": 'A1 (Başlangıç)',
        "kategori": 'Günlük İfadeler',
        "turkce": 'İyi akşamlar / İyi geceler',
        "ingilizce": 'Good evening / Good night',
        "ing_okunus": 'Gud ivning / Gud nayt',
        "ornek_en": 'Good night, see you tomorrow.',
        "arapca": 'مَسَاءُ الْخَيْرِ / تُصْبِحُ عَلَى خَيْرٍ',
        "ara_okunus": "Mesâu'l-hayr / Tusbihu alâ hayr",
        "ornek_ar": 'تُصْبِحُ عَلَى خَيْرٍ، أَرَاكَ غَدًا.',
        "bengalce": 'শুভ সন্ধ্যা / শুভ রাত্রি',
        "ben_okunus": 'Shubho shondhya / Shubho ratri',
        "ornek_bn": 'শুভ রাত্রি, আগামীকাল দেখা হবে।',
    },
    {
        "id": 7,
        "seviye": 'A1 (Başlangıç)',
        "kategori": 'Aile & Kişiler',
        "turkce": 'Babam ve annem',
        "ingilizce": 'My father and my mother',
        "ing_okunus": 'May fadır end may madır',
        "ornek_en": 'I love my father and my mother very much.',
        "arapca": 'أَبِي وَأُمِّي',
        "ara_okunus": 'Ebî ve ümmî',
        "ornek_ar": 'أَنَا أُحِبُّ أَبِي وَأُمِّي كَثِيرًا.',
        "bengalce": 'আমার বাবা এবং আমার মা',
        "ben_okunus": 'Amar baba ebong amar ma',
        "ornek_bn": 'আমি আমার বাবা এবং মাকে খুব ভালোবাসি।',
    },
    {
        "id": 8,
        "seviye": 'A1 (Başlangıç)',
        "kategori": 'Okul & Eğitim',
        "turkce": 'Ben lise öğrencisiyim.',
        "ingilizce": 'I am a high school student.',
        "ing_okunus": 'Ay em e hay skul studınt.',
        "ornek_en": 'I am a high school student in Istanbul.',
        "arapca": 'أَنَا طَالِبٌ فِي الْمَدْرَسَةِ الثَّانَوِيَّةِ.',
        "ara_okunus": "Ene tâlibun fi'l-medreseti's-sâneviyyeti.",
        "ornek_ar": 'أَنَا طَالِبٌ فِي إِسْطَنْبُولَ.',
        "bengalce": 'আমি হাই স্কুলের ছাত্র।',
        "ben_okunus": 'Ami hai skuler chatro.',
        "ornek_bn": 'আমি ইস্তাম্বুলের একটি হাই স্কুলের ছাত্র।',
    },
    {
        "id": 9,
        "seviye": 'A1 (Başlangıç)',
        "kategori": 'Okul & Eğitim',
        "turkce": 'Kitap, defter ve kalem',
        "ingilizce": 'Book, notebook and pen',
        "ing_okunus": 'Buk, notbuk end pen',
        "ornek_en": 'My book, notebook and pen are on the table.',
        "arapca": 'كِتَابٌ، دَفْتَرٌ وَقَلَمٌ',
        "ara_okunus": 'Kitâbun, defterun ve kalemun',
        "ornek_ar": 'كِتَابِي وَقَلَمِي عَلَى الطَّاوِلَةِ.',
        "bengalce": 'বই, খাতা এবং কলম',
        "ben_okunus": 'Boi, khata ebong kolom',
        "ornek_bn": 'আমার বই, খাতা এবং কলম টেবিলের ওপর আছে।',
    },
    {
        "id": 10,
        "seviye": 'A1 (Başlangıç)',
        "kategori": 'Temel Sorular',
        "turkce": 'Bu nedir? / Kimdir?',
        "ingilizce": 'What is this? / Who is this?',
        "ing_okunus": 'Vat iz dis? / Hu iz dis?',
        "ornek_en": 'What is this device? This is a sensor.',
        "arapca": 'مَا هَذَا؟ / مَنْ هَذَا؟',
        "ara_okunus": 'Mâ hâzâ? / Men hâzâ?',
        "ornek_ar": 'مَا هَذَا الْجِهَازُ؟ هَذَا مُسْتَشْعِرٌ.',
        "bengalce": 'এটা কী? / উনি কে?',
        "ben_okunus": 'Eta ki? / Uni ke?',
        "ornek_bn": 'এই যন্ত্রটি কী? এটি একটি সেন্সর।',
    },
    {
        "id": 11,
        "seviye": 'A1 (Başlangıç)',
        "kategori": 'Zaman & Saat',
        "turkce": 'Saat kaç? / Bugün',
        "ingilizce": 'What time is it? / Today',
        "ing_okunus": 'Vat taym iz it? / Tudey',
        "ornek_en": 'What time is it right now?',
        "arapca": 'كَمِ السَّاعَةُ؟ / الْيَوْمَ',
        "ara_okunus": "Kemi's-sâatü? / El-yevm",
        "ornek_ar": 'كَمِ السَّاعَةُ الْآنَ مَنْ فَضْلِكَ؟',
        "bengalce": 'এখন কয়টা বাজে? / আজ',
        "ben_okunus": 'Ekhon koyta baje? / Aj',
        "ornek_bn": 'অনুগ্রহ করে বলবেন এখন কয়টা বাজে?',
    },
    {
        "id": 12,
        "seviye": 'A1 (Başlangıç)',
        "kategori": 'Günlük İhtiyaçlar',
        "turkce": 'Su ve yemek istiyorum.',
        "ingilizce": 'I want water and food.',
        "ing_okunus": 'Ay vant votır end fud.',
        "ornek_en": 'Can I have a glass of cold water, please?',
        "arapca": 'أُرِيدُ مَاءً وَطَعَامًا.',
        "ara_okunus": 'Ürîdü mâen ve taâmen.',
        "ornek_ar": 'هَلْ يُمْكِنُنِي كُوبُ مَاءٍ؟',
        "bengalce": 'আমি পানি এবং খাবার চাই।',
        "ben_okunus": 'Ami pani ebong khabar chai.',
        "ornek_bn": 'দয়া করে আমাকে এক গ্লাস পানি দেবেন?',
    },
    {
        "id": 13,
        "seviye": 'A1 (Başlangıç)',
        "kategori": 'Sayılar & Hesap',
        "turkce": 'Bir, iki, üç, dört, beş',
        "ingilizce": 'One, two, three, four, five',
        "ing_okunus": 'Van, tu, tri, for, fayv',
        "ornek_en": 'I have five new books in my bag.',
        "arapca": 'وَاحِدٌ، اِثْنَانِ، ثَلَاثَةٌ، أَرْبَعَةٌ، خَمْسَةٌ',
        "ara_okunus": 'Vâhid, isnân, selâse, erbaa, hamse',
        "ornek_ar": 'عِنْدِي خَمْسَةُ كُتُبٍ جَدِيدَةٍ.',
        "bengalce": 'এক, দুই, তিন, চার, পাঁচ',
        "ben_okunus": 'Ek, dui, tin, char, panch',
        "ornek_bn": 'আমার ব্যাগে পাঁচটি নতুন বই আছে।',
    },
    {
        "id": 14,
        "seviye": 'A1 (Başlangıç)',
        "kategori": 'Yardım & İletişim',
        "turkce": 'Lütfen bana yardım eder misin?',
        "ingilizce": 'Can you help me, please?',
        "ing_okunus": 'Ken yu help mi, pliz?',
        "ornek_en": 'Excuse me, can you help me with this question?',
        "arapca": 'هَلْ يُمْكِنُكَ مُسَاعَدَتِي مَنْ فَضْلِكَ؟',
        "ara_okunus": 'Hel yümkınuke müsâadetî min fadlike?',
        "ornek_ar": 'عَفْوًا، هَلْ يُمْكِنُكَ مُسَاعَدَتِي؟',
        "bengalce": 'দয়া করে আমাকে সাহায্য করতে পারবেন?',
        "ben_okunus": 'Doya kore amake shahajjo korte parben?',
        "ornek_bn": 'আমাকে এই প্রশ্নে একটু সাহায্য করতে পারবেন?',
    },
    {
        "id": 15,
        "seviye": 'A1 (Başlangıç)',
        "kategori": 'Dil Öğrenimi',
        "turkce": 'İngilizce, Arapça ve Bengalce öğreniyorum.',
        "ingilizce": 'I am learning English, Arabic and Bengali.',
        "ing_okunus": 'Ay em lörning İngliş, Arabik end Bengali.',
        "ornek_en": 'I practice new words every day.',
        "arapca": 'أَنَا أَتَعَلَّمُ الْإِنْجِلِيزِيَّةَ وَالْعَرَبِيَّةَ وَالْبَنْغَالِيَّةَ.',
        "ara_okunus": "Ene eteallemu el-İncilîziyyete ve'l-Arabiyyete ve'l-Bengâliyyete.",
        "ornek_ar": 'أَنَا أَتَدَرَّبُ كُلَّ يَوْمٍ.',
        "bengalce": 'আমি ইংরেজি, আরবি এবং বাংলা শিখছি।',
        "ben_okunus": 'Ami Ingreji, Arbi ebong Bangla shikhchi.',
        "ornek_bn": 'আমি প্রতিদিন নতুন শব্দ অনুশীলন করি।',
    },
    {
        "id": 16,
        "seviye": 'A2 (Temel Orta)',
        "kategori": 'Teknoloji & Yazılım',
        "turkce": 'Bilgisayarda Python kodu yazıyorum.',
        "ingilizce": 'I am writing Python code on the computer.',
        "ing_okunus": 'Ay em rayting Paytın kod on dı kompyutır.',
        "ornek_en": 'I am developing my own AI assistant with Python.',
        "arapca": 'أَنَا أَكْتُبُ بَرْمَجَةَ بَايْثُون عَلَى الْحَاسُوبِ.',
        "ara_okunus": "Ene ektübü bermecete Python ale'l-hâsûbi.",
        "ornek_ar": 'أَنَا أُطَوِّرُ مُسَاعِدَ الذَّكَاءِ الِاصْطِنَاعِيِّ.',
        "bengalce": 'আমি কম্পিউটারে পাইথন কোড লিখছি।',
        "ben_okunus": 'Ami kompiutare Python kod likhchi.',
        "ornek_bn": 'আমি পাইথন দিয়ে আমার নিজের এআই সহকারী তৈরি করছি।',
    },
    {
        "id": 17,
        "seviye": 'A2 (Temel Orta)',
        "kategori": 'Mühendislik & Projeler',
        "turkce": 'Otonom bir drone ve akıllı bebek arabası tasarlıyorum.',
        "ingilizce": 'I am designing an autonomous drone and a smart baby stroller.',
        "ing_okunus": 'Ay em dizayning en otonomıs dron end e smart beybi strolır.',
        "ornek_en": 'This project will compete in TEKNOFEST.',
        "arapca": 'أَنَا أُصَمِّمُ طَائِرَةً مُسَيَّرَةً ذَاتِيَّةً.',
        "ara_okunus": 'Ene usammimu tâiraten müseyyeraten zâtiyyeten.',
        "ornek_ar": 'سَيُشَارِكُ فِي تَكْنُوفِسْت.',
        "bengalce": 'আমি একটি স্বয়ংক্রিয় ড্রোন ডিজাইন করছি।',
        "ben_okunus": 'Ami ekti sboyongkriyo drone dijain korchi.',
        "ornek_bn": 'এই প্রজেক্টটি টেকনোফেস্টে অংশ নেবে।',
    },
    {
        "id": 18,
        "seviye": 'A2 (Temel Orta)',
        "kategori": 'Okul & Eğitim',
        "turkce": 'Matematik ve fizik derslerini çok seviyorum.',
        "ingilizce": 'I like mathematics and physics lessons very much.',
        "ing_okunus": 'Ay layk matematiks end fiziks lesıns veri maç.',
        "ornek_en": 'Solving square root and algebra problems is fun.',
        "arapca": 'أَنَا أُحِبُّ دُرُوسَ الرِّيَاضِيَّاتِ وَالْفِيزْيَاءِ.',
        "ara_okunus": "Ene uhibbu dürûse'r-riyâdiyyâti ve'l-fîzyâi.",
        "ornek_ar": 'حَلُّ مَسَائِلِ الْجَبْرِ مُمْتِعٌ جِدًّا.',
        "bengalce": 'আমি গণিত এবং পদার্থবিজ্ঞান ক্লাস খুব পছন্দ করি।',
        "ben_okunus": 'Ami gonit ebong podarthobiggan klas khub pochondo kori.',
        "ornek_bn": 'বীজগণিতের সমস্যা সমাধান করা খুব আনন্দের।',
    },
    {
        "id": 19,
        "seviye": 'A2 (Temel Orta)',
        "kategori": 'Günlük İfadeler',
        "turkce": 'Sabah erken uyanırım ve ödevlerimi tamamlarım.',
        "ingilizce": 'I wake up early in the morning and finish my homework.',
        "ing_okunus": 'Ay veyk ap örli in dı morning end finiş may homvörk.',
        "ornek_en": 'Regular sleep and discipline are important for success.',
        "arapca": 'أَسْتَيْقِظُ مُبَكِّرًا فِي الصَّبَاحِ.',
        "ara_okunus": "Esteykızu mübekkiran fi's-sabâhı.",
        "ornek_ar": 'النَّوْمُ الْمُنْتَظَمُ مُهِمٌّ لِلنَّجَاحِ.',
        "bengalce": 'আমি সকালে তাড়াতাড়ি উঠি এবং বাড়ির কাজ শেষ করি।',
        "ben_okunus": 'Ami shokale taratari uthi ebong barir kaj shesh kori.',
        "ornek_bn": 'নিয়মিত ঘুম সাফল্যের জন্য গুরুত্বপূর্ণ।',
    },
    {
        "id": 20,
        "seviye": 'A2 (Temel Orta)',
        "kategori": 'Spor & Hobiler',
        "turkce": 'Hafta sonu arkadaşlarımla futbol oynuyorum.',
        "ingilizce": 'I play football with my friends on the weekend.',
        "ing_okunus": 'Ay pley futbol vit may frendz on dı vikend.',
        "ornek_en": 'Galatasaray is my favorite football team.',
        "arapca": 'أَلْعَبُ كُرَةَ الْقَدَمِ مَعَ أَصْدِقَائِي.',
        "ara_okunus": "El'abu kürate'l-kademi mea esdıkâî.",
        "ornek_ar": 'فَرِيقِي الْمُفَضَّلُ هُوَ غَلَطَة سَرَاي.',
        "bengalce": 'সপ্তাহান্তে আমি বন্ধুদের সাথে ফুটবল খেলি।',
        "ben_okunus": 'Shoptahante ami bondhuder sathe futbol kheli.',
        "ornek_bn": 'গ্যালাতাসারাই আমার প্রিয় ফুটবল দল।',
    },
    {
        "id": 21,
        "seviye": 'A2 (Temel Orta)',
        "kategori": 'Yön & Ulaşım',
        "turkce": 'Okula veya kütüphaneye nasıl gidebilirim?',
        "ingilizce": 'How can I get to the school or the library?',
        "ing_okunus": 'Hav ken ay get tu dı skul or dı laybreri?',
        "ornek_en": 'Go straight ahead and turn right at the corner.',
        "arapca": 'كَيْفَ يُمْكِنُنِي الذَّهَابُ إِلَى الْمَدْرَسَةِ؟',
        "ara_okunus": "Keyfe yümkınunî ez-zehâbu ile'l-medreseti?",
        "ornek_ar": 'اِذْهَبْ مُبَاشَرَةً ثُمَّ انْعَطِفْ يَمِينًا.',
        "bengalce": 'আমি কীভাবে স্কুলে যেতে পারি?',
        "ben_okunus": 'Ami kibhabe skule jete pari?',
        "ornek_bn": 'সোজা সামনে যান এবং ডানে ঘুরুন।',
    },
    {
        "id": 22,
        "seviye": 'A2 (Temel Orta)',
        "kategori": 'Yardım & İletişim',
        "turkce": 'Lütfen biraz daha yavaş konuşabilir misiniz?',
        "ingilizce": 'Could you speak a little more slowly, please?',
        "ing_okunus": 'Kud yu spik e litıl mor slovli, pliz?',
        "ornek_en": 'Could you repeat that sentence, please?',
        "arapca": 'هَلْ يُمْكِنُكَ التَّحَدُّثُ بِبُطْءٍ؟',
        "ara_okunus": "Hel yümkınuke et-tehaddüsü bi-but'in?",
        "ornek_ar": 'هَلْ يُمْكِنُكَ إِعَادَةُ هَذِهِ الْجُمْلَةِ؟',
        "bengalce": 'দয়া করে আরেকটু ধীরে কথা বলতে পারবেন?',
        "ben_okunus": 'Doya kore arektu dhire kotha bolte parben?',
        "ornek_bn": 'দয়া করে এই বাক্যটি আবার বলবেন?',
    },
    {
        "id": 23,
        "seviye": 'A2 (Temel Orta)',
        "kategori": 'Teknoloji & Yazılım',
        "turkce": 'Sensör engeli algılar ve motorları otomatik durdurur.',
        "ingilizce": 'The sensor detects the obstacle and stops the motors automatically.',
        "ing_okunus": 'Dı sensör ditekts dı obstıkıl end stops dı motors otomatikli.',
        "ornek_en": 'Safety is the most important part of the system.',
        "arapca": 'يَكْتَشِفُ الْمُسْتَشْعِرُ الْعَائِقَ تِلْقَائِيًّا.',
        "ara_okunus": "Yekteşifu'l-müsteş'iru el-âika tilkâiyyen.",
        "ornek_ar": 'السَّلَامَةُ هِيَ أَهَمُّ جُزْءٍ.',
        "bengalce": 'সেন্সরটি বাধা শনাক্ত করে এবং মোটর থামিয়ে দেয়।',
        "ben_okunus": 'Sensorti badha shonakto kore ebong motor thamiye dey.',
        "ornek_bn": 'নিরাপত্তা সবচেয়ে গুরুত্বপূর্ণ অংশ।',
    },
    {
        "id": 24,
        "seviye": 'A2 (Temel Orta)',
        "kategori": 'Mühendislik & Projeler',
        "turkce": 'Gelecekte başarılı bir yazılım mühendisi olmak istiyorum.',
        "ingilizce": 'I want to become a successful software engineer in the future.',
        "ing_okunus": 'Ay vant tu bikam e saksesful softveyr encinir in dı fyuçır.',
        "ornek_en": 'Working hard every day brings great achievements.',
        "arapca": 'أُرِيدُ أَنْ أُصْبِحَ مُهَنْدِسَ بَرْمَجِيَّاتٍ نَاجِحًا.',
        "ara_okunus": 'Ürîdü en usbiha mühendise bermeciyyâtin nâcihan.',
        "ornek_ar": 'الْعَمَلُ الْجَادُّ يَجْلِبُ النَّجَاحَ.',
        "bengalce": 'আমি ভবিষ্যতে সফল সফটওয়্যার ইঞ্জিনিয়ার হতে চাই।',
        "ben_okunus": 'Ami bhobishshote shofol software injiniyar hote chai.',
        "ornek_bn": 'কঠোর পরিশ্রমে বড় সাফল্য আসে।',
    },
    {
        "id": 25,
        "seviye": 'A1 (Başlangıç)',
        "kategori": 'Günlük İfadeler',
        "turkce": 'Ev, okul ve kütüphane',
        "ingilizce": 'House, school and library',
        "ing_okunus": 'Hauz, skul end laybreri',
        "ornek_en": 'I go from my house to school and then to the library.',
        "arapca": 'بَيْتٌ، مَدْرَسَةٌ وَمَكْتَبَةٌ',
        "ara_okunus": 'Beytun, medresetün ve mektebetün',
        "ornek_ar": 'أَذْهَبُ مِنَ الْبَيْتِ إِلَى الْمَدْرَسَةِ.',
        "bengalce": 'বাড়ি, স্কুল এবং লাইব্রেরি',
        "ben_okunus": 'Bari, skul ebong laibreri',
        "ornek_bn": 'আমি বাড়ি থেকে স্কুলে ও লাইব্রেরিতে যাই।',
    },
    {
        "id": 26,
        "seviye": 'A1 (Başlangıç)',
        "kategori": 'Zaman & Saat',
        "turkce": 'Bugün hava çok güzel.',
        "ingilizce": 'The weather is very nice today.',
        "ing_okunus": 'Dı vedır iz veri nays tudey.',
        "ornek_en": 'The weather is sunny and warm today.',
        "arapca": 'الطَّقْسُ جَمِيلٌ جِدًّا الْيَوْمَ.',
        "ara_okunus": 'Et-taksu cemîlün cidden el-yevm.',
        "ornek_ar": 'الشَّمْسُ مُشْرِقَةٌ الْيَوْمَ.',
        "bengalce": 'আজ আবহাওয়া খুব সুন্দর।',
        "ben_okunus": 'Aj abohawa khub shundor.',
        "ornek_bn": 'আজ আকাশ পরিষ্কার এবং রোদেলা।',
    },
    {
        "id": 27,
        "seviye": 'A1 (Başlangıç)',
        "kategori": 'Aile & Kişiler',
        "turkce": 'Benim altı kardeşim var.',
        "ingilizce": 'I have six siblings.',
        "ing_okunus": 'Ay hev siks siblings.',
        "ornek_en": 'We are a big and happy family.',
        "arapca": 'لَدَيَّ سِتَّةُ إِخْوَةٍ.',
        "ara_okunus": 'Ledeyye sittetü ihvetin.',
        "ornek_ar": 'نَحْنُ عَائِلَةٌ سَعِيدَةٌ.',
        "bengalce": 'আমার ছয় ভাইবোন আছে।',
        "ben_okunus": 'Amar choy bhaibon ache.',
        "ornek_bn": 'আমরা একটি সুখী পরিবার।',
    },
    {
        "id": 28,
        "seviye": 'A1 (Başlangıç)',
        "kategori": 'Okul & Eğitim',
        "turkce": 'Öğretmen sınıfta ders anlatıyor.',
        "ingilizce": 'The teacher is teaching in the classroom.',
        "ing_okunus": 'Dı tiçır iz tiçing in dı klasrum.',
        "ornek_en": 'All students are listening carefully.',
        "arapca": 'الْمُعَلِّمُ يَشْرَحُ الدَّرْسَ فِي الصَّفِّ.',
        "ara_okunus": "El-muallimu yeşrahu'd-derse fi's-saffi.",
        "ornek_ar": 'الطُّلَّابُ يَسْتَمِعُونَ بِانْتِبَاهٍ.',
        "bengalce": 'শিক্ষক শ্রেণিকক্ষে পাঠদান করছেন।',
        "ben_okunus": 'Shikkhok shrenikokkhe pathdan korchen.',
        "ornek_bn": 'সব ছাত্রছাত্রী মনোযোগ দিয়ে শুনছে।',
    },
    {
        "id": 29,
        "seviye": 'A1 (Başlangıç)',
        "kategori": 'Günlük İhtiyaçlar',
        "turkce": 'Kahvaltıda çay ve peynir severim.',
        "ingilizce": 'I like tea and cheese for breakfast.',
        "ing_okunus": 'Ay layk ti end çiz for brekfıst.',
        "ornek_en": 'Turkish breakfast is delicious.',
        "arapca": 'أُحِبُّ الشَّايَ وَالْجُبْنَ فِي الْفَطُورِ.',
        "ara_okunus": "Uhibbu'ş-şâye ve'l-cübne fi'l-fatûri.",
        "ornek_ar": 'الْفَطُورُ التُّرْكِيُّ لَذِيذٌ جِدًّا.',
        "bengalce": 'আমি নাস্তায় চা এবং পনির পছন্দ করি।',
        "ben_okunus": 'Ami nastay cha ebong ponir pochondo kori.',
        "ornek_bn": 'সকালের নাস্তা খুব সুস্বাদু।',
    },
    {
        "id": 30,
        "seviye": 'A1 (Başlangıç)',
        "kategori": 'Yön & Ulaşım',
        "turkce": "İstanbul Türkiye'nin en büyük şehridir.",
        "ingilizce": 'Istanbul is the largest city in Turkey.',
        "ing_okunus": 'İstanbul iz dı larcıst siti in Törki.',
        "ornek_en": 'Istanbul connects Asia and Europe.',
        "arapca": 'إِسْطَنْبُولُ هِيَ أَكْبَرُ مَدِينَةٍ فِي تُرْكِيَا.',
        "ara_okunus": 'İstanbul hiye ekberu medînetin fî Türkiyâ.',
        "ornek_ar": 'إِسْطَنْبُولُ تَرْبِطُ آسْيَا وَأُورُوبَّا.',
        "bengalce": 'ইস্তাম্বুল তুরস্কের বৃহত্তম শহর।',
        "ben_okunus": 'Istambul Turosker brihottomo shohor.',
        "ornek_bn": 'ইস্তাম্বুল এশিয়া ও ইউরোপকে যুক্ত করেছে।',
    },
    {
        "id": 31,
        "seviye": 'A1 (Başlangıç)',
        "kategori": 'Okul & Eğitim',
        "turkce": 'Okumak, yazmak ve düşünmek',
        "ingilizce": 'To read, to write and to think',
        "ing_okunus": 'Tu rid, tu rayt end tu tink',
        "ornek_en": 'Reading books improves our thinking.',
        "arapca": 'الْقِرَاءَةُ، الْكِتَابَةُ وَالتَّفْكِيرُ',
        "ara_okunus": "El-kırâetü, el-kitâbetü ve't-tefkîru",
        "ornek_ar": 'قِرَاءَةُ الْكُتُبِ تُنَمِّي الْعَقْلَ.',
        "bengalce": 'পড়া, লেখা এবং চিন্তা করা',
        "ben_okunus": 'Pora, lekha ebong chinta kora',
        "ornek_bn": 'বই পড়া আমাদের চিন্তাশক্তি বাড়ায়।',
    },
    {
        "id": 32,
        "seviye": 'A1 (Başlangıç)',
        "kategori": 'Günlük İfadeler',
        "turkce": 'Koyu lacivert, mavi ve beyaz',
        "ingilizce": 'Dark navy, blue and white',
        "ing_okunus": 'Dark neyvi, blu end vayt',
        "ornek_en": 'My app interface uses dark navy and blue.',
        "arapca": 'أَزْرَقُ دَاكِنٌ، أَزْرَقُ وَأَبْيَضُ',
        "ara_okunus": 'Ezraku dâkinun, ezraku ve ebyadu',
        "ornek_ar": 'اللَّوْنُ الْأَزْرَقُ الدَّاكِنُ جَمِيلٌ.',
        "bengalce": 'গাঢ় নেভি, নীল এবং সাদা',
        "ben_okunus": 'Garho nebhi, nil ebong shada',
        "ornek_bn": 'গাঢ় নীল রং দেখতে খুব সুন্দর।',
    },
    {
        "id": 33,
        "seviye": 'A1 (Başlangıç)',
        "kategori": 'Temel Sorular',
        "turkce": 'Nerede yaşıyorsun?',
        "ingilizce": 'Where do you live?',
        "ing_okunus": 'Ver du yu liv?',
        "ornek_en": 'I live in Fatih, Istanbul.',
        "arapca": 'أَيْنَ تَعِيشُ؟',
        "ara_okunus": 'Eyne teîşu?',
        "ornek_ar": 'أَعِيشُ فِي مَدِينَةِ إِسْطَنْبُولَ.',
        "bengalce": 'আপনি কোথায় থাকেন?',
        "ben_okunus": 'Apni kothay thaken?',
        "ornek_bn": 'আমি ইস্তাম্বুলে থাকি।',
    },
    {
        "id": 34,
        "seviye": 'A1 (Başlangıç)',
        "kategori": 'Temel Sorular',
        "turkce": 'Kaç yaşındasın?',
        "ingilizce": 'How old are you?',
        "ing_okunus": 'Hav old ar yu?',
        "ornek_en": 'I am sixteen years old.',
        "arapca": 'كَمْ عُمْرُكَ؟',
        "ara_okunus": 'Kem umruke?',
        "ornek_ar": 'عُمْرِي سِتَّةَ عَشَرَ عَامًا.',
        "bengalce": 'আপনার বয়স কত?',
        "ben_okunus": 'Apnar boyosh koto?',
        "ornek_bn": 'আমার বয়স ষোল বছর।',
    },
    {
        "id": 35,
        "seviye": 'A1 (Başlangıç)',
        "kategori": 'Teknoloji & Yazılım',
        "turkce": 'Telefon ve bilgisayar ekranı',
        "ingilizce": 'Phone and computer screen',
        "ing_okunus": 'Fon end kompyutır skrin',
        "ornek_en": 'The design looks clean on both phone and computer.',
        "arapca": 'شَاشَةُ الْهَاتِفِ وَالْحَاسُوبِ',
        "ara_okunus": "Şâşetü'l-hâtifi ve'l-hâsûbi",
        "ornek_ar": 'التَّصْمِيمُ مُمْتَازٌ عَلَى الْهَاتِفِ.',
        "bengalce": 'ফোন এবং কম্পিউটারের পর্দা',
        "ben_okunus": 'Fon ebong kompiutarer porda',
        "ornek_bn": 'ফোন এবং কম্পিউটার দুই জায়গাতেই ভালো দেখায়।',
    },
    {
        "id": 36,
        "seviye": 'A1 (Başlangıç)',
        "kategori": 'Yardım & İletişim',
        "turkce": 'Özür dilerim, rica ederim.',
        "ingilizce": 'Excuse me, you are welcome.',
        "ing_okunus": 'Ekskyuz mi, yu ar velkım.',
        "ornek_en": 'Excuse me, can I ask a question? You are welcome!',
        "arapca": 'عَفْوًا، عَلَى الرَّحْبِ وَالسَّعَةِ.',
        "ara_okunus": "Afven, ale'r-rahbi ve's-seati.",
        "ornek_ar": 'أَهْلًا وَسَهْلًا بِكَ دَائِمًا.',
        "bengalce": 'দুঃখিত, আপনাকে স্বাগতম।',
        "ben_okunus": 'Dukkhito, apnake sbagotom.',
        "ornek_bn": 'আপনাকে সবসময় স্বাগতম।',
    },
    {
        "id": 37,
        "seviye": 'A2 (Temel Orta)',
        "kategori": 'Bilim & Tarih',
        "turkce": 'İslam âlimleri bilime büyük katkı sağladı.',
        "ingilizce": 'Islamic scholars made great contributions to science.',
        "ing_okunus": 'İslamik skolırs meyd greyt kontribyuşınz tu sayns.',
        "ornek_en": 'Al-Khwarizmi founded algebra and algorithms.',
        "arapca": 'قَدَّمَ عُلَمَاءُ الْإِسْلَامِ مُسَاهَمَاتٍ عَظِيمَةً لِلْعِلْمِ.',
        "ara_okunus": "Kaddeme ulemâu'l-İslâmi müsâhemâtin azîmeten.",
        "ornek_ar": 'الْخَوَارِزْمِيُّ أَسَّسَ عِلْمَ الْجَبْرِ.',
        "bengalce": 'ইসলামী পণ্ডিতগণ বিজ্ঞানে বিশাল অবদান রেখেছেন।',
        "ben_okunus": 'Islami ponditgon biggane bishal obodan rekhechen.',
        "ornek_bn": 'আল-খোয়ারিজমি বীজগণিত প্রতিষ্ঠা করেন।',
    },
    {
        "id": 38,
        "seviye": 'A2 (Temel Orta)',
        "kategori": 'Mühendislik & Projeler',
        "turkce": 'Elektrik motoru yüksek tork üretir.',
        "ingilizce": 'The electric motor produces high torque.',
        "ing_okunus": 'Dı elektrik motor prodüsuz hay tork.',
        "ornek_en": 'High torque helps the stroller climb hills easily.',
        "arapca": 'يُنْتِجُ الْمُحَرِّكُ الْكَهْرَبَائِيُّ عَزْمَ دَوَرَانٍ عَالٍ.',
        "ara_okunus": "Yünticü'l-muharrikü'l-kehrabâiyyü azme deverânin âlin.",
        "ornek_ar": 'الْعَزْمُ الْعَالِي يُسَاعِدُ فِي الصُّعُودِ.',
        "bengalce": 'বৈদ্যুতিক মোটর উচ্চ টর্ক উৎপন্ন করে।',
        "ben_okunus": 'Boiddutik motor uccho tork utponno kore.',
        "ornek_bn": 'উচ্চ টর্ক ঢালু পথে উঠতে সাহায্য করে।',
    },
    {
        "id": 39,
        "seviye": 'A2 (Temel Orta)',
        "kategori": 'Mühendislik & Projeler',
        "turkce": 'İnsansız hava aracı hedefe otonom uçar.',
        "ingilizce": 'The unmanned aerial vehicle flies autonomously to the target.',
        "ing_okunus": 'Dı anmend eriyıl viikıl flayz otonomısli tu dı targıt.',
        "ornek_en": 'Our UAV uses GPS and camera telemetry.',
        "arapca": 'تَطِيرُ الطَّائِرَةُ بِدُونِ طَيَّارٍ ذَاتِيًّا إِلَى الْهَدَفِ.',
        "ara_okunus": "Tetîru't-tâiratü bidûni tayyârin zâtiyyen ile'l-hedefi.",
        "ornek_ar": 'تَسْتَخْدِمُ نِظَامَ تَحْدِيدِ الْمَوَاقِعِ.',
        "bengalce": 'মনুষ্যবিহীন বিমানটি স্বয়ংক্রিয়ভাবে লক্ষ্যে উড়ে যায়।',
        "ben_okunus": 'Monusshobihin bimanti sboyongkriyobhabe lokkhe ure jay.',
        "ornek_bn": 'ড্রোনটি জিপিএস এবং ক্যামেরা ব্যবহার করে।',
    },
    {
        "id": 40,
        "seviye": 'A2 (Temel Orta)',
        "kategori": 'Teknoloji & Yazılım',
        "turkce": 'Veritabanı tüm bilgileri güvenle saklar.',
        "ingilizce": 'The database stores all information safely.',
        "ing_okunus": 'Dı deytabeys stors ol informeyşın seyfli.',
        "ornek_en": 'Every learned answer is saved in JSON memory.',
        "arapca": 'تَحْفَظُ قَاعِدَةُ الْبَيَانَاتِ جَمِيعَ الْمَعْلُومَاتِ بِأَمَانٍ.',
        "ara_okunus": "Tehfazu kâidetü'l-beyânâti cemîa'l-ma'lûmâti bi-emânin.",
        "ornek_ar": 'كُلُّ مَعْلُومَةٍ مَحْفُوظَةٌ فِي الذَّاكِرَةِ.',
        "bengalce": 'ডেটাবেস সমস্ত তথ্য নিরাপদে সংরক্ষণ করে।',
        "ben_okunus": 'Detabes shomosto tottho nirapode shongrokkhon kore.',
        "ornek_bn": 'সব শেখা উত্তর মেমোরিতে জমা থাকে।',
    },
    {
        "id": 41,
        "seviye": 'A1',
        "kategori": 'Günlük Yaşam',
        "turkce": 'Saat kaç?',
        "ingilizce": 'What time is it?',
        "ing_okunus": 'vat taym iz it',
        "ornek_en": 'Excuse me, what time is it now?',
        "arapca": 'كم الساعة؟',
        "ara_okunus": 'kem es-saa',
        "ornek_ar": 'كم الساعة الآن من فضلك؟',
        "bengalce": 'কয়টা বাজে?',
        "ben_okunus": 'koyta baje',
        "ornek_bn": 'দয়া করে বলবেন এখন কয়টা বাজে?',
    },
    {
        "id": 42,
        "seviye": 'A1',
        "kategori": 'Günlük Yaşam',
        "turkce": 'Bugün günlerden ne?',
        "ingilizce": 'What day is it today?',
        "ing_okunus": 'vat dey iz it tudey',
        "ornek_en": 'What day is it today, Monday or Tuesday?',
        "arapca": 'ما هو اليوم؟',
        "ara_okunus": 'ma huve el-yevm',
        "ornek_ar": 'ما هو اليوم، الإثنين أم الثلاثاء؟',
        "bengalce": 'আজ কী বার?',
        "ben_okunus": 'aj ki bar',
        "ornek_bn": 'আজ কী বার, সোমবার নাকি মঙ্গলবার?',
    },
    {
        "id": 43,
        "seviye": 'A1',
        "kategori": 'Günlük Yaşam',
        "turkce": 'Çok acıktım',
        "ingilizce": 'I am very hungry',
        "ing_okunus": 'ay em veri hangri',
        "ornek_en": 'I am very hungry after school.',
        "arapca": 'أنا جائع جداً',
        "ara_okunus": 'ene caiun cidden',
        "ornek_ar": 'أنا جائع جداً بعد المدرسة.',
        "bengalce": 'আমার খুব ক্ষুধা লেগেছে',
        "ben_okunus": 'amar khub khudha legeche',
        "ornek_bn": 'স্কুলের পর আমার খুব ক্ষুধা লেগেছে।',
    },
    {
        "id": 44,
        "seviye": 'A1',
        "kategori": 'Günlük Yaşam',
        "turkce": 'Su içmek istiyorum',
        "ingilizce": 'I want to drink water',
        "ing_okunus": 'ay vont tu drink votır',
        "ornek_en": 'I want to drink cold water.',
        "arapca": 'أريد أن أشرب الماء',
        "ara_okunus": 'uridu en eşreb el-ma',
        "ornek_ar": 'أريد أن أشرب ماءً بارداً.',
        "bengalce": 'আমি জল খেতে চাই',
        "ben_okunus": 'ami jol khete chai',
        "ornek_bn": 'আমি ঠান্ডা জল খেতে চাই।',
    },
    {
        "id": 45,
        "seviye": 'A1',
        "kategori": 'Günlük Yaşam',
        "turkce": 'Yorgunum',
        "ingilizce": 'I am tired',
        "ing_okunus": 'ay em tayırd',
        "ornek_en": 'I am tired today, I need rest.',
        "arapca": 'أنا متعب',
        "ara_okunus": "ene mut'ab",
        "ornek_ar": 'أنا متعب اليوم وأحتاج إلى راحة.',
        "bengalce": 'আমি ক্লান্ত',
        "ben_okunus": 'ami klanto',
        "ornek_bn": 'আমি আজ ক্লান্ত, বিশ্রাম দরকার।',
    },
    {
        "id": 46,
        "seviye": 'A1',
        "kategori": 'Aile',
        "turkce": 'Babam mühendis',
        "ingilizce": 'My father is an engineer',
        "ing_okunus": 'may fadır iz en enciniır',
        "ornek_en": 'My father is a great engineer.',
        "arapca": 'أبي مهندس',
        "ara_okunus": 'ebi muhendis',
        "ornek_ar": 'أبي مهندس رائع.',
        "bengalce": 'আমার বাবা একজন প্রকৌশলী',
        "ben_okunus": 'amar baba ekjon prokousholi',
        "ornek_bn": 'আমার বাবা একজন ভালো প্রকৌশলী।',
    },
    {
        "id": 47,
        "seviye": 'A1',
        "kategori": 'Aile',
        "turkce": 'Annem evde',
        "ingilizce": 'My mother is at home',
        "ing_okunus": 'may madır iz et hom',
        "ornek_en": 'My mother is cooking at home.',
        "arapca": 'أمي في البيت',
        "ara_okunus": 'ummi fil beyt',
        "ornek_ar": 'أمي تطبخ في البيت.',
        "bengalce": 'আমার মা বাড়িতে আছেন',
        "ben_okunus": 'amar ma barite achen',
        "ornek_bn": 'আমার মা বাড়িতে রান্না করছেন।',
    },
    {
        "id": 48,
        "seviye": 'A1',
        "kategori": 'Aile',
        "turkce": 'Kardeşim okula gidiyor',
        "ingilizce": 'My brother goes to school',
        "ing_okunus": 'may bradır goz tu skul',
        "ornek_en": 'My brother goes to school every morning.',
        "arapca": 'أخي يذهب إلى المدرسة',
        "ara_okunus": 'ehi yezhebu ilel medrese',
        "ornek_ar": 'أخي يذهب إلى المدرسة كل صباح.',
        "bengalce": 'আমার ভাই স্কুলে যায়',
        "ben_okunus": 'amar bhai skule jay',
        "ornek_bn": 'আমার ভাই প্রতিদিন সকালে স্কুলে যায়।',
    },
    {
        "id": 49,
        "seviye": 'A1',
        "kategori": 'Okul & Ders',
        "turkce": 'Matematik en sevdiğim ders',
        "ingilizce": 'Math is my favorite subject',
        "ing_okunus": 'met iz may feyvrit sabcekt',
        "ornek_en": 'Math is my favorite subject at school.',
        "arapca": 'الرياضيات مادتي المفضلة',
        "ara_okunus": 'er-riyadiyyat maddeti el-mufaddale',
        "ornek_ar": 'الرياضيات هي مادتي المفضلة في المدرسة.',
        "bengalce": 'গণিত আমার প্রিয় বিষয়',
        "ben_okunus": 'gonit amar priyo bishoy',
        "ornek_bn": 'গণিত স্কুলে আমার সবচেয়ে প্রিয় বিষয়।',
    },
    {
        "id": 50,
        "seviye": 'A1',
        "kategori": 'Okul & Ders',
        "turkce": 'Sınava hazırlanıyorum',
        "ingilizce": 'I am preparing for the exam',
        "ing_okunus": 'ay em pripering for dı igzem',
        "ornek_en": 'I am preparing for the math exam.',
        "arapca": 'أنا أستعد للامتحان',
        "ara_okunus": 'ene esteiddu lil imtihan',
        "ornek_ar": 'أنا أستعد لامتحان الرياضيات.',
        "bengalce": 'আমি পরীক্ষার প্রস্তুতি নিচ্ছি',
        "ben_okunus": 'ami porikkhar prostuti nicchi',
        "ornek_bn": 'আমি গণিত পরীক্ষার প্রস্তুতি নিচ্ছি।',
    },
    {
        "id": 51,
        "seviye": 'A1',
        "kategori": 'Okul & Ders',
        "turkce": 'Ödevimi bitirdim',
        "ingilizce": 'I finished my homework',
        "ing_okunus": 'ay finişd may homvörk',
        "ornek_en": 'I finished my homework before dinner.',
        "arapca": 'أنهيت واجبي المنزلي',
        "ara_okunus": 'enheytu vacibi el-menzili',
        "ornek_ar": 'أنهيت واجبي المنزلي قبل العشاء.',
        "bengalce": 'আমি আমার বাড়ির কাজ শেষ করেছি',
        "ben_okunus": 'ami amar barir kaj shesh korechi',
        "ornek_bn": 'আমি রাতের খাবারের আগে বাড়ির কাজ শেষ করেছি।',
    },
    {
        "id": 52,
        "seviye": 'A1',
        "kategori": 'Okul & Ders',
        "turkce": 'Defterim çantamda',
        "ingilizce": 'My notebook is in my bag',
        "ing_okunus": 'may notbuk iz in may beg',
        "ornek_en": 'My notebook is in my school bag.',
        "arapca": 'دفتري في حقيبتي',
        "ara_okunus": 'defteri fi hakibeti',
        "ornek_ar": 'دفتري في حقيبتي المدرسية.',
        "bengalce": 'আমার খাতা আমার ব্যাগে আছে',
        "ben_okunus": 'amar khata amar bage ache',
        "ornek_bn": 'আমার খাতা স্কুল ব্যাগে আছে।',
    },
    {
        "id": 53,
        "seviye": 'A1',
        "kategori": 'Teknoloji',
        "turkce": 'Bilgisayarımı açıyorum',
        "ingilizce": 'I am turning on my computer',
        "ing_okunus": 'ay em törning on may kompyutır',
        "ornek_en": 'I am turning on my computer to code.',
        "arapca": 'أشغل حاسوبي',
        "ara_okunus": 'uşağğilu hasubi',
        "ornek_ar": 'أشغل حاسوبي لكتابة الكود.',
        "bengalce": 'আমি আমার কম্পিউটার চালু করছি',
        "ben_okunus": 'ami amar kompiutar chalu korchi',
        "ornek_bn": 'কোড লেখার জন্য আমি কম্পিউটার চালু করছি।',
    },
    {
        "id": 54,
        "seviye": 'A1',
        "kategori": 'Teknoloji',
        "turkce": 'İnternet bağlantısı hızlı',
        "ingilizce": 'The internet connection is fast',
        "ing_okunus": 'dı intırnet konekşın iz fest',
        "ornek_en": 'The internet connection is very fast here.',
        "arapca": 'اتصال الإنترنت سريع',
        "ara_okunus": 'ittisal el-internet seri',
        "ornek_ar": 'اتصال الإنترنت سريع جداً هنا.',
        "bengalce": 'ইন্টারনেট সংযোগ দ্রুত',
        "ben_okunus": 'intarnet songjog druto',
        "ornek_bn": 'এখানে ইন্টারনেট সংযোগ খুব দ্রুত।',
    },
    {
        "id": 55,
        "seviye": 'A2',
        "kategori": 'Teknoloji',
        "turkce": 'Python ile kod yazıyorum',
        "ingilizce": 'I write code with Python',
        "ing_okunus": 'ay rayt kod vit paytın',
        "ornek_en": 'I write AI code with Python every day.',
        "arapca": 'أكتب الكود بلغة بايثون',
        "ara_okunus": 'ektubu el-kod bi-luğat baytun',
        "ornek_ar": 'أكتب كود الذكاء الاصطناعي بلغة بايثون.',
        "bengalce": 'আমি পাইথন দিয়ে কোড লিখি',
        "ben_okunus": 'ami paithon diye kod likhi',
        "ornek_bn": 'আমি প্রতিদিন পাইথন দিয়ে কোড লিখি।',
    },
    {
        "id": 56,
        "seviye": 'A2',
        "kategori": 'Teknoloji',
        "turkce": 'Hata ayıklama yapıyorum',
        "ingilizce": 'I am debugging the code',
        "ing_okunus": 'ay em dibaging dı kod',
        "ornek_en": 'I am debugging the Python module now.',
        "arapca": 'أقوم بتصحيح الأخطاء البرمجية',
        "ara_okunus": 'ekumu bi-tashih el-ahta el-bermeciyye',
        "ornek_ar": 'أقوم بتصحيح الأخطاء في وحدة بايثون.',
        "bengalce": 'আমি কোড ডিবাগ করছি',
        "ben_okunus": 'ami kod dibag korchi',
        "ornek_bn": 'আমি এখন পাইথন মডিউলটি ডিবাগ করছি।',
    },
    {
        "id": 57,
        "seviye": 'A2',
        "kategori": 'Teknoloji',
        "turkce": 'Dosyayı kaydet',
        "ingilizce": 'Save the file',
        "ing_okunus": 'seyv dı fayl',
        "ornek_en": 'Please save the file before closing.',
        "arapca": 'احفظ الملف',
        "ara_okunus": 'ihfaz el-milef',
        "ornek_ar": 'من فضلك احفظ الملف قبل الإغلاق.',
        "bengalce": 'ফাইলটি সংরক্ষণ করুন',
        "ben_okunus": 'failti songrokkhon korun',
        "ornek_bn": 'বন্ধ করার আগে দয়া করে ফাইলটি সংরক্ষণ করুন।',
    },
    {
        "id": 58,
        "seviye": 'A2',
        "kategori": 'Teknoloji',
        "turkce": 'Yeni bir özellik ekledim',
        "ingilizce": 'I added a new feature',
        "ing_okunus": 'ay edıd e nyu fiçır',
        "ornek_en": 'I added a new feature to my app.',
        "arapca": 'أضفت ميزة جديدة',
        "ara_okunus": 'adaftu mize cedide',
        "ornek_ar": 'أضفت ميزة جديدة إلى تطبيقي.',
        "bengalce": 'আমি একটি নতুন ফিচার যোগ করেছি',
        "ben_okunus": 'ami ekti notun fichar jog korechi',
        "ornek_bn": 'আমি আমার অ্যাপে একটি নতুন ফিচার যোগ করেছি।',
    },
    {
        "id": 59,
        "seviye": 'A2',
        "kategori": 'Mühendislik',
        "turkce": 'İHA uçuşa hazır',
        "ingilizce": 'The UAV is ready for flight',
        "ing_okunus": 'dı yu-ey-vi iz redi for flayt',
        "ornek_en": 'The UAV is ready for its test flight.',
        "arapca": 'الطائرة المسيرة جاهزة للطيران',
        "ara_okunus": 'et-taire el-museyyere cahize lit-tayaran',
        "ornek_ar": 'الطائرة المسيرة جاهزة لرحلة الاختبار.',
        "bengalce": 'ড্রোনটি ওড়ার জন্য প্রস্তুত',
        "ben_okunus": 'dronti orar jonno prostut',
        "ornek_bn": 'ড্রোনটি পরীক্ষামূলক উড্ডয়নের জন্য প্রস্তুত।',
    },
    {
        "id": 60,
        "seviye": 'A2',
        "kategori": 'Mühendislik',
        "turkce": 'Ağırlık merkezini hesapla',
        "ingilizce": 'Calculate the center of gravity',
        "ing_okunus": 'kelkyleyt dı sentır ov greviti',
        "ornek_en": 'We must calculate the center of gravity first.',
        "arapca": 'احسب مركز الثقل',
        "ara_okunus": 'ihsib merkez es-sikal',
        "ornek_ar": 'يجب أن نحسب مركز الثقل أولاً.',
        "bengalce": 'ভরকেন্দ্র হিসাব করুন',
        "ben_okunus": 'bhorkendro hisab korun',
        "ornek_bn": 'আমাদের প্রথমে ভরকেন্দ্র হিসাব করতে হবে।',
    },
    {
        "id": 61,
        "seviye": 'A2',
        "kategori": 'Mühendislik',
        "turkce": 'Batarya seviyesi yüzde seksen',
        "ingilizce": 'Battery level is eighty percent',
        "ing_okunus": 'betıri levıl iz eyti pörsent',
        "ornek_en": 'The battery level is eighty percent now.',
        "arapca": 'مستوى البطارية ثمانون بالمئة',
        "ara_okunus": "musteva el-battariye semanon bil-mi'e",
        "ornek_ar": 'مستوى البطارية ثمانون بالمئة الآن.',
        "bengalce": 'ব্যাটারির চার্জ আশি শতাংশ',
        "ben_okunus": 'byatarir charj ashi shotangsho',
        "ornek_bn": 'এখন ব্যাটারির চার্জ আশি শতাংশ।',
    },
    {
        "id": 62,
        "seviye": 'A2',
        "kategori": 'Mühendislik',
        "turkce": 'Kanat açıklığı iki metre',
        "ingilizce": 'Wingspan is two meters',
        "ing_okunus": 'vingspen iz tu mitırz',
        "ornek_en": 'The aircraft wingspan is two meters.',
        "arapca": 'باع الجناح متران',
        "ara_okunus": 'ba el-cinah mitran',
        "ornek_ar": 'باع الجناح للطائرة متران.',
        "bengalce": 'ডানার বিস্তার দুই মিটার',
        "ben_okunus": 'danar bistar dui mitar',
        "ornek_bn": 'বিমানটির ডানার বিস্তার দুই মিটার।',
    },
    {
        "id": 63,
        "seviye": 'A2',
        "kategori": 'Seyahat',
        "turkce": 'Havaalanı nerede?',
        "ingilizce": 'Where is the airport?',
        "ing_okunus": 'ver iz dı erport',
        "ornek_en": 'Excuse me, where is the nearest airport?',
        "arapca": 'أين المطار؟',
        "ara_okunus": 'eyne el-matar',
        "ornek_ar": 'عفواً، أين يقع أقرب مطار؟',
        "bengalce": 'বিমানবন্দর কোথায়?',
        "ben_okunus": 'bimanbondor kothay',
        "ornek_bn": 'মাফ করবেন, সবচেয়ে কাছের বিমানবন্দর কোথায়?',
    },
    {
        "id": 64,
        "seviye": 'A2',
        "kategori": 'Seyahat',
        "turkce": 'Bilet almak istiyorum',
        "ingilizce": 'I want to buy a ticket',
        "ing_okunus": 'ay vont tu bay e tikıt',
        "ornek_en": 'I want to buy a train ticket.',
        "arapca": 'أريد شراء تذكرة',
        "ara_okunus": 'uridu şira tezkire',
        "ornek_ar": 'أريد شراء تذكرة قطار.',
        "bengalce": 'আমি একটি টিকিট কিনতে চাই',
        "ben_okunus": 'ami ekti tikit kinte chai',
        "ornek_bn": 'আমি একটি ট্রেনের টিকিট কিনতে চাই।',
    },
    {
        "id": 65,
        "seviye": 'A2',
        "kategori": 'Seyahat',
        "turkce": 'Sağa dönün',
        "ingilizce": 'Turn right',
        "ing_okunus": 'törn rayt',
        "ornek_en": 'Turn right at the next corner.',
        "arapca": 'انعطف يميناً',
        "ara_okunus": "in'atif yeminen",
        "ornek_ar": 'انعطف يميناً عند الزاوية التالية.',
        "bengalce": 'ডানে ঘুরুন',
        "ben_okunus": 'dane ghurun',
        "ornek_bn": 'পরের মোড়ে ডানে ঘুরুন।',
    },
    {
        "id": 66,
        "seviye": 'A2',
        "kategori": 'Seyahat',
        "turkce": 'Sola dönün',
        "ingilizce": 'Turn left',
        "ing_okunus": 'törn left',
        "ornek_en": 'Turn left after the traffic light.',
        "arapca": 'انعطف يساراً',
        "ara_okunus": "in'atif yesaren",
        "ornek_ar": 'انعطف يساراً بعد إشارة المرور.',
        "bengalce": 'বামে ঘুরুন',
        "ben_okunus": 'bame ghurun',
        "ornek_bn": 'ট্রাফিক সিগন্যালের পর বামে ঘুরুন।',
    },
    {
        "id": 67,
        "seviye": 'A2',
        "kategori": 'Alışveriş',
        "turkce": 'Bunun fiyatı ne kadar?',
        "ingilizce": 'How much does this cost?',
        "ing_okunus": 'hav maç daz dis kost',
        "ornek_en": 'How much does this notebook cost?',
        "arapca": 'كم سعر هذا؟',
        "ara_okunus": "kem si'ru haza",
        "ornek_ar": 'كم سعر هذا الدفتر؟',
        "bengalce": 'এটার দাম কত?',
        "ben_okunus": 'etar dam koto',
        "ornek_bn": 'এই খাতাটির দাম কত?',
    },
    {
        "id": 68,
        "seviye": 'A2',
        "kategori": 'Alışveriş',
        "turkce": 'Biraz indirim yapabilir misiniz?',
        "ingilizce": 'Can you give a discount?',
        "ing_okunus": 'ken yu giv e diskaunt',
        "ornek_en": 'Can you give a small discount please?',
        "arapca": 'هل يمكنك عمل خصم؟',
        "ara_okunus": 'hel yumkinuke amel hasm',
        "ornek_ar": 'هل يمكنك عمل خصم بسيط من فضلك؟',
        "bengalce": 'আপনি কি একটু ছাড় দিতে পারবেন?',
        "ben_okunus": 'apni ki ektu char dite parben',
        "ornek_bn": 'দয়া করে কি একটু ছাড় দেবেন?',
    },
    {
        "id": 69,
        "seviye": 'A1',
        "kategori": 'Hava Durumu',
        "turkce": 'Bugün hava güneşli',
        "ingilizce": 'Today the weather is sunny',
        "ing_okunus": 'tudey dı vedır iz sani',
        "ornek_en": 'Today the weather is warm and sunny.',
        "arapca": 'الطقس مشمس اليوم',
        "ara_okunus": 'et-taks müşmis el-yevm',
        "ornek_ar": 'الطقس دافئ ومشمس اليوم.',
        "bengalce": 'আজ আবহাওয়া রৌদ্রোজ্জ্বল',
        "ben_okunus": 'aj abhawa roudrojjol',
        "ornek_bn": 'আজ আবহাওয়া উষ্ণ এবং রৌদ্রোজ্জ্বল।',
    },
    {
        "id": 70,
        "seviye": 'A1',
        "kategori": 'Hava Durumu',
        "turkce": 'Dışarıda yağmur yağıyor',
        "ingilizce": 'It is raining outside',
        "ing_okunus": 'it iz reyning autsayd',
        "ornek_en": 'Take an umbrella, it is raining outside.',
        "arapca": 'إنها تمطر في الخارج',
        "ara_okunus": 'inneha tumtir fil haric',
        "ornek_ar": 'خذ مظلة، إنها تمطر في الخارج.',
        "bengalce": 'বাইরে বৃষ্টি হচ্ছে',
        "ben_okunus": 'baire brishti hocche',
        "ornek_bn": 'ছাতা নিয়ে যাও, বাইরে বৃষ্টি হচ্ছে।',
    },
    {
        "id": 71,
        "seviye": 'A1',
        "kategori": 'Zaman',
        "turkce": 'Yarın görüşürüz',
        "ingilizce": 'See you tomorrow',
        "ing_okunus": 'si yu tumorov',
        "ornek_en": 'See you tomorrow morning at nine.',
        "arapca": 'أراك غداً',
        "ara_okunus": 'erake ğaden',
        "ornek_ar": 'أراك غداً صباحاً في الساعة التاسعة.',
        "bengalce": 'আগামীকাল দেখা হবে',
        "ben_okunus": 'agamikal dekha hobe',
        "ornek_bn": 'আগামীকাল সকাল নয়টায় দেখা হবে।',
    },
    {
        "id": 72,
        "seviye": 'A1',
        "kategori": 'Zaman',
        "turkce": 'Geçen hafta çok çalıştım',
        "ingilizce": 'I worked hard last week',
        "ing_okunus": 'ay vörkd hard lest vik',
        "ornek_en": 'I worked hard on my project last week.',
        "arapca": 'عملت بجد الأسبوع الماضي',
        "ara_okunus": 'amiltu bi-cidd el-usbu el-madi',
        "ornek_ar": 'عملت بجد على مشروعي الأسبوع الماضي.',
        "bengalce": 'গত সপ্তাহে আমি কঠোর পরিশ্রম করেছি',
        "ben_okunus": 'goto soptahe ami kothor porishrom korechi',
        "ornek_bn": 'গত সপ্তাহে আমি আমার প্রজেক্টে কঠোর পরিশ্রম করেছি।',
    },
    {
        "id": 73,
        "seviye": 'A2',
        "kategori": 'Sohbet',
        "turkce": 'Fikrine katılıyorum',
        "ingilizce": 'I agree with your idea',
        "ing_okunus": 'ay egri vit yor aydiya',
        "ornek_en": 'I completely agree with your idea.',
        "arapca": 'أتفق مع فكرتك',
        "ara_okunus": 'ettefiku mea fikretike',
        "ornek_ar": 'أتفق تماماً مع فكرتك.',
        "bengalce": 'আমি তোমার ধারণার সাথে একমত',
        "ben_okunus": 'ami tomar dharonar sathe ekmot',
        "ornek_bn": 'আমি তোমার ধারণার সাথে পুরোপুরি একমত।',
    },
    {
        "id": 74,
        "seviye": 'A2',
        "kategori": 'Sohbet',
        "turkce": 'Bunu açıklayabilir misin?',
        "ingilizce": 'Can you explain this?',
        "ing_okunus": 'ken yu ikspleyn dis',
        "ornek_en": 'Can you explain this step again?',
        "arapca": 'هل يمكنك شرح هذا؟',
        "ara_okunus": 'hel yumkinuke şerh haza',
        "ornek_ar": 'هل يمكنك شرح هذه الخطوة مرة أخرى؟',
        "bengalce": 'তুমি কি এটা ব্যাখ্যা করতে পারবে?',
        "ben_okunus": 'tumi ki eta byakhya korte parbe',
        "ornek_bn": 'তুমি কি এই ধাপটি আবার ব্যাখ্যা করতে পারবে?',
    },
    {
        "id": 75,
        "seviye": 'A2',
        "kategori": 'Sohbet',
        "turkce": 'Harika bir fikir!',
        "ingilizce": 'That is a great idea!',
        "ing_okunus": 'det iz e gret aydiya',
        "ornek_en": 'That is a great idea for our team!',
        "arapca": 'هذه فكرة رائعة!',
        "ara_okunus": 'hazihi fikre raia',
        "ornek_ar": 'هذه فكرة رائعة لفريقنا!',
        "bengalce": 'এটি একটি দারুণ ধারণা!',
        "ben_okunus": 'eti ekti darun dharona',
        "ornek_bn": 'আমাদের দলের জন্য এটি একটি দারুণ ধারণা!',
    },
    {
        "id": 76,
        "seviye": 'A2',
        "kategori": 'Sohbet',
        "turkce": 'Emin değilim',
        "ingilizce": 'I am not sure',
        "ing_okunus": 'ay em not şur',
        "ornek_en": 'I am not sure about the answer yet.',
        "arapca": 'لست متأكداً',
        "ara_okunus": 'lestu muteekkiden',
        "ornek_ar": 'لست متأكداً من الإجابة بعد.',
        "bengalce": 'আমি নিশ্চিত নই',
        "ben_okunus": 'ami nishchit noi',
        "ornek_bn": 'আমি এখনো উত্তরটি সম্পর্কে নিশ্চিত নই।',
    },
    {
        "id": 77,
        "seviye": 'B1',
        "kategori": 'İleri İfade',
        "turkce": 'Elinden gelenin en iyisini yap',
        "ingilizce": 'Do your best',
        "ing_okunus": 'du yor best',
        "ornek_en": 'Always do your best in every project.',
        "arapca": 'ابذل قصارى جهدك',
        "ara_okunus": 'ibzil kusara cuhdike',
        "ornek_ar": 'ابذل قصارى جهدك دائماً في كل مشروع.',
        "bengalce": 'তোমার সর্বোচ্চ চেষ্টা করো',
        "ben_okunus": 'tomar sorbocco chesta koro',
        "ornek_bn": 'সব প্রজেক্টে সবসময় তোমার সর্বোচ্চ চেষ্টা করো।',
    },
    {
        "id": 78,
        "seviye": 'B1',
        "kategori": 'İleri İfade',
        "turkce": 'Adım adım ilerleyelim',
        "ingilizce": 'Let us go step by step',
        "ing_okunus": 'let as go step bay step',
        "ornek_en": 'Let us go step by step to solve this.',
        "arapca": 'لنمشِ خطوة بخطوة',
        "ara_okunus": 'linemşi hatve bi-hatve',
        "ornek_ar": 'لنمشِ خطوة بخطوة لحل هذا.',
        "bengalce": 'চলো ধাপে ধাপে এগোই',
        "ben_okunus": 'cholo dhape dhape egoi',
        "ornek_bn": 'এটি সমাধান করতে চলো ধাপে ধাপে এগোই।',
    },
    {
        "id": 79,
        "seviye": 'B1',
        "kategori": 'İleri İfade',
        "turkce": 'Sonuçları karşılaştıralım',
        "ingilizce": 'Let us compare the results',
        "ing_okunus": 'let as komper dı rizalts',
        "ornek_en": 'Let us compare the test results now.',
        "arapca": 'لنقارن النتائج',
        "ara_okunus": 'linukarin en-netaic',
        "ornek_ar": 'لنقارن نتائج الاختبار الآن.',
        "bengalce": 'চলো ফলাফলগুলো তুলনা করি',
        "ben_okunus": 'cholo folafolgulo tulona kori',
        "ornek_bn": 'চলো এখন পরীক্ষার ফলাফলগুলো তুলনা করি।',
    },
    {
        "id": 80,
        "seviye": 'B1',
        "kategori": 'İleri İfade',
        "turkce": 'Önemli olan devam etmektir',
        "ingilizce": 'What matters is to keep going',
        "ing_okunus": 'vat metırz iz tu kip going',
        "ornek_en": 'What matters is to keep going and learning.',
        "arapca": 'المهم هو الاستمرار',
        "ara_okunus": 'el-muhim huvel istimrar',
        "ornek_ar": 'المهم هو الاستمرار في التعلم.',
        "bengalce": 'গুরুত্বপূর্ণ হলো এগিয়ে যাওয়া',
        "ben_okunus": 'guruttopurno holo egiye jawa',
        "ornek_bn": 'গুরুত্বপূর্ণ হলো শেখা চালিয়ে যাওয়া।',
    },
    {
        "id": 81,
        "seviye": 'A1',
        "kategori": 'Yemek',
        "turkce": 'Kahvaltı hazır',
        "ingilizce": 'Breakfast is ready',
        "ing_okunus": 'brekfıst iz redi',
        "ornek_en": 'Breakfast is ready on the table.',
        "arapca": 'الإفطار جاهز',
        "ara_okunus": 'el-iftar cahiz',
        "ornek_ar": 'الإفطار جاهز على الطاولة.',
        "bengalce": 'সকালের নাস্তা তৈরি',
        "ben_okunus": 'sokaler nasta toiri',
        "ornek_bn": 'টেবিলে সকালের নাস্তা তৈরি।',
    },
    {
        "id": 82,
        "seviye": 'A1',
        "kategori": 'Yemek',
        "turkce": 'Çay severim',
        "ingilizce": 'I like tea',
        "ing_okunus": 'ay layk ti',
        "ornek_en": 'I like hot Turkish tea in the morning.',
        "arapca": 'أحب الشاي',
        "ara_okunus": 'uhibbu eş-şay',
        "ornek_ar": 'أحب الشاي الساخن في الصباح.',
        "bengalce": 'আমি চা পছন্দ করি',
        "ben_okunus": 'ami cha pochondo kori',
        "ornek_bn": 'আমি সকালে গরম চা পছন্দ করি।',
    },
    {
        "id": 83,
        "seviye": 'A1',
        "kategori": 'Sağlık',
        "turkce": 'Kendimi iyi hissediyorum',
        "ingilizce": 'I feel good',
        "ing_okunus": 'ay fil gud',
        "ornek_en": 'I feel good and energetic today.',
        "arapca": 'أشعر أنني بخير',
        "ara_okunus": "eş'uru enneni bi-hayr",
        "ornek_ar": 'أشعر أنني بخير ونشيط اليوم.',
        "bengalce": 'আমি ভালো অনুভব করছি',
        "ben_okunus": 'ami bhalo onubhob korchi',
        "ornek_bn": 'আজ আমি ভালো এবং উদ্যমী অনুভব করছি।',
    },
    {
        "id": 84,
        "seviye": 'A1',
        "kategori": 'Sağlık',
        "turkce": 'Biraz dinlenmeliyim',
        "ingilizce": 'I should rest a little',
        "ing_okunus": 'ay şud rest e litıl',
        "ornek_en": 'I should rest a little after studying.',
        "arapca": 'يجب أن أرتاح قليلاً',
        "ara_okunus": 'yecibu en ertah kalilen',
        "ornek_ar": 'يجب أن أرتاح قليلاً بعد الدراسة.',
        "bengalce": 'আমার একটু বিশ্রাম নেওয়া উচিত',
        "ben_okunus": 'amar ektu bishram newa uchit',
        "ornek_bn": 'পড়াশোনার পর আমার একটু বিশ্রাম নেওয়া উচিত।',
    },
    {
        "id": 85,
        "seviye": 'A2',
        "kategori": 'Spor',
        "turkce": 'Her gün yürüyüş yapıyorum',
        "ingilizce": 'I walk every day',
        "ing_okunus": 'ay vok evri dey',
        "ornek_en": 'I walk for thirty minutes every day.',
        "arapca": 'أمشي كل يوم',
        "ara_okunus": 'emşi kulle yevm',
        "ornek_ar": 'أمشي لمدة ثلاثين دقيقة كل يوم.',
        "bengalce": 'আমি প্রতিদিন হাঁটি',
        "ben_okunus": 'ami protidin hati',
        "ornek_bn": 'আমি প্রতিদিন ত্রিশ মিনিট হাঁটি।',
    },
    {
        "id": 86,
        "seviye": 'A2',
        "kategori": 'Spor',
        "turkce": 'Takım oyunu önemlidir',
        "ingilizce": 'Teamwork is important',
        "ing_okunus": 'timvörk iz importınt',
        "ornek_en": 'Teamwork is very important in competitions.',
        "arapca": 'العمل الجماعي مهم',
        "ara_okunus": 'el-amel el-cemai muhim',
        "ornek_ar": 'العمل الجماعي مهم جداً في المسابقات.',
        "bengalce": 'দলগত কাজ গুরুত্বপূর্ণ',
        "ben_okunus": 'dologoto kaj guruttopurno',
        "ornek_bn": 'প্রতিযোগিতায় দলগত কাজ খুব গুরুত্বপূর্ণ।',
    },
    {
        "id": 87,
        "seviye": 'A2',
        "kategori": 'Bilim',
        "turkce": 'Deney başarılı oldu',
        "ingilizce": 'The experiment succeeded',
        "ing_okunus": 'dı iksperimınt saksidıd',
        "ornek_en": 'Our science experiment succeeded today!',
        "arapca": 'نجحت التجربة',
        "ara_okunus": 'necehat et-tecribe',
        "ornek_ar": 'نجحت تجربتنا العلمية اليوم!',
        "bengalce": 'পরীক্ষাটি সফল হয়েছে',
        "ben_okunus": 'porikkhati sofol hoyeche',
        "ornek_bn": 'আজ আমাদের বিজ্ঞান পরীক্ষাটি সফল হয়েছে!',
    },
    {
        "id": 88,
        "seviye": 'A2',
        "kategori": 'Bilim',
        "turkce": 'Verileri analiz ediyoruz',
        "ingilizce": 'We are analyzing the data',
        "ing_okunus": 'vi ar enalayzing dı deyta',
        "ornek_en": 'We are analyzing the sensor data carefully.',
        "arapca": 'نحن نحلل البيانات',
        "ara_okunus": 'nahnu nuhallil el-beyanat',
        "ornek_ar": 'نحن نحلل بيانات المستشعر بعناية.',
        "bengalce": 'আমরা ডেটা বিশ্লেষণ করছি',
        "ben_okunus": 'amra deta bishleshon korchi',
        "ornek_bn": 'আমরা সেন্সরের ডেটা মনোযোগ দিয়ে বিশ্লেষণ করছি।',
    },
    {
        "id": 89,
        "seviye": 'B1',
        "kategori": 'Motivasyon',
        "turkce": 'Asla vazgeçme',
        "ingilizce": 'Never give up',
        "ing_okunus": 'nevır giv ap',
        "ornek_en": 'Never give up on your big dreams.',
        "arapca": 'لا تستسلم أبداً',
        "ara_okunus": 'la testeslim ebeden',
        "ornek_ar": 'لا تستسلم أبداً لأحلامك الكبيرة.',
        "bengalce": 'কখনো হাল ছেড়ো না',
        "ben_okunus": 'kokhono hal chero na',
        "ornek_bn": 'তোমার বড় স্বপ্নগুলো থেকে কখনো হাল ছেড়ো না।',
    },
    {
        "id": 90,
        "seviye": 'B1',
        "kategori": 'Motivasyon',
        "turkce": 'Başarı sabır ister',
        "ingilizce": 'Success requires patience',
        "ing_okunus": 'sakses rikvayırz peyşıns',
        "ornek_en": 'Great success always requires patience.',
        "arapca": 'النجاح يتطلب الصبر',
        "ara_okunus": 'en-necah yetetalleb es-sabr',
        "ornek_ar": 'النجاح العظيم يتطلب الصبر دائماً.',
        "bengalce": 'সাফল্যের জন্য ধৈর্য দরকার',
        "ben_okunus": 'safoller jonno dhoirjo dorkar',
        "ornek_bn": 'বড় সাফল্যের জন্য সবসময় ধৈর্য দরকার।',
    },
]

# 41..100 ARASI TAMAMI ÖZGÜN 60 YENİ KART (TOPLAM 100 FARKLI KART)
_YENI_KART_VERILERI = [
    (41, "A1 (Başlangıç)", "Günlük İfadeler", "Lütfen bekle, geliyorum.", "Please wait, I am coming.", "Pliz veyt, ay em kaming.", "مَنْ فَضْلِكَ انْتَظِرْ، أَنَا قَادِمٌ.", "Min fadlike intazır, ene kâdim.", "দয়া করে অপেক্ষা করুন, আমি আসছি।", "Doya kore opekkha korun, ami ashchi."),
    (42, "A1 (Başlangıç)", "Günlük İfadeler", "Anlıyorum / Anlamıyorum", "I understand / I don't understand", "Ay andırstend / Ay dont andırstend", "أَفْهَمُ / لَا أَفْهَمُ", "Efhemu / Lâ efhemu", "আমি বুঝি / আমি বুঝি না", "Ami bujhi / Ami bujhi na"),
    (43, "A1 (Başlangıç)", "Temel Sorular", "Bu ne kadar?", "How much is this?", "Hav maç iz dis?", "بِكَمْ هَذَا؟", "Bikem hâzâ?", "এটার দাম কত?", "Etar dam koto?"),
    (44, "A1 (Başlangıç)", "Temel Sorular", "Neden? Çünkü...", "Why? Because...", "Vay? Bikoz...", "لِمَاذَا؟ لِأَنَّ...", "Limâzâ? Li-enne...", "কেন? কারণ...", "Keno? Karon..."),
    (45, "A1 (Başlangıç)", "Zaman & Saat", "Dün, bugün, yarın", "Yesterday, today, tomorrow", "Yestırdey, tudey, tumorov", "أَمْسِ، الْيَوْمَ، غَدًا", "Emsi, el-yevme, gaden", "গতকাল, আজ, আগামীকাল", "Gotokal, aj, agamikal"),
    (46, "A1 (Başlangıç)", "Zaman & Saat", "Sabah, öğle, akşam", "Morning, noon, evening", "Morning, nun, ivning", "صَبَاحٌ، ظُهْرٌ، مَسَاءٌ", "Sabâh, zuhr, mesâ", "সকাল, দুপুর, সন্ধ্যা", "Shokal, dupur, shondhya"),
    (47, "A1 (Başlangıç)", "Sayılar & Hesap", "On, yirmi, otuz, kırk, elli", "Ten, twenty, thirty, forty, fifty", "Ten, tventi, törti, forti, fifti", "عَشَرَةٌ، عِشْرُونَ، ثَلَاثُونَ، أَرْبَعُونَ، خَمْسُونَ", "Aşera, işrûn, selâsûn, erbaûn, hamsûn", "দশ, বিশ, ত্রিশ, চল্লিশ, পঞ্চাশ", "Dosh, bish, trish, chollish, ponchash"),
    (48, "A1 (Başlangıç)", "Sayılar & Hesap", "Yüz ve bin", "One hundred and one thousand", "Van handrıd end van tauzınd", "مِائَةٌ وَأَلْفٌ", "Mietun ve elfun", "একশ এবং এক হাজার", "Eksho ebong ek hajar"),
    (49, "A1 (Başlangıç)", "Günlük İhtiyaçlar", "Acıktım ve susadım.", "I am hungry and thirsty.", "Ay em hangri end törsti.", "أَنَا جَائِعٌ وَعَطْشَانُ.", "Ene câiun ve atşânu.", "আমি ক্ষুধার্ত এবং তৃষ্ণার্ত।", "Ami khudharto ebong trishnarto."),
    (50, "A1 (Başlangıç)", "Günlük İhtiyaçlar", "Kahve veya çay ister misin?", "Would you like coffee or tea?", "Vud yu layk kofi or ti?", "هَلْ تُرِيدُ قَهْوَةً أَوْ شَايًا؟", "Hel türîdü kahveten ev şâyen?", "আপনি কি কফি না চা পছন্দ করবেন?", "Apni ki kofi na cha pochondo korben?"),
    (51, "A1 (Başlangıç)", "Yön & Ulaşım", "Sağa dön, sola dön, düz git.", "Turn right, turn left, go straight.", "Törn rayt, törn left, go streyt.", "اِنْعَطِفْ يَمِينًا، يَسَارًا، اِذْهَبْ مُبَاشَرَةً.", "İn'atıf yemînen, yesâren, izheb mübâşeraten.", "ডানে ঘুরুন, বামে ঘুরুন, সোজা যান।", "Dane ghurun, bame ghurun, shoja jan."),
    (52, "A1 (Başlangıç)", "Yön & Ulaşım", "Otobüs durağı nerede?", "Where is the bus stop?", "Ver iz dı bas stop?", "أَيْنَ مَوْقِفُ الْحَافِلَةِ؟", "Eyne mevkıfu'l-hâfileti?", "বাস স্টপ কোথায়?", "Bus stop kothay?"),
    (53, "A1 (Başlangıç)", "Aile & Kişiler", "Erkek kardeşim ve kız kardeşim", "My brother and my sister", "May bradır end may sistır", "أَخِي وَأُخْتِي", "Ehî ve uhtî", "আমার ভাই এবং আমার বোন", "Amar bhai ebong amar bon"),
    (54, "A1 (Başlangıç)", "Aile & Kişiler", "En iyi arkadaşım", "My best friend", "May best frend", "أَفْضَلُ صَدِيقٍ لِي", "Efdalü sadîkın lî", "আমার সবচেয়ে ভালো বন্ধু", "Amar shobcheye bhalo bondhu"),
    (55, "A1 (Başlangıç)", "Günlük İfadeler", "Sorun değil, önemli değil.", "No problem, it is okay.", "No problım, it iz okey.", "لَا مُشْكِلَةَ، لَا بَأْسَ.", "Lâ müşkilete, lâ be'se.", "কোনো সমস্যা নেই, ঠিক আছে।", "Kono shomossha nei, thik ache."),
    (56, "A1 (Başlangıç)", "Günlük İfadeler", "Görüşmek üzere, kendine iyi bak!", "See you later, take care!", "Si yu leytır, teyk keyr!", "أَرَاكَ لَاحِقًا، اِعْتَنِ بِنَفْسِكَ!", "Erâke lâhikan, i'teni bi-nefsike!", "পরে দেখা হবে, ভালো থাকবেন!", "Pore dekha hobe, bhalo thakben!"),
    (57, "A1 (Başlangıç)", "Okul & Eğitim", "Matematik sınavım yarın.", "My math exam is tomorrow.", "May met igzem iz tumorov.", "اِمْتِحَانُ الرِّيَاضِيَّاتِ غَدًا.", "İmtihânü'r-riyâdiyyâti gaden.", "আমার গণিত পরীক্ষা আগামীকাল।", "Amar gonit porikkha agamikal."),
    (58, "A1 (Başlangıç)", "Okul & Eğitim", "Yeni kelimeler ezberliyorum.", "I am memorizing new words.", "Ay em memorayzing nyu vördz.", "أَحْفَظُ كَلِمَاتٍ جَدِيدَةً.", "Ehfazu kelimâtin cedîdeten.", "আমি নতুন শব্দ মুখস্থ করছি।", "Ami notun shobdo mukhostho korchi."),
    (59, "A1 (Başlangıç)", "Spor & Hobiler", "Yüzmeyi ve koşmayı seviyorum.", "I love swimming and running.", "Ay lav sviming end raning.", "أُحِبُّ السِّبَاحَةَ وَالْجَرْيَ.", "Uhibbu's-sibâhate ve'l-cerye.", "আমি সাঁতার কাটতে এবং দৌড়াতে ভালোবাসি।", "Ami shatar katte ebong dourate bhalobashi."),
    (60, "A1 (Başlangıç)", "Spor & Hobiler", "Her gün spor yapıyorum.", "I do sports every day.", "Ay du sports evri dey.", "أُمَارِسُ الرِّيَاضَةَ كُلَّ يَوْمٍ.", "Ümârisü'r-riyâdate külle yevmin.", "আমি প্রতিদিন ব্যায়াম করি।", "Ami protidin byayam kori."),
    (61, "A2 (Temel Orta)", "Teknoloji & Yazılım", "Uygulamayı telefonda test ediyorum.", "I am testing the app on my phone.", "Ay em testing di ep on may fon.", "أَخْتَبِرُ التَّطْبِيقَ عَلَى هَاتِفِي.", "Ehtebirü't-tatbîka alâ hâtifî.", "আমি আমার ফোনে অ্যাপটি পরীক্ষা করছি।", "Ami amar fone appti porikkha korchi."),
    (62, "A2 (Temel Orta)", "Teknoloji & Yazılım", "Bu kod hatasını düzelttim.", "I fixed this code error.", "Ay fikst dis kod erır.", "أَصْلَحْتُ هَذَا الْخَطَأَ الْبَرْمَجِيَّ.", "Eslahtü hâze'l-hatae'l-bermeciyye.", "আমি এই কোডের ভুলটি ঠিক করেছি।", "Ami ei koder bhulti thik korechi."),
    (63, "A2 (Temel Orta)", "Teknoloji & Yazılım", "Yapay zeka sorularımı hızlıca yanıtlıyor.", "Artificial intelligence answers my questions quickly.", "Artifişıl intelicıns ensırs may kvesçıns kvikli.", "الذَّكَاءُ الِاصْطِنَاعِيُّ يُجِيبُ بِسُرْعَةٍ.", "Ez-zekâü'l-ıstınâiyyu yücîbü bi-sür'atin.", "কৃত্রিম বুদ্ধিমত্তা দ্রুত উত্তর দেয়।", "Kritrim buddhimotta druto uttor dey."),
    (64, "A2 (Temel Orta)", "Teknoloji & Yazılım", "İnternet bağlantısı çok hızlı.", "The internet connection is very fast.", "Dı intırnet konekşın iz veri fest.", "اِتِّصَالُ الْإِنْتَرْنِت سَرِيعٌ جِدًّا.", "İttisâlü'l-internet serîun cidden.", "ইন্টারনেট সংযোগ খুব দ্রুত।", "Internet shongjog khub druto."),
    (65, "A2 (Temel Orta)", "Matematik & Bilim", "Bu denklemi çözebilir misin?", "Can you solve this equation?", "Ken yu solv dis ikveyjın?", "هَلْ يُمْكِنُكَ حَلُّ هَذِهِ الْمُعَادَلَةِ؟", "Hel yümkınuke hallü hâzihi'l-muâdeleti?", "আপনি কি এই সমীকরণটি সমাধান করতে পারবেন?", "Apni ki ei shomikoronti shomadhan korte parben?"),
    (66, "A2 (Temel Orta)", "Matematik & Bilim", "İki sayıyı çarpıp sonucu bulalım.", "Let's multiply the two numbers and find the result.", "Lets maltıplay dı tu nambırs end faynd dı rizalt.", "لِنَضْرِبِ الرَّقْمَيْنِ وَنَجِدَ النَّتِيجَةَ.", "Li-nadribi'r-rakmeyni ve necide'n-netîcete.", "চলুন দুটি সংখ্যা গুণ করে ফলাফল বের করি।", "Cholun duti shongkha gun kore folafol ber kori."),
    (67, "A2 (Temel Orta)", "Matematik & Bilim", "Üçgenin iç açıları toplamı 180 derecedir.", "The sum of the interior angles of a triangle is 180 degrees.", "Dı sam of di intiriyır engıls of e trayengıl iz van handrıd eyti digriz.", "مَجْمُوعُ زَوَايَا الْمُثَلَّثِ 180 دَرَجَةً.", "Mecmûu zevâya'l-müsellesi 180 dereceten.", "ত্রিভুজের তিন কোণের সমষ্টি ১৮০ ডিগ্রি।", "Tribhujer tin koner shomoshti 180 digri."),
    (68, "A2 (Temel Orta)", "Mühendislik & Projeler", "Pil dolduğunda sistem çalışmaya başlar.", "When the battery is full, the system starts working.", "Ven dı betıri iz ful, dı sistım starts vörking.", "عِنْدَمَا تَمْتَلِئُ الْبَطَّارِيَّةُ يَبْدَأُ النِّظَامُ.", "İndemâ temteliü'l-battâriyyetü yebdeü'n-nizâm.", "ব্যাটারি পূর্ণ হলে সিস্টেম কাজ শুরু করে।", "Byatari purno hole sistem kaj shuru kore."),
    (69, "A2 (Temel Orta)", "Mühendislik & Projeler", "3D yazıcı yeni parçayı üretiyor.", "The 3D printer is producing the new part.", "Dı tri-di printır iz prodyusing dı nyu part.", "الطَّابِعَةُ ثُلَاثِيَّةُ الْأَبْعَادِ تَطْبَعُ الْقِطْعَةَ.", "Et-tâbiatü sülâsiyyetü'l-eb'âdi tatbau'l-kıt'a.", "থ্রিডি প্রিন্টার নতুন অংশটি তৈরি করছে।", "3D printar notun ongshoti toiri korche."),
    (70, "A2 (Temel Orta)", "Mühendislik & Projeler", "Kameradan gelen görüntüyü analiz ediyoruz.", "We are analyzing the image from the camera.", "Vi ar enalayzing dı imic from dı kemıra.", "نَحْنُ نُحَلِّلُ الصُّورَةَ مِنَ الْكَامِيرَا.", "Nahnu nuhallilü's-sûrate mine'l-kâmîrâ.", "আমরা ক্যামেরার ছবি বিশ্লেষণ করছি।", "Amra kyamerar chobi bishleshon korchi."),
    (71, "A2 (Temel Orta)", "Yardım & İletişim", "İngilizce konuşma pratiği yapmak istiyorum.", "I want to practice speaking English.", "Ay vant tu prektıs spiking İngliş.", "أُرِيدُ أَنْ أَتَدَرَّبَ عَلَى التَّحَدُّثِ بِالْإِنْجِلِيزِيَّةِ.", "Ürîdü en etederrabe ale't-tehaddüsi bi'l-İncilîziyyeti.", "আমি ইংরেজিতে কথা বলার অনুশীলন করতে চাই।", "Ami Ingrejite kotha bolar onushilon korte chai."),
    (72, "A2 (Temel Orta)", "Yardım & İletişim", "Bana bunun ne anlama geldiğini söyleyebilir misin?", "Can you tell me what this means?", "Ken yu tel mi vat dis minz?", "هَلْ يُمْكِنُكَ أَنْ تُخْبِرَنِي مَا مَعْنَى هَذَا؟", "Hel yümkınuke en tuhbiranî mâ ma'nâ hâzâ?", "এটার মানে কী আমাকে বলতে পারবেন?", "Etar mane ki amake bolte parben?"),
    (73, "A2 (Temel Orta)", "Yardım & İletişim", "Fikrin gerçekten çok yaratıcı!", "Your idea is really creative!", "Yor aydia iz rili krieytiv!", "فِكْرَتُكَ مُبْدِعَةٌ حَقًّا!", "Fikratüke mübdiatün hakkan!", "আপনার ধারণাটি সত্যিই সৃজনশীল!", "Apnar dharonati shotti srijonshil!"),
    (74, "A2 (Temel Orta)", "Günlük İfadeler", "Hafta içi erken yatmalıyım.", "I should go to bed early on weekdays.", "Ay şud go tu bed örli on vikdeyz.", "يَجِبُ أَنْ أَنَامَ مُبَكِّرًا فِي أَيَّامِ الْأُسْبُوعِ.", "Yecibü en enâme mübekkiran.", "সপ্তাহের দিনগুলোতে আমার তাড়াতাড়ি ঘুমানো উচিত।", "Shoptaher dingulote amar taratari ghumano uchit."),
    (75, "A2 (Temel Orta)", "Günlük İfadeler", "Bugün kendimi çok enerjik hissediyorum.", "I feel very energetic today.", "Ay fil veri enercetik tudey.", "أَشْعُرُ بِطَاقَةٍ كَبِيرَةٍ الْيَوْمَ.", "Eş'uru bi-tâkatin kebîratin el-yevm.", "আজ আমি খুব উদ্যমী বোধ করছি।", "Aj ami khub uddomi bodh korchi."),
    (76, "A2 (Temel Orta)", "Günlük İfadeler", "Yağmur yağıyor, şemsiyeni al.", "It is raining, take your umbrella.", "İt iz reyning, teyk yor ambrela.", "إِنَّهَا تُمْطِرُ، خُذْ مِظَلَّتَكَ.", "İnnehâ tumtiru, huz mızalleteke.", "বৃষ্টি হচ্ছে, আপনার ছাতা নিন।", "Brishti hocche, apnar chata nin."),
    (77, "A2 (Temel Orta)", "Yön & Ulaşım", "Havalimanına gitmek ne kadar sürer?", "How long does it take to go to the airport?", "Hav long daz it teyk tu go tu di eyrport?", "كَمْ يَسْتَغْرِقُ الذَّهَابُ إِلَى الْمَطَارِ؟", "Kem yestağriku'z-zehâbü ile'l-metâri?", "বিমানবন্দরে যেতে কতক্ষণ সময় লাগে?", "Bimanbondore jete kotokkhon shomoy lage?"),
    (78, "A2 (Temel Orta)", "Yön & Ulaşım", "Bir sonraki istasyonda ineceğim.", "I will get off at the next station.", "Ay vil get of et dı nekst steyşın.", "سَأَنْزِلُ فِي الْمَحَطَّةِ التَّالِيَةِ.", "Se-enzilü fi'l-mahattati't-tâliyeti.", "আমি পরের স্টেশনে নেমে যাব।", "Ami porer steshone neme jabo."),
    (79, "A2 (Temel Orta)", "Okul & Eğitim", "Kütüphanede sessizce ders çalışıyoruz.", "We are studying quietly in the library.", "Vi ar stadiing kvayıtli in dı laybreri.", "نَحْنُ نَدْرُسُ بِهُدُوءٍ فِي الْمَكْتَبَةِ.", "Nahnu nedrusu bi-hudûin fi'l-mektebeti.", "আমরা লাইব্রেরিতে চুপচাপ পড়াশোনা করছি।", "Amra laibrerite chupchap porashona korchi."),
    (80, "A2 (Temel Orta)", "Okul & Eğitim", "Notlarımı düzenli olarak tekrar ediyorum.", "I review my notes regularly.", "Ay rivyu may nots regyulırli.", "أُرَاجِعُ مُلَاحَظَاتِي بِانْتِظَامٍ.", "Ürâciu mülâhazâtî bi-intizâmin.", "আমি নিয়মিত আমার নোটগুলো রিভিশন দিই।", "Ami niyomito amar notgulo ribhishon dii."),
    (81, "B1 (Orta)", "Teknoloji & Yazılım", "API anahtarını bağlayarak canlı yapay zekayı etkinleştirdik.", "We activated live AI by connecting the API key.", "Vi ektiveytıd layv ey-ay bay konekting di ey-pi-ay ki.", "فَعَّلْنَا الذَّكَاءَ الِاصْطِنَاعِيَّ الْمُبَاشِرَ.", "Fe'alnâ ez-zekâe'l-ıstınâiyye'l-mübâşir.", "এপিআই কী সংযুক্ত করে আমরা লাইভ এআই চালু করেছি।", "API ki shongjukto kore amra laibh AI chalu korechi."),
    (82, "B1 (Orta)", "Teknoloji & Yazılım", "Arayüz hem masaüstünde hem de mobilde harika görünüyor.", "The interface looks great on both desktop and mobile.", "Dı intırfeys luks greyt on bot desktop end mobayl.", "الْوَاجِهَةُ رَائِعَةٌ عَلَى الْحَاسُوبِ وَالْهَاتِفِ.", "El-vâcihetü râiatün ale'l-hâsûbi ve'l-hâtifi.", "ইন্টারফেসটি ডেস্কটপ ও মোবাইলে দারুণ দেখাচ্ছে।", "Intarfeisti desktap o mobaile darun dekhacche."),
    (83, "B1 (Orta)", "Teknoloji & Yazılım", "Kullanıcı deneyimini geliştirmek için yeni özellikler ekliyoruz.", "We are adding new features to improve user experience.", "Vi ar eding nyu fiçırs tu impruv yuzır ikspiriyıns.", "نُضِيفُ مِيزَاتٍ جَدِيدَةً لِتَحْسِينِ التَّجْرِبَةِ.", "Nudîfü mîzâtin cedîdeten.", "ব্যবহারকারীর অভিজ্ঞতা উন্নত করতে নতুন ফিচার যোগ করছি।", "Byaboharkarir obhiggota unnoto korte notun fichar jog korchi."),
    (84, "B1 (Orta)", "Bilim & Tarih", "El-Cezerî mekanik mühendisliğinin öncüsüdür.", "Al-Jazari is a pioneer of mechanical engineering.", "El-Cezeri iz e payınir of mekenikıl enciniring.", "الْجَزَرِيُّ رَائِدُ الْهَنْدَسَةِ الْمِيكَانِيكِيَّةِ.", "El-Cezerî râidü'l-hendeseti'l-mîkânîkiyyeti.", "আল-জাজারি যন্ত্রকৌশলের অগ্রদূত।", "Al-Jajari jontrokousholer ogrodut."),
    (85, "B1 (Orta)", "Bilim & Tarih", "Deneyler hipotezimizi doğruladı.", "The experiments confirmed our hypothesis.", "Dı iksperimınts kınförmd aur haypotısıs.", "أَكَّدَتِ التَّجَارِبُ فَرَضِيَّتَنَا.", "Ekkedeti't-tecâribü feradiyyetenâ.", "পরীক্ষাগুলো আমাদের অনুমানকে নিশ্চিত করেছে।", "Porikkhagulo amader onumanke nishchit koreche."),
    (86, "B1 (Orta)", "Mühendislik & Projeler", "Rüzgar direncini azaltmak için gövdeyi hafiflettik.", "We lightened the body to reduce wind resistance.", "Vi laytınd dı badi tu ridyus vind rizistıns.", "خَفَّفْنَا الْهَيْكَلَ لِتَقْلِيلِ مُقَاوَمَةِ الرِّيَاحِ.", "Haffefne'l-heykele li-taklîli mukâvemeti'r-riyâh.", "বাতাসের বাধা কমাতে আমরা কাঠামো হালকা করেছি।", "Batasher badha komate amra kathamo halka korechi."),
    (87, "B1 (Orta)", "Mühendislik & Projeler", "Güvenlik eşiği 40 santimetrenin altına düşerse fren yapar.", "If the safety threshold drops below 40 centimeters, it brakes.", "İf dı seyfti treşhold drops bilov forti sentimitırs, it breyks.", "إِذَا قَلَّتِ الْمَسَافَةُ عَنْ ٤٠ سَم تَتَوَقَّفُ.", "İzâ kalleti'l-mesâfetü an 40 sm tetevekkaf.", "নিরাপত্তা দূরত্ব ৪০ সেমির নিচে নামলে ব্রেক করে।", "Nirapotta durottvo 40 semir niche namle brek kore."),
    (88, "B1 (Orta)", "Yardım & İletişim", "Sana tamamen katılıyorum, çok mantıklı.", "I completely agree with you, that makes a lot of sense.", "Ay kımplitli egri vit yu, det meyks e lot of sens.", "أُوَافِقُكَ تَمَامًا، هَذَا مَنْطِقِيٌّ جِدًّا.", "Üvâfikuke temâmen, hâzâ mantıkıyyun cidden.", "আমি আপনার সাথে পুরোপুরি একমত, এটি খুব যুক্তিসঙ্গত।", "Ami apnar sathe puropuri ekmot, eti khub juktishonggoto."),
    (89, "B1 (Orta)", "Yardım & İletişim", "Farklı bir açıdan bakmayı deneyelim.", "Let's try looking at it from a different perspective.", "Lets tray luking et it from e difrınt pörspektiv.", "لِنَنْظُرْ إِلَيْهِ مِنْ زَاوِيَةٍ مُخْتَلِفَةٍ.", "Li-nenzur ileyhi min zâviyetin muhtelifetin.", "চলুন ভিন্ন দৃষ্টিকোণ থেকে এটি দেখি।", "Cholun bhinno drishtikon theke eti dekhi."),
    (90, "B1 (Orta)", "Günlük İfadeler", "Hedeflerime ulaşmak için her gün çalışıyorum.", "I work every day to achieve my goals.", "Ay vörk evri dey tu eçiv may golz.", "أَعْمَلُ كُلَّ يَوْمٍ لِتَحْقِيقِ أَهْدَافِي.", "E'melü külle yevmin li-tahkîkı ehdâfî.", "আমার লক্ষ্য অর্জনের জন্য আমি প্রতিদিন কাজ করি।", "Amar lokkho orjoner jonno ami protidin kaj kori."),
    (91, "A1 (Başlangıç)", "Günlük İfadeler", "Evet, tabii ki! / Hayır, teşekkürler.", "Yes, of course! / No, thank you.", "Yes, of kors! / No, tenk yu.", "نَعَمْ، بِالطَّبْعِ! / لَا، شُكْرًا.", "Neam, bi't-tab'! / Lâ, şükran.", "হ্যাঁ, অবশ্যই! / না, ধন্যবাদ।", "Hyan, oboshshoi! / Na, dhonnobad."),
    (92, "A1 (Başlangıç)", "Günlük İfadeler", "Çok güzel! / Harika!", "Very good! / Wonderful!", "Veri gud! / Vandırful!", "جَيِّدٌ جِدًّا! / رَائِعٌ!", "Ceyyidun cidden! / Râiun!", "খুব ভালো! / দারুণ!", "Khub bhalo! / Darun!"),
    (93, "A1 (Başlangıç)", "Temel Sorular", "Adınız nedir? / Nerelisiniz?", "What is your name? / Where are you from?", "Vat iz yor neym? / Ver ar yu from?", "مَا اسْمُكَ؟ / مِنْ أَيْنَ أَنْتَ؟", "Me'smüke? / Min eyne ente?", "আপনার নাম কী? / আপনি কোথা থেকে এসেছেন?", "Apnar nam ki? / Apni kotha theke eshechen?"),
    (94, "A1 (Başlangıç)", "Temel Sorular", "İngilizce biliyor musun?", "Do you speak English?", "Du yu spik İngliş?", "هَلْ تَتَحَدَّثُ الْإِنْجِلِيزِيَّةَ؟", "Hel teteheddesü'l-İncilîziyyete?", "আপনি কি ইংরেজি বলতে পারেন?", "Apni ki Ingreji bolte paren?"),
    (95, "A2 (Temel Orta)", "Günlük İhtiyaçlar", "Bir bardak su alabilir miyim?", "Could I have a glass of water?", "Kud ay hev e glas of votır?", "هَلْ يُمْكِنُنِي كُوبُ مَاءٍ؟", "Hel yümkınunî kûbu mâin?", "আমি কি এক গ্লাস পানি পেতে পারি?", "Ami ki ek glas pani pete pari?"),
    (96, "A2 (Temel Orta)", "Spor & Hobiler", "Satranç oynamak zekayı geliştirir.", "Playing chess improves intelligence.", "Pleying çes impruvs intelicıns.", "لَعِبُ الشَّطْرَنْجِ يُنَمِّي الذَّكَاءَ.", "Le'bü'ş-şatranci yünemmi'z-zekâe.", "দাবা খেলা বুদ্ধিমত্তা বাড়ায়।", "Daba khela buddhimotta baray."),
    (97, "A2 (Temel Orta)", "Okul & Eğitim", "Ödevimi zamanında bitirdim.", "I finished my homework on time.", "Ay finişt may homvörk on taym.", "أَنْهَيْتُ وَاجِبِي فِي الْوَقْتِ الْمُحَدَّدِ.", "Enheytü vâcibî fi'l-vakti'l-muhadded.", "আমি সময়মতো বাড়ির কাজ শেষ করেছি।", "Ami shomoymoto barir kaj shesh korechi."),
    (98, "B1 (Orta)", "Teknoloji & Yazılım", "Sesli komutları metne dönüştürüyoruz.", "We convert voice commands into text.", "Vi kınvört voys komendz intu tekst.", "نُحَوِّلُ الْأَوَامِرَ الصَّوْتِيَّةَ إِلَى نَصٍّ.", "Nuhavvilü'l-evâmira's-savtiyyete ilâ nassın.", "আমরা ভয়েস কমান্ডকে টেক্সটে রূপান্তর করি।", "Amra bhoies komandke tekste rupantor kori."),
    (99, "B1 (Orta)", "Matematik & Bilim", "Formülleri ezberlemek yerine mantığını kavrayalım.", "Let's understand the logic instead of memorizing formulas.", "Lets andırstend dı locik insted of memorayzing formyılas.", "لِنَفْهَمِ الْمَنْطِقَ بَدَلًا مِنَ الْحِفْظِ.", "Li-nefhemi'l-mantıka bedelen mine'l-hıfzı.", "সূত্র মুখস্থ করার বদলে যুক্তি বুঝি।", "Shutro mukhostho korar bodole jukti bujhi."),
    (100, "B1 (Orta)", "Günlük İfadeler", "Birlikte çok daha büyük projeler başaracağız!", "Together we will achieve much bigger projects!", "Tugedır vi vil eçiv maç bigır procekts!", "مَعًا سَنُحَقِّقُ مَشَارِيعَ أَكْبَرَ بِكَثِيرٍ!", "Mean se-nuhakkıku meşârîa ekbera bi-kesîrin!", "একসাথে আমরা আরও অনেক বড় প্রজেক্ট সফল করব!", "Ekshathe amra aro onek boro projekt shofol korbo!"),
]

for _item in _YENI_KART_VERILERI:
    _kid, _sev, _kat, _tr, _en, _eno, _oe, _ar, _aro, _oa, _bn, _bno, _ob = (
        _item[0], _item[1], _item[2], _item[3], _item[4], _item[5],
        _item[4], _item[6], _item[7], _item[6], _item[8], _item[9], _item[8]
    )
    A1_A2_DIL_PRATIK_KARTLARI.append({
        "id": _kid, "seviye": _sev, "kategori": _kat, "turkce": _tr,
        "ingilizce": _en, "ing_okunus": _eno, "ornek_en": _oe,
        "arapca": _ar, "ara_okunus": _aro, "ornek_ar": _oa,
        "bengalce": _bn, "ben_okunus": _bno, "ornek_bn": _ob,
    })


def guvenli_cevir(metin: str, src: str = "auto", dest: str = "tr") -> str:
    if _translator_nesnesi is not None:
        try:
            sonuc = _translator_nesnesi.translate(metin, src=src, dest=dest)
            if inspect.iscoroutine(sonuc):
                try:
                    loop = asyncio.get_event_loop()
                    if loop.is_running():
                        import concurrent.futures
                        with concurrent.futures.ThreadPoolExecutor() as pool:
                            sonuc = pool.submit(asyncio.run, sonuc).result()
                    else:
                        sonuc = loop.run_until_complete(sonuc)
                except RuntimeError:
                    sonuc = asyncio.run(sonuc)
            if hasattr(sonuc, "text") and sonuc.text:
                return sonuc.text
        except Exception:
            pass
    try:
        q = urllib.parse.quote(metin)
        url = f"https://translate.googleapis.com/translate_a/single?client=gtx&sl={src}&tl={dest}&dt=t&q={q}"
        req = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
        with urllib.request.urlopen(req, timeout=6) as resp:
            veri = json.loads(resp.read().decode("utf-8"))
            return "".join(parca[0] for parca in veri[0] if parca and parca[0])
    except Exception:
        return metin


def ses_metnini_dogallastir(metin: str) -> str:
    yazi = re.sub(r"<[^>]+>", "", str(metin))
    yazi = yazi.replace("×", " çarpı ").replace("÷", " bölü ").replace("=", " eşittir ")
    yazi = yazi.replace("√", " karekök ").replace("+", " artı ").replace("%", " yüzde ")
    yazi = re.sub(r"[#*`*_•|]", " ", yazi)
    yazi = re.sub(r"[⚡🚀📜➕➖✖️➗🔺📐🥧🤖🔌🚁🖨️⚙️🇹🇷🏰🪐💧🧬🕌✨🤲💪😄🛠️⚽🌍🧑💻🕒🏷️📅🔢🧩❗💯ℹ️⚠️✅🎉❌🔬🍎⚗️📖]", "", yazi)
    yazi = re.sub(r"\s+", " ", yazi).strip()
    return yazi[:750]


async def _edge_ses_olustur_bellek(metin: str, ses_adi: str) -> bytes:
    iletisim = edge_tts.Communicate(metin, ses_adi, rate="+4%")
    tampon = io.BytesIO()
    async for paket in iletisim.stream():
        if paket.get("type") == "audio" and paket.get("data"):
            tampon.write(paket["data"])
    return tampon.getvalue()


def _asenkron_calistir(coro):
    try:
        loop = asyncio.get_event_loop()
        if loop.is_running():
            import concurrent.futures
            with concurrent.futures.ThreadPoolExecutor(max_workers=1) as havuz:
                return havuz.submit(asyncio.run, coro).result(timeout=12)
        return loop.run_until_complete(coro)
    except Exception:
        return asyncio.run(coro)


def sesli_soyle(metin: str, dil: str = "tr", rerun_sonrasi: bool = False):
    if st.session_state.get("sessiz_mod", False) or not st.session_state.get("ses_aktif", True):
        return
    try:
        temiz_metin = ses_metnini_dogallastir(metin)
        if not temiz_metin:
            return
        ses_bayt = b""
        if EDGE_TTS_MEVCUT:
            try:
                cinsiyet = st.session_state.get("ses_cinsiyet", "Erkek")
                if dil == "tr":
                    ses_adi = "tr-TR-AhmetNeural" if cinsiyet == "Erkek" else "tr-TR-EmelNeural"
                else:
                    ses_adi = EDGE_SESLER.get(dil, "tr-TR-AhmetNeural") if cinsiyet == "Erkek" else EDGE_KADIN_SESLER.get(dil, "tr-TR-EmelNeural")
                ses_bayt = _asenkron_calistir(_edge_ses_olustur_bellek(temiz_metin, ses_adi)) or b""
            except Exception:
                ses_bayt = b""

        if not ses_bayt and GTTS_MEVCUT and gTTS is not None:
            try:
                gtts_dil = GTTS_DIL_ESLESME.get(dil, dil)
                tts = gTTS(text=temiz_metin, lang=gtts_dil, slow=False)
                mp3_tampon = io.BytesIO()
                tts.write_to_fp(mp3_tampon)
                ses_bayt = mp3_tampon.getvalue()
            except Exception:
                ses_bayt = b""

        if not ses_bayt:
            return
        if rerun_sonrasi:
            st.session_state.son_ses_bayt = ses_bayt
        else:
            try:
                st.audio(ses_bayt, format="audio/mp3", autoplay=True)
            except TypeError:
                st.audio(ses_bayt, format="audio/mp3")

        if PYGAME_MEVCUT and st.session_state.get("pygame_aktif", False):
            try:
                if not pygame.mixer.get_init():
                    pygame.mixer.init()
                pygame.mixer.music.load(io.BytesIO(ses_bayt))
                pygame.mixer.music.play()
                while pygame.mixer.music.get_busy():
                    pygame.time.Clock().tick(10)
            except Exception:
                pass
    except Exception as e:
        st.toast(f"Ses motoru uyarısı: {e}", icon="⚠️")


def mikrofon_sesini_metne_cevir(ses_bayt: bytes, dil: str = "tr-TR"):
    if not SPEECH_RECOGNITION_MEVCUT or sr is None:
        return None, "Ses tanıma için `pip install SpeechRecognition` kurulmalıdır."
    try:
        taniyici = sr.Recognizer()
        with sr.AudioFile(io.BytesIO(ses_bayt)) as kaynak:
            ses_verisi = taniyici.record(kaynak)
        metin = taniyici.recognize_google(ses_verisi, language=dil)
        return metin, None
    except Exception as e:
        return None, f"Ses net duyulamadı ({e}). Tekrar deneyin."


def dil_ve_cevirmeli_kart_studyosu_goster():
    toplam_kart = len(A1_A2_DIL_PRATIK_KARTLARI)
    st.subheader(f"🌐 {toplam_kart} Adet A1-A2-B1 3D Çevirmeli Dil Kartı (İngilizce 🇬🇧 • Arapça 🇸🇦 • Bengalce 🇧🇩)")
    tab_kart_calis, tab_interaktif_test, tab_ceviri = st.tabs([
        f"🃏 3D Çevirmeli Kartlar ({toplam_kart} Özgün Kart)",
        "🎯 Kart Üzerinden İnteraktif Dil Testi",
        "🔄 28 Dilli Akıllı Çeviri & Seslendirme",
    ])

    tema_adi = st.session_state.get("secili_tema", "Derin Lacivert (Klasik Ar)")
    cihaz_modu = st.session_state.get("cihaz_modu", "Masaüstü")

    with tab_kart_calis:
        kategoriler = ["Tümü"] + sorted(list({k["kategori"] for k in A1_A2_DIL_PRATIK_KARTLARI}))
        fk1, fk2, fk3, fk4 = st.columns([1.1, 1.1, 1.2, 1.1])
        with fk1:
            secili_seviye = st.selectbox("Seviye:", ["Tümü", "A1 (Başlangıç)", "A2 (Temel Orta)", "B1 (Orta)"], key="m5_secili_seviye")
        with fk2:
            secili_kat = st.selectbox("Kategori:", kategoriler, key="m5_secili_kat")
        with fk3:
            on_yuz_dili = st.selectbox("Ön Yüz Dili:", ["🇬🇧 İngilizce", "🇸🇦 Arapça", "🇧🇩 Bengalce", "🇹🇷 Türkçe (Tahmin Et)"], key="m5_on_yuz_dili")
        with fk4:
            gorunum_modu = st.selectbox("Görünüm:", ["🃏 Tek Büyük Çevirmeli Kart", "🎛️ Çoklu Kart Masası (6'lı)"], key="m5_gorunum_modu")

        filtrelenmis_kartlar = [
            k for k in A1_A2_DIL_PRATIK_KARTLARI
            if (secili_seviye == "Tümü" or k["seviye"] == secili_seviye)
            and (secili_kat == "Tümü" or k["kategori"] == secili_kat)
        ]
        if not filtrelenmis_kartlar:
            filtrelenmis_kartlar = A1_A2_DIL_PRATIK_KARTLARI

        toplam_k = len(filtrelenmis_kartlar)
        aktif_idx = st.session_state.aktif_flip_indeks % toplam_k
        aktif_kart = filtrelenmis_kartlar[aktif_idx]

        st.caption(f"📌 Filtrede **{toplam_k} kart** var | Öğrenilen: **{len(st.session_state.ogrenilen_kart_idleri)} / {toplam_kart}**")

        if gorunum_modu == "🃏 Tek Büyük Çevirmeli Kart":
            nb1, nb2, nb3, nb4, nb5 = st.columns(5)
            if nb1.button("⬅️ Önceki", key="m5_onceki_btn", use_container_width=True):
                st.session_state.aktif_flip_indeks = (aktif_idx - 1) % toplam_k
                st.session_state.kart_ters_mi = False
                st.rerun()
            if nb2.button("🔄 Kartı Çevir", key="m5_cevir_btn", use_container_width=True):
                st.session_state.kart_ters_mi = not st.session_state.kart_ters_mi
                st.rerun()
            if nb3.button("🎲 Rastgele", key="m5_rastgele_btn", use_container_width=True):
                st.session_state.aktif_flip_indeks = random.randint(0, toplam_k - 1)
                st.session_state.kart_ters_mi = False
                st.rerun()
            if nb4.button("➡️ Sonraki", key="m5_sonraki_btn", use_container_width=True):
                st.session_state.aktif_flip_indeks = (aktif_idx + 1) % toplam_k
                st.session_state.kart_ters_mi = False
                st.rerun()
            if nb5.button("✅ Öğrendim!", key="m5_ogrendim_btn", use_container_width=True):
                if aktif_kart["id"] not in st.session_state.ogrenilen_kart_idleri:
                    st.session_state.ogrenilen_kart_idleri.append(aktif_kart["id"])
                st.toast(f"Kart #{aktif_kart['id']} öğrenilenlere eklendi! 🎉", icon="✅")
                st.rerun()

            cevirmeli_dil_karti_goster(
                aktif_kart,
                on_yuz_dili=on_yuz_dili,
                ters_cevir=st.session_state.kart_ters_mi,
                kart_key=f"tek_{aktif_idx}_{st.session_state.kart_ters_mi}",
                yukseklik=380 if cihaz_modu == "Masaüstü" else 410,
                tema_adi=tema_adi,
            )

            dk1, dk2, dk3 = st.columns(3)
            if dk1.button("🔊 İngilizce Seslendir", key="m5_ses_en_btn", use_container_width=True):
                sesli_soyle(aktif_kart["ingilizce"], dil="en")
            if dk2.button("🔊 Arapça Seslendir", key="m5_ses_ar_btn", use_container_width=True):
                sesli_soyle(aktif_kart["arapca"], dil="ar")
            if dk3.button("🔊 Bengalce Seslendir", key="m5_ses_bn_btn", use_container_width=True):
                sesli_soyle(aktif_kart["bengalce"], dil="bn")
        else:
            if "masa_sayfa" not in st.session_state:
                st.session_state.masa_sayfa = 0
            toplam_sayfa = max(1, (toplam_k + 5) // 6)
            sayfa_no = st.session_state.masa_sayfa % toplam_sayfa
            ms1, ms2, ms3 = st.columns([1, 2, 1])
            if ms1.button("⬅️ Önceki 6 Kart", key="m5_masa_prev", use_container_width=True):
                st.session_state.masa_sayfa = (sayfa_no - 1) % toplam_sayfa
                st.rerun()
            ms2.markdown(f"<div style='text-align:center;padding-top:10px;'>📄 Sayfa <b>{sayfa_no + 1} / {toplam_sayfa}</b> — Kartın üzerine dokun, 3D döner!</div>", unsafe_allow_html=True)
            if ms3.button("➡️ Sonraki 6 Kart", key="m5_masa_next", use_container_width=True):
                st.session_state.masa_sayfa = (sayfa_no + 1) % toplam_sayfa
                st.rerun()

            bas = sayfa_no * 6
            parca = filtrelenmis_kartlar[bas : bas + 6]
            if cihaz_modu == "Mobil":
                for i_k, k_item in enumerate(parca):
                    cevirmeli_dil_karti_goster(k_item, on_yuz_dili=on_yuz_dili, ters_cevir=False, kart_key=f"m_mob_{sayfa_no}_{i_k}", yukseklik=380, tema_adi=tema_adi)
            else:
                g_col1, g_col2 = st.columns(2, gap="medium")
                for i_k, k_item in enumerate(parca):
                    with (g_col1 if i_k % 2 == 0 else g_col2):
                        cevirmeli_dil_karti_goster(k_item, on_yuz_dili=on_yuz_dili, ters_cevir=False, kart_key=f"m_desk_{sayfa_no}_{i_k}", yukseklik=360, tema_adi=tema_adi)

    with tab_interaktif_test:
        st.markdown("#### 🎯 Kart Üzerinden Kendini Dene (İngilizce • Arapça • Bengalce)")
        t_col1, t_col2, t_col3 = st.columns(3)
        with t_col1:
            pratik_dil = st.selectbox("Pratik Dili Seç:", ["🇬🇧 İngilizce", "🇸🇦 Arapça", "🇧🇩 Bengalce"], key="m5_pratik_dil")
        with t_col2:
            pratik_seviye = st.selectbox("Pratik Seviyesi:", ["Tümü", "A1 (Başlangıç)", "A2 (Temel Orta)", "B1 (Orta)"], key="m5_pratik_seviye")
        with t_col3:
            st.metric("Dil Pratiği Puanın", f"{st.session_state.dil_quiz_puan} Puan", "Aktif")

        havuz_kartlar = [
            k for k in A1_A2_DIL_PRATIK_KARTLARI
            if pratik_seviye == "Tümü" or k["seviye"] == pratik_seviye
        ]
        if st.button("🎲 Bana Yeni Çalışma Kartı Ver", key="m5_yeni_calisma_karti_btn", use_container_width=True):
            st.session_state.dil_quiz_indeks = random.randint(0, len(havuz_kartlar) - 1)

        sec_idx = st.session_state.dil_quiz_indeks % len(havuz_kartlar)
        soru_kart = havuz_kartlar[sec_idx]

        cevirmeli_dil_karti_goster(soru_kart, on_yuz_dili=pratik_dil, ters_cevir=False, kart_key=f"test_{soru_kart['id']}", yukseklik=360, tema_adi=tema_adi)

        rng = random.Random(soru_kart["id"])
        secenekler = [soru_kart["turkce"]]
        digerleri = [k["turkce"] for k in A1_A2_DIL_PRATIK_KARTLARI if k["id"] != soru_kart["id"]]
        secenekler.extend(rng.sample(digerleri, 3))
        rng.shuffle(secenekler)

        secilen_cevap = st.radio("Bu karttaki ifadenin Türkçe anlamı nedir?", secenekler, key=f"dil_secim_{soru_kart['id']}_{pratik_dil}")
        if st.button("✅ Cevabımı Kontrol Et", key="dil_cevap_kontrol", use_container_width=True):
            if secilen_cevap == soru_kart["turkce"]:
                st.session_state.dil_quiz_puan += 10
                st.success(f"🎉 Tebrikler Ahmet! Doğru cevap: **{soru_kart['turkce']}** (+10 Puan)")
            else:
                st.error(f"❌ Doğru anlamı: **{soru_kart['turkce']}**")

    with tab_ceviri:
        c1, c2 = st.columns(2, gap="large")
        with c1:
            kaynak = st.selectbox("Kaynak Dil:", options=["auto"] + list(DESTEKLENEN_DILLER.keys()), format_func=lambda x: "✨ Otomatik Algıla" if x == "auto" else DESTEKLENEN_DILLER[x], key="m5_ceviri_kaynak")
            metin_giris = st.text_area("Çevrilecek Metin:", height=190, placeholder="Çevirmek istediğin metni buraya yaz...", key="m5_ceviri_giris")
        with c2:
            hedef = st.selectbox("Hedef Dil:", options=list(DESTEKLENEN_DILLER.keys()), index=1, format_func=lambda x: DESTEKLENEN_DILLER[x], key="m5_ceviri_hedef")
            cikti = st.empty()
            cikti.text_area("Çeviri Sonucu:", value="", height=190, key="ceviri_bos")

        b1, b2 = st.columns(2)
        btn_cevir = b1.button("🔄 Sadece Çevir", key="m5_sadece_cevir_btn", use_container_width=True)
        btn_sesli = b2.button("🔊 Çevir ve Doğal Sesle Oku", key="m5_cevir_oku_btn", use_container_width=True)
        if btn_cevir or btn_sesli:
            if metin_giris.strip():
                try:
                    cevrilen = guvenli_cevir(metin_giris, src=kaynak, dest=hedef)
                    cikti.text_area("Çeviri Sonucu:", value=cevrilen, height=190, key="ceviri_dolu")
                    if btn_sesli:
                        sesli_soyle(cevrilen, dil=hedef)
                except Exception as e:
                    st.error(f"Çeviri hatası: {e}")
            else:
                st.warning("Lütfen çevirmek için bir metin girin.")
