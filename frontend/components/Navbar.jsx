"use client";

import { useRouter } from "next/navigation";
import React, { useEffect, useState } from "react";

function Navbar() {
  const router = useRouter();
  const [isLoggedIn, setIsLoggedIn] = useState(false);
  const [isValidToken, setIsValidToken] = useState(false);

  useEffect(() => {
    const token = localStorage.getItem("token");
    setIsLoggedIn(!!token);
  }, []);

  useEffect(() => {
    const token = localStorage.getItem("token");
    if (token) {
      fetch("http://localhost:8000/token/verify_token", {
        method: "GET",
        headers: {
          "Content-Type": "application/json",
          Authorization: `Bearer ${token}`,
        },
      })
        .then((response) => response.json())
        .then((data) => {
          setIsValidToken(data.is_valid);
          if (!data.is_valid) {
            localStorage.removeItem("token");
            setIsLoggedIn(false);
            router.push("/login");
          }
        })
        .catch((error) => {
          console.error("Error verifying token:", error);
        });
    }
  }
  , [router]);

  const handleLogout = () => {
    localStorage.removeItem("token");
    setIsLoggedIn(false);
    router.push("/");
  };

  const handleLogin = () => {
    router.push("/login"); 
  };

  return (
    <div className="flex flex-row items-center bg-gray-300 p-2">
      <h1
        className="p-2 w-full text-2xl cursor-pointer bg-gray-300 text-black font-bold text-center"
        onClick={() => router.push("/")}
      >
        Code Reviewer AI
      </h1>

      {isLoggedIn && isValidToken ? (
        <button
          onClick={handleLogout}
          className="bg-red-500 cursor-pointer hover:bg-red-600 text-white font-semibold px-4 py-2 rounded"
        >
          Logout
        </button>
      ) : (
        <button
          onClick={handleLogin}
          className="bg-blue-500 cursor-pointer hover:bg-blue-600 text-white font-semibold px-4 py-2 rounded"
        >
          Login
        </button>
      )}
    </div>
  );
}

export default Navbar;
