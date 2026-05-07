# 📈 Invest Skills: AI Agent for Financial Investment

AI 에이전트가 금융 투자를 더 쉽고 효율적으로 수행할 수 있도록 돕는 전문 스킬셋 프로젝트입니다. 한국투자증권(KIS) API와 가상자산 거래소(Upbit) 연동을 통해 시장 분석부터 매매 실행까지 자동화된 워크플로우를 지원합니다.

## Key Features
- **한국투자증권(KIS) 연동**: 국내 및 해외 주식 시세 조회, 잔고 확인, 주문 실행 (`kis_utils`)
- **AI 에이전트 최적화**: LLM 에이전트가 직접 실행 가능한 CLI 및 스크립트 기반의 스킬 구성
- **간결한 워크플로우**: `uv`를 활용한 빠른 의존성 관리 및 실행 환경 제공

## Project Structure
```text
invest-skills/
├── hello/               # 기본 에이전트 연동 테스트를 위한 Hello World 스킬
│   ├── SKILL.md         # 스킬 정의서
│   └── scripts/         # 실행 스크립트 (hello.py)
├── kis_utils/           # 한국투자증권 API 연동 유틸리티 스킬
│   └── SKILL.md         # 상세 사용 가이드 및 환경 설정 안내
└── README.md            # 프로젝트 개요
```

## 🛠️ Prerequisites

이 프로젝트를 실행하기 위해 다음 도구들이 필요합니다:

- **Python 3.10+**
- **[uv](https://github.com/astral-sh/uv)**: 고성능 파이썬 패키지 및 프로젝트 관리자
- **Node.js 18.x+**: https://nodejs.org/en/download/
- **Git**: 소스 코드 형상 관리

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
# 한국투자증권(KIS) 유틸리티 스킬만 설치
npm skills add FinanceData/invest-skills/kis_utils

# Hello World 테스트 스킬만 설치
npm skills add FinanceData/invest-skills/hello
```

### 에이전트 지정 설치
특정 에이전트에 스킬을 할당하여 설치할 수 있습니다.
```sh
# 'my-invest-agent' 에이전트에 스킬 설치
npm skills add FinanceData/invest-skills --agent my-invest-agent
```


## 🤝 Contributing

프로젝트에 기여하고 싶으시다면 Issue를 등록하거나 Pull Request를 보내주세요. 모든 기여를 환영합니다!

---
© 2026 [FinanceData.KR](https://financedata.kr) All rights reserved.
