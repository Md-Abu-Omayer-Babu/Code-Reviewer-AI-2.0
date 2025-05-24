"use client";

import { useEffect } from "react";
import { useRouter } from "next/navigation";
import Navbar from "./Navbar";

const UnauthorizedPage = () => {
  const router = useRouter();

  return (
    <div>
      <Navbar />
      <div className="min-h-screen flex items-center justify-center bg-red-50">
        <div className="bg-white p-8 rounded-2xl shadow-lg text-center max-w-md w-full">
          <h1 className="text-4xl font-extrabold text-red-600 mb-4">401</h1>
          <h2 className="text-xl font-semibold text-gray-800 mb-2">
            Unauthorized Access
          </h2>
          <p className="text-gray-600 mb-6">
            You are not authorized to view this page.
          </p>
          <button
            onClick={() => router.push("/")}
            className="px-6 py-2 cursor-pointer bg-red-600 text-white rounded-md hover:bg-red-700 transition"
          >
            Go to Home
          </button>
        </div>
      </div>
    </div>
  );
};

export default UnauthorizedPage;
