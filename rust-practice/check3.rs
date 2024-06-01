// 1~ 50 순서대로 출력하며
// 3의 배수와 3이 포함된 숫자는 숫자대신 'A'를 화면에 출력

fn main() {
    for i in 1..51 {
        if i % 3 == 0 || i % 10 == 3 {
            println!("A");
            continue;
        }
        if i > 30 && i <= 39 {
            println!("A");
            continue;
        }
        println!("{}", i);
    }
}