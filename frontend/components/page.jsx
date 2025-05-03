"use client";

import { useSearchParams } from "next/navigation";
import React, { useState } from "react";
import Navbar from "../../../components/Navbar";

function ExploreClasses() {
  // const [classes, setClasses] = useState(["Box 1", "Box 2"]);
  const [classes, setClasses] = useState([
    { name: "Box 1", x: 100, y: 100 },
    { name: "Box 2", x: 300, y: 200 },
  ]);

  const searchParams = useSearchParams();
  const handleDrag = (index, e) => {
    const updated = [...classes];
    updated[index].x = e.clientX - 64; // half of width
    updated[index].y = e.clientY - 64;
    setClasses(updated);
  };

  const handleMouseDown = (index) => {
    const onMouseMove = (e) => handleDrag(index, e);
    const onMouseUp = () => {
      window.removeEventListener("mousemove", onMouseMove);
      window.removeEventListener("mouseup", onMouseUp);
    };
    window.addEventListener("mousemove", onMouseMove);
    window.addEventListener("mouseup", onMouseUp);
  };


  // making draggable
  const makeDraggable = (e) => {
    let isDragging = false;
    let X, Y;

    const element = e.target;

    // Start dragging on mousedown
    element.addEventListener("mousedown", (e) => {
      isDragging = true;
      X = e.clientX - element.getBoundingClientRect().left;
      Y = e.clientY - element.getBoundingClientRect().top;
      element.style.position = "absolute";
    });

    // Move the box on mousemove
    document.addEventListener("mousemove", (e) => {
      if (!isDragging) return;
      element.style.left = `${e.clientX - X}px`;
      element.style.top = `${e.clientY - Y}px`;
    });

    // Stop dragging on mouseup
    document.addEventListener("mouseup", () => {
      isDragging = false;
    });
  };

  return (
    <div>
      <Navbar />

      <div className="flex flex-wrap gap-4 items-center justify-center min-h-screen py-8 px-4 sm:px-6 lg:px-8 bg-amber-200">
        <div className="flex flex-col gap-10 justify-center items-center text-center">
          <div className="text-center font-semibold max-w-xl">
            <div className="flex flex-row gap-5">
              {/* {classes.map((cls, index) => (
                <div>
                  <div
                  key={index}
                  className="relative bg-blue-400 cursor-pointer rounded-xl font-bold text-white h-32 w-32 text-center justify-center items-center flex"
                  onMouseOver={(e) => makeDraggable(e)}
                >
                  {cls}
                </div>
                  <hr className="w-12"/>
                </div>
              ))} */}
              {classes.map((cls, index) => (
                <div
                  key={index}
                  onMouseDown={() => handleMouseDown(index)}
                  style={{
                    position: "absolute",
                    top: cls.y,
                    left: cls.x,
                    width: 128,
                    height: 128,
                    backgroundColor: "skyblue",
                    borderRadius: 16,
                    color: "white",
                    fontWeight: "bold",
                    textAlign: "center",
                    lineHeight: "128px",
                    cursor: "grab",
                  }}
                >
                  {cls.name}
                </div>
              ))}
              <svg className="absolute top-0 left-0 w-full h-full pointer-events-none">
                {classes.length > 1 &&
                  classes.slice(1).map((box, i) => {
                    const prev = classes[i];
                    return (
                      <line
                        key={i}
                        x1={prev.x + 64}
                        y1={prev.y + 64}
                        x2={box.x + 64}
                        y2={box.y + 64}
                        stroke="black"
                        strokeWidth="2"
                      />
                    );
                  })}
              </svg>

            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

export default ExploreClasses;
