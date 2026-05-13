---
name: FinanceDataReader 금융 데이터
description: FinanceDataReader CLI 도구 `fdr`을 활용하여 국내외 주가, 지수, 환율, ETF, 종목 리스팅, 재무제표 등 금융 데이터를 조회·분석할 수 있도록 돕는 스킬입니다.
---

# FinanceDataReader 금융 데이터
이 스킬은 FinanceDataReader의 CLI 도구 `fdr`을 통해
국내외 주가, 지수, 환율, ETF, 종목 리스팅, 재무제표 등 금융 데이터를 손쉽게 조회·분석할 수 있도록 돕는 스킬입니다.

> **⚠️ 중요: 이 스킬은 반드시 `fdr` CLI 명령어만 사용합니다.**  
> `FinanceDataReader` 라이브러리를 import하여 파이썬 API 코드를 작성하지 마세요.  
> 모든 조회·분석은 `fdr` CLI 명령어를 실행하여 수행합니다.

## What this skill does
국내외 주식 가격, 지수(코스피/나스닥 등), 환율(USD/KRW 등), ETF 종목, KRX 전종목 리스팅,
재무제표(네이버), FRED 경제지표, ECOS 100대 경제지표 등 다양한 금융 데이터를 CLI로 조회합니다.
출력 형식을 CSV, JSON, Markdown 등으로 지정할 수 있어 분석 파이프라인과의 연계도 용이합니다.

## When to use
* "삼성전자 2026년 주가 데이터 조회해줘"
* "Apple 올해 상반기 주가 보여줘"
* "코스피 지수 2026년 추이 조회해줘"
* "달러/원 환율 추이 보여줘"
* "KRX 전종목 리스트 보여줘"
* "나스닥 종목 리스트 뽑아줘"
* "삼성전자 재무제표 조회해줘"
* "코스피 지수 구성종목 보여줘"
* "한국 ETF 전종목 리스트 조회해줘"
* "S&P500 종목 목록 보여줘"
* "100대 경제지표 목록 보여줘"
* "KRX 종목 리스트를 CSV 파일로 저장해줘"

## When not to use
* 투자 의견이나 매수/매도 추천을 요청하는 경우
* 실시간 주가 시세를 조회하는 경우 (→ `kis-utils` 스킬 사용)
* 주식 매매 주문을 실행하는 경우 (→ `kis-utils` 스킬 사용)
* 기업 공시(사업보고서, 지분공시 등)를 조회하는 경우 (→ `dart` 스킬 사용)

## Prerequisites

### fdr CLI 설치

`fdr` CLI는 `finance-datareader` 패키지에 포함되어 있습니다. 다음과 같이 설치합니다.

```bash
uv tool install finance-datareader
```

이미 설치되어 있고 업그레이드가 필요하다면 다음과 같이 실행합니다.

```bash
uv tool install --upgrade finance-datareader
```

> **참고:** `finance-datareader` 패키지는 `fdr` CLI를 제공하기 위해 설치합니다.  
> 파이썬 코드에서 `import FinanceDataReader`로 직접 API를 호출하지 않습니다.

설치 없이 바로 실행할 수도 있습니다.

```bash
uvx --from finance-datareader fdr price AAPL --start 2024
```

## 활용법

CLI 인터페이스를 사용합니다. `fdr`은 3가지 핵심 서브커맨드를 제공합니다.

### 가격 데이터 조회 (`price`)

시계열 가격 데이터(주가, 지수, 환율 등)를 조회합니다.

```bash
# 삼성전자 2024년~현재
fdr price 005930 --start 2024

# Apple 기간 지정
fdr price AAPL -s 2024-01-01 -e 2024-06-30

# 코스피 지수
fdr price KS11 -s 2024

# FRED 달러/원 환율
fdr price FRED:DEXKOUS -s 2020

# 달러 원화 환율
fdr price USD/KRW -s 2024
```

#### 주요 심볼 예시
| 심볼 | 설명 |
|------|------|
| `005930` | 삼성전자 (KRX 종목코드) |
| `AAPL` | Apple (미국 티커) |
| `KS11` | 코스피 지수 |
| `KQ11` | 코스닥 지수 |
| `DJI` | 다우존스 산업지수 |
| `IXIC` | 나스닥 종합지수 |
| `US500` | S&P 500 지수 |
| `USD/KRW` | 달러/원 환율 |
| `FRED:DEXKOUS` | FRED 달러/원 환율 |

