import React, { useState, useEffect } from 'react';
import FileDisplay from './FileDisplay';

const FileDisplayArea = () => {
    const [files, setFiles] = useState([]);
  
    useEffect(() => {
      // Fetching files from the backend
      fetch('http://localhost:8000/files')
        .then((response) => response.json())
        .then((data) => setFiles(data))
        .catch((error) => console.error('Error fetching files:', error));
    }, []);
    
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
        <div className="grid gap-4 p-4 place-items-center grid-cols-[repeat(auto-fit,minmax(10rem,1fr))] ">
          {files.map((file) => (
            <FileDisplay
              key={file.uuid} // Use UUID as the key
              fileName={file.name}
              fileExt={file.ext}
              fileSize={file.size}
              fileUUID={file.uuid}
              onDownload={handleDownload}
            />
          ))}
          </div>
      );
    };

  export default FileDisplayArea;