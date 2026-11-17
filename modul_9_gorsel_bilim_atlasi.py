# -*- coding: utf-8 -*-
"""
==============================================================================
MODÜL 9: GÖRSEL BİLİM İNSANLARI & İSLAM ÂLİMLERİ ATLASI (102 KİŞİ)
Kronolojik Yürüyüş, SVG İnfografik Kartlar ve Adım Adım Keşif Hikâyesi
==============================================================================
"""
import importlib.util
import os
import sys
import streamlit as st
import streamlit.components.v1 as components


def _guvenli_modul_yukle(modul_adi: str):
    if modul_adi in sys.modules:
        return sys.modules[modul_adi]
    mevcut_dizin = os.path.dirname(os.path.abspath(__file__))
    hedef_yol = os.path.join(mevcut_dizin, f"{modul_adi}.py")
    if os.path.exists(hedef_yol):
        spec = importlib.util.spec_from_file_location(modul_adi, hedef_yol)
        if spec and spec.loader:
            mod = importlib.util.module_from_spec(spec)
            sys.modules[modul_adi] = mod
            spec.loader.exec_module(mod)
            return mod
    return None


m2_alimler = _guvenli_modul_yukle("modul_2_islam_alimleri")
ISLAM_ALIMLERI = getattr(m2_alimler, "ISLAM_ALIMLERI", {})


def _alan_ikon_ve_renk(alan: str):
    a = alan.lower()
    if any(k in a for k in ["fizik", "kuantum", "radyoaktivite", "elektrik", "kozmoloji"]):
        return "⚛️", "#38bdf8", "#0284c7", "atom"
    if any(k in a for k in ["matematik", "cebir", "geometri", "istatistik", "topoloji"]):
        return "📐", "#a78bfa", "#7c3aed", "math"
    if any(k in a for k in ["bilgisayar", "yapay zeka", "yazılım", "ağ", "kriptoloji"]):
        return "💻", "#34d399", "#059669", "code"
    if any(k in a for k in ["tıp", "cerrahi", "anatomi", "biyoloji", "mikrobiyoloji", "kimya"]):
        return "🧬", "#f472b6", "#db2777", "bio"
    if any(k in a for k in ["astronomi", "harita", "denizcilik", "coğrafya", "havacılık", "mühendislik", "robotik"]):
        return "🔭", "#fbbf24", "#d97706", "astro"
    return "📜", "#f59e0b", "#b45309", "scroll"


