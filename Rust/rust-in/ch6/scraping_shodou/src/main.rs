use scraper::Selector;
use std::{fs::File, io::Write};
use tokio::time;

#[tokio::main]
async fn main() {
	// 특정 제목을 가진 작품 목록을 다운로드
	for title in ["test", "yiy"] {
		download_images(title).await;
	}
}

// 지정한 제목의 이밎지르 ㄹ다운 받는 함수
async fn download_images(title: &str) {
	let shodou_url = "https://uta.pw/shodou";
	// 제목으로 작품 검색
	let url = format!(
		"{}/index.php?titles&show&title={}",
		shodou_url,
		urlencoding::encode(title));
	// HTML 취득
	println!("get: {}", url);
	let html = reqwest::get(url)
		.await.unwrap()
		.text().await.unwrap();
	// HTML 구문 분석
	let doc = scraper::Html::parse_document(&html);
	// img 태그 추출
	let sel = Selector::parse(".articles img").unwrap();
	for (i, node) in doc.select(&sel).enumerate() {
		// <img src="***">의 src 속성값 추출
		let src = node.value().attr("src").unwrap();
		let img_url = format!("{}/{}", shodou_url, src);
		println!("{}", img_url);
		// 파일로 이미지를 저장
		let filename = format!("shodou_{}_{}.png", title, i);
		let bytes = reqwest::get(img_url).await.unwrap()
			.bytes().await.unwrap();
		let mut file = File::create(filename).unwrap();
		file.write_all(&bytes).unwrap();
		// 대기 시간을 설정(중요)
		time::sleep(time::Duration::from_millis(1000)).await;
	}
}