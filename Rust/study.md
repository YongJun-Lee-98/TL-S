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

### 