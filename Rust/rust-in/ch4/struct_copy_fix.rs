struct Person {
	name: String,
	age: i32,
}
impl Person {
	fn new(name: &str, age: i32) -> Self {
		Self { name: name.to_string(), age }
	}
}
fn main() {
	// Alex 생성
	let alex = Person::new("Alex", 18);
	// betty는 alex를 복제해 이름만 변경
	let betty = Person {
		name: String::from("Betty"),
		..alex
	};
	println!("{},{}", alex.name, alex.age);
	println!("{},{}", betty.name, betty.age);
}