def _svg_ikon_uret(tip: str, renk1: str, renk2: str) -> str:
    if tip == "atom":
        return f'''<svg width="96" height="96" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
          <defs><linearGradient id="g1" x1="0" y1="0" x2="1" y2="1"><stop offset="0%" stop-color="{renk1}"/><stop offset="100%" stop-color="{renk2}"/></linearGradient></defs>
          <circle cx="50" cy="50" r="46" fill="rgba(15,23,42,0.85)" stroke="url(#g1)" stroke-width="2.5"/>
          <ellipse cx="50" cy="50" rx="32" ry="12" fill="none" stroke="{renk1}" stroke-width="2" transform="rotate(30 50 50)"/>
          <ellipse cx="50" cy="50" rx="32" ry="12" fill="none" stroke="{renk1}" stroke-width="2" transform="rotate(-30 50 50)"/>
          <ellipse cx="50" cy="50" rx="32" ry="12" fill="none" stroke="{renk2}" stroke-width="2" transform="rotate(90 50 50)"/>
          <circle cx="50" cy="50" r="6" fill="#fde047"/>
        </svg>'''
    if tip == "math":
        return f'''<svg width="96" height="96" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
          <circle cx="50" cy="50" r="46" fill="rgba(15,23,42,0.85)" stroke="{renk1}" stroke-width="2.5"/>
          <polygon points="26,72 74,72 26,28" fill="none" stroke="{renk1}" stroke-width="2.5"/>
          <rect x="26" y="60" width="12" height="12" fill="none" stroke="{renk2}" stroke-width="2"/>
          <text x="58" y="42" fill="#f8fafc" font-size="18" font-family="serif" font-weight="bold">π ∑</text>
        </svg>'''
    if tip == "code":
        return f'''<svg width="96" height="96" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
          <circle cx="50" cy="50" r="46" fill="rgba(15,23,42,0.85)" stroke="{renk1}" stroke-width="2.5"/>
          <rect x="22" y="28" width="56" height="40" rx="6" fill="none" stroke="{renk1}" stroke-width="2.2"/>
          <text x="50" y="54" text-anchor="middle" fill="{renk1}" font-size="19" font-family="monospace" font-weight="bold">&lt;/&gt;</text>
          <line x1="36" y1="74" x2="64" y2="74" stroke="{renk2}" stroke-width="3" stroke-linecap="round"/>
        </svg>'''
    if tip == "bio":
        return f'''<svg width="96" height="96" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
          <circle cx="50" cy="50" r="46" fill="rgba(15,23,42,0.85)" stroke="{renk1}" stroke-width="2.5"/>
          <path d="M34,24 C66,36 34,64 66,76" fill="none" stroke="{renk1}" stroke-width="3"/>
          <path d="M66,24 C34,36 66,64 34,76" fill="none" stroke="{renk2}" stroke-width="3"/>
          <line x1="39" y1="34" x2="61" y2="34" stroke="#f8fafc" stroke-width="2"/>
          <line x1="39" y1="50" x2="61" y2="50" stroke="#f8fafc" stroke-width="2"/>
          <line x1="39" y1="66" x2="61" y2="66" stroke="#f8fafc" stroke-width="2"/>
        </svg>'''
    if tip == "astro":
        return f'''<svg width="96" height="96" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
          <circle cx="50" cy="50" r="46" fill="rgba(15,23,42,0.85)" stroke="{renk1}" stroke-width="2.5"/>
          <circle cx="50" cy="50" r="26" fill="none" stroke="{renk1}" stroke-width="1.8" stroke-dasharray="4 3"/>
          <circle cx="50" cy="50" r="9" fill="#fde047"/>
          <circle cx="72" cy="36" r="4.5" fill="{renk1}"/>
          <circle cx="28" cy="64" r="3.5" fill="#38bdf8"/>
        </svg>'''
    return f'''<svg width="96" height="96" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
      <circle cx="50" cy="50" r="46" fill="rgba(15,23,42,0.85)" stroke="{renk1}" stroke-width="2.5"/>
      <rect x="30" y="26" width="40" height="48" rx="5" fill="none" stroke="{renk1}" stroke-width="2.3"/>
      <line x1="38" y1="38" x2="62" y2="38" stroke="#f8fafc" stroke-width="2"/>
      <line x1="38" y1="48" x2="62" y2="48" stroke="#f8fafc" stroke-width="2"/>
      <line x1="38" y1="58" x2="54" y2="58" stroke="{renk2}" stroke-width="2"/>
    </svg>'''


def bilim_insani_adimlari_olustur(bilgi: dict):
    """Bir bilim insanının hayatını ve keşiflerini 4 görsel yürüyüş adımına böler."""
    ad = bilgi["ad"]
    donem = bilgi["donem"]
    alan = bilgi["alan"]
    eserler = bilgi["eserler"]
    ozet = bilgi["bilgi"]
    return [
        ("1️⃣ Doğum & Dönem", f"{ad}, **{donem}** yılları arasında yaşayarak çağının bilimsel atmosferine yön verdi."),
        ("2️⃣ Uzmanlık Alanı", f"Temel çalışma alanları: **{alan}**."),
        ("3️⃣ Başlıca Eser & Keşif", f"İnsanlığa bıraktığı en önemli miras: **{eserler}**."),
        ("4️⃣ Tarihe Etkisi", ozet),
    ]


def bilim_insani_gorsel_karti_ciz(bilgi: dict, aktif_adim: int = 4):
    """Seçili bilim insanı için etkileşimli SVG + HTML görsel infografik kartı çizer."""
    ikon, r1, r2, tip = _alan_ikon_ve_renk(bilgi["alan"])
    svg_kod = _svg_ikon_uret(tip, r1, r2)
    adimlar = bilim_insani_adimlari_olustur(bilgi)

    adim_html = ""
    for i, (baslik, metin) in enumerate(adimlar, 1):
        acik = i <= aktif_adim
        op = "1" if acik else "0.28"
        bg = "rgba(56,189,248,0.12)" if acik else "rgba(15,23,42,0.4)"
        bd = r1 if acik else "rgba(148,163,184,0.2)"
        adim_html += f'''
        <div style="opacity:{op}; background:{bg}; border:1px solid {bd}; border-radius:12px; padding:10px 12px; margin-bottom:8px;">
            <div style="font-weight:700; color:{r1}; font-size:13px;">{baslik}</div>
            <div style="color:#e2e8f0; font-size:13px; margin-top:3px; line-height:1.45;">{metin.replace("**", "")}</div>
        </div>'''

    html_kart = f'''
    <div style="font-family:'Inter',sans-serif; background:linear-gradient(135deg,#071329,#0b1d3d); border:1.5px solid {r1}; border-radius:18px; padding:18px; color:#f8fafc; box-shadow:0 12px 30px rgba(0,0,0,0.45);">
        <div style="display:flex; align-items:center; gap:16px; margin-bottom:14px;">
            <div>{svg_kod}</div>
            <div>
                <div style="font-size:12px; color:{r1}; font-weight:700; letter-spacing:0.5px;">{ikon} {bilgi['donem']} · {bilgi['alan']}</div>
                <div style="font-size:21px; font-weight:800; color:#ffffff; margin:4px 0;">{bilgi['ad']}</div>
                <div style="font-size:13px; color:#cbd5e1;">📚 <b>Eserler / Keşifler:</b> {bilgi['eserler']}</div>
            </div>
        </div>
        <div style="margin-top:8px;">{adim_html}</div>
    </div>
    '''
    components.html(html_kart, height=430, scrolling=True)


