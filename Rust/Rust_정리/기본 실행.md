# Rust 활용해서 간단한 도구 만들기

## Cargo로 신규 프로젝트 생성
>$ cargo new [프로젝트 명]

tree 는 brew로 설치해서 보면 된다.
tree .

TOML은 설정 파일 작성을 위한 언어이다.  

## TOML
사양은 Github에 공개되어 있음  
몇 페이지 안되는 간단한 사양서로  TOML 형식이 단순하다는 것을 나타냄  
[Github TOML](https://github.com/toml-lang/toml.io)  
[한국어 문서](https://toml.io/ko/v0.5.0)

> 프로젝트 명으로 들어간 뒤  
> cargo run / cargo build를 사용할 수 있다.  

러스트에서 거듭제곱을 계산하기 위해서는 pow 메서드를 이용한다.  

### 큰수 계산을 위한 공개된 크레이트 사용하기
crates.io에 공개된 num-bigint 크레이트를 이용해보기  

Cargo.toml의 [dependencies] 내에 의존 라이브러리를 적는다.  
> num-bigint = "0.4"

main.rs에서는 
```rust
use num_bigint::BigInt;
```

### 크레이트는 Cargo.toml에 추가해서 사용 가능
num-bigint라는 크레이트를 이용하기 위해 Cargo.toml  
'extern crate ***' 표기
공개 러스트 소스 코드 중 extern crate 크레이트 명과 같이 선언하는 것을 볼 수 있다.  
이 선언 방법은 프로젝트 안에서 이용하고 싶은 크레이트를 프로젝트에 링크한다는 것  
러스트 2018부터는 사용하지 않는다.  
Cargo.toml에 'edition="2021"'과 같이 설정돼 있다면  
extern crate 선언을 하지 않아도 자동으로 크레이트를 링크해줌  

use는 반드시 사용할 필요는 없다.  
```rust
fn main() {
    let v = num_bigint::BigInt::from(1234);
    println!("{}", v.pow(5678));
}
```

### use 사용법
use 크레이트명::모듈;
use 크레이트명::모듈1::모듈1-1;
use 크레이트명::{모듈A, 모듈B};



