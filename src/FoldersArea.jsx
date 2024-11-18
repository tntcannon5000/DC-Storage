import React, { useState, useEffect } from 'react';
import FolderDisplay from './FolderDisplay';
import FileDisplayArea from './FileDisplayArea';
import Popup from './Popup';

const FoldersArea = () => {
    const [folders, setFolders] = useState([]);
    const [files, setFiles] = useState([]);
    const [isPopupVisible, setIsPopupVisible] = useState(false);
    const [currentFolder, setCurrentFolder] = useState(null);


    useEffect(() => {
        // Fetching folders from the backend
        fetch('http://localhost:8000/folders')
            .then((response) => response.json())
            .then((data) => setFolders(data))
            .catch((error) => console.error('Error fetching folders:', error));
    }, []);

    const handleFolderClick = (folderId) => {
        setCurrentFolder(folderId);
        fetch(`http://localhost:8000/folders/${folderId}/files`)
            .then((response) => response.json())
            .then((data) => setFiles(data))
            .catch((error) => console.error('Error fetching files:', error));
    };

    const showPopup = () => {
        setIsPopupVisible(true);
    };

    const submitPopup = () => {
        setIsPopupVisible(false);
    };

    
    return (
            <div class="flex">
                <div class="w-2/12">
                    <div className='grid grid-cols-1 p-4'>
                    <div className="bg-[#1A0B2E] bg-opacity-45 text-white text-center select-none text-md xl:text-lg p-4 rounded-xl border border-[#00FFE1] border-opacity-70 border-x-2 border-y-2 w-full h-12  my-1 flex flex-col justify-center items-center cursor-pointer"
                    onClick={showPopup}> New Folder
                    {/* Here, insert onclick functionality for a popup to appear, with a text box for a folder name, and an enter button which posts the foldername to the backend*/}
                    </div>
                        {folders.map((folder) => (
                            <FolderDisplay
                                key={folder.uuid} // Use UUID as the key
                                folderName={folder.name}
                                folderUUID={folder.uuid}
                                onDownload={handleFolderClick}
                                className={folder.uuid == currentFolder ? 'bg-purple-600 bg-opacity-25' : 'bg-[#1A0B2E]'}
                            />
                        ))}
                    </div>
                </div>
                <div class="w-10/12">
                    <FileDisplayArea files={files} />
                </div>
                {isPopupVisible && <Popup onClose={submitPopup} />}
            </div>
    );
};

export default FoldersArea;