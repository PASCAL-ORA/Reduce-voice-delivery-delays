Front 사용법(Node가 깔려있다는 기반)
실행 명령어 : npm run dev


python 사용법
설치 명령어 : pip install websockets google-cloud-speech python-dotenv
서비스 계정 키 파일 경로(google cloud console -> I AM 및 관리자 -> 서비스 계정 -> 키)
실행 명령어 : F5로 시작

Wav파일로 하면 OpenAi가 음성측면에서는 거의 다른 speech보다 압도적인 성능을 보여주었다.(https://github.com/PASCAL-ORA/Speech-Recognition-Comparison) 하지만 OpenAi는 실시간 스트리밍 방식이 아니라 wav파일 형식으로 저장해야하는 단점이 있어 딜레이가 생기는 문제점을 발견하였다.
그래서 2번째로 성능이 좋고 실시간 스트리밍 방식을 지원하는 google-speech를 채택하기로 하였다. 시간이 몇초에 걸리는지는 실시간이기 때문에 말하는 길이에 따라서 모든 시간이 다르기 때문에 결과값이 육안으로 나오는 걸 확인해야한다. 빠른걸 확인했다
