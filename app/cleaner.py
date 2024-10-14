import json

class Cleaner:
    def __init__(self) -> None:
        pass

    def degrees(self):
        data = {}
        temp = []

        with open('./data/degrees.json', 'r') as file:
            data = json.load(file)

        for d in data:    
            temp.append({
                "puan_turu": d["puanturu"],
                "osym_kodu": d["osymprogramkodu"],
                "bolum_adi": d["program_title"],
                "fakulte_adi": d["fakulteyuksekokul"],
                "universite_adi": d["universite"],
                "universite_turu": d["universiteturu"],
                "siralama": d["012katsayiileyerlesensonkisininbasarisirasi"],
                "kontenjan": d["genelkontenjan"]
            })

        with open('./data/degrees.json', 'w') as file:
            json.dump(temp, file, indent=4, ensure_ascii=False)