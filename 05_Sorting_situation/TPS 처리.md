websocket은 언제,왜 사용 하는가?

RPC 통신  
client -> 서버
client <- 서버

WebSocket 통신
client 1 -> 서버
서버 -> client 1
서버 -> client 2
서버 -> client 3
...

---
## websocket 사용시 주의사항
http 프로토콜을 사용하지는 않는 이유는  
리소스 절감이 목적  
