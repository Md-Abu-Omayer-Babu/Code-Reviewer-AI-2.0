"use client";

import React, { useEffect, useState } from "react";

function Draggable() {
  const [draggingBox, setDraggingBox] = useState(null); // 'blue' or 'green' or null
  const [bluePosition, setBluePosition] = useState({ x: 0, y: 0 });
  const [greenPosition, setGreenPosition] = useState({ x: 0, y: 0 });

  useEffect(() => {
    const token = localStorage.getItem("token");
    if (!token) {
      router.push("/unauthorized");
    }
  }, [router]);

  useEffect(() => {
    const centerX = window.innerWidth / 2;
    const centerY = window.innerHeight / 2;

    setBluePosition({ x: centerX - 100, y: centerY });
    setGreenPosition({ x: centerX + 100, y: centerY });
  }, []);

  const handleMouseMove = (e) => {
    if (!draggingBox) return;

    if (draggingBox === "blue") {
      setBluePosition({ x: e.clientX, y: e.clientY });
    } else if (draggingBox === "green") {
      setGreenPosition({ x: e.clientX, y: e.clientY });
    }
  };

  return (
    <div
      className="relative flex h-screen w-screen items-center justify-center"
      onMouseMove={handleMouseMove}
      onMouseUp={() => setDraggingBox(null)}
    >
      <div
        className="absolute bg-blue-500 h-32 w-32 flex items-center justify-center text-white rounded-md"
        onMouseDown={() => setDraggingBox("blue")}
        style={{
          left: bluePosition.x - 64,
          top: bluePosition.y - 64,
        }}
      >
        Blue Box
      </div>

      <div
        className="absolute bg-green-500 h-32 w-32 flex items-center justify-center text-white rounded-md"
        onMouseDown={() => setDraggingBox("green")}
        style={{
          left: greenPosition.x - 64,
          top: greenPosition.y - 64,
        }}
      >
        Green Box
      </div>
    </div>
  );
}

export default Draggable;
