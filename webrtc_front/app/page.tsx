"use client";
import { useEffect, useState, useRef } from "react";

export default function Home() {
  const [isListening, setIsListening] = useState(false);

  const wsRef = useRef<WebSocket | null>(null);
  const mediaRecorderRef = useRef<MediaRecorder | null>(null);

  const startListening = async () => {
    setIsListening(true);
 

    // ✅ WebSocket을 녹음 시작 시 연결
    wsRef.current = new WebSocket("ws://localhost:8000");
    wsRef.current.onopen = () => {
      console.log("✅ WebSocket 연결됨");
      startRecording(); // 웹소켓이 열리면 녹음 시작
    };

   
    wsRef.current.onerror = (error) => console.error("❌", error);
    wsRef.current.onclose = () => console.warn("⚠️ WebSocket 닫힘");
  };

  const startRecording = async () => {
    const stream = await navigator.mediaDevices.getUserMedia({ audio: true });
    mediaRecorderRef.current = new MediaRecorder(stream, { mimeType: "audio/webm;codecs=opus" });

    mediaRecorderRef.current.ondataavailable = async (event) => {
      if (event.data.size > 0 && wsRef.current?.readyState === WebSocket.OPEN) {
        const buffer = await event.data.arrayBuffer();
        wsRef.current.send(buffer);
      }
    };

    mediaRecorderRef.current.start(250); // 250ms 간격 전송
  };

  const stopListening = () => {
    setIsListening(false);
    mediaRecorderRef.current?.stop();
    wsRef.current?.close(); // 녹음 중지 시 웹소켓 종료
  };

  return (
    <div className="p-6 space-y-4">
      <h1 className="text-xl font-bold">🎤 WebRTC+STT 실시간 Demo</h1>
      <button onClick={startListening} disabled={isListening}>
        🎤 인식 시작
      </button>
      <button onClick={stopListening} disabled={!isListening}>
        ⏹️ 인식 중지
      </button>
   
    </div>
  );
}


