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
  
    return (
      <div className="grid grid-cols-3 gap-4 p-4">
        {files.map((file) => (
          <FileDisplay key={file.name || file.key} fileName={file.name} fileSize={file.size} />
        ))}
      </div>
    );
  };
  
  export default FileDisplayArea;