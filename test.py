from KoMS import KoMS

koms = KoMS()
result = koms.spacing_correction("안녕하세요 만나서 반갑습니다!", clean_text=True)

print(result)