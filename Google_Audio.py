import asyncio
import websockets
from google.cloud import speech
import os
from queue import Queue
import threading
from dotenv import load_dotenv

load_dotenv()
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "youtube-api-416409-5cf8548b6099.json"

client = speech.SpeechClient()

async def recognize(websocket):
    print("✅ 클라이언트 연결됨")
    audio_queue = Queue()

    def audio_generator():
        while True:
            chunk = audio_queue.get()
            if chunk is None:
                break
            yield speech.StreamingRecognizeRequest(audio_content=chunk)

    def stt_worker():
        config = speech.RecognitionConfig(
            encoding=speech.RecognitionConfig.AudioEncoding.WEBM_OPUS,
            sample_rate_hertz=48000,
            language_code="ko-KR",
        )
        streaming_config = speech.StreamingRecognitionConfig(
            config=config,
            interim_results=False,
            single_utterance=True
        )

        requests = audio_generator()
        responses = client.streaming_recognize(streaming_config, requests)

        try:
            for response in responses:
                for result in response.results:
                    if result.is_final:
                        transcript = result.alternatives[0].transcript
                        print(f"✅ STT 결과: {transcript}")
        except Exception as e:
            print(f"⚠️ STT 에러: {e}")

    stt_thread_started = False

    try:
        async for message in websocket:
            if isinstance(message, bytes):
                audio_queue.put(message)

                # ✅ 오디오 데이터가 처음 들어왔을 때만 STT 시작
                if not stt_thread_started:
                    threading.Thread(target=stt_worker, daemon=True).start()
                    stt_thread_started = True

    except websockets.exceptions.ConnectionClosed:
        print("⚠️ 클라이언트 연결 종료됨")
    finally:
        audio_queue.put(None)

async def main():
    async with websockets.serve(recognize, "localhost", 8000):
        print("🚀 서버가 localhost:8000에서 실행 중...")
        await asyncio.Future()

if __name__ == "__main__":
    asyncio.run(main())
