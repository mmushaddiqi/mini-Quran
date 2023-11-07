import json
import random

file_surah = open("surah.json",encoding="utf8" )
surah = json.load(file_surah)

# load file surah_terjemah.json ke dictionary
file_surah_terjemah = open("surah_terjemah.json", encoding="utf8")
surah_terjemah = json.load(file_surah_terjemah)

# gabungkan informasi dari kedua surah
for k in surah:
    s = surah[k]
    s["nama"] = surah_terjemah[k]["nama"]
    s["arti_nama"] = surah_terjemah[k]["nama"]
    
# memilih 10 surah secara acak
surah = list(surah.values())
surah_10 = random.sample(surah, k =10)

for s in surah_10:
    print(s["nama"])


print(surah["10"])
print(surah_terjemah["10"])