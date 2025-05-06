// 소유권 테스트
fn main() {
    // 블록 1
    let a = String::from("test 문구입니다.");
    {
        let b = a;
        println!("{}", b);
    }
    println!("{}", a);
}