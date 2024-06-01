// println은 줄바꿈을 하는 프린트 print는 줄바꿈을 하지 않는 프린트

fn main() {
    for y in 1..10 {
        for x in 1..10 {
            if x == 9 {
                println!("{:3}", x * y);
            }
            else {
                print!("{:3},", x * y);
            }
        }
    }
}