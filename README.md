# Naver Band Crawler - Clean Gangnam
이 프로젝트는 강남구 청소용역업체 Band에 올라오는 포스팅을 분석하여 키워드 맞춤형 알림 서비스를 제공하는 텔레그램 챗봇입니다.


## 0. Requirement
requirement.txt 에 필요한 pip 패키지가 기술되어 있습니다.
* python 3.6 이상
* Linux Based System(Raspbian Buster 에서 테스트 되었습니다.)
  
## 1. Prepare
  1) 프로젝트 클론
    `git clone https://github.com/CXZ7720/BandCrawler_Cleangangnam.git`

  2) env 파일 생성 
    프로젝트 루트에 `env` 이름을 가진 파일을 생성하고 다음과 같이 각 줄에 순서대로 입력하여 저장합니다.

    ```
    ASDF1234-XX1234 <- Band 개발자센터에서 발급받은 API 키
    korea <- DB 접속 Username
    SUPERHARDPWD <- DB 접속 Password
    HELLO_WORLD <- 테이블 명
    1234123456:ASDFGHJKKLQWERTYUIOPZXCVBNNM <- Telegram Bot Father 에서 발급받은 Token
    -123456789123 <- 메시지를 보낼 Telegram 채널 ID
    ```

## 2. 원하는 키워드 수정
추출할 키워드는 `parseAddress.py`에 정규표현식으로 정의되어 있습니다. 정규표현식 규칙에 맞게 원하는 키워드로 교체하여 사용하시면 됩니다.

## 3. pip 패키지 설치
`pip3 install -r requirement.txt`

## 4. 실행
`python3 main.py`



그밖의 코드에 대한 간단한 설명 및 동작양상 : 
[Naver Band 키워드알림 챗봇 제작기](https://zerogyun.dev/2020/03/03/Naver-Band-%ED%81%AC%EB%A1%A4%EB%9F%AC-%EC%A0%9C%EC%9E%91%EA%B8%B0/)