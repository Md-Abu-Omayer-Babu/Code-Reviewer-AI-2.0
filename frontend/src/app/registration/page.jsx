"use client"

import React from 'react'
import Navbar from '../../../components/Navbar'
import RegistrationForm from '../../../components/RegistrationForm'

function Register() {
  return (
    <div>
      <Navbar/>
      <div className='bg-black w-full h-screen py-8 text-white'>
        <RegistrationForm/>
      </div>
    </div>
  )
}

export default Register
