"use client";

import React, { useState } from "react";

function Draggrable() {
  const [isDragging, setIsDragging] = useState(false);
  const [position, setPosition] = useState({ x: 350, y: 350 });

  const handleDragging = (e) => {
    if (!isDragging) {
      return;
    }

    setPosition({
      x: e.clientX,
      y: e.clientY,
    });
  };

  return (
    <div className="flex h-screen w-screen"
    onMouseDown={() => {
      setIsDragging(true);
    }}
    onMouseUp={() => {
      setIsDragging(false);
    }}
    
    onMouseMove={(e) => {
      handleDragging(e);
    }}
    
    >
      <div
        style={{
            position:'absolute', 
            left: position.x - 64,
            top: position.y - 64,
        }}
        className="bg-blue-500 h-32 w-32 items-center justify-center text-center text-white flex rounded-md"
      >
        Box
      </div>
    </div>
  );
}

export default Draggrable;
