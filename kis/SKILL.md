---
name: KIS Utils 
description: 한국투자증권 API를 파이썬에서 쉽고 간편하게 사용할 수 있도록 도와주는 유틸리티 스킬입니다.
---

# KIS Utils
이 스킬은 사용자가 한국투자증권 API를 사용하여 주식을 거래할 수 있도록 도와주는 
kis-utils 유틸리티 함수를 손쉽게 사용할 수 있도록 돕는 스킬입니다.

## What this skill does
접근 토큰 관리, 시세 조회, 잔고 확인 및 주문 기능을 간결한 인터페이스로 제공합니다. 
또한, 이러한 유틸리티 모듈을 파이썬에서 사용할 수 있도록 도와주는 역할을 수행합니다.

## When to use
* ".env 파일 생성해줘"
* "삼성전자 현재가 조회"
* "삼성전자 5주 시장가 매수 주문해줘"
* "실전투자 모드로 변경해줘"
* "내 계좌에 삼성전자 얼마 있는지 알려줘"
* "모의투자 계좌에 100만원 시장가 매수 주문해줘"
* "한국투자증권 모의투자 환경변수 설정해줘"

## When not to use
* 투자의견을 물어보는 경우
* 금융경제 지식 질문
* 시장 분석kis

## Prerequisites 

### .env 파일 설정
KIS API 연동을 위한 .env 설정 파일이 확인되지 않는 경우 웹 검색을 통해 실시간 시세를 확인하지 말고, 사용자에게 .env 파일 설정을 요청합니다.

환경변수의 값은 `.env` 파일에서만 읽어 옵니다.
사용자의 홈디렉토리에 `.env` 파일이 있는지 확인하여 파일이 없다면 다음 스크립트를 실행하여 홈디렉토리에 .env 파일을 생성합니다.

한국투자증권 API 계정은 https://api.koreainvestment.com 에서 발급받을 수 있습니다. 발급받은 앱키와 앱시크릿, 계좌번호를 
`.env` 파일의 해당 값에 입력합니다.

#### 윈도우 PowerShell
```powershell
$envFile = Join-Path $HOME ".env"

if (-not (Test-Path $envFile)) {

@'
# 실행 환경 ("실전투자" 또는 "모의투자")
KIS_ENVIRONMENT="실전투자"

# 실전투자 정보
KIS_APP_KEY="앱키"
KIS_APP_SECRET="앱시크릿"
KIS_ACCOUNT="계좌번호"
KIS_ACCOUNT_PROD="01"

# 모의투자 정보 (KIS_ENVIRONMENT="모의투자"인 경우 필수)
KIS_APP_KEY_VTS="모의투자 앱키"
KIS_APP_SECRET_VTS="모의투자 앱시크릿"
KIS_ACCOUNT_VTS="모의투자 계좌번호"
KIS_ACCOUNT_PROD_VTS="01"
'@ | Set-Content -Encoding UTF8 $envFile

    Write-Host ".env 파일 생성 완료: $envFile"

} else {

    Write-Host ".env 파일이 이미 존재합니다: $envFile"

}
```

#### 우분투 리눅스 Bash
```bash
#!/usr/bin/env bash

ENV_FILE="$HOME/.env"

if [ ! -f "$ENV_FILE" ]; then

cat << 'EOF' > "$ENV_FILE"
# 실행 환경 ("실전투자" 또는 "모의투자")
KIS_ENVIRONMENT="실전투자"

# 실전투자 정보
KIS_APP_KEY="앱키"
KIS_APP_SECRET="앱시크릿"
KIS_ACCOUNT="계좌번호"
KIS_ACCOUNT_PROD="01"

# 모의투자 정보 (KIS_ENVIRONMENT="모의투자"인 경우 필수)
KIS_APP_KEY_VTS="모의투자 앱키"
KIS_APP_SECRET_VTS="모의투자 앱시크릿"
KIS_ACCOUNT_VTS="모의투자 계좌번호"
KIS_ACCOUNT_PROD_VTS="01"
EOF

    echo ".env 파일 생성 완료: $ENV_FILE"

else

    echo ".env 파일이 이미 존재합니다: $ENV_FILE"

fi
```


### kis_utils CLI 설치

```bash
uv tool install kis_utils
```

## 활용법
CLI 인터페이스를 사용합니다. 

```bash
# 토큰 갱신
kis_utils token

# 현재가 조회 (기본 JSON 출력)
kis_utils price 005930

# 사람이 읽기 좋은 포맷으로 조회
kis_utils price 005930 --pretty

# 계좌 잔고 확인
kis_utils balance --pretty

# 주식 주문 (삼성전자 1주 시장가 매수)
kis_utils order 005930 -t buy -q 1 -p 0

# 주식 주문 (삼성전자 1주 시장가 매수)
kis_utils order 005930 --type buy --qty 1 --price 0

# 주식 주문 (삼성전자 1주 지정가 매수)
kis_utils order 005930 -t buy -q 1 -p 260000

# 주식 주문 (삼성전자 10주 지정가 매도)
kis_utils order 005930 -t sell -q 10 -p 280000

# 기간별 시세 (삼성전자 일자별 시세 조회)
kis_utils daily 005930 --pretty

# 매수가능 수량 조회 (삼성전자, 지정가 260000원 기준)
kis_utils buyable -p 260000 005930 --pretty

# 매수가능 수량 조회 (삼성전자, 시장가 기준)
kis_utils buyable -p 0 005930 --pretty

# 최근 7일간 주문 및 체결 내역 조회
kis_utils history --pretty
```

### 주요 명령어
- `token`: 접근 토큰 신규 발급 (토큰이 만료되었을 때 혹은 토큰이 없을 때 사용합니다)
- `price <종목코드>`: 현재가 정보 조회
- `daily <종목코드>`: 일/주/월 봉 데이터 조회
- `balance`: 계좌 잔고 및 보유 종목 조회
- `history`: 주문 및 체결 내역 조회
- `order <종목코드> --type <buy|sell> --qty <수량> --price <가격>`: 주식 주문 (매수/매도)
- `buyable <종목코드>`: 매수 가능 수량 조회

모든 명령어 뒤에 `--pretty`를 붙이면 한글 라벨이 포함된 가독성 좋은 화면을 볼 수 있습니다.
```

## Failure modes
- KIS API KEY 가 유효하지 않은 경우 실행을 중단하고, 한국투자증권 API의 접근 권한(AppKey/Secret) 설정을 안내 합니다.
- 작업공간에 KIS API 연동을 위한 .env 설정 파일이 확인되지 않는 경우 웹 검색을 통해 실시간 시세를 확인하지 말고, 사용자에게 .env 파일 설정을 요청합니다.
- 수신한 API의 에러 메시지를 사용자에게 그대로 전달하지 말고, 사용자 친화적인 메시지로 변환하여 전달합니다.

## Best practices
* 모든 명령어 뒤에 `--pretty`를 붙이면 한글 라벨이 포함된 가독성 좋은 화면을 볼 수 있습니다.
* 주문 요청 시 종목코드 뒤에 한글종목명을 함께 출력하면 사용자가 확인하기 쉽습니다.
* 가격이나 수량을 묻는 경우 현재가를 기준으로 시장가, 지정가, 최유리호가, 최우선호가를 안내하고 사용자가 원하는 가격을 선택하도록 합니다.

