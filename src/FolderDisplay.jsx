import React from 'react';

export default function FolderDisplay({ folderName, folderUUID, onDownload, className }) {
    return (
        <div
            className={`${className} bg-opacity-20 select-none text-white text-lg p-4 rounded-xl border border-[#B23AFC] border-opacity-80 border-x-2 border-y-2 w-full h-16 my-1 flex flex-col justify-center items-center cursor-pointer`}
            onClick={() => onDownload(folderUUID)}
        >
            <h1>{folderName}</h1>
        </div>
    );
}