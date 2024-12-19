fn main() {
    // 전화번호
    let phone = "010-1234-5678";

    // '-'로 분리
    let telno: Vec<&str> = phone.split('-').collect();
    println!("1: {}", telno[0]);
    println!("2: {}", telno[1]);
    println!("3: {}", telno[2]);
}