"use client";

import Link from "next/link";
import { useState } from "react";

function LoginForm() {
  const [email, setEmail] = useState("");
  const [password, setPassword] = useState("");
  const [message, setMessage] = useState("");

  const handleLogin = async (e) => {
    e.preventDefault();

    const formData = new FormData();
    formData.append("email", email);
    formData.append("password", password);

    try {
      const response = await fetch(`http://localhost:8000/login/login_api`, {
        method: "POST",
        body: formData,
      });

      const data = await response.json();

      if (data.message === "Invalid email") {
        setMessage(data.message);
      } else if (data.email && data.password) {
        setMessage(`Logged in as ${data.email}`);
      } else {
        setMessage("Unexpected server response");
      }
      console.log(data);
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <form
      onSubmit={handleLogin}
      className="flex flex-col gap-4 max-w-md mx-auto mt-10"
    >
      <h2 className="text-3xl font-bold text-center">Welcom Back</h2>
      <p className="text-center text-gray-500">Login to your account</p>
      <input
        type="email"
        placeholder="Email"
        className="p-2 border rounded"
        value={email}
        onChange={(e) => setEmail(e.target.value)}
        required
      />

      <input
        type="password"
        placeholder="Password"
        className="p-2 border rounded"
        value={password}
        onChange={(e) => setPassword(e.target.value)}
        required
      />

      <button type="submit" className="bg-blue-600 text-white py-2 rounded">
        Login
      </button>

      <div className="text-sm text-center mt-2">
        <p>
          Don&apos;t have an account?{" "}
          <Link href="/registration" className="text-blue-500 underline">
            Register
          </Link>
        </p>
        <p>
          <Link href="/forgot-password" className="text-blue-500 underline">
            Forgot Password?
          </Link>
        </p>
      </div>

      {message && <p className="text-center">{message}</p>}
    </form>
  );
}

export default LoginForm;
