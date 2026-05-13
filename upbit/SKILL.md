---
name: upbit
description: 업비트 시세 조회, 캔들 조회, 잔고 확인, 주문 조회, 주문, 취소, 손절을 upbit_utils의 upbit CLI만으로 수행하도록 돕는 스킬입니다.
---

# Upbit

이 스킬은 사용자가 업비트의 코인 시세, 분봉 캔들, 계좌 잔고, 주문 내역, 주문, 주문 취소, 손절 기능을 `upbit` CLI로 사용할 수 있도록 돕는 스킬입니다.

## What this skill does

업비트 공개 시세 조회와 인증이 필요한 계좌/주문 작업을 CLI 명령으로 실행합니다.
Python API를 직접 호출하지 않고, `upbit_utils` 패키지가 제공하는 `upbit` 명령만 사용합니다.

## When to use

* "업비트 비트코인 현재가 조회"
* "KRW-BTC 1분봉 200개 가져와"
* "업비트 원화 마켓 코인 목록 보여줘"
* "업비트 잔고 조회"
* "업비트 미체결 주문 조회"
* "KRW-BTC 0.01개 지정가 매수"
* "업비트 주문 취소해줘"
* "보유 코인 -3% 손절 실행"
* "업비트 API KEY 환경변수 설정해줘"

## When not to use

* 투자의견을 물어보는 경우
* 금융경제 지식 질문
* 코인 시장 분석
* 업비트와 무관한 거래소 작업

## Prerequisites

### CLI only

업비트 작업은 반드시 `upbit` CLI로만 수행합니다.
`python -c`, 직접 Python 스크립트 작성, `upbit_utils` Python API 직접 호출, `requests`를 통한 업비트 REST API 직접 호출은 사용하지 않습니다.

Python API 예시는 CLI 명령을 이해하기 위한 대응표로만 사용합니다.

### .env 파일 설정

시세 조회 명령은 API KEY 없이 실행할 수 있습니다.

계좌/주문 명령은 `UPBIT_ACCESS_KEY`, `UPBIT_SECRET_KEY` 환경 변수가 필요합니다.
환경변수 값은 사용자의 홈디렉토리 `.env` 파일에서만 읽어 옵니다.

홈디렉토리에 `.env` 파일이 없으면 다음 스크립트로 생성합니다.
이미 `.env` 파일이 있으면 덮어쓰지 말고, 필요한 키만 사용자가 직접 채우도록 안내합니다.

업비트 API KEY는 업비트 Open API 관리 화면에서 발급받습니다.
주문, 취소, 손절을 실행하려면 해당 API KEY에 필요한 권한이 있어야 합니다.

#### 윈도우 PowerShell

```powershell
$envFile = Join-Path $HOME ".env"

if (-not (Test-Path $envFile)) {

@'
# 업비트 Open API 인증 정보
UPBIT_ACCESS_KEY="업비트 Access Key"
UPBIT_SECRET_KEY="업비트 Secret Key"
'@ | Set-Content -Encoding UTF8 $envFile

    Write-Host ".env 파일 생성 완료: $envFile"

} else {

    Write-Host ".env 파일이 이미 존재합니다: $envFile"
    Write-Host "UPBIT_ACCESS_KEY, UPBIT_SECRET_KEY 값을 확인하세요."

}
```

#### 우분투 리눅스 Bash

```bash
#!/usr/bin/env bash

ENV_FILE="$HOME/.env"

if [ ! -f "$ENV_FILE" ]; then

cat << 'EOF' > "$ENV_FILE"
# 업비트 Open API 인증 정보
UPBIT_ACCESS_KEY="업비트 Access Key"
UPBIT_SECRET_KEY="업비트 Secret Key"
EOF

    echo ".env 파일 생성 완료: $ENV_FILE"

else

    echo ".env 파일이 이미 존재합니다: $ENV_FILE"
    echo "UPBIT_ACCESS_KEY, UPBIT_SECRET_KEY 값을 확인하세요."

fi
```

### upbit_utils CLI 설치

```bash
uv tool install upbit_utils
```

설치된 환경에서는 `upbit` 명령을 바로 실행합니다.

## 활용법

CLI 인터페이스만 사용합니다.

