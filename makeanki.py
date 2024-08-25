from pref import prefecture

outfile = open("a.tsv", "w",encoding="utf8")

for p in prefecture.values():
    print(f"""<img src="{p}.png">\t{p}<br><img src="alljapan.svg"><br>[sound:{p}.mp3]""", file=outfile)

outfile.close()
