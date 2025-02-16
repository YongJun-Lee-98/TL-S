fn main() {
    // 거스름돈
    let price: i64 = 3950;
    let count500: i64 = 10;
    let count100: i64 = 3;
    let count50: i64 = 10;
    //조합계산
    for i500 in 0..(count500+1) {
        for i100 in 0..(count100+1) {
            for i50 in 0..(count50+1) {
                let total: i64 = i500 * 500 + i100 * 100 + i50 * 50;
                if total == price {
                    println!("500원x{}+100원x{}+50원x{}={}",
                i500, i100, i50, total);
                }
            }
        }
    }
}