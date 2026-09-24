guests = ['山田さん', '渡辺さん', '小林さん']
print("もっと大きなテーブルが見つかりました！")

guests.insert(0, '佐々木さん')       # 先頭に追加
guests.insert(2, '高橋さん')         # 中間に追加
guests.append('伊藤さん')            # 末尾に追加

for i in range(len(guests)):
    print(f"{guests[i]}、夕食にご招待します。")