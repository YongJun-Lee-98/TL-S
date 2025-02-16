// 제네릭을 이용해 add 정의
fn add <T: std::ops::Add<Output=T>> (a:T, b:T) -> T {
	a + b
}

// 함수 사용하기
fn main() {
	println!("{}", add(10, 25));
	println!("{}", add(10.0, 25.0));
	println!("{}", add::<i32>(10, 25));
}