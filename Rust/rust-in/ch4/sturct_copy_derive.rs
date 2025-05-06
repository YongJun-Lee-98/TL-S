#[derive(Clone)]
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
	let alex = Person::new("Alex", 18);
	let mut betty = alex.clone();
	betty.name = String::from("Betty");
	println!("{},{}", alex.name, alex.age);
	println!("{},{}", betty.name, betty.age);
}