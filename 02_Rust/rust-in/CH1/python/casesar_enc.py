def encrypt(text, shift):
    code_a = ord('A')
    code_z = ord('Z')
    # 결과를 대입할 변수를 준비
    result = ""
    
    for ch in text:
        code = ord(ch)
        if code_a <= code <= code_z:
            code = (code - code_a + shift) % 26 + code_a
        result += chr(code)
    return result

# 함수 호출
enc = encrypt("I LOVE RUST.", 3)
dec = encrypt(enc, -3)

print(f"{enc}=>{dec}")