# 🎙️ Speech Recognition Comparison

이 프로젝트는 다양한 음성 인식(STT) 서비스의 성능과 속도를 비교하여, 가장 빠르고 정확한 실시간 음성 인식 솔루션을 찾기 위해 만들어졌습니다.

## 🚀 프로젝트 개요

여러 음성 인식 서비스(네이버 Clova, IBM Watson, Google Cloud STT, OpenAI Whisper)를 동일한 오디오 파일을 이용해 테스트한 결과, **OpenAI Whisper**가 정확도 측면에서는 압도적인 성능을 보였습니다.

다만, OpenAI의 Whisper 모델은 실시간 스트리밍 방식이 아니라, 음성을 미리 WAV 파일 형식으로 저장해야 하는 특성상 실시간 처리에서 딜레이가 발생하는 단점이 존재합니다.

이에 따라, 실시간 음성 처리가 필수적인 환경에서는 Whisper 대신 실시간 스트리밍을 지원하는 Google Cloud STT를 활용하는 것이 가장 효율적입니다.

## 🥇 결과 요약

| 서비스 | 정확도 | 실시간 스트리밍 지원 | 속도(지연시간) |
|---|---|---|---|
| **OpenAI Whisper** | ✅ 매우 우수함 | ❌ 미지원 (wav파일 필요) | ⚠️ 처리 딜레이 존재 |
| **Google Cloud STT** | ✅ 우수함 | ✅ 지원 (Streaming) | ✅ 매우 빠름 |
| IBM Watson | ✅ 우수함 | ✅ 지원 (Streaming) | ✅ 빠름 |
| Naver STT | ✅ 우수함 | ✅ 지원 (Streaming) | ✅ 빠름 |

테스트 결과, WAV 형식으로 처리 시 **OpenAI Whisper**가 음성 인식 정확도에서는 압도적인 성능을 보였지만, 실시간 음성 인식에서는 **Google Cloud Speech-to-Text**가 우수한 정확도와 빠른 응답속도로 가장 뛰어난 성능을 보였습니다.

## 🔥 최종 선택

- **음성 정확도 (정적 파일 처리)**: ✅ **OpenAI Whisper 압도적 우위**
- **실시간 음성 인식 처리 속도**: ✅ **Google Cloud Speech-to-Text (Streaming)**

따라서 실시간 음성 통화 및 스트리밍 환경에서는 **Google Cloud Speech-to-Text**를 적극 추천합니다.

## 🛠️ 실행 방법

### ⚙️ 프론트엔드(Next.js)

```bash
npm install
npm run dev
```

### ⚙️ 백엔드(Python + Google STT)

```bash
pip install websockets google-cloud-speech python-dotenv
python server.py
```

## 📊 성능 평가

지연시간(latency)은 음성 데이터를 서버로 전송한 순간부터 서버에서 처리된 텍스트 결과가 다시 클라이언트로 돌아오는 순간까지의 시간을 밀리초(ms) 단위로 측정했습니다.

- ✅ **Google Cloud STT**의 실시간 스트리밍 방식 사용 결과, 실제 음성 입력 후 수 초 이내에 정확한 텍스트 결과를 받아올 수 있음을 확인했습니다.

## 🎯 결론

실시간 음성 인식을 구현할 때는 지연시간을 최소화하는 것이 핵심이며, **Google Cloud Speech-to-Text API**가 최적의 선택임을 실험을 통해 확인했습니다.

> 실시간 음성 처리가 핵심이라면 **Google Cloud STT** 사용을 강력히 추천합니다.

---

©️ **Speech Recognition Comparison Project** | Made by [PASCAL-ORA](https://github.com/PASCAL-ORA) 🚀✨

