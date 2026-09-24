guests = ['山田さん', '中村さん', '小林さん']

print(f"{guests[1]}は来られなくなりました。")
guests[1] = '渡辺さん'   

for i in range(len(guests)):
    print(f"{guests[i]}、夕食にご招待します。")