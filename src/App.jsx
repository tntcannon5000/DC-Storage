import { useState } from 'react'
import UploadArea from './UploadArea'
import FileDisplay from './FileDisplay'

export default function App() {
  return (
    <main className="flex items-center justify-center min-h-screen bg-black ">
      <div className="space-y-8">
        <h1 className="text-6xl text-center text-stone-400">Discord Data Storage!</h1>
        <FileDisplay string1="File Name" string2="File Size" />
        <div className="mx-[4vw]">
          <UploadArea />
        </div>
      </div>
    </main>
  )
}