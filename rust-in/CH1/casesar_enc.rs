fn encrypt(text: &str, shift: i16) -> String {
    let code_a = 'A' as i16;
    let code_z = 'Z' as i16;
    let mut result = String::new();
    for ch in text.chars() {
        // 문자 코드로 변환
        let mut code = ch as i16;
        // A와 Z 사이의 값인지
        if code_a <= code && code <= code_z {
            // shift만큼 뒤의 문자로 치환
            code = (code - code_a + shift + 26) % 26 + code_a;
        }

        result.push((code as u8) as char);
    }
    return result;
}

fn main() {
    let enc = encrypt("I LOVE RUST.", 3);
    let dec = encrypt(&enc, -3);
    println!("{} => {}", enc, dec);
}