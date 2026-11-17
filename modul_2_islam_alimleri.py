# -*- coding: utf-8 -*-
"""
==============================================================================
AR AI STUDIO v4.0 — MODÜL 2: 30 BÜYÜK İSLAM ÂLİMİ ANSİKLOPEDİSİ, ESERLERİ VE
SESLİ BİYOGRAFİ STÜDYOSU (modul_2_islam_alimleri.py)
==============================================================================
"""
import streamlit as st
import importlib.util
import os
import sys

_MODUL_DIZINI = os.path.dirname(os.path.abspath(__file__))
if _MODUL_DIZINI not in sys.path:
    sys.path.insert(0, _MODUL_DIZINI)


def _guvenli_modul_yukle(modul_adi: str):
    if modul_adi in sys.modules and getattr(sys.modules[modul_adi], "__file__", None):
        return sys.modules[modul_adi]
    aday_yollar = [os.path.join(_MODUL_DIZINI, f"{modul_adi}.py")]
    for _ana in [_MODUL_DIZINI]:
        for _kok, _altlar, _dosyalar in os.walk(_ana):
            _altlar[:] = [d for d in _altlar if not d.startswith(".") and d not in ("__pycache__", "venv", ".venv")]
            if f"{modul_adi}.py" in _dosyalar:
                tam = os.path.join(_kok, f"{modul_adi}.py")
                if tam not in aday_yollar:
                    aday_yollar.append(tam)
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

