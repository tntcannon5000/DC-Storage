import { useState } from 'react';

export default function FileDisplay({ fileName, fileSize }) {
  
  
  return (
    <div className="bg-black text-white p-4 rounded-xl border border-gray-700 w-40 h-40 flex flex-col justify-center items-center">
      <p className="text-base font-semibold text-gray-100 text-center">{fileName}</p>
      <p className="text-sm text-gray-400 text-center">{fileSize}</p>
    </div>
  );
}
