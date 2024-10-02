
fn main() {
    for y in 1..10{
        let s = (1..10)
        // map을 이용해 문자열 벡터를 생성
        .map(|x| format!("{:3}", x * y))
        // join 메서드를 이용해 합치는 방식
        .collect::<Vec<String>>().join(",");
        println!("{}", s)
    }
}