import React, { useState } from 'react';

const Popup = ({ onClose }) => {
    const [folderName, setFolderName] = useState('');

    const handleInputChange = (e) => {
        setFolderName(e.target.value);
    };

    const handleButtonClick = () => {
        onClose(folderName);
    };

    return (
        <div className="fixed inset-0 bg-black bg-opacity-50 flex justify-center items-center">
            <div className="bg-white p-4 rounded-lg shadow-lg relative">
                <button 
                    className="absolute top-2 right-2 text-gray-500 hover:text-gray-700"
                    onClick={() => onClose('')}
                >
                    &times;
                </button>
                <h2 className="text-xl mb-4">Enter Folder Name</h2>
                <input 
                    type="text" 
                    className="border p-2 mb-4 w-full" 
                    placeholder="Folder Name" 
                    value={folderName} 
                    onChange={handleInputChange} 
                />
                <button 
                    className="bg-blue-500 text-white px-4 py-2 rounded" 
                    onClick={handleButtonClick}
                >
                    Enter
                </button>
            </div>
        </div>
    );
};

export default Popup;