import { useState } from 'react';

export default function FileDisplay({ fileName, fileExt, fileSize, fileUUID, onDownload }) {

  return (
    <div className="relative bg-[#1A0B2E] bg-opacity-45 text-white select-none p-4 rounded-xl border border-[#B23AFC] border-x-2 border-y-2 w-40 h-40 my-1 flex flex-col justify-center items-center">
      <p className="absolute top-1 right-2 text-sm select-none text-gray-400">{fileExt}</p>
      <p className="text-xl font-semibold text-gray-100 select-none text-center">{fileName}</p>
      <p className="text-base text-gray-400 select-none text-center">{fileSize}</p>
      <button
        className="absolute bottom-1 right-1 bg-opacity-75 bg-fuchsia-500 hover:bg-fuchsia-700 transition-colors duration-300 text-white select-none py-1 px-1 rounded-lg flex items-center"
        onClick={() => [onDownload(fileUUID)]}
      >
        <svg
          xmlns="http://www.w3.org/2000/svg"
          className="h-7 w-7"
          viewBox="0 0 20 20"
          fill="currentColor"
        >
          <path
            fillRule="evenodd"
            d="M10 3a1 1 0 011 1v8.586l2.293-2.293a1 1 0 111.414 1.414l-4 4a1 1 0 01-1.414 0l-4-4a1 1 0 111.414-1.414L9 12.586V4a1 1 0 011-1z"
            clipRule="evenodd"
          />
        </svg>
      </button>
    </div>
  );
}