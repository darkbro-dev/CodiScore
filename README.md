# 🎨 CodiScore - AI 패션 스타일리스트

AI 기반 패션 분석 및 코디 점수 평가 앱입니다.

## 주요 기능

- 📸 **사진 업로드**: 자신의 패션 사진을 업로드
- 🎯 **TPO 분석**: 상황에 맞는 옷차림 평가
- 💯 **점수 산출**: 패션 점수, TPO 적합도, 스타일 분석
- 💡 **개선 제안**: AI가 제공하는 구체적인 스타일링 팁
- 🌍 **다국어 지원**: 12개 언어 지원

## 배포 방법

### Streamlit Community Cloud (무료)

1. GitHub에 코드 업로드
2. [Streamlit Community Cloud](https://streamlit.io/cloud) 접속
3. GitHub 저장소 연결
4. Secrets에 `GOOGLE_API_KEY` 추가
5. Deploy 클릭!

## 설정

### API 키 설정

Streamlit Community Cloud의 Secrets에 다음을 추가하세요:

```toml
GOOGLE_API_KEY = "your-api-key-here"
```

## 사용 기술

- **Streamlit**: 웹 인터페이스
- **Google Gemini API**: AI 분석
- **Python**: 백엔드

## 라이선스

개인 프로젝트
