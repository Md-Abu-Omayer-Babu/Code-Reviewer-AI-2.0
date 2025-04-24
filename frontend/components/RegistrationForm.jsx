"use client";

import Link from "next/link";
import { useState } from "react";

export default function RegistrationForm() {
  const [form, setForm] = useState({
    name: "",
    email: "",
    password: "",
  });

  const [message, setMessage] = useState("");

  const handleChange = (e) => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleRegister = async (e) => {
    e.preventDefault();
    
    const formData = new FormData();
    formData.append("name", form.name);
    formData.append("email", form.email);
    formData.append("password", form.password);

    try {
      const response = await fetch(`http://localhost:8000/register/register_api`,{
        method: "POST",
        body: formData
      });

      const data = await response.json();

      if(data.message){
        setMessage(data.message)
      }else{
        setMessage("Registration Successful!")
      }

      console.log(data);
    } catch (error) {
      console.log(error);
    }
  };

  return (
    <form
      onSubmit={handleRegister}
      className="flex flex-col gap-4 max-w-md mx-auto mt-10"
    >
      <h2 className="text-xl font-bold justify-center items-center text-center">
        Register
      </h2>
      <input
        name="name"
        type="text"
        placeholder="Name"
        className="p-2 border rounded"
        value={form.name}
        onChange={handleChange}
        required
      />
      <input
        name="email"
        type="email"
        placeholder="Email"
        className="p-2 border rounded"
        value={form.email}
        onChange={handleChange}
        required
      />
      <input
        name="password"
        type="password"
        placeholder="Password"
        className="p-2 border rounded"
        value={form.password}
        onChange={handleChange}
        required
      />
      <button type="submit" className="bg-green-600 text-white py-2 rounded">
        Register
      </button>

      <Link href="/login">
        Already have an account?{" "}
        <span className="text-blue-500 underline">Login</span>
      </Link>

      {message && <p className="text-center">{message}</p>}
    </form>
  );
}
