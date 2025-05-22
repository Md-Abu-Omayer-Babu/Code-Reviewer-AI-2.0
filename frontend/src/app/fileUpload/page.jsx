"use client";

import { useRouter } from "next/navigation";
import React, { use, useEffect, useState } from "react";
import Navbar from "../../../components/Navbar";

function fileUpload() {
  const router = useRouter();
  // const [file, setFile] = useState(null);
  const [files, setFiles] = useState([]);

  const [status, setStatus] = useState("");
  const [loading, setLoading] = useState(false);

  useEffect(() => {
    const token = localStorage.getItem("token");
    if (!token) {
      router.push("/unauthorized");
    }
  }, [router]);

  // upload multiple files
  const handleUpload = async (e) => {
    e.preventDefault();

    if (!files || files.length === 0) {
      setStatus("Please select at least one file");
      return;
    }

    const formData = new FormData();

    files.forEach((file) => {
      formData.append("files", file);
    });

    try {
      const response = await fetch("http://localhost:8000/files/upload", {
        method: "POST",
        body: formData,
        headers: {
          Authorization: `Bearer ${localStorage.getItem("token")}`,
        },
      });

      const data = await response.json();
      console.log(data);

      if (data.message) {
        setStatus(data.message);
      } else {
        setStatus("Unexpected server response");
      }
    } catch (error) {
      console.error(error);
      setStatus("Failed to upload files");
    }
  };

  useEffect(() => {
    if (status === "File uploaded successfully!") {
      setTimeout(() => {
        setStatus("");
      }, 3000);
    }
  }, [status]);

  return (
    <div>
      <Navbar />

      <div className="flex bg-gray- flex-col gap-4 items-center justify-center min-h-screen py-8 px-4 sm:px-6 lg:px-8">
        <form className="flex flex-col items-center gap-4">
          <input
            type="file"
            multiple
            className="bg-blue-600 text-white px-6 py-2 rounded-md cursor-pointer"
            onChange={(e) => setFiles(Array.from(e.target.files))}
          />
          <button
            type="submit"
            className="bg-blue-600 hover:text-black hover:bg-blue-500 text-white px-6 py-2 rounded-md cursor-pointer"
            onClick={handleUpload}
          >
            Upload
          </button>
        </form>
        <p>{status}</p>

        <div>
          <button
            className="bg-green-600 text-white px-6 py-2 rounded-md cursor-pointer hover:bg-green-400 hover:text-black"
            onClick={() => {
              router.push("/review_code");
              setLoading(true);
            }}
          >
            Review Your Code
          </button>
        </div>

        {loading && (
          <div className="mt-8 bg-black text-white">
            <p>Loading...</p>
          </div>
        )}
      </div>
    </div>
  );
}

export default fileUpload;