### 스냅샷 데이터 조회 (`snap`)

특정 시점의 정보(종목 구성, 재무제표, 경제지표 목록 등)를 조회합니다.

```bash
# KRX 전체 지수 목록
fdr snap KRX/INDEX/LIST

# KOSPI 지수 구성종목
fdr snap KRX/INDEX/STOCK/1001

# 삼성전자 재무제표 (연간)
fdr snap NAVER/FINSTATE/005930

# 삼성전자 분기 재무제표 (별도)
fdr snap NAVER/FINSTATE-1Q/005930

# 삼성전자 분기 재무제표 (연결)
fdr snap NAVER/FINSTATE-2Q/005930

# 100대 경제지표
fdr snap ECOS/KEYSTAT/LIST
```

#### 주요 스냅샷 데이터 소스
| 경로 패턴 | 설명 |
|-----------|------|
| `KRX/INDEX/LIST` | KRX 전체 지수 목록 |
| `KRX/INDEX/STOCK/<지수코드>` | 특정 지수 구성종목 |
| `NAVER/FINSTATE/<종목코드>` | 네이버 재무제표 (연간) |
| `NAVER/FINSTATE-1Q/<종목코드>` | 네이버 분기 재무제표 (별도) |
| `NAVER/FINSTATE-2Q/<종목코드>` | 네이버 분기 재무제표 (연결) |
| `ECOS/KEYSTAT/LIST` | 한국은행 100대 경제지표 |

### 종목 리스팅 (`listing`)

거래소별 전종목 리스트를 조회합니다.

```bash
# KRX 전종목
fdr listing KRX

# KOSPI 종목
fdr listing KOSPI

# KOSDAQ 종목
fdr listing KOSDAQ

# 나스닥 종목
fdr listing NASDAQ

# S&P500 종목
fdr listing "S&P500"

# 한국 ETF 전종목
fdr listing ETF/KR
```

#### 지원하는 리스팅 거래소/시장
| 시장 코드 | 설명 |
|-----------|------|
| `KRX` | KRX 전종목 (KOSPI + KOSDAQ + KONEX) |
| `KOSPI` | KOSPI 종목 |
| `KOSDAQ` | KOSDAQ 종목 |
| `KONEX` | KONEX 종목 |
| `NASDAQ` | 나스닥 종목 |
| `NYSE` | 뉴욕증권거래소 종목 |
| `AMEX` | 아멕스 종목 |
| `S&P500` | S&P 500 종목 |
| `ETF/KR` | 한국 ETF 전종목 |

### 출력 형식 (`-f` 옵션)

모든 데이터 명령에 `-f` 옵션으로 출력 형식을 지정할 수 있습니다.

```bash
# CSV 형식
fdr price AAPL -s 2024 -f csv

# JSON 형식
fdr price AAPL -s 2024 -f json

# Markdown 테이블 형식
fdr price AAPL -s 2024 -f markdown

# 파일로 저장 (리다이렉션)
fdr listing KRX -f csv > krx_stocks.csv
```

| 형식 | 옵션 값 | 용도 |
|------|---------|------|
| CSV | `-f csv` | 스프레드시트, 데이터 분석 |
| JSON | `-f json` | 자동화 파이프라인, API 연계 |
| Markdown | `-f markdown` | 문서, 보고서 |

## 투자 활용 시나리오

### 시나리오 1: 개별 종목 분석
1. `fdr price 005930 -s 2024` 로 삼성전자 최근 주가 추이 조회
2. `fdr snap NAVER/FINSTATE/005930` 로 연간 재무제표 확인
3. `fdr snap NAVER/FINSTATE-1Q/005930` 로 분기 실적 추이 확인

### 시나리오 2: 시장 전체 현황 파악
1. `fdr price KS11 -s 2024` 로 코스피 지수 추이 확인
2. `fdr listing KRX -f csv > krx_stocks.csv` 로 전종목 리스트 저장
3. `fdr snap KRX/INDEX/LIST` 로 전체 지수 목록 확인
4. `fdr snap KRX/INDEX/STOCK/1001` 로 코스피 구성종목 확인