ISLAM_ALIMLERI = {'aksemsettin': {'ad': 'Akşemseddin (Muhammed Şemseddin)',
                 'alan': 'Tıp, Mikrobiyoloji, Tasavvuf',
                 'anahtar_kelimeler': ['akşemseddin', 'aksemsettin', 'mikrop', 'fatihin hocası'],
                 'bilgi': "Fatih Sultan Mehmet'in hocası ve büyük tıp âlimidir. 'Mâddetü'l-Hayât' eserinde "
                          'hastalıkların gözle görülmeyen canlı tohumlar (mikroplar) yoluyla bulaştığını '
                          'açıkça yazmıştır.',
                 'donem': '1389 – 1459 (Şam – Göynük)',
                 'eserler': "Mâddetü'l-Hayât, Risâletü'n-Nûriyye"},
 'ali_kuscu': {'ad': 'Ali Kuşçu (Alâeddin Ali bin Muhammed)',
               'alan': 'Astronomi, Matematik, Kelâm',
               'anahtar_kelimeler': ['ali kuşçu', 'ali kuscu', 'kuşçu'],
               'bilgi': "Fatih Sultan Mehmet'in davetiyle İstanbul'a gelmiş, İstanbul'un enlem ve boylamını "
                        "yeniden hesaplamış ve Ay'ın haritasını çıkarmıştır.",
               'donem': '1403 – 1474 (Semerkant – İstanbul)',
               'eserler': "Risâle fi'l-Hey'e, Risâle fi'l-Hisâb"},
 'biruni': {'ad': 'El-Bîrûnî (Ebû Reyhân Muhammed)',
            'alan': 'Astronomi, Matematik, Jeodezi, Eczacılık',
            'anahtar_kelimeler': ['biruni', 'bîrûnî', 'el biruni', 'dünyanın yarıçapı'],
            'bilgi': "Dünya'nın yarıçapını ve çevresini kendi geliştirdiği trigonometrik yöntemlerle bugünkü "
                     "değerine çok yakın hesaplamış, yer çekiminin varlığına Newton'dan asırlar önce işaret "
                     'etmiştir.',
            'donem': '973 – 1048 (Hârizm – Gazne)',
            'eserler': "El-Kânûnü'l-Mes'ûdî, Tahdîdü Nihâyâti'l-Emâkin"},
 'cabir_bin_hayyan': {'ad': 'Câbir bin Hayyân',
                      'alan': 'Kimya, Simya, Eczacılık',
                      'anahtar_kelimeler': ['cabir', 'câbir', 'cabir bin hayyan', 'kimya kurucusu'],
                      'bilgi': 'Deneysel kimyanın kurucusu kabul edilir. Damıtma (imbik) ve kristalleştirme '
                               'yöntemlerini geliştirmiş, nitrik ve sülfürik asidi keşfetmiştir.',
                      'donem': '721 – 815 (Tûs – Kûfe)',
                      'eserler': "Kitâbü'l-Kimyâ, Kitâbü's-Seb'în"},
 'cezeri': {'ad': "El-Cezerî (Bedîüzzamân Ebü'l-İz İsmâil)",
            'alan': 'Sibernetik, Robotik, Mekanik Mühendisliği',
            'anahtar_kelimeler': ['cezeri',
                                  'el cezeri',
                                  'el-cezeri',
                                  'cezerî',
                                  'filli su saati',
                                  'sibernetik kurucusu',
                                  'robotik kurucusu'],
            'bilgi': "12. ve 13. yüzyıllarda Cizre'de yaşamış büyük mucit ve mekanik mühendisidir. "
                     'Sibernetiğin ve robotik biliminin kurucusu kabul edilir; su gücü ve dişli çarklarla '
                     "çalışan otomatik makineler, krank-biyel mekanizması ve ünlü Filli Su Saati'ni "
                     'tasarlamıştır.',
            'donem': '1136 – 1206 (Artuklu / Cizre)',
            'eserler': "Kitâbü'l-Hiyel"},
 'ebul_vefa': {'ad': "Ebü'l-Vefâ el-Bûzcânî",
               'alan': 'Trigonometri, Astronomi, Matematik',
               'anahtar_kelimeler': ['ebül vefa', 'ebul vefa', 'buzcani', 'tanjant'],
               'bilgi': 'Trigonometride tanjant, kotanjant, sekant ve kosekant fonksiyonlarını tanımlayan ve '
                        'küresel trigonometriyi geliştiren büyük matematikçidir.',
               'donem': '940 – 998 (Bûzcan – Bağdat)',
               'eserler': "Kitâbü'l-Mecistî"},
 'farabi': {'ad': 'Fârâbî (Ebû Nasr Muhammed)',
            'alan': 'Felsefe, Mantık, Siyaset Bilimi, Müzik',
            'anahtar_kelimeler': ['farabi', 'fârâbî', 'muallim-i sani', 'medinetül fazıla'],
            'bilgi': "'Muallim-i Sânî' (İkinci Öğretmen) unvanıyla anılır. İdeal devlet düzenini anlattığı "
                     "El-Medînetü'l-Fâzıla siyaset felsefesinin başyapıtlarındandır.",
            'donem': '872 – 950 (Fârâb – Şam)',
            'eserler': "El-Medînetü'l-Fâzıla, Kitâbü'l-Mûsîka'l-Kebîr"},
 'harezmi': {'ad': 'El-Hârizmî (Muhammed bin Mûsâ el-Hârizmî)',
             'alan': 'Matematik, Cebir, Algoritma, Astronomi',
             'anahtar_kelimeler': ['harezmi',
                                   'hârizmî',
                                   'harizmi',
                                   'algoritma kurucusu',
                                   'cebir kurucusu',
                                   'sıfırı bulan'],
             'bilgi': "Cebir ilminin kurucusu ve bilgisayar biliminin temelini oluşturan 'algoritma' "
                      'kavramının isim babasıdır. Hint-Arap rakam sistemini ve sıfır (0) rakamının '
                      'matematiksel kullanımını dünyaya tanıtmıştır.',
             'donem': '780 – 850 (Abbâsî / Bağdat Beytülhikme)',
             'eserler': "El-Kitâbü'l-Muhtasar fî Hisâbi'l-Cebr ve'l-Mukâbele"},
 'ibn_nefis': {'ad': "İbnü'n-Nefîs",
               'alan': 'Tıp, Fizyoloji, Anatomi',
               'anahtar_kelimeler': ['ibnün nefis', 'ibn nefis', 'küçük kan dolaşımı'],
               'bilgi': "Akciğerlerdeki küçük kan dolaşımını (pulmoner dolaşım) Avrupa'dan yaklaşık 300 yıl "
                        'önce keşfederek tıp tarihinde devrim yapmıştır.',
               'donem': '1213 – 1288 (Şam – Kahire)',
               'eserler': "Şerhu Teşrîhi'l-Kânûn"},
 'ibni_arabi': {'ad': 'Muhyiddin İbn-i Arabî',
                'alan': 'Tasavvuf, İslam Felsefesi, Tefsir',
                'anahtar_kelimeler': ['ibni arabi',
                                      'ibn-i arabi',
                                      'ibn arabi',
                                      'muhyiddin',
                                      'şeyh-i ekber',
                                      'fütuhatı mekkiyye'],
                'bilgi': "İslam düşünce tarihinde 'Şeyh-i Ekber' unvanıyla anılan büyük mutasavvıf ve "
                         "mütefekkirdir. Anadolu'da Konya ve Malatya'da bulunmuş, yüzlerce eser kaleme "
                         'almıştır.',
                'donem': '1165 – 1240 (Endülüs – Şam)',
                'eserler': "Fütûhât-ı Mekkiyye, Fusûsü'l-Hikem"},
 'ibni_battuta': {'ad': 'İbn-i Battûta (Ebû Abdillâh Muhammed)',
                  'alan': 'Coğrafya, Seyahatname, Antropoloji, Tarih',
                  'anahtar_kelimeler': ['ibni batuta',
                                        'ibni battuta',
                                        'ibn-i batuta',
                                        'ibn battuta',
                                        'seyyah',
                                        'rıhle'],
                  'bilgi': "Orta Çağ'ın en büyük seyyahı kabul edilir. Yaklaşık 29 yıl süren yolculuklarında "
                           '120.000 kilometreden fazla yol katetmiş, üç kıtadaki şehirleri ve kültürleri '
                           'kayıt altına almıştır.',
                  'donem': '1304 – 1369 (Tanca / Fas)',
                  'eserler': 'Rıhle (İbn Battûta Seyahatnamesi)'},
 'ibni_haldun': {'ad': 'İbn-i Haldûn (Abdurrahman bin Muhammed)',
                 'alan': 'Sosyoloji, Tarih Felsefesi, İktisat',
                 'anahtar_kelimeler': ['ibni haldun',
                                       'ibn-i haldun',
                                       'ibn haldun',
                                       'mukaddime',
                                       'sosyoloji kurucusu'],
                 'bilgi': 'Modern sosyolojinin, tarih felsefesinin ve iktisat biliminin öncüsü kabul edilir. '
                          "Mukaddime'de devletlerin yükseliş ve çöküş süreçlerini 'asabiyet' kavramıyla "
                          'açıklamıştır.',
                 'donem': '1332 – 1406 (Tunus – Kahire)',
                 'eserler': "Mukaddime, Kitâbü'l-İber"},
 'ibni_rusd': {'ad': 'İbn Rüşd (Averroes)',
               'alan': 'Felsefe, Tıp, Hukuk, Astronomi',
               'anahtar_kelimeler': ['ibni rüşd', 'ibn rüşd', 'ibn rusd', 'averroes'],
               'bilgi': "Endülüslü büyük filozof ve hekimdir. Aristo üzerine yaptığı şerhler Avrupa'da "
                        'Rönesans düşüncesinin doğuşuna doğrudan kaynaklık etmiştir.',
               'donem': '1126 – 1198 (Kurtuba / Endülüs)',
               'eserler': "Tehâfütü't-Tehâfüt, El-Külliyyât fi't-Tıb"},
 'ibni_sina': {'ad': 'İbn-i Sînâ (Ebû Alî el-Hüseyn bin Abdillâh)',
               'alan': 'Tıp, Felsefe, Kimya, Fizik',
               'anahtar_kelimeler': ['ibni sina',
                                     'ibn-i sina',
                                     'ibn sina',
                                     'avicenna',
                                     'tıbbın hükümdarı',
                                     'el kanun fit tıb'],
               'bilgi': "Batı dünyasında 'Avicenna' adıyla tanınan ve 'Tıbbın Hükümdarı' unvanına sahip "
                        "büyük bilgindir. El-Kânûn fi't-Tıb eseri 600 yıl boyunca Avrupa'da temel tıp "
                        'ansiklopedisi olarak okutulmuştur.',
               'donem': '980 – 1037 (Buhara – Hemedan)',
               'eserler': "El-Kânûn fi't-Tıb, Kitâbü'ş-Şifâ"},
 'ibnul_heysem': {'ad': "İbnü'l-Heysem (Hasan bin Heysem)",
                  'alan': 'Optik, Fizik, Matematik, Bilimsel Yöntem',
                  'anahtar_kelimeler': ['ibnül heysem',
                                        'ibnul heysem',
                                        'heysem',
                                        'optik kurucusu',
                                        'alhazen',
                                        'camera obscura'],
                  'bilgi': 'Modern optik biliminin kurucusu ve deneysel bilimsel yöntemin öncüsüdür. '
                           'Karanlık oda (camera obscura) çalışmaları modern kameraların temelini atmıştır.',
                  'donem': '965 – 1040 (Basra – Kahire)',
                  'eserler': "Kitâbü'l-Menâzır"},
 'imam_azam': {'ad': "İmam-ı Âzam Ebû Hanîfe (Nu'mân bin Sâbit)",
               'alan': 'Fıkıh, İslam Hukuku, Kelâm',
               'anahtar_kelimeler': ['imam-ı azam', 'imam azam', 'ebu hanife', 'hanefi'],
               'bilgi': 'İslam hukukunda Hanefî mezhebinin kurucusudur. Kıyas ve istihsan yöntemleriyle '
                        'hukuki meselelerin çözümünde sistematik bir çığır açmıştır.',
               'donem': '699 – 767 (Kûfe – Bağdat)',
               'eserler': "El-Fıkhü'l-Ekber"},
 'imam_buhari': {'ad': 'İmam Buhârî (Muhammed bin İsmâil)',
                 'alan': 'Hadis İlmi, Tarih',
                 'anahtar_kelimeler': ['buhari', 'imam buhari', 'sahih-i buhari'],
                 'bilgi': 'Binlerce hadisi senet ve ravilerini titizlikle inceleyerek derlediği Sahîh-i '
                          'Buhârî eseriyle hadis ilminin zirve ismidir.',
                 'donem': '810 – 870 (Buhara – Semerkant)',
                 'eserler': "El-Câmiu's-Sahîh (Sahîh-i Buhârî)"},
 'imam_gazali': {'ad': "İmam Gazzâlî (Hüccetü'l-İslâm)",
                 'alan': 'Kelâm, Fıkıh, Felsefe, Ahlâk',
                 'anahtar_kelimeler': ['gazali', 'gazzali', 'imam gazali', 'ihya'],
                 'bilgi': 'Nizâmiye Medresesi başmüderrisi ve İslam düşünce tarihinin en etkili '
                          'âlimlerindendir. Akıl ile kalp (maneviyat) arasındaki dengeyi sistemleştirmiştir.',
                 'donem': '1058 – 1111 (Tûs / Horasan)',
                 'eserler': "İhyâü Ulûmi'd-Dîn, El-Munkız mine'd-Dalâl"},
 'imam_maturidi': {'ad': 'İmam Mâtürîdî (Ebû Mansûr)',
                   'alan': 'Kelâm, Tefsir, İslam Akaidi',
                   'anahtar_kelimeler': ['maturidi', 'imam maturidi', 'kitabüt tevhid'],
                   'bilgi': 'Ehl-i Sünnet kelâm okulunun kurucularındandır. Dini metinlerin anlaşılmasında '
                            'aklın ve bilginin vazgeçilmez rolünü vurgulamıştır.',
                   'donem': '853 – 944 (Semerkant)',
                   'eserler': "Kitâbü't-Tevhîd, Te'vîlâtü'l-Kur'ân"},
 'imam_safii': {'ad': 'İmam Şâfiî (Muhammed bin İdrîs)',
                'alan': 'Fıkıh Usulü, İslam Hukuku',
                'anahtar_kelimeler': ['imam şafii', 'imam safii', 'er-risale'],
                'bilgi': 'İslam hukuk metodolojisini (Fıkıh Usulü) ilk kez bağımsız bir disiplin olarak '
                         'kaleme alan büyük hukuk bilginidir.',
                'donem': '767 – 820 (Gazze – Kahire)',
                'eserler': 'Er-Risâle, El-Ümm'},
 'katip_celebi': {'ad': 'Kâtip Çelebi (Hacı Halîfe)',
                  'alan': 'Coğrafya, Bibliyografya, Tarih',
                  'anahtar_kelimeler': ['katip çelebi', 'katip celebi', 'cihannüma', 'keşfüz zünun'],
                  'bilgi': "Osmanlı'nın en büyük coğrafya ve ansiklopedi bilginlerindendir. Keşfü'z-Zünûn "
                           "eserinde 15.000'den fazla kitabı ve 10.000'e yakın yazarı tanıtmıştır.",
                  'donem': '1609 – 1657 (İstanbul)',
                  'eserler': "Cihannümâ, Keşfü'z-Zünûn"},
 'matrakci_nasuh': {'ad': 'Matrakçı Nasuh',
                    'alan': 'Matematik, Minyatür, Haritacılık, Tarih',
                    'anahtar_kelimeler': ['matrakçı nasuh', 'matrakci nasuh', 'beyanı menazil'],
                    'bilgi': 'Kanuni döneminin çok yönlü matematikçisi, tarihçisi ve minyatür sanatçısıdır. '
                             'Şehirleri kuşbakışı üç boyutlu topografik haritalarla resmetmiştir.',
                    'donem': '1480 – 1564 (Bosna – İstanbul)',
                    'eserler': "Beyân-ı Menâzil, Cemâlü'l-Küttâb"},
 'mimar_sinan': {'ad': "Mimar Sinan (Koca Mi'mâr Sinân Âğâ)",
                 'alan': 'Mimari, İnşaat Mühendisliği, Akustik',
                 'anahtar_kelimeler': ['mimar sinan', 'sinan', 'süleymaniye', 'selimiye'],
                 'bilgi': "Osmanlı'nın başmimarıdır. Depreme dayanıklı temel sistemleri, kubbe statiği ve "
                          'akustik çözümleriyle yüzlerce şaheser bırakmıştır.',
                 'donem': '1489 – 1588 (Kayseri – İstanbul)',
                 'eserler': 'Şehzade, Süleymaniye ve Selimiye Camileri'},
 'nasiruddin_tusi': {'ad': 'Nasîrüddîn-i Tûsî',
                     'alan': 'Astronomi, Trigonometri, Mantık',
                     'anahtar_kelimeler': ['nasirüddin tusi', 'tusi', 'meraga rasathanesi'],
                     'bilgi': "Merâga Rasathanesi'ni kurmuş, trigonometriyi astronomiden bağımsız bir "
                              "matematik dalı haline getirmiş ve 'Tûsî Çifti' teoremini geliştirmiştir.",
                     'donem': '1201 – 1274 (Tûs – Merâga)',
                     'eserler': "Zîc-i İlhânî, Şeklü'l-Kattâ"},
 'omer_hayyam': {'ad': "Ömer Hayyâm (Gıyâseddin Ebü'l-Feth)",
                 'alan': 'Matematik, Cebir, Astronomi, Edebiyat',
                 'anahtar_kelimeler': ['ömer hayyam', 'omer hayyam', 'hayyam', 'celali takvimi'],
                 'bilgi': 'Kübik denklemleri geometrik yöntemlerle çözen büyük matematikçidir. Binom '
                          "açılımını kullanmış ve Celâlî Takvimi'ni hazırlamıştır.",
                 'donem': '1048 – 1131 (Nişabur)',
                 'eserler': 'Cebir Risalesi, Rubâiyyât'},
 'piri_reis': {'ad': 'Pîrî Reis (Hacı Ahmed Muhiddin Pîrî)',
               'alan': 'Denizcilik, Haritacılık, Coğrafya',
               'anahtar_kelimeler': ['piri reis', 'pîrî reis', 'kitab-ı bahriye', 'dünya haritası'],
               'bilgi': '1513 yılında çizdiği Dünya Haritası Amerika kıyılarını dönemin en yüksek '
                        'doğruluğuyla gösterir. Kitâb-ı Bahriye eşsiz bir denizcilik kılavuzudur.',
               'donem': '1465 – 1553 (Gelibolu / Osmanlı)',
               'eserler': 'Kitâb-ı Bahriye, 1513 Dünya Haritası'},
 'sabitu_bin_kurra': {'ad': 'Sâbit bin Kurra',
                      'alan': 'Matematik, Astronomi, Mekanik',
                      'anahtar_kelimeler': ['sabit bin kurra', 'harran'],
                      'bilgi': 'Dost sayılar teoremini bulan, diferansiyel ve integral hesabın öncü '
                               'adımlarını atan Harranlı büyük matematikçi ve astronomdur.',
                      'donem': '836 – 901 (Harran – Bağdat)',
                      'eserler': "Kitâbü'l-Karastûn"},
 'takiyuddin': {'ad': 'Takîyüddîn er-Râsıd',
                'alan': 'Astronomi, Optik, Mekanik Saatler',
                'anahtar_kelimeler': ['takiyüddin', 'takiyuddin', 'istanbul rasathanesi'],
                'bilgi': "İstanbul Rasathanesi'nin kurucusudur. Saniyeyi gösteren mekanik saatler yapmış ve "
                         'buhar gücüyle dönen düzenekler tasarlamıştır.',
                'donem': '1526 – 1585 (Şam – İstanbul)',
                'eserler': "Sidretü'l-Müntehâ, Et-Turuku's-Seniyye"},
 'ulug_bey': {'ad': 'Uluğ Bey (Muhammed Taragay)',
              'alan': 'Astronomi, Trigonometri',
              'anahtar_kelimeler': ['uluğ bey', 'ulug bey', 'semerkant rasathanesi'],
              'bilgi': "Semerkant'ta kurduğu dev rasathanede 1000'den fazla yıldızın konumunu ölçmüş ve bir "
                       'yılın süresini saniyeler mertebesinde yakın hesaplamıştır.',
              'donem': '1394 – 1449 (Semerkant)',
              'eserler': 'Zîc-i Uluğ Bey'},
 'zehrawi': {'ad': "ez-Zehrâvî (Ebü'l-Kâsım)",
             'alan': 'Cerrahi, Tıp, Biyomedikal Aletler',
             'anahtar_kelimeler': ['zehravi', 'ez-zehravi', 'cerrahi kurucusu', 'tasrif'],
             'bilgi': "Modern cerrahinin babası kabul edilir. 200'den fazla cerrahi aleti (bistüri, pens, "
                      'koter) çizimleriyle tanıtmış ve ameliyat dikişinde katgüt kullanmıştır.',
             'donem': '936 – 1013 (Endülüs / Kurtuba)',
             'eserler': "Kitâbü't-Tasrîf"},
 'ebu_hanife': {'ad': 'İmam-ı Âzam Ebû Hanîfe (Numan bin Sabit)',
                'donem': '699 - 767',
                'alan': 'Fıkıh, Kelam, İslam Hukuku',
                'eserler': "El-Fıkhu'l-Ekber, El-Âlim ve'l-Müteallim",
                'bilgi': 'Hanefî mezhebinin kurucusu, akıl ve nakli birleştiren büyük fıkıh ve kelam '
                         'bilginidir.',
                'anahtar_kelimeler': ['ebu hanife', 'imam azam', 'hanefi']},
 'imam_malik': {'ad': 'İmam Mâlik bin Enes',
                'donem': '711 - 795',
                'alan': 'Hadis, Fıkıh',
                'eserler': 'El-Muvatta',
                'bilgi': 'Medine ehlinin uygulamasını ve hadisleri derlediği El-Muvatta ile tanınan büyük '
                         'âlimdir.',
                'anahtar_kelimeler': ['imam malik', 'maliki', 'muvatta']},
 'ahmed_bin_hanbel': {'ad': 'İmam Ahmed bin Hanbel',
                      'donem': '780 - 855',
                      'alan': 'Hadis, Fıkıh',
                      'eserler': 'El-Müsned',
                      'bilgi': '30 binden fazla hadisi içeren El-Müsned adlı dev eserin yazarıdır.',
                      'anahtar_kelimeler': ['ahmed bin hanbel', 'hanbeli', 'müsned']},
 'imam_muslim': {'ad': 'İmam Müslim (Müslim bin Haccâc)',
                 'donem': '821 - 875',
                 'alan': 'Hadis İlmi',
                 'eserler': 'Sahîh-i Müslim',
                 'bilgi': "Kütüb-i Sitte'nin en temel iki kaynağından biri olan Sahîh-i Müslim'in yazarıdır.",
                 'anahtar_kelimeler': ['imam müslim', 'müslim', 'sahih müslim']},
 'imam_tirmizi': {'ad': 'İmam Tirmizî',
                  'donem': '824 - 892',
                  'alan': 'Hadis, Şemâil',
                  'eserler': 'Sünen-i Tirmizî, Şemâil-i Şerîf',
                  'bilgi': 'Hadisleri sıhhat derecelerine göre tasnif eden ve Şemâil geleneğini başlatan '
                           'âlimdir.',
                  'anahtar_kelimeler': ['tirmizi', 'imam tirmizi']},
 'imam_rabbani': {'ad': 'İmam Rabbânî (Ahmed Sirhindî)',
                  'donem': '1564 - 1624',
                  'alan': 'Tasavvuf, Kelam',
                  'eserler': 'Mektûbât',
                  'bilgi': 'İkinci bin yılın yenileyicisi (Müceddid-i Elf-i Sânî) olarak bilinen büyük '
                           'âlimdir.',
                  'anahtar_kelimeler': ['imam rabbani', 'mektubat']},
 'taberi': {'ad': 'İbn Cerîr et-Taberî',
            'donem': '839 - 923',
            'alan': 'Tefsir, Tarih',
            'eserler': "Câmiu'l-Beyân, Târîhu'l-Ümem ve'l-Mülûk",
            'bilgi': 'Rivayet tefsirinin ve İslam tarihçiliğinin kurucu isimlerindendir.',
            'anahtar_kelimeler': ['taberi', 'tefsir']},
 'zemahseri': {'ad': 'Zemahşerî',
               'donem': '1075 - 1144',
               'alan': 'Tefsir, Arap Dili, Belagat',
               'eserler': "El-Keşşâf, Esâsü'l-Belâğa",
               'bilgi': "Kur'an'ın dil ve belagat inceliklerini çözümleyen büyük dil ve tefsir bilginidir.",
               'anahtar_kelimeler': ['zemahşeri', 'keşşaf']},
 'fahruddin_razi': {'ad': 'Fahrüddin er-Râzî',
                    'donem': '1149 - 1209',
                    'alan': 'Tefsir, Kelam, Felsefe',
                    'eserler': "Mefâtîhu'l-Gayb (Tefsîr-i Kebîr)",
                    'bilgi': 'Felsefî kelam ve büyük dirayet tefsiriyle tanınan çok yönlü İslam bilginidir.',
                    'anahtar_kelimeler': ['fahruddin razi', 'razi']},
 'el_kindi': {'ad': 'El-Kindî (Yakub bin İshak)',
              'donem': '801 - 873',
              'alan': 'Felsefe, Kriptografi, Optik, Müzik',
              'eserler': "Risâle fî İstihrâci'l-Muammâ",
              'bilgi': 'İlk İslam filozofu sayılır; frekans analiziyle modern kriptolojinin (şifre '
                       'biliminin) temelini atmıştır.',
              'anahtar_kelimeler': ['kindi', 'el kindi', 'kriptoloji']},
 'zehravi': {'ad': "Ebü'l-Kâsım ez-Zehrâvî",
             'donem': '936 - 1013',
             'alan': 'Tıp, Cerrahi',
             'eserler': "Kitâbü't-Tasrîf",
             'bilgi': "Modern cerrahinin babasıdır; 200'den fazla cerrahi aleti tasarlamış ve katgüt dikiş "
                      'ipliğini kullanmıştır.',
             'anahtar_kelimeler': ['zehravi', 'cerrahi']},
 'battani': {'ad': 'El-Battânî',
             'donem': '858 - 929',
             'alan': 'Astronomi, Trigonometri',
             'eserler': "Kitâbü'z-Zîc",
             'bilgi': 'Güneş yılını 365 gün 5 saat 46 dakika olarak çok hassas hesaplamış ve sinüs/tanjantı '
                      'geliştirmiştir.',
             'anahtar_kelimeler': ['battani', 'trigonometri']},
 'fergani': {'ad': 'El-Fergânî',
             'donem': '800 - 870',
             'alan': 'Astronomi, Mühendislik',
             'eserler': "Cevâmiu İlmi'n-Nücûm",
             'bilgi': "Dünya'nın çevresini ölçen ekibin önde gelen astronomlarındandır; Ay'da bir kratere "
                      'adı verilmiştir.',
             'anahtar_kelimeler': ['fergani', 'astronomi']},
 'ibn_battuta': {'ad': 'İbn Battûta',
                 'donem': '1304 - 1369',
                 'alan': 'Coğrafya, Seyahatname',
                 'eserler': 'Rıhle (İbn Battûta Seyahatnamesi)',
                 'bilgi': "29 yıl boyunca yaklaşık 120.000 km yol katederek Asya, Afrika ve Anadolu'yu "
                          'anlatan büyük seyyahdır.',
                 'anahtar_kelimeler': ['ibn battuta', 'seyyah']},
 'evliya_celebi': {'ad': 'Evliya Çelebi',
                   'donem': '1611 - 1682',
                   'alan': 'Seyahatname, Kültür Tarihi',
                   'eserler': 'Seyahatnâme (10 Cilt)',
                   'bilgi': "50 yıla yakın gezdiği Osmanlı ve çevre coğrafyalarını 10 ciltlik Seyahatnâme'de "
                            'ölümsüzleştirmiştir.',
                   'anahtar_kelimeler': ['evliya çelebi', 'seyahatname']},
 'elmalili_hamdi': {'ad': 'Elmalılı Muhammed Hamdi Yazır',
                    'donem': '1878 - 1942',
                    'alan': 'Tefsir, Felsefe, Hukuk',
                    'eserler': "Hak Dini Kur'an Dili",
                    'bilgi': "Türkçe yazılmış en kapsamlı Kur'an tefsirlerinden Hak Dini Kur'an Dili'nin "
                             'müellifidir.',
                    'anahtar_kelimeler': ['elmalılı', 'hak dini']},
 'fuat_sezgin': {'ad': 'Prof. Dr. Fuat Sezgin',
                 'donem': '1924 - 2018',
                 'alan': 'İslam Bilim Tarihi',
                 'eserler': 'GAS (Arap-İslam Bilimler Tarihi)',
                 'bilgi': 'İslam medeniyetinin bilim tarihine katkılarını 17 ciltlik dev eseri ve İstanbul '
                          "Gülhane'deki müzesiyle belgelemiştir.",
                 'anahtar_kelimeler': ['fuat sezgin', 'bilim tarihi']},
 'aziz_sancar': {'ad': 'Prof. Dr. Aziz Sancar',
                 'donem': '1946 - Günümüz',
                 'alan': 'Biyokimya, Moleküler Biyoloji',
                 'eserler': 'DNA Onarım Mekanizmaları',
                 'bilgi': "2015 Nobel Kimya Ödülü'nü DNA onarım mekanizmalarını haritalandıran "
                          'çalışmalarıyla kazanan Türk bilim insanıdır.',
                 'anahtar_kelimeler': ['aziz sancar', 'nobel', 'dna']},
 'cahit_arf': {'ad': 'Ord. Prof. Dr. Cahit Arf',
               'donem': '1910 - 1997',
               'alan': 'Matematik (Cebir)',
               'eserler': 'Arf Değişmezi, Arf Halkaları',
               'bilgi': 'Matematik literatürüne Arf Sabiti ve Arf Halkaları kavramlarını kazandıran ünlü '
                        'Türk matematikçisidir.',
               'anahtar_kelimeler': ['cahit arf', 'arf sabiti']},
 'oktay_sinanoglu': {'ad': 'Prof. Dr. Oktay Sinanoğlu',
                     'donem': '1935 - 2015',
                     'alan': 'Kuantum Kimyası, Türkçe Bilim Dili',
                     'eserler': 'Bye Bye Türkçe, Hedef Türkiye',
                     'bilgi': "28 yaşında Yale'de en genç profesör olmuş, Türkçenin bilim dili olarak "
                              'korunmasını savunmuştur.',
                     'anahtar_kelimeler': ['oktay sinanoğlu', 'kuantum kimyası']},
 'isaac_newton': {'ad': 'Sir Isaac Newton (Yabancı Bilim İnsanı)',
                  'donem': '1643 - 1727',
                  'alan': 'Fizik, Matematik, Astronomi',
                  'eserler': 'Principia Mathematica',
                  'bilgi': 'Evrensel kütle çekim yasasını, hareketin üç temel kanununu ve '
                           'diferansiyel/integral kalkülüsü geliştirmiştir.',
                  'anahtar_kelimeler': ['newton', 'isaac newton', 'yerçekimi']},
 'albert_einstein': {'ad': 'Albert Einstein (Yabancı Bilim İnsanı)',
                     'donem': '1879 - 1955',
                     'alan': 'Kuramsal Fizik',
                     'eserler': 'Özel ve Genel Görelilik Kuramı, E=mc²',
                     'bilgi': 'Fotoelektrik etkiyle Nobel Fizik Ödülü almış, uzay-zaman ve görelilik '
                              'kuramıyla modern fiziği kurmuştur.',
                     'anahtar_kelimeler': ['einstein', 'albert einstein', 'görelilik']},
 'nikola_tesla': {'ad': 'Nikola Tesla (Yabancı Bilim İnsanı)',
                  'donem': '1856 - 1943',
                  'alan': 'Elektrik Mühendisliği, Fizik',
                  'eserler': 'Alternatif Akım (AC) Sistemi, Tesla Bobini',
                  'bilgi': 'Alternatif akım elektrik sistemini, asenkron motoru ve kablosuz enerji iletimi '
                           'temellerini geliştirmiştir.',
                  'anahtar_kelimeler': ['tesla', 'nikola tesla', 'alternatif akım']},
 'galileo_galilei': {'ad': 'Galileo Galilei (Yabancı Bilim İnsanı)',
                     'donem': '1564 - 1642',
                     'alan': 'Astronomi, Fizik',
                     'eserler': 'İki Büyük Dünya Sistemi Hakkında Diyalog',
                     'bilgi': "Teleskopu gökyüzüne çevirerek Jüpiter'in uydularını keşfetmiş, deneysel "
                              'bilimsel yöntemin öncüsü olmuştur.',
                     'anahtar_kelimeler': ['galileo', 'teleskop']},
 'marie_curie': {'ad': 'Marie Curie (Yabancı Bilim İnsanı)',
                 'donem': '1867 - 1934',
                 'alan': 'Fizik, Kimya (Radyoaktivite)',
                 'eserler': 'Polonyum ve Radyum Keşfi',
                 'bilgi': 'Hem Fizik hem Kimya alanında iki farklı Nobel Ödülü kazanan ilk ve tek bilim '
                          'insanıdır.',
                 'anahtar_kelimeler': ['marie curie', 'curie', 'radyoaktivite']},
 'alan_turing': {'ad': 'Alan Turing (Yabancı Bilim İnsanı)',
                 'donem': '1912 - 1954',
                 'alan': 'Bilgisayar Bilimi, Yapay Zeka, Kriptoloji',
                 'eserler': 'Turing Makinesi, Turing Testi',
                 'bilgi': 'Modern bilgisayar biliminin ve yapay zeka kavramının kurucusudur; II. Dünya '
                          "Savaşı'nda Enigma şifresini kırmıştır.",
                 'anahtar_kelimeler': ['alan turing', 'turing', 'enigma']},
 'ada_lovelace': {'ad': 'Ada Lovelace (Yabancı Bilim İnsanı)',
                  'donem': '1815 - 1852',
                  'alan': 'Matematik, Bilgisayar Programlama',
                  'eserler': 'Analitik Makine Notları',
                  'bilgi': 'Tarihin ilk bilgisayar programcısı olarak kabul edilir; Bernoulli sayılarını '
                           'hesaplayan ilk algoritmayı yazmıştır.',
                  'anahtar_kelimeler': ['ada lovelace', 'ilk programcı']},
 'grace_hopper': {'ad': 'Grace Hopper (Yabancı Bilim İnsanı)',
                  'donem': '1906 - 1992',
                  'alan': 'Bilgisayar Bilimi',
                  'eserler': 'İlk Derleyici (Compiler), COBOL',
                  'bilgi': 'İnsan diline yakın programlama dillerinin ve ilk derleyicinin geliştirilmesine '
                           'öncülük etmiştir.',
                  'anahtar_kelimeler': ['grace hopper', 'cobol', 'derleyici']},
 'tim_berners_lee': {'ad': 'Tim Berners-Lee (Yabancı Bilim İnsanı)',
                     'donem': '1955 - Günümüz',
                     'alan': 'Bilgisayar Bilimi, Ağ Teknolojileri',
                     'eserler': 'World Wide Web (WWW), HTTP, HTML',
                     'bilgi': "1989'da CERN'de World Wide Web'i (WWW), HTTP protokolünü ve HTML'i icat "
                              'etmiştir.',
                     'anahtar_kelimeler': ['tim berners lee', 'www', 'http']},
 'arsimet': {'ad': 'Arşimet (Archimedes - Yabancı Bilim İnsanı)',
             'donem': 'MÖ 287 - MÖ 212',
             'alan': 'Matematik, Fizik, Mühendislik',
             'eserler': 'Yüzen Cisimler Üzerine, Arşimet Vidası',
             'bilgi': 'Suyun kaldırma kuvvetini, kaldıraç yasalarını ve pi sayısının yaklaşık değerini '
                      'hesaplamıştır.',
             'anahtar_kelimeler': ['arşimet', 'archimedes', 'kaldırma kuvveti']},
 'oklid': {'ad': 'Öklid (Euclid - Yabancı Bilim İnsanı)',
           'donem': 'MÖ 325 - MÖ 265',
           'alan': 'Matematik, Geometri',
           'eserler': 'Elementler (Stoikheia)',
           'bilgi': 'Geometrinin babası olarak bilinir; Elementler eseri 2000 yıl boyunca temel matematik '
                    'ders kitabı olmuştur.',
           'anahtar_kelimeler': ['öklid', 'euclid', 'elementler']},
 'pisagor': {'ad': 'Pisagor (Pythagoras - Yabancı Bilim İnsanı)',
             'donem': 'MÖ 570 - MÖ 495',
             'alan': 'Matematik, Felsefe, Müzik',
             'eserler': 'Pisagor Teoremi (a² + b² = c²)',
             'bilgi': 'Dik üçgenlerde kenar bağıntısını formüle etmiş, sayılarla müzik armonisi arasındaki '
                      'ilişkiyi keşfetmiştir.',
             'anahtar_kelimeler': ['pisagor', 'pythagoras']},
 'aristoteles': {'ad': 'Aristoteles (Yabancı Filozof & Bilim İnsanı)',
                 'donem': 'MÖ 384 - MÖ 322',
                 'alan': 'Felsefe, Mantık, Biyoloji',
                 'eserler': "Organon, Nikomakhos'a Etik, Metafizik",
                 'bilgi': 'Biçimsel mantığın kurucusu olup Orta Çağ İslam ve Batı düşüncesini derinden '
                          'etkilemiştir.',
                 'anahtar_kelimeler': ['aristoteles', 'aristo', 'mantık']},
 'platon': {'ad': 'Platon (Eflatun - Yabancı Filozof)',
            'donem': 'MÖ 427 - MÖ 347',
            'alan': 'Felsefe, Siyaset, Matematik',
            'eserler': 'Devlet, Şölen, Timaios',
            'bilgi': "Atina Akademisi'ni kurmuş ve 'Geometri bilmeyen giremez' ilkesiyle matematiği "
                     'felsefenin temeline koymuştur.',
            'anahtar_kelimeler': ['platon', 'eflatun']},
 'sokrates': {'ad': 'Sokrates (Yabancı Filozof)',
              'donem': 'MÖ 469 - MÖ 399',
              'alan': 'Felsefe, Etik',
              'eserler': 'Sokratik Yöntem (Diyaloglar)',
              'bilgi': "'Bildiğim tek şey hiçbir şey bilmediğimdir' sözüyle sorgulayıcı düşünme yöntemini "
                       'geliştirmiştir.',
              'anahtar_kelimeler': ['sokrates', 'sokratik']},
 'rene_descartes': {'ad': 'René Descartes (Yabancı Bilim İnsanı)',
                    'donem': '1596 - 1650',
                    'alan': 'Matematik, Felsefe',
                    'eserler': 'Yöntem Üzerine Konuşma, Analitik Geometri',
                    'bilgi': 'Kartezyen koordinat sistemini kurarak cebir ile geometriyi birleştirmiştir.',
                    'anahtar_kelimeler': ['descartes', 'kartezyen']},
 'leonhard_euler': {'ad': 'Leonhard Euler (Yabancı Bilim İnsanı)',
                    'donem': '1707 - 1783',
                    'alan': 'Matematik, Fizik',
                    'eserler': 'Euler Özdeşliği (e^(iπ)+1=0), Graf Teorisi',
                    'bilgi': 'Modern matematik gösterimlerinin (f(x), e, i, Σ) çoğunu standartlaştıran en '
                             'üretken matematikçidir.',
                    'anahtar_kelimeler': ['euler', 'leonhard euler']},
 'carl_gauss': {'ad': 'Carl Friedrich Gauss (Yabancı Bilim İnsanı)',
                'donem': '1777 - 1855',
                'alan': 'Matematik, İstatistik, Fizik',
                'eserler': 'Disquisitiones Arithmeticae, Normal Dağılım',
                'bilgi': "'Matematikçilerin Prensi' olarak anılır; sayı teorisi, Gauss dağılımı ve "
                         'manyetizma alanında devrim yapmıştır.',
                'anahtar_kelimeler': ['gauss', 'normal dağılım']},
 'blaise_pascal': {'ad': 'Blaise Pascal (Yabancı Bilim İnsanı)',
                   'donem': '1623 - 1662',
                   'alan': 'Matematik, Fizik, Bilgisayar',
                   'eserler': 'Pascal Üçgeni, Pascaline Hesap Makinesi',
                   'bilgi': "İlk mekanik hesap makinelerinden Pascaline'i icat etmiş, olasılık teorisi ve "
                            'sıvı basıncı yasalarını kurmuştur.',
                   'anahtar_kelimeler': ['pascal', 'pascal üçgeni']},
 'gottfried_leibniz': {'ad': 'Gottfried Wilhelm Leibniz (Yabancı Bilim İnsanı)',
                       'donem': '1646 - 1716',
                       'alan': 'Matematik, Felsefe, Mantık',
                       'eserler': 'Kalkülüs (dy/dx), İkili (Binary) Sayı Sistemi',
                       'bilgi': 'Modern bilgisayarların temelini oluşturan ikili (0-1) sayı sistemini ve '
                                'türev/integral gösterimini geliştirmiştir.',
                       'anahtar_kelimeler': ['leibniz', 'binary', 'ikili sistem']},
 'michael_faraday': {'ad': 'Michael Faraday (Yabancı Bilim İnsanı)',
                     'donem': '1791 - 1867',
                     'alan': 'Fizik, Elektromanyetizma, Kimya',
                     'eserler': 'Elektromanyetik İndüksiyon, Faraday Kafesi',
                     'bilgi': 'Elektrik motoru ve jeneratörün temelini oluşturan elektromanyetik indüksiyonu '
                              'keşfetmiştir.',
                     'anahtar_kelimeler': ['faraday', 'indüksiyon']},
 'james_maxwell': {'ad': 'James Clerk Maxwell (Yabancı Bilim İnsanı)',
                   'donem': '1831 - 1879',
                   'alan': 'Fizik',
                   'eserler': 'Maxwell Denklemleri',
                   'bilgi': 'Elektrik, manyetizma ve ışığı dört denklemde birleştirerek kablosuz iletişimin '
                            'kuramsal temelini atmıştır.',
                   'anahtar_kelimeler': ['maxwell', 'elektromanyetik']},
 'johannes_kepler': {'ad': 'Johannes Kepler (Yabancı Bilim İnsanı)',
                     'donem': '1571 - 1630',
                     'alan': 'Astronomi, Matematik',
                     'eserler': "Kepler'in Gezegen Hareket Yasaları",
                     'bilgi': 'Gezegenlerin Güneş etrafında elips yörüngelerde döndüğünü matematiksel olarak '
                              'kanıtlamıştır.',
                     'anahtar_kelimeler': ['kepler', 'yörünge']},
 'richard_feynman': {'ad': 'Richard Feynman (Yabancı Bilim İnsanı)',
                     'donem': '1918 - 1988',
                     'alan': 'Kuantum Fiziği, Nanoteknoloji',
                     'eserler': 'Feynman Diyagramları, Feynman Dersleri',
                     'bilgi': "Kuantum elektrodinamiğiyle Nobel almış, nanoteknoloji fikrini ve 'Feynman "
                              "Öğrenme Tekniği'ni ortaya koymuştur.",
                     'anahtar_kelimeler': ['feynman', 'nanoteknoloji']},
 'stephen_hawking': {'ad': 'Stephen Hawking (Yabancı Bilim İnsanı)',
                     'donem': '1942 - 2018',
                     'alan': 'Kozmoloji, Astrofizik',
                     'eserler': 'Zamanın Kısa Tarihi, Hawking Işıması',
                     'bilgi': 'Kara deliklerin kuantum etkileriyle ışıma yaydığını (Hawking Işıması) öne '
                              'süren ünlü kozmologdur.',
                     'anahtar_kelimeler': ['hawking', 'kara delik']},
 'max_planck': {'ad': 'Max Planck (Yabancı Bilim İnsanı)',
                'donem': '1858 - 1947',
                'alan': 'Kuantum Fiziği',
                'eserler': 'Planck Sabiti (h), Kuantum Kuramı',
                'bilgi': 'Enerjinin kesikli paketler (kuanta) hâlinde yayıldığını göstererek kuantum '
                         'fiziğini başlatmıştır.',
                'anahtar_kelimeler': ['planck', 'kuantum']},
 'niels_bohr': {'ad': 'Niels Bohr (Yabancı Bilim İnsanı)',
                'donem': '1885 - 1962',
                'alan': 'Atom Fiziği, Kuantum Mekaniği',
                'eserler': 'Bohr Atom Modeli',
                'bilgi': 'Elektronların atom çekirdeği etrafında belirli enerji seviyelerinde döndüğünü '
                         'açıklayarak Nobel Fizik Ödülü almıştır.',
                'anahtar_kelimeler': ['bohr', 'atom modeli']},
 'louis_pasteur': {'ad': 'Louis Pasteur (Yabancı Bilim İnsanı)',
                   'donem': '1822 - 1895',
                   'alan': 'Mikrobiyoloji, Kimya',
                   'eserler': 'Pastörizasyon, Kuduz Aşısı',
                   'bilgi': 'Mikropların hastalıklara yol açtığını kanıtlamış, kuduz aşısını ve '
                            'pastörizasyon yöntemini geliştirmiştir.',
                   'anahtar_kelimeler': ['pasteur', 'pastörizasyon', 'aşı']},
 'alexander_fleming': {'ad': 'Alexander Fleming (Yabancı Bilim İnsanı)',
                       'donem': '1881 - 1955',
                       'alan': 'Tıp, Bakteriyoloji',
                       'eserler': 'Penisilin Keşfi',
                       'bilgi': "1928'de ilk antibiyotik olan penisilini keşfederek milyonlarca insanın "
                                'hayatını kurtarmıştır.',
                       'anahtar_kelimeler': ['fleming', 'penisilin']},
 'wright_kardesler': {'ad': 'Wright Kardeşler (Orville & Wilbur - Yabancı Mühendisler)',
                      'donem': '1867 - 1948',
                      'alan': 'Havacılık ve Uçak Mühendisliği',
                      'eserler': 'Wright Flyer (İlk Motorlu Uçuş)',
                      'bilgi': "1903'te ilk kontrollü ve motorlu insanlı uçuşu gerçekleştirerek modern "
                               'havacılığı başlatmışlardır.',
                      'anahtar_kelimeler': ['wright kardeşler', 'ilk uçak', 'havacılık']},
 'thomas_edison': {'ad': 'Thomas Alva Edison (Yabancı Mucit)',
                   'donem': '1847 - 1931',
                   'alan': 'Elektrik, İcatlar',
                   'eserler': 'Ticari Ampul, Fonograf, 1093 Patent',
                   'bilgi': 'Uzun ömürlü elektrik ampulünü ve ses kayıt cihazı fonografı geliştirerek '
                            'endüstriyel Ar-Ge laboratuvarını kurmuştur.',
                   'anahtar_kelimeler': ['edison', 'ampul']},
 'guglielmo_marconi': {'ad': 'Guglielmo Marconi (Yabancı Bilim İnsanı)',
                       'donem': '1874 - 1937',
                       'alan': 'Radyo İletişimi, Elektrik',
                       'eserler': 'Uzun Mesafe Kablosuz Telgraf / Radyo',
                       'bilgi': 'Atlantik ötesi ilk kablosuz radyo sinyalini göndererek 1909 Nobel Fizik '
                                "Ödülü'nü kazanmıştır.",
                       'anahtar_kelimeler': ['marconi', 'radyo']},
 'charles_darwin': {'ad': 'Charles Darwin (Yabancı Bilim İnsanı)',
                    'donem': '1809 - 1882',
                    'alan': 'Biyoloji, Doğa Tarihi',
                    'eserler': 'Türlerin Kökeni',
                    'bilgi': 'Doğal seçilim kuramıyla canlıların çevreye uyum süreçlerini incelemiştir.',
                    'anahtar_kelimeler': ['darwin', 'doğal seçilim']},
 'werner_heisenberg': {'ad': 'Werner Heisenberg (Yabancı Bilim İnsanı)',
                       'donem': '1901 - 1976',
                       'alan': 'Kuantum Mekaniği',
                       'eserler': 'Belirsizlik İlkesi',
                       'bilgi': 'Bir parçacığın konum ve momentumunun aynı anda kesin olarak '
                                "ölçülemeyeceğini belirten Belirsizlik İlkesi'ni kurmuştur.",
                       'anahtar_kelimeler': ['heisenberg', 'belirsizlik ilkesi']},
 'erwin_schrodinger': {'ad': 'Erwin Schrödinger (Yabancı Bilim İnsanı)',
                       'donem': '1887 - 1961',
                       'alan': 'Kuantum Mekaniği',
                       'eserler': 'Schrödinger Dalga Denklemi',
                       'bilgi': 'Kuantum sistemlerinin zaman içindeki değişimini tanımlayan dalga '
                                'denklemiyle Nobel Fizik Ödülü almıştır.',
                       'anahtar_kelimeler': ['schrödinger', 'dalga denklemi']},
 'graham_bell': {'ad': 'Alexander Graham Bell (Yabancı Mucit)',
                 'donem': '1847 - 1922',
                 'alan': 'İletişim Mühendisliği',
                 'eserler': 'Telefon Patenti (1876)',
                 'bilgi': 'Sesin elektrik sinyalleriyle iletilmesini sağlayan ilk pratik telefonun patentini '
                          'almıştır.',
                 'anahtar_kelimeler': ['graham bell', 'telefon']},
 'guido_van_rossum': {'ad': 'Guido van Rossum (Yabancı Yazılımcı)',
                      'donem': '1956 - Günümüz',
                      'alan': 'Bilgisayar Bilimi, Yazılım',
                      'eserler': 'Python Programlama Dili',
                      'bilgi': 'Okunabilirliği yüksek, yapay zeka ve bilimsel hesaplamada dünya lideri olan '
                               'Python dilinin yaratıcısıdır.',
                      'anahtar_kelimeler': ['guido', 'python yaratıcısı']},
 'linus_torvalds': {'ad': 'Linus Torvalds (Yabancı Yazılımcı)',
                    'donem': '1969 - Günümüz',
                    'alan': 'İşletim Sistemleri, Açık Kaynak',
                    'eserler': 'Linux Çekirdeği, Git',
                    'bilgi': 'Dünyadaki sunucuların ve Android cihazların temelini oluşturan Linux '
                             'çekirdeğini ve Git sürüm kontrol sistemini yazmıştır.',
                    'anahtar_kelimeler': ['linus torvalds', 'linux', 'git']},
 'geoffrey_hinton': {'ad': 'Geoffrey Hinton (Yabancı Yapay Zeka Bilimcisi)',
                     'donem': '1947 - Günümüz',
                     'alan': 'Yapay Zeka, Derin Öğrenme',
                     'eserler': 'Geri Yayılım (Backpropagation), Sinir Ağları',
                     'bilgi': "'Yapay Zekanın Babalarından' biri sayılır; derin öğrenme çalışmalarıyla 2024 "
                              "Nobel Fizik Ödülü'nü almıştır.",
                     'anahtar_kelimeler': ['geoffrey hinton', 'derin öğrenme']},
 'demis_hassabis': {'ad': 'Demis Hassabis (Yabancı Yapay Zeka Bilimcisi)',
                    'donem': '1976 - Günümüz',
                    'alan': 'Yapay Zeka, Biyoinformatik',
                    'eserler': 'AlphaGo, AlphaFold',
                    'bilgi': 'Google DeepMind kurucusu; protein katlanmasını çözen AlphaFold ile 2024 Nobel '
                             "Kimya Ödülü'nü kazanmıştır.",
                    'anahtar_kelimeler': ['demis hassabis', 'deepmind', 'alphafold']}}


