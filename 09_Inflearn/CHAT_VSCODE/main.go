package main

import "log"

func init() {
	// 먼저 시작되는 작업
	log.Println("먼저 시작 됩니다.")
}

func main() {
	// 메인은 고유해야함
	log.Print("메인 함수 시작")
}
