strings1 = "パトカー"
strings2 = "タクシー"

ans = "".join([i + j for i, j in zip(strings1, strings2)])
print(ans)
