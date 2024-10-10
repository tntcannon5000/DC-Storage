import { useState, useEffect } from 'react';
import FileDisplay from './FileDisplay';

export default function FileList() {
  const [files, setFiles] = useState([]);

  useEffect(() => {
    const fetchFiles = async () => {
      try {
        const response = await fetch('/api/files'); // Replace with your backend endpoint
        if (!response.ok) {
          throw new Error(`HTTP error! status: ${response.status}`);
        }
        const data = await response.json();
        setFiles(data);
      } catch (error) {
        console.error('Error fetching files:', error);
        // Handle error, e.g., display an error message
        setFiles([]); // Or set to an error state
      }
    };

    fetchFiles();
  }, []); // Empty dependency array ensures this runs only once on mount

  return (
    <div>
      {files.map(file => (
        <FileDisplay key={file.id || file.name} string1={file.name} string2={file.size} />
      ))}
      {files.length === 0 && <p>No files found.</p>} {/* Optional: Display message if no files */}
    </div>
  );
}