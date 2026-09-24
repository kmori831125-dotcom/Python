guests = ['佐々木さん', '山田さん', '高橋さん', '渡辺さん', '小林さん', '伊藤さん']
print("残念ながら、2人しか招待できなくなりました。")

while len(guests) > 2:
    removed_guest = guests.pop()
    print(f"{removed_guest}、申し訳ありませんが今回はご招待できません。")

for guest in guests:
    print(f"{guest}、引き続きご招待しております。")

del guests[0]
del guests[0]
print(guests)   # 空のリスト [] になっていることを確認