places = ['京都', '台北', 'ニューヨーク', 'ローマ', 'バンコク']

print("元の順番:", places)
print("一時的にアルファベット順:", sorted(places))
print("まだ元の順番のまま:", places)
print("一時的に逆アルファベット順:", sorted(places, reverse=True))
print("それでも元の順番のまま:", places)

places.reverse()
print("reverse()で反転:", places)
places.reverse()
print("もう一度reverse()で元に戻る:", places)

places.sort()
print("sort()で永久に並べ替え:", places)
places.sort(reverse=True)
print("sort(reverse=True)で永久に逆順:", places)