# FinWise
## 💻 Tech Stack

### **Backend**
![FastAPI](https://img.shields.io/badge/FastAPI-009688?style=for-the-badge&logo=fastapi&logoColor=white)
![Python](https://img.shields.io/badge/Python%203.8.10-3776AB?style=for-the-badge&logo=python&logoColor=white)
![KoalaNLP](https://img.shields.io/badge/KoalaNLP-FF4500?style=for-the-badge)
![HGNN](https://img.shields.io/badge/HGNN-4CAF50?style=for-the-badge)
![TF-IDF](https://img.shields.io/badge/TF--IDF-FFDD44?style=for-the-badge)
![KeyBERT](https://img.shields.io/badge/KeyBERT-8E44AD?style=for-the-badge)
![DeBERTa](https://img.shields.io/badge/DeBERTa-1E90FF?style=for-the-badge)
![JAVA](https://img.shields.io/badge/Java%2021-007396?style=for-the-badge&logo=java&logoColor=white)

### **Database**
![MongoDB](https://img.shields.io/badge/MongoDB-47A248?style=for-the-badge&logo=mongodb&logoColor=white)

### **Frontend**
![React](https://img.shields.io/badge/React-61DAFB?style=for-the-badge&logo=react&logoColor=white)
![D3.js](https://img.shields.io/badge/D3.js-F9A03C?style=for-the-badge&logo=d3.js&logoColor=white)

### **Chrome Extension**
![HTML](https://img.shields.io/badge/HTML-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![CSS](https://img.shields.io/badge/CSS-1572B6?style=for-the-badge&logo=css3&logoColor=white)

---

## 프로젝트 소개
FinWise는 Linear Hyper-GNN을 이용하여 경제 기사 데이터를 수집, 분류, 그리고 시각화하여 
사용자에게 직관적인 방식으로 경제 관련 정보를 chrome exetension을 통해 제공하는 시스템입니다. 
이 프로젝트는 최신 기술 스택인 FastAPI, React, MongoDB 및 D3.js를 활용하여 설계되었습니다.

![image](https://github.com/user-attachments/assets/56c42a1c-ce62-4a06-905a-49335d9004c0)
## Team
FinWise 크롬 확장 프로그램은 고려대학교 지능정보 소프트웨어 아카데미 5기 1조에 의해 개발되었습니다.

<table>
  <tbody>
    <tr>
      <td align="center"><a href="https://github.com/soosookentelmanis"><img src="https://avatars.githubusercontent.com/u/150493527?v=4" width="100px;" alt=""/><br /><sub><b>팀원 : 권수현</b></sub></a><br /></td>
      <td align="center"><a href="https://github.com/imkhkim"><img src="https://avatars.githubusercontent.com/u/101717060?v=4" width="100px;" alt=""/><br /><sub><b>팀원 : 김금환</b></sub></a><br /></td>
      <td align="center"><a href="https://github.com/rosey418"><img src="https://avatars.githubusercontent.com/u/126850666?v=4" width="100px;" alt=""/><br /><sub><b>팀원 : 박서현</b></sub></a><br /></td>
     <tr/>
      <td align="center"><a href="https://github.com/leejoon2067"><img src="https://avatars.githubusercontent.com/u/77916205?v=4" width="100px;" alt=""/><br /><sub><b>팀원 : 이준혁</b></sub></a><br /></td>
      <td align="center"><a href="https://github.com/ntbboi"><img src="https://avatars.githubusercontent.com/u/175026543?v=4" width="100px;" alt=""/><br /><sub><b>팀원 : 조창희</b></sub></a><br /></td>
      <td align="center"><a href="https://github.com/csihyeon9"><img src="https://avatars.githubusercontent.com/u/110538039?v=4" width="100px;" alt=""/><br /><sub><b>팀원 : 차시현</b></sub></a><br /></td>
    </tr>
  </tbody>
</table>

## 시스템 아키텍처
![image](https://github.com/user-attachments/assets/9c546fbf-ac15-4f7d-9ea6-85be1222f5e9)

### 1. **FastAPI (백엔드)**
- **기사 데이터 수집 및 전처리**
  - 뉴스 기사를 웹에서 크롤링하여 데이터 수집.
  - KoalaNLP와 KSS를 활용한 자연어 처리.
- **관계 데이터 생성**
  - 동시 카테고리 분류를 위해 HGNN(Heterogeneous Graph Neural Network) 적용.
  - PMI와 HGNN을 사용해 기사 간 관계를 추출.
  - TF-IDF, KeyBERT, DeBERTa로 주요 노드를 선정해 그래프 데이터를 생성.

### 2. **MongoDB (데이터베이스)**
- 관계 및 그래프 데이터를 저장.
- 누적된 기사 그래프 데이터 요청 및 제공.

### 3. **프론트엔드**
- **크롬 확장 프로그램**
  - URL을 전송하여 백엔드와 통신.
  - D3.js 기반 시각화를 제공.
- **React 프론트엔드**
  - 개인화된 그래프 데이터를 사용자에게 시각적으로 제공.
  - 누적된 기사 그래프를 기반으로 사용자 이동 경로 생성.

---

## 주요 기능
1. **실시간 뉴스 크롤링 및 분석**
   - 경제 기사 웹 페이지에 접속하여 익스텐션 실행 시 NLP & HGNN 기술을 활용해 분석.
   - 문장 분리 및 키워드 추출.

2. **그래프 데이터 생성**
   - 기사 간 관계를 그래프로 표현.
   - 노드 중요도를 기반으로 주요 관계를 시각화.

3. **D3.js를 활용한 데이터 시각화**
   - 분석된 데이터를 시각화하여 직관적인 정보 제공.

4. **크롬 확장 프로그램**
   - 사용자가 읽고 있는 기사를 분석하고 연관된 데이터를 실시간으로 시각화.

---

### 사용 방법
1. 크롬 확장 프로그램 관리 페이지 열기.
2. "개발자 모드" 활성화.
3. "압축 해제된 확장 프로그램 로드" 선택.
4. 제공된 폴더 선택.

---

## FastAPI
FastAPI는 FinWise 백엔드의 주요 프레임워크로, 빠르고 직관적인 API 설계를 제공합니다.

### 사용 방법
#### Ubuntu 22.04 LTS에서 Certbot을 이용한 HTTPS 인증서 발급

#### Docker 설치 및 실행
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

---

## React + Vite
React와 Vite 기반으로 설계된 프론트엔드는 빠른 개발 환경과 HMR(Hot Module Replacement)을 제공합니다.

### 사용된 주요 플러그인
- `@vitejs/plugin-react`: Babel을 사용한 Fast Refresh 제공.
- `@vitejs/plugin-react-swc`: SWC를 사용한 Fast Refresh 제공.

---

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

---

## 사용 기술
- **백엔드**: FastAPI, Python(3.8.10), KoalaNLP, HGNN, TF-IDF, KeyBERT, DeBERTa, JAVA(21)
- **데이터베이스**: MongoDB
- **프론트엔드**: React, D3.js
- **크롬 확장 프로그램**: HTML, JavaScript, CSS

---

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

---

## 레포지토리 링크
[FinWise GitHub](https://github.com/csihyeon9/KU_INISW_5th_G1_FinWise)

---

## 참고 사항
- `inisw5th_G1_FinWise_Trial&Error` 폴더는 프로젝트에서 제외된 테스트 코드 및 참고 자료입니다.

---

## plus-alpha
1. 레포지토리를 포크합니다.
2. 새로운 브랜치를 생성합니다 (`git checkout -b feature/새로운기능`).
3. 변경 사항을 커밋합니다 (`git commit -m 'Add 새로운기능'`).
4. 브랜치에 푸시합니다 (`git push origin feature/새로운기능`).
5. Pull Request를 생성합니다.

---

## 라이선스
이 프로젝트는 MIT 라이선스를 따릅니다. 자세한 내용은 `LICENSE` 파일을 참조하세요.
