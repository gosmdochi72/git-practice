def calc_volume(r, h):
    r = r / 12
    v = 3.141592 * (r ** 2) * h
    gallon = v * 7.48
    return gallon

r = int(input("반지름 길이 입력 : (단위 : inch) "))
h = int(input("높이 입력 : (단위 : feet) "))
volume = calc_volume(r, h)
print(f"물의 부피 : {volume:.1f} 갤런")