# osmanlica_ceviri.py

osmanli_to_latin = {
    "ا": "a", "ب": "b", "پ": "p", "ت": "t", "ث": "s",
    "ج": "c", "چ": "ç", "ح": "h", "خ": "h", "د": "d",
    "ذ": "z", "ر": "r", "ز": "z", "ژ": "j", "س": "s",
    "ش": "ş", "ص": "s", "ض": "z", "ط": "t", "ظ": "z",
    "ع": "a", "غ": "ğ", "ف": "f", "ق": "k", "ك": "k",
    "گ": "g", "ڭ": "ŋ", "ل": "l", "م": "m", "ن": "n",
    "و": "v", "ه": "h", "ﻩ": "e", "ى": "i", "ی": "i",
    "آ": "a", "ي": "i",
}

def osmanlica_cevir(metin, tablo):
    return ''.join([tablo.get(harf, '?') for harf in metin])

def harf_benzeme_orani(asci, gercek):
    min_len = min(len(asci), len(gercek))
    dogru = sum([1 for i in range(min_len) if asci[i] == gercek[i]])
    return round(dogru / len(gercek) * 100, 2)

veriler = [
    ("رمضان", "ramazan"),
    ("قراهلرله", "kurallarla"),
    ("اولماسى", "uyulması"),
    ("آينده", "ayında"),
    ("علـاقـدر", "ilgili"),
]

if _name_ == "_main_":
    for osmanlica, gercek in veriler:
        ceviri = osmanlica_cevir(osmanlica, osmanli_to_latin)
        oran = harf_benzeme_orani(ceviri, gercek)
        print(f"Osmanlıca: {osmanlica} → Çeviri: {ceviri} | Gerçek: {gercek} | Doğruluk: %{oran}")