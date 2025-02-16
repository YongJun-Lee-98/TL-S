#[cfg(test)]
mod tests {
    #[test]
    fn calc_test1() {
        assert_eq!(100 *2, 200);
    }

    #[test]
    fn calc_test2() {
        assert_eq!(2 * 3, 6);
        // 일부러 틀린 값을 설정
        assert_eq!(2 * 3, 7);
    }
}
