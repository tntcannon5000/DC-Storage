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
            <div className="bg-[#1A0B2E] bg-opacity-90 text-white p-6 rounded-xl shadow-lg relative border border-[#B23AFC] border-opacity-80 border-x-2 border-y-2">
                <button 
                    className="absolute top-2 right-2 text-gray-500 hover:text-gray-300"
                    onClick={() => onClose('')}
                >
                    &times;
                </button>
                <h2 className="text-2xl mb-4 text-[#E5B8F4]">Enter Folder Name</h2>
                <input 
                    type="text" 
                    className="border border-[#B23AFC] bg-[#1A0B2E] text-white p-2 mb-4 w-full rounded"
                    placeholder="Folder Name" 
                    value={folderName} 
                    onChange={handleInputChange} 
                />
                <button 
                    className="bg-[#B23AFC] hover:bg-[#9C1BB0] transition-colors duration-300 text-white px-4 py-2 rounded"
                    onClick={handleButtonClick}
                >
                    Submit
                </button>
            </div>
        </div>
    );
};

export default Popup;