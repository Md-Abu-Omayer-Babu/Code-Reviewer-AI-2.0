"use client";

import { useSearchParams } from "next/navigation";
import React, { useEffect, useState } from "react";
import Navbar from "../../../components/Navbar";
import { useRouter } from "next/navigation";

function ExploreClasses() {
  const router = useRouter();
  const [classes, setClasses] = useState([]);
  const [isAllClassesClicked, setIsAllClassesClicked] = useState(false);

  const searchParams = useSearchParams();
  const selectedFile = searchParams.get("file");

  useEffect(() => {
    const token = localStorage.getItem("token");
    if (!token) {
      router.push("/unauthorized");
    }
  }, [router]);

  // show all classes
  const showAllClasses = async (fileName) => {
    try {
      const response = await fetch(
        `http://localhost:8000/class_finding/get_classes/${fileName}`,
        {
          method: "GET",
          headers: {
            "Content-Type": "application/json",
            Authorization: `Bearer ${localStorage.getItem("token")}`,
          },
        }
      );
      const data = await response.json();
      console.log(data);

      setClasses(data.classes);
    } catch (error) {
      console.log(error);
    }
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

  // make resizable

  // const makeResizable = (e, index) => {
  //   e.preventDefault();
  //   e.stopPropagation();
  // };

  return (
    <div>
      <Navbar />

      <div className="flex flex-wrap gap-4 items-center justify-center min-h-screen py-8 px-4 sm:px-6 lg:px-8 bg-amber-200">
        {/* hidden */}

        {showAllClasses && classes && (
          <div className="flex flex-col gap-10 justify-center items-center text-center">
            <div className="cursor-pointer">
              <button
                className={`bg-blue-500 ${
                  isAllClassesClicked ? "hidden" : ""
                } rounded-sm h-full w-40 cursor-pointer`}
                onClick={() => {
                  setIsAllClassesClicked(true);
                  showAllClasses(selectedFile);
                }}
              >
                Show All Classes
              </button>
            </div>

            <div className="text-center font-semibold max-w-xl">
              <div className="flex flex-row gap-5">
                {classes.map((cls, index) => (
                  <div
                    key={index}
                    className="relative bg-blue-400 cursor-pointer rounded-xl font-bold text-white h-32 w-32 text-center justify-center items-center flex"
                    onMouseOver={(e) => makeDraggable(e)}
                  >
                    {cls}
                  </div>
                ))}
              </div>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default ExploreClasses;