def gorsel_bilim_atlasi_studyosu_goster(sesli_soyle_fn):
    st.subheader(f"🌌 Görsel Bilim İnsanları & İslam Âlimleri Atlası ({len(ISLAM_ALIMLERI)} Kişi)")
    st.caption("İster Marie Curie, ister Einstein, ister İbn Sînâ veya El-Cezerî seç; SVG görsel infografiklerle adım adım keşif yürüyüşüne çık!")

    if not ISLAM_ALIMLERI:
        st.warning("Bilim insanı veritabanı yüklenemedi.")
        return

    if "atlas_adim" not in st.session_state:
        st.session_state.atlas_adim = 4

    c1, c2 = st.columns([2, 1])
    with c1:
        anahtar_listesi = list(ISLAM_ALIMLERI.keys())
        varsayilan_idx = anahtar_listesi.index("marie_curie") if "marie_curie" in anahtar_listesi else 0
        secili_kod = st.selectbox(
            "🔭 Görsel Hikâyesini İncelemek İstediğin Bilim İnsanını Seç:",
            options=anahtar_listesi,
            index=varsayilan_idx,
            format_func=lambda k: f"{_alan_ikon_ve_renk(ISLAM_ALIMLERI[k]['alan'])[0]} {ISLAM_ALIMLERI[k]['ad']} ({ISLAM_ALIMLERI[k]['donem']})",
            key="atlas_kisi_sec",
        )
    with c2:
        kategori_sayilari = {
            "İslam & Türk Bilginleri": sum(1 for v in ISLAM_ALIMLERI.values() if "Yabancı" not in v["ad"]),
            "Yabancı Bilim İnsanları": sum(1 for v in ISLAM_ALIMLERI.values() if "Yabancı" in v["ad"]),
        }
        st.metric("Toplam Atlas Kaydı", f"{len(ISLAM_ALIMLERI)} Kişi", f"{kategori_sayilari['İslam & Türk Bilginleri']} İslam + {kategori_sayilari['Yabancı Bilim İnsanları']} Yabancı")

    secili_bilgi = ISLAM_ALIMLERI[secili_kod]

    b1, b2, b3, b4 = st.columns(4)
    if b1.button("⏮️ 1. Adımdan Başla", use_container_width=True, key="atlas_b1"):
        st.session_state.atlas_adim = 1
    if b2.button("🚶‍♂️ Bir Adım İlerle", use_container_width=True, key="atlas_b2"):
        st.session_state.atlas_adim = min(4, st.session_state.atlas_adim + 1)
    if b3.button("🌟 Tüm Hikâyeyi Aç", use_container_width=True, key="atlas_b3"):
        st.session_state.atlas_adim = 4
    with b4:
        if st.button("🔊 Sesli Anlat", use_container_width=True, key="atlas_ses"):
            metin = (
                f"{secili_bilgi['ad']}. {secili_bilgi['donem']} yılları arasında yaşamıştır. "
                f"Çalışma alanı {secili_bilgi['alan']}. Başlıca eserleri {secili_bilgi['eserler']}. {secili_bilgi['bilgi']}"
            )
            ses = sesli_soyle_fn(metin, "tr")
            if ses:
                st.audio(ses, format="audio/mp3")

    bilim_insani_gorsel_karti_ciz(secili_bilgi, aktif_adim=st.session_state.atlas_adim)
