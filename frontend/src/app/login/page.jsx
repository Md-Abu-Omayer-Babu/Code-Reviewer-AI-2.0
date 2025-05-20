"use client"

import React from 'react'
import Navbar from '../../../components/Navbar'
import LoginForm from '../../../components/LoginForm'

function Login() {
  return (
    <div>
      <Navbar/>
      <div>
        <LoginForm/>
      </div>
    </div>
  )
}

export default Login