### 시나리오 3: 환율 및 거시경제 분석
1. `fdr price USD/KRW -s 2024` 로 달러/원 환율 추이 확인
2. `fdr price FRED:DEXKOUS -s 2020` 로 장기 환율 추이 확인
3. `fdr snap ECOS/KEYSTAT/LIST` 로 100대 경제지표 목록 확인

### 시나리오 4: 해외 종목 비교
1. `fdr price AAPL -s 2024` 로 Apple 주가 조회
2. `fdr listing NASDAQ -f csv > nasdaq.csv` 로 나스닥 종목 목록 저장
3. `fdr listing "S&P500"` 로 S&P500 구성종목 확인

### 시나리오 5: 한국 ETF 투자
1. `fdr listing ETF/KR` 로 한국 ETF 전종목 목록 조회
2. 관심 ETF의 종목코드로 `fdr price <종목코드> -s 2024` 로 수익률 추이 확인

## 주요 명령어 요약

| 명령어 | 설명 |
|--------|------|
| `fdr price <심볼> -s <시작일>` | 가격/시세 시계열 데이터 조회 |
| `fdr price <심볼> -s <시작일> -e <종료일>` | 기간 지정 가격 데이터 조회 |
| `fdr snap KRX/INDEX/LIST` | KRX 전체 지수 목록 |
| `fdr snap KRX/INDEX/STOCK/<지수코드>` | 특정 지수 구성종목 |
| `fdr snap NAVER/FINSTATE/<종목코드>` | 재무제표 (연간) |
| `fdr snap NAVER/FINSTATE-1Q/<종목코드>` | 분기 재무제표 (별도) |
| `fdr snap NAVER/FINSTATE-2Q/<종목코드>` | 분기 재무제표 (연결) |
| `fdr snap ECOS/KEYSTAT/LIST` | 100대 경제지표 |
| `fdr listing KRX` | KRX 전종목 리스팅 |
| `fdr listing KOSPI` | KOSPI 종목 리스팅 |
| `fdr listing NASDAQ` | 나스닥 종목 리스팅 |
| `fdr listing "S&P500"` | S&P500 종목 리스팅 |
| `fdr listing ETF/KR` | 한국 ETF 전종목 리스팅 |

모든 명령어에 `-f csv`, `-f json`, `-f markdown` 옵션을 추가하여 출력 형식을 지정할 수 있습니다.

## Failure modes
- `fdr` CLI가 설치되어 있지 않은 경우 `uv tool install finance-datareader` 설치를 안내합니다.
- 종목코드나 심볼이 잘못 입력된 경우 올바른 형식(국내 6자리 종목코드, 해외 티커 심볼)을 안내합니다.
- 네트워크 오류로 데이터 조회가 실패한 경우 인터넷 연결을 확인하도록 안내합니다.
- 지원하지 않는 시장 코드가 입력된 경우 지원 가능한 시장 코드 목록을 안내합니다.
- 수신한 에러 메시지를 사용자에게 그대로 전달하지 말고, 사용자 친화적인 메시지로 변환하여 전달합니다.

## Best practices
* **반드시 `fdr` CLI 명령어만 사용합니다.** 파이썬 스크립트에서 `FinanceDataReader`를 import하여 API를 직접 호출하는 코드를 작성하지 않습니다.
* 국내 종목은 6자리 종목코드(예: `005930`)를, 해외 종목은 티커 심볼(예: `AAPL`)을 사용합니다.
* 날짜는 `--start`(`-s`)와 `--end`(`-e`) 옵션으로 지정하며, 연도만 입력해도 됩니다(예: `-s 2024`).
* 데이터를 파일로 저장할 때는 `-f csv` 옵션과 리다이렉션(`>`)을 함께 사용합니다.
* `-f markdown` 옵션은 결과를 보고서에 삽입할 때 유용합니다.
* 재무제표 조회 시 연간(`FINSTATE`), 분기 별도(`FINSTATE-1Q`), 분기 연결(`FINSTATE-2Q`)을 구분하여 사용합니다.
* 지수 구성종목 조회 시 `KRX/INDEX/LIST`로 먼저 지수코드를 확인한 후 `KRX/INDEX/STOCK/<지수코드>`로 조회합니다.
