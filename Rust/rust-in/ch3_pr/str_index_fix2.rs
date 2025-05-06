fn main() {
    // 첫 번째 글자 출력
    let ss = "베풀면 반드시 돌아온다";

    // str을 String으로 변환
    let so1: String = String::from(ss);
    let so2: String = ss.to_string();

    // String을 str로 변환
    let ss2: &str = &so1;
    let ss3: &str = so1.as_str();

    println!("{}\n{}\n{}\n{}", so1, so2, ss2, ss3);

    println!("{:p}\n{:p}", ss2, ss3)
}