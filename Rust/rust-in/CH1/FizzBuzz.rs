// 1~100의 수를 순서대로 출력하는 프로그램
// 3의 배수에서는 Fizz
// 5의 배수에서는 Buzz
// 3과 5의 공배수인 경우 FizzBuzz
fn main() {
    for i in 1..101 {
        // 조건 일치를 확인
        if i % 3 == 0 && i % 5 == 0 {
            println!("FizzBuzz");
        }

        else if i % 3 == 0 {
            println!("Fizz");
        }

        else if i % 5 == 0 {
            println!("Buzz");
        }
        
        else {
            println!("{}", i);
        }
    }
}