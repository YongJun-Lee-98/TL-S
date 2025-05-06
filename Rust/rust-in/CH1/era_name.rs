
fn main() {
    //1392 ~ 1450 연호를 서력과 함께 나타낸다.
    /* 
        태조는 1392년 정종은 1399년 태종은 1401년 세종은 1419년
        연호의 1년차는 '원년'으로 표시
    */

    for year in 1392..1451 {
        print!("서력 {}", year);
        // 대응 연호 출력 후 행 바꿈
        if year >= 1419 {
            if year == 1419 { println!("세종 원년");}
            else {println!("세종 {} 년", year-1419+1)}
        }
        else if year >= 1401 {
            if year == 1401 { println!("태종 원년")}
            else {println!("태종 {} 년", year-1401+1)}
        }
        else if year >= 1399 {
            if year == 1399 { println!("정종 원년")}
            else {println!("정종 {} 년", year-1399+1)}
        }
        else if year >= 1392 {
            if year == 1392 { println!("태조 원년")}
            else {println!("태조 {} 년", year-1392+1)}
        }
    }
}