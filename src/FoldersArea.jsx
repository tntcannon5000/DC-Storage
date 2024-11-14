import React, { useState, useEffect } from 'react';
import FolderDisplay from './FolderDisplay';

const FoldersArea = () => {
    const [folders, setFolders] = useState([]);
  
    useEffect(() => {
      // Fetching files from the backend
      fetch('http://localhost:8000/folders')
        .then((response) => response.json())
        .then((data) => setFolders(data))
        .catch((error) => console.error('Error fetching folders:', error));
    }, []);

    const handleDownload = (folderId) => {
        fetch(`http://localhost:8000/folders/${folderId}`)
            .then((response) => response.json())
            .then((data) => {
                // Handle the list of file names here
                console.log('Files in folder:', data);
            })
            .catch((error) => console.error('Error fetching files:', error));
    };

    return (
        <div>
            <div className='grid grid-cols-1 p-4'>
                <div className="bg-[#1A0B2E] bg-opacity-45 text-white p-4 rounded-xl border border-[#B23AFC] border-x-2 border-y-2 w-full h-16 my-1 flex flex-col justify-center items-center">
                    {/* Stuff to be put here for later to have the Plus icon*/}
                </div>
                {folders.map((file) => (
            <FolderDisplay
              key={file.uuid} // Use UUID as the key
              folderName={file.name}
              foldeUUID={file.uuid}
              onDownload={handleDownload}
            />
          ))}
            </div>

        </div>
    );
};

export default FoldersArea;