fn main() {
    // let 불변 변수 선언
    // let mut는 가변 선언
    let mut a = 1;
    let mut b = 1;
    println!("{}", a);
    println!("{}", b);
    for _ in 0..30{
        println!("{}", a+b);
        let tmp = a;
        a = b;
        b = tmp + b;
    }
}