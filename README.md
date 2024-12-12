# FinWise

## 프로젝트 소개
FinWise는 경제 기사 데이터를 수집, 분류, 그리고 시각화하여 사용자에게 직관적인 방식으로 경제 관련 정보를 제공하는 시스템입니다. 이 프로젝트는 FastAPI, React, MongoDB 및 D3.js와 같은 최신 기술을 활용하여 구성되었습니다.

## 시스템 아키텍처
프로젝트는 다음과 같은 주요 구성 요소로 이루어져 있습니다:
![image](https://github.com/user-attachments/assets/2a3b8bda-4409-446a-a4cd-8475af44069b)


### 1. **FastAPI (백엔드)**
- **기사 데이터 수집 및 전처리**
  - 뉴스 기사를 웹에서 크롤링하여 수집.
  - KoalaNLP와 KSS를 사용한 자연어 처리.
- **관계 데이터 생성**
  - 동시 카테고리 분류를 위해 HGNN(Heterogeneous Graph Neural Network) 적용.
  - PMI와 HGNN을 활용하여 기사 간 관계를 추출.
  - TF-IDF, KeyBERT, DeBERTa를 사용하여 중요 노드 선정 및 그래프 데이터 생성.

### 2. **MongoDB (데이터베이스)**
- 생성된 그래프 데이터를 저장.
- 누적 기사 그래프 데이터 요청 및 제공.

### 3. **프론트엔드**
- **크롬 확장 프로그램**
  - 경제 기사 URL을 전송하여 백엔드로 전달.
  - D3.js를 활용한 데이터 시각화.
- **React 기반 프론트엔드**
  - 사용자에게 개인화된 그래프 데이터를 시각적으로 제공.
  - 누적된 기사 그래프를 기반으로 사용자 이동 경로 생성.

## 주요 기능
1. **뉴스 기사 크롤링 및 NLP 분석**
   - 경제 관련 뉴스 데이터를 실시간으로 수집하고 전처리.
   - 문장 분리 및 키워드 추출.

2. **그래프 데이터 생성**
   - 기사 간 관계를 그래프로 표현.
   - 노드 중요도를 분석하여 주요 관계 시각화.

3. **D3.js 시각화**
   - 생성된 그래프 데이터를 D3.js로 시각화하여 사용자에게 제공.

4. **크롬 확장 프로그램**
   - 사용자가 읽고 있는 기사를 분석하고 관련 그래프 데이터를 제공.

## 크롬 확장 프로그램

Fin￦i$E 서비스를 위한 크롬 확장 프로그램은 한국대학교 INISW 아카데미 5기 소속 권수현, 김금환, 박서현, 이준혁, 조창희, 차시현에 의해 개발되었습니다.

### 사용 방법
1. 크롬 확장 프로그램 관리 페이지를 엽니다.
2. "개발자 모드"를 활성화합니다.
3. "압축 해제된 확장 프로그램 로드"를 선택합니다.
4. 해당 폴더를 선택합니다.

## FastAPI

Fin￦i$E 서비스를 위한 FastAPI는 한국대학교 INISW 아카데미 5기 소속 권수현, 김금환, 박서현, 이준혁, 조창희, 차시현에 의해 개발되었습니다.

### 사용 방법
#### Ubuntu 22.04 LTS 환경에서 Certbot을 사용하여 HTTPS 인증서 발급

#### Docker 설치
```bash
sudo apt update
sudo apt install docker.io
sudo systemctl start docker
sudo systemctl enable docker
```

#### Docker 이미지 빌드
```bash
docker build -t finwise-backend .
```

#### 컨테이너 실행
```bash
docker run -d --name finwise-backend -p 8000:8000 -v /etc/letsencrypt:/etc/letsencrypt finwise-backend
```

## React + Vite

이 템플릿은 Vite에서 React를 HMR과 ESLint 규칙과 함께 작동하도록 최소한의 설정을 제공합니다.

현재 두 가지 공식 플러그인이 사용 가능합니다:

- `@vitejs/plugin-react`는 Babel을 사용하여 Fast Refresh를 제공합니다.
- `@vitejs/plugin-react-swc`는 SWC를 사용하여 Fast Refresh를 제공합니다.

## 프로젝트 구조
```
├── Backend
│   ├── main.py                # FastAPI 엔드포인트 정의
│   ├── models                 # 데이터베이스 모델 정의
│   ├── utils                  # 전처리 및 알고리즘 유틸리티 함수
│   └── ...
├── Frontend
│   ├── public
│   ├── src
│   │   ├── components         # React 컴포넌트
│   │   ├── pages              # 페이지 정의
│   │   └── ...
│   └── ...
├── chrome_extension
│   ├── manifest.json          # 크롬 확장 프로그램 설정
│   ├── popup.html             # 팝업 UI
│   ├── background.js          # 백그라운드 스크립트
│   └── ...
├── README.md                  # 프로젝트 설명 파일
└── ...
```

## 사용 기술
- **백엔드**: FastAPI, Python, KoalaNLP, HGNN, TF-IDF, KeyBERT, DeBERTa
- **데이터베이스**: MongoDB
- **프론트엔드**: React, D3.js
- **크롬 확장 프로그램**: HTML, JavaScript, CSS

## 설치 및 실행 방법

### 1. 백엔드
```bash
cd Backend
pip install -r requirements.txt
uvicorn main:app --reload
```

### 2. 프론트엔드
```bash
cd Frontend
npm install
npm start
```

### 3. 크롬 확장 프로그램
1. `chrome_extension` 폴더를 크롬 확장 프로그램 로드 경로로 설정.
2. 확장 프로그램 활성화.

## 레포지토리 링크
[FinWise GitHub](https://github.com/csihyeon9/KU_INISW_5th_G1_FinWise)

## 참고 사항
- `inisw5th_G1_FinWise_Trial&Error` 폴더는 프로젝트에서 제외된 테스트 코드 및 참고 자료입니다.

## 기여 방법
1. 레포지토리를 포크합니다.
2. 새로운 브랜치를 생성합니다 (`git checkout -b feature/새로운기능`).
3. 변경 사항을 커밋합니다 (`git commit -m 'Add 새로운기능'`).
4. 브랜치에 푸시합니다 (`git push origin feature/새로운기능`).
5. Pull Request를 생성합니다.

## 라이선스
이 프로젝트는 MIT 라이선스를 따릅니다. 자세한 내용은 `LICENSE` 파일을 참조하세요.
