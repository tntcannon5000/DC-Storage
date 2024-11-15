import React from 'react';
import FileDisplay from './FileDisplay';

const FileDisplayArea = ({ files }) => {
    const handleDownload = (id) => {
        const downloadUrl = `http://localhost:8000/download/${id}`;
        // Create a hidden link element and click it to start the download
        const link = document.createElement('a');
        link.href = downloadUrl;
        link.setAttribute('download', ''); // Ensures the browser triggers a download
        document.body.appendChild(link);
        link.click();
        document.body.removeChild(link); // Cleanup the element after click
    };

    return (
        <div className="grid gap-4 p-4 place-items-center
  grid-cols-2          // Mobile: 1 column
  sm:grid-cols-2       // Small screens (640px+): 2 columns
  md:grid-cols-3       // Medium screens (768px+): 3 columns
  lg:grid-cols-4       // Large screens (1024px+): 4 columns
  xl:grid-cols-5       // Extra large screens (1280px+): 5 columns
  2xl:grid-cols-6       // Extra large screens (1280px+): 5 columns
  3xl:grid-cols-7
  
">
            {Array.isArray(files) && files.length > 0 ? (
                files.map((file) => (
                    <FileDisplay
                        key={file.uuid} // Use UUID as the key
                        fileName={file.name}
                        fileExt={file.ext}
                        fileSize={file.size}
                        fileUUID={file.uuid}
                        onDownload={handleDownload}
                    />
                ))
            ) : (
                <p></p>
            )}
        </div>
    );
};

export default FileDisplayArea;