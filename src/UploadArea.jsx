import { useState } from 'react';

export default function UploadArea() {
  const [selectedFile, setSelectedFile] = useState(null);

  const handleFileChange = (event) => {
    setSelectedFile(event.target.files[0]);
  };

  return (
    <div className="flex flex-col items-center justify-center w-full h-64 border-2 border-dashed border-gray-300 bg-stone-900 rounded-lg w-64">
      {selectedFile ? (
        <div>
          <p className="mb-2 text-gray-600">Selected file: {selectedFile.name}</p>
          {/* You can add more information about the selected file here (e.g., size, type) */}
          {/* You can also add a preview of the file if it's an image */}
        </div>
      ) : (
        <div className="text-center">
          <svg
            className="mx-auto h-12 w-12 text-gray-400" stroke="currentColor" fill="none" viewBox="0 0 48 48" aria-hidden="true">
            <path
              d="M28 8H12a4 4 0 00-4 4v20m32-12v8m0 0v8a4 4 0 01-4 4H12a4 4 0 01-4-4v-4m32-4l-3.172-3.172a4 4 0 00-5.656 0L28 28M8 32l9.172-9.172a4 4 0 015.656 0L28 28m0 0l4 4m4-24h8m-4-4v8m-12 4h.02"
              strokeWidth={2}
              strokeLinecap="round"
              strokeLinejoin="round"
            />
          </svg>
          <p className="mt-2 pb-4 text-sm text-gray-300">Drag and drop files here or click to upload</p>
            <input id="file-upload" type="file" className="hidden mb-16" onChange={handleFileChange}/>
          <label htmlFor="file-upload" className="px-4 py-2 text-sm font-medium text-white bg-blue-500 rounded-md cursor-pointer hover:bg-blue-600">Select Files
          </label>
        </div>
      )}
    </div>
  );
}