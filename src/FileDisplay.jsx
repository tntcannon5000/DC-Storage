import { useState } from 'react';

export default function FileDisplay({ fileName, fileExt, fileSize, fileUUID, onDownload }) {

  return (
    <div className="bg-[#1A0B2E] bg-opacity-45 text-white p-4 rounded-xl border border-[#B23AFC] border-x-2 border-y-2 w-40 h-40 my-1 flex flex-col justify-center items-center">
      <p className="text-xl font-semibold text-gray-100 text-center">{fileName+"."+fileExt}</p>
      <p className="text-base text-gray-400 text-center">{fileSize}</p>
      <button
        className="mt-2 bg-fuchsia-700 hover:bg-slate-800 transition-colors duration-300 text-white py-1 px-1 rounded flex items-center"
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