```bash
# 매매가능한 모든 코인 목록: upbit.coin_list()
upbit --help
upbit coins
upbit coins --krw

# 특정 코인의 분단위 캔들: upbit.price_minute("KRW-BTC")
upbit candle KRW-BTC
upbit candle KRW-BTC --unit 1 --count 200
upbit candle KRW-BTC --unit 5 --count 100

# 특정 기간동안 분단위 캔들: upbit.price_minute_range(...)
upbit candle-range KRW-BTC --start "2025-11-08" --end "2025-11-09"
upbit candle-range KRW-BTC --start "2025-11-08 00:00:00" --end "2025-11-09 00:00:00" --unit 5

# 특정 코인의 현재가: upbit.price_ticker("KRW-BTC")
upbit price KRW-BTC

# 여러 코인의 현재가: upbit.price_ticker("KRW-BTC,KRW-ETH")
upbit price KRW-BTC,KRW-ETH

# 시장의 전체코인 현재가: upbit.price_ticker()
upbit price
```

계좌/주문 명령은 `UPBIT_ACCESS_KEY`, `UPBIT_SECRET_KEY` 환경 변수가 설정된 경우에만 실행합니다.

```bash
# 잔고 조회: upbit.balance()
upbit balance

# 미체결 목록: upbit.order_list()
upbit orders
upbit orders --market KRW-BTC --state wait

# 최근 체결 주문: upbit.order_list(None, state="done")
upbit orders --state done

# 주문: upbit.order("KRW-BTC", 0.01, 120000000, side="bid")
upbit order KRW-BTC 0.01 120000000 --side bid

# 주문취소: upbit.order_cancel(...)
upbit cancel 20233409-2f48-41e2-9340-eb25029c5777

# 모든 코인에 대해 -3% 손절: upbit.loss_cut(loss=-0.03)
upbit losscut --loss -0.03

# 여러 코인에 대해 손절: upbit.loss_cut(markets=["KRW-BTC", "KRW-ETH"], loss=-0.03)
upbit losscut --markets KRW-BTC,KRW-ETH --loss -0.03
```

### 주요 명령어

- `coins`: 매매 가능한 코인 목록 조회
- `coins --krw`: 원화 마켓 코인 목록 조회
- `candle <마켓>`: 특정 코인의 분단위 캔들 조회
- `candle <마켓> --unit <분> --count <개수>`: 분 단위와 개수를 지정해 캔들 조회
- `candle-range <마켓> --start <시작> --end <종료>`: 특정 기간의 분단위 캔들 조회
- `price [마켓목록]`: 현재가 조회. 마켓을 생략하면 전체 코인 현재가 조회
- `balance`: 계좌 잔고 조회
- `orders`: 주문 목록 조회
- `orders --market <마켓> --state <상태>`: 마켓과 주문 상태로 주문 목록 필터링
- `order <마켓> <수량> <가격> --side <bid|ask>`: 주문 실행
- `cancel <주문 UUID>`: 주문 취소
- `losscut --loss <손실률>`: 보유 코인 손절
- `losscut --markets <마켓목록> --loss <손실률>`: 지정 코인 손절

`order_closed()`에 직접 대응되는 CLI 명령은 아직 없습니다. 체결 완료 주문은 `upbit orders --state done`, 취소 주문은 `upbit orders --state cancel`로 조회합니다.

주문, 취소, 손절 명령은 실행 전 확인 프롬프트가 표시됩니다.

## Failure modes

- `upbit` 명령이 없으면 `uv tool install upbit_utils` 설치를 안내합니다.
- 시세 조회는 API KEY 없이 CLI로 실행합니다. 웹 검색이나 직접 REST API 호출로 대체하지 않습니다.
- 계좌/주문 작업에서 `.env` 설정이 확인되지 않으면 실행하지 말고, `UPBIT_ACCESS_KEY`, `UPBIT_SECRET_KEY` 설정을 안내합니다.
- API KEY가 유효하지 않거나 권한이 부족하면 작업을 중단하고, 업비트 Open API 권한과 키 설정을 확인하도록 안내합니다.
- 주문, 취소, 손절 명령은 확인 프롬프트가 있으므로 사용자의 의도와 마켓, 수량, 가격, 손실률을 명확히 확인한 뒤 실행합니다.
- CLI 에러 메시지를 그대로 던지지 말고, 실패한 명령과 원인을 사용자가 이해할 수 있게 요약합니다.

## Best practices

* 마켓 코드는 `KRW-BTC`처럼 업비트 형식으로 사용합니다.
* 여러 마켓은 `KRW-BTC,KRW-ETH`처럼 쉼표로 연결합니다.
* 날짜/시간 인자는 따옴표로 감쌉니다. 예: `"2025-11-08 00:00:00"`
* 주문 전에는 현재가를 먼저 조회하고, 시장가/지정가 의도를 확인합니다.
* 손절 전에는 대상 마켓과 손실률을 다시 확인합니다.
* 사용자가 Python API 형태로 요청해도 실제 실행은 대응되는 `upbit` CLI 명령으로 변환합니다.
