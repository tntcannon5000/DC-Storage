import { useState } from 'react'
import UploadArea from './UploadArea'
import FileDisplayArea from './FileDisplayArea'

export default function App() {
  return (
    <main className="flex items-center justify-center min-h-screen bg-black ">
      <div className="space-y-8">
        <h1 className="text-6xl text-center text-stone-400">Discord Data Storage!</h1>
        <FileDisplayArea />
        <div className="mx-[4vw]">
          <UploadArea />
        </div>
      </div>
    </main>
  )
}