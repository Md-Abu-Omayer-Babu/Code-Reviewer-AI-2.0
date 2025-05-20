"use client";

import { useEffect } from "react";
import { useRouter } from "next/navigation";

const UnauthorizedPage = () => {
  const router = useRouter();

  useEffect(() => {
    let count = 5;
    const interval = setInterval(() => {
      count--;
      document.getElementById("countdown").textContent = count;
      if (count === 0) {
        clearInterval(interval);
        router.push("/");
      }
    }, 1000);
    return () => clearInterval(interval);
  }, []);

  return (
    <div className="min-h-screen flex items-center justify-center bg-red-50">
      <div className="bg-white p-8 rounded-2xl shadow-lg text-center max-w-md w-full">
        <h1 className="text-4xl font-extrabold text-red-600 mb-4">401</h1>
        <h2 className="text-xl font-semibold text-gray-800 mb-2">Unauthorized Access</h2>
        <p className="text-gray-600 mb-6">
          You are not authorized to view this page.
        </p>
        <button
          onClick={() => router.push("/")}
          className="px-6 py-2 bg-red-600 text-white rounded-md hover:bg-red-700 transition"
        >
          Go to Home
        </button>
        <p className="text-sm text-gray-400 mt-4">Redirecting in <span id="countdown">5</span> seconds...</p>
      </div>
    </div>
  );
};

export default UnauthorizedPage;
