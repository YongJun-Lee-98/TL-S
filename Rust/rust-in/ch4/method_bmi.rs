// 키와 몸무게 항목을 가지는 구조체 Body 정의
struct Body {
	height: f64, // 키 cm
	weight: f64, // 몸무게 kg
}

impl Body {
	// BMI를 계산하는 메서드
	fn calc_bmi(&self) -> f64 {
		let h = self.height / 100.0;
		// BMI를 계산해 값을 반환
		self.weight / h.powf(2.0)
	}
	
	// 비만율을 계산하는 메서드
	fn calc_per(&self) -> f64 {
		self.calc_bmi() / 22.0 * 100.0
	}
}

// Body 구조체를 이용
fn main() {
	let yang = Body {
		height: 160.0,
		weight: 70.0,
	};
	println!("BMI = {:.2}", yang.calc_bmi());
	println!("비만율 = {:.1}%", yang.calc_per());
}