ISLAM_ALIMLERI.update({'sah_veliyullah': {'ad': 'Şah Veliyullah Dehlevî', 'donem': '1703 - 1762', 'alan': 'Hadis, Fıkıh, İslam Düşüncesi', 'eserler': "Hüccetullahi'l-Bâliğa", 'bilgi': 'Hikmet-i teşrî (hükümlerin hikmetleri) alanında çığır açan Hindistanlı büyük İslam bilginidir.', 'anahtar_kelimeler': ['şah veliyullah', 'dehlevi']}, 'ibn_kesir': {'ad': 'İbn Kesîr', 'donem': '1301 - 1373', 'alan': 'Tefsir, Tarih, Hadis', 'eserler': "Tefsîrü'l-Kur'âni'l-Azîm, El-Bidâye ve'n-Nihâye", 'bilgi': "Kur'an'ı yine Kur'an ve sahih hadislerle açıklayan meşhur tefsir ve tarih âlimidir.", 'anahtar_kelimeler': ['ibn kesir', 'el bidaye']}, 'aziz_mahmud_hudayi': {'ad': 'Aziz Mahmud Hüdâyî', 'donem': '1541 - 1628', 'alan': 'Tasavvuf, Edebiyat, Hukuk', 'eserler': 'Dîvân-ı İlâhiyât, Tarîkatnâme', 'bilgi': "Üsküdar'daki dergâhıyla Osmanlı kültür ve irfan hayatına yön veren büyük mutasavvıftır.", 'anahtar_kelimeler': ['aziz mahmud hüdayi', 'hüdayi']}, 'mehmet_akif': {'ad': 'Mehmet Akif Ersoy', 'donem': '1873 - 1936', 'alan': 'Şiir, Düşünce, Veteriner Hekimlik', 'eserler': 'Safahat, İstiklâl Marşı', 'bilgi': "İstiklâl Marşı'mızın şairi, 'Asım'ın nesli' idealiyle bilim ve ahlakı birleştiren mütefekkirdir.", 'anahtar_kelimeler': ['mehmet akif', 'safahat', 'istiklal marşı']}, 'semseddin_sami': {'ad': 'Şemseddin Sâmî', 'donem': '1850 - 1904', 'alan': 'Sözlükçülük, Dilbilim, Edebiyat', 'eserler': "Kâmûs-ı Türkî, Kâmûsü'l-A'lâm", 'bilgi': "Türkçenin ilk modern sözlüklerinden Kâmûs-ı Türkî'yi ve ilk Türkçe romanı kaleme alan dil bilginidir.", 'anahtar_kelimeler': ['şemseddin sami', 'kamus']}, 'halil_inalcik': {'ad': 'Prof. Dr. Halil İnalcık', 'donem': '1916 - 2016', 'alan': 'Tarih (Osmanlı Tarihi)', 'eserler': 'Devlet-i Aliyye, Osmanlı İmparatorluğu Klasik Çağ', 'bilgi': "'Tarihçilerin Kutbu' unvanıyla anılan, Osmanlı tarihini dünya akademisine tanıtan büyük tarihçidir.", 'anahtar_kelimeler': ['halil inalcık', 'devlet-i aliyye']}, 'johann_gauss_bernoulli': {'ad': 'Jacob Bernoulli (Yabancı Bilim İnsanı)', 'donem': '1655 - 1705', 'alan': 'Matematik, Olasılık', 'eserler': 'Ars Conjectandi (Büyük Sayılar Yasası)', 'bilgi': "Olasılık teorisinde Büyük Sayılar Yasası'nı ve doğal logaritma tabanı e sayısını keşfetmiştir.", 'anahtar_kelimeler': ['bernoulli', 'olasılık']}, 'henri_poincare': {'ad': 'Henri Poincaré (Yabancı Bilim İnsanı)', 'donem': '1854 - 1912', 'alan': 'Matematik, Topoloji, Kaos Teorisi', 'eserler': 'Bilim ve Hipotez, Poincaré Sanısı', 'bilgi': 'Kaos teorisinin ve cebirsel topolojinin öncüsü kabul edilen ünlü Fransız matematikçidir.', 'anahtar_kelimeler': ['poincare', 'kaos teorisi']}, 'emmy_noether': {'ad': 'Emmy Noether (Yabancı Bilim İnsanı)', 'donem': '1882 - 1935', 'alan': 'Soyut Cebir, Kuramsal Fizik', 'eserler': 'Noether Teoremi', 'bilgi': "Fizikteki her simetrinin bir korunum yasasına karşılık geldiğini kanıtlayan Noether Teoremi'nin sahibidir.", 'anahtar_kelimeler': ['noether', 'simetri']}, 'john_von_neumann': {'ad': 'John von Neumann (Yabancı Bilim İnsanı)', 'donem': '1903 - 1957', 'alan': 'Bilgisayar Mimarisi, Oyun Teorisi, Matematik', 'eserler': 'Von Neumann Mimarisi, Oyun Teorisi', 'bilgi': 'Bugünkü tüm bilgisayarların işlemci-bellek yapısını (Von Neumann Mimarisi) tasarlayan dâhi matematikçidir.', 'anahtar_kelimeler': ['von neumann', 'bilgisayar mimarisi']}, 'claude_shannon': {'ad': 'Claude Shannon (Yabancı Bilim İnsanı)', 'donem': '1916 - 2001', 'alan': 'Bilgi Kuramı, Elektrik Mühendisliği', 'eserler': 'A Mathematical Theory of Communication', 'bilgi': "'Bilgi Kuramının Babası'dır; bit kavramını ve dijital devrelerin Boole cebriyle tasarımını kurmuştur.", 'anahtar_kelimeler': ['shannon', 'bilgi kuramı']}, 'dmitri_mendeleyev': {'ad': 'Dmitri Mendeleyev (Yabancı Bilim İnsanı)', 'donem': '1834 - 1907', 'alan': 'Kimya', 'eserler': 'Periyodik Tablo (1869)', 'bilgi': "Elementleri atom kütlelerine ve kimyasal özelliklerine göre sıralayarak Periyodik Tablo'yu oluşturmuştur.", 'anahtar_kelimeler': ['mendeleyev', 'periyodik tablo']}})

