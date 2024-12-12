# FinWise

## 프로젝트 소개
FinWise는 경제 기사 데이터를 수집, 분류, 그리고 시각화하여 사용자에게 직관적인 방식으로 경제 관련 정보를 제공하는 시스템입니다. 이 프로젝트는 FastAPI, React, MongoDB 및 D3.js와 같은 최신 기술을 활용하여 구성되었습니다.

## 시스템 아키텍처
프로젝트는 다음과 같은 주요 구성 요소로 이루어져 있습니다:
![image](https://github.com/user-attachments/assets/9b572a30-b690-4fa9-971e-f1e32d4e581e)


### 1. **FastAPI (Backend)**
- **기사 데이터 수집 및 전처리**
  - 뉴스 기사를 웹에서 크롤링하여 수집.
  - KoalaNLP와 KSS를 사용한 자연어 처리.
- **관계 데이터 생성**
  - 동시 카테고리 분류를 위해 HGNN(Heterogeneous Graph Neural Network) 적용.
  - PMI와 HGNN을 활용하여 기사 간 관계를 추출.
  - TF-IDF, KeyBERT, DeBERTa를 사용하여 중요 노드 선정 및 그래프 데이터 생성.

### 2. **MongoDB (Database)**
- 생성된 그래프 데이터를 저장.
- 누적 기사 그래프 데이터 요청 및 제공.

### 3. **Frontend**
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

## Chrome Extension for Fin￦i$E Services

Developed by Soohyun Kwon, Keumhwan Kim, Seohyun Park, Junhyeok Lee, Changhee Cho, and Sihyun Cha from the 5th cohort of Korea University INISW Academy.

### Usage
1. Open the Chrome Extensions management page.
2. Enable "Developer mode".
3. Select "Load unpacked".
4. Choose the folder.

### License
MIT License.

## FastAPI for Fin￦i$E Services

Developed by Soohyun Kwon, Keumhwan Kim, Seohyun Park, Junhyeok Lee, Changhee Cho, and Sihyun Cha from the 5th cohort of Korea University INISW Academy.

### Usage
#### Obtain an HTTPS certificate using Let's Encrypt's Certbot in an Ubuntu 22.04 LTS environment.

#### Install Docker
```bash
sudo apt update
sudo apt install docker.io
sudo systemctl start docker
sudo systemctl enable docker
```

#### Build the Docker Image
```bash
docker build -t finwise-backend .
```

#### Run the Container
```bash
docker run -d --name finwise-backend -p 8000:8000 -v /etc/letsencrypt:/etc/letsencrypt finwise-backend
```

### License
MIT License.

## React + Vite

This template provides a minimal setup to get React working in Vite with HMR and some ESLint rules.

Currently, two official plugins are available:

- `@vitejs/plugin-react` uses Babel for Fast Refresh
- `@vitejs/plugin-react-swc` uses SWC for Fast Refresh

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
- **Backend**: FastAPI, Python, KoalaNLP, HGNN, TF-IDF, KeyBERT, DeBERTa
- **Database**: MongoDB
- **Frontend**: React, D3.js
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
