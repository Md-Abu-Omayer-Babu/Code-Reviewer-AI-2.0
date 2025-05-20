'use client'

import { useRouter } from "next/navigation";
import { useState } from "react";

function Home() {
  const router = useRouter()
  const [loading, setLoading] = useState(false)

  return (
    <div className="flex bg-black flex-col items-center justify-center min-h-screen py-8 px-4 sm:px-6 lg:px-8">
      <h1 className="text-4xl font-bold text-white">Code Reviewer AI</h1>
      <p className="text-lg text-gray-300 mt-4">
        A tool to help you write better code.
      </p>
      <div className="mt-8">
        <button className="bg-blue-500 cursor-pointer text-white px-6 py-2 rounded-md"
          onClick={() => {
            router.push('/login')
            setLoading(true)
          }}
        >
          Get Started
        </button>
      </div>
      {loading && (
        <div className="mt-8 bg-amber-50 text-shadow-white">
          <p>Loading...</p>
        </div>
      )}
    </div>
  );
}

export default Home