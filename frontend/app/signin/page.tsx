'use client';

import React, { useState } from 'react';

export default function SignInPage() {
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = (e: React.FormEvent) => {
    e.preventDefault();
    console.log('Email:', email, 'Password:', password);
  };

  return (
    <div className="flex flex-col items-center justify-center h-screen bg-[#313131] text-white">
      <div className="bg-[#414141] p-6 rounded-lg shadow-md w-96">
        <h1 className="text-2xl font-bold mb-4 text-center">Sign In</h1>
        <form onSubmit={handleSubmit} className="flex flex-col">
          <label className="mb-2 font-medium text-gray-300">Email</label>
          <input
            type="email"
            value={email}
            onChange={(e) => setEmail(e.target.value)}
            className="border border-gray-600 rounded-lg px-4 py-2 mb-4 bg-[#313131] text-white"
            required
          />
          <label className="mb-2 font-medium text-gray-300">Password</label>
          <input
            type="password"
            value={password}
            onChange={(e) => setPassword(e.target.value)}
            className="border border-gray-600 rounded-lg px-4 py-2 mb-6 bg-[#313131] text-white"
            required
          />
          <button className="bg-[#2cd3a7] text-white px-6 py-2 rounded-lg hover:bg-[#55f86b]">
            Sign In
          </button>
        </form>
      </div>
    </div>
  );
}
