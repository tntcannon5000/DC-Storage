import { useState } from 'react';

export default function FolderDisplay({ folderName, folderUUID, onDownload }) {

  return (
    <div className="bg-[#1A0B2E] bg-opacity-45 text-white p-4 rounded-xl border border-[#B23AFC] border-x-2 border-y-2 w-full h-16 my-1 flex flex-col justify-center items-center">
      <h1>{folderName}</h1>
    </div>
  );
}
