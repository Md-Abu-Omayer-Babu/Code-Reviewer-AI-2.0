"use client"

import React from 'react'
import Navbar from '../../../components/Navbar'
import LoginForm from '../../../components/LoginForm'

function Login() {
  return (
    <div>
      <Navbar/>
      <div className='bg-black w-full h-screen py-8 text-white'>
        <LoginForm/>
      </div>
    </div>
  )
}

export default Login