def islam_alimleri_studyosu_goster(sesli_soyle_fn):
    st.subheader(f"📜 İslam Âlimleri & Dünya Bilim İnsanları Ansiklopedisi ({len(ISLAM_ALIMLERI)} Kişi)")
    c_f1, c_f2 = st.columns([2, 1])
    with c_f1:
        arama_k = st.text_input("🔎 Bilim İnsanı veya Alan Ara:", placeholder="Örn: İbn Sina, Newton, Turing, Cezeri...", key="alim_arama_kutusu")
    with c_f2:
        kat_f = st.selectbox("Kategori:", ["Tümü", "İslam Âlimleri & Türk Bilginler", "Yabancı Bilim İnsanları"], key="alim_kat_filtre")

    filtrelenmis = []
    for kod, bilgi in ISLAM_ALIMLERI.items():
        yabanci_mi = "Yabancı" in bilgi["ad"]
        if kat_f == "İslam Âlimleri & Türk Bilginler" and yabanci_mi:
            continue
        if kat_f == "Yabancı Bilim İnsanları" and not yabanci_mi:
            continue
        if arama_k.strip():
            q_low = arama_k.strip().lower()
            birlesik = f"{bilgi['ad']} {bilgi['alan']} {bilgi['eserler']} {bilgi['bilgi']}".lower()
            if q_low not in birlesik:
                continue
        filtrelenmis.append((kod, bilgi))

    st.caption(f"Gösterilen kayıt: **{len(filtrelenmis)} / {len(ISLAM_ALIMLERI)}**")
    cols = st.columns(2, gap="medium")
    for idx, (kod, bilgi) in enumerate(filtrelenmis):
        with cols[idx % 2]:
            st.markdown(
                bilgi_karti_olustur(
                    f"📜 {bilgi['ad']} ({bilgi['donem']})",
                    f"{bilgi['alan']} | Eserler: {bilgi['eserler']}",
                    bilgi["bilgi"],
                ),
                unsafe_allow_html=True,
            )
            if st.button(f"🔊 Dinle: {bilgi['ad'].split('(')[0].strip()}", key=f"alim_ses_{kod}"):
                ses_metni = f"{bilgi['ad']}. {bilgi['donem']} yılları arasında yaşamıştır. {bilgi['bilgi']}"
                ses_bayt = sesli_soyle_fn(ses_metni, "tr")
                if ses_bayt:
                    st.audio(ses_bayt, format="audio/mp3")
