use std::rc::Rc;
use std::cell::RefCell;

fn main() {
	// 힙 영역에 i32 가변성을 가진 i32 타입 값 1000을 저장 -1
	let a = Rc::new(RefCell::new(1000));
	// 참조 카운터 증가 -2
	let b = Rc::clone(&a);
	// 값 변경 시도 -3
	*b.borrow_mut() += 100;
	// 원래의 참조 값 확인 -4
	println!("{}", a.borrow());
}