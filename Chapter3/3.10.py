rivers = ['ナイル川', 'アマゾン川', '長江', 'ドナウ川']

print(rivers)
rivers.append('メコン川')
rivers.insert(0, 'ガンジス川')
rivers.remove('ドナウ川')
popped = rivers.pop()
print(f"最後に取り出したのは{popped}でした。")
print("アルファベット/五十音順（一時的）:", sorted(rivers))
rivers.sort()
print("並べ替え後（永久）:", rivers)
rivers.reverse()
print("反転:", rivers)
print(f"現在の川の数: {len(rivers)}")