import { useState } from 'react'
import FileDisplayArea from './FileDisplayArea'
import GlobalFileDropzone from './GlobalFileDropzone'
import bgVideo from './assets/bg.mp4'
import FoldersArea from './FoldersArea'

export default function App() {
  const [fileInfo, setFileInfo] = useState(null)

  const handleFilesDrop = (files) => {
    const file = files[0];
    const fileInfo = {
      name: file.name,
      size: file.size,
      type: file.type
    };
    setFileInfo(fileInfo);
    console.log("Dropped files:", fileInfo)
  };

  return (
    <GlobalFileDropzone onFilesDrop={handleFilesDrop}>
      <video autoPlay loop muted playsInline className="fixed top-0 left-0 min-w-full min-h-screen w-auto h-auto object-cover -z-10">
        <source src={bgVideo} type="video/mp4" />
        Your browser does not support the video tag.
      </video>
      <main className="flex pt-20 justify-center min-h-screen">
          <div className="space-y-8 w-[80%]">
            <h1 className="text-6xl text-center text-[#E5B8F4] pb-12">Discord Data Storage!</h1>
            <div class="flex">
              <div class="w-2/12">
                <FoldersArea />
              </div>
              <div class="w-10/12">
                <FileDisplayArea />
              </div>
          </div>

          </div>
      </main>
    </GlobalFileDropzone>
  )
}