# Invest Skills: AI Agent for Financial Investment

AI 에이전트가 금융 데이터를 조회하고 투자 관련 작업을 CLI 기반으로 수행할 수 있도록 돕는 전문 스킬셋 프로젝트입니다. 금융감독원 DART 전자공시, FinanceDataReader, 한국투자증권(KIS), 업비트(Upbit) 연동을 통해 공시 분석, 시장 데이터 조회, 잔고 확인, 주문 실행까지 자동화된 워크플로우를 지원합니다.

## Key Features
- **DART 전자공시 연동**: 공시 검색, 재무제표 조회, 지분공시 추적, 사업보고서 분석 (`dart`)
- **FinanceDataReader 금융 데이터 조회**: 국내외 주가, 지수, 환율, ETF, 종목 리스팅, 재무제표 조회 (`fdr`)
- **한국투자증권(KIS) 연동**: 국내 주식 시세 조회, 잔고 확인, 주문 실행 (`kis`)
- **업비트(Upbit) 연동**: 코인 목록, 현재가, 분봉 캔들, 잔고, 주문, 취소, 손절 실행 (`upbit`)
- **AI 에이전트 최적화**: LLM 에이전트가 직접 실행 가능한 CLI 및 스크립트 기반의 스킬 구성
- **간결한 워크플로우**: `uv`를 활용한 빠른 의존성 관리 및 실행 환경 제공

## Project Structure
```text
invest-skills/
├── fdr/                 # FinanceDataReader 금융 데이터 조회 스킬
│   └── SKILL.md         # 주가·지수·환율·리스팅 조회 가이드
├── dart/                # DART 전자공시 연동 스킬
│   └── SKILL.md         # 공시 조회·분석 가이드 및 CLI 레퍼런스
├── kis/                 # 한국투자증권 API 연동 스킬
│   └── SKILL.md         # KIS CLI 사용 가이드 및 환경 설정 안내
└── upbit/               # 업비트 가상자산 거래소 연동 스킬
    └── SKILL.md         # Upbit CLI 사용 가이드 및 환경 설정 안내
```

## Prerequisites

이 프로젝트를 실행하기 위해 다음 도구들이 필요합니다:

- **Python 3.10+**
- **[uv](https://github.com/astral-sh/uv)**: 고성능 파이썬 패키지 및 프로젝트 관리자
- **Node.js 18.x+**: https://nodejs.org/en/download/
- **Git**: 소스 코드 형상 관리

각 스킬은 가능하면 Python API를 직접 호출하지 않고 대응되는 CLI 명령을 실행하도록 구성되어 있습니다.

## Installation

에이전트 스킬 관리자(`npm skills`)를 사용하여 필요한 스킬을 설치할 수 있습니다.

### 전체 설치
저장소에 포함된 모든 스킬을 설치합니다.
```sh
npm skills add FinanceData/invest-skills
```

### 선별적 설치
특정 스킬만 선택하여 설치하려면 저장소 경로 뒤에 하위 디렉토리를 지정합니다.
```sh
# DART 전자공시 스킬만 설치
npm skills add FinanceData/invest-skills/dart

# FinanceDataReader 스킬만 설치
npm skills add FinanceData/invest-skills/fdr

# 한국투자증권(KIS) 스킬만 설치
npm skills add FinanceData/invest-skills/kis

# 업비트 스킬만 설치
npm skills add FinanceData/invest-skills/upbit

```

## CLI Packages

스킬 설치와 별도로 실제 CLI 도구가 필요한 경우 `uv tool install`로 설치합니다.

```sh
# DART CLI
uv tool install opendartreader

# FinanceDataReader CLI
uv tool install finance-datareader

# KIS CLI
uv tool install kis_utils

# Upbit CLI
uv tool install upbit_utils
```

KIS와 Upbit의 계좌/주문 기능은 홈 디렉터리의 `.env` 파일에 API KEY와 계좌 정보를 설정해야 합니다. 공개 시세 조회는 인증 없이 실행 가능한 명령도 있습니다.

### 에이전트 지정 설치
특정 에이전트에 스킬을 할당하여 설치할 수 있습니다.
```sh
# 'claude-code' 에이전트에 스킬 설치
npm skills add FinanceData/invest-skills --agent claude-code

# 'codex' 에이전트에 스킬 설치
npm skills add FinanceData/invest-skills --agent codex

# 'codespaces' 에이전트에 스킬 설치
npm skills add FinanceData/invest-skills --agent codespaces

```


## Contributing

프로젝트에 기여하고 싶으시다면 Issue를 등록하거나 Pull Request를 보내주세요. 모든 기여를 환영합니다!

---
© 2026 [FinanceData.KR](https://financedata.kr) All rights reserved.
