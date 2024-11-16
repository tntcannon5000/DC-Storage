import { useCallback } from 'react';
import { useDropzone } from 'react-dropzone';

const FileDropzone = ({ onFilesDrop }) => {
  const onDrop = useCallback((acceptedFiles) => {
    onFilesDrop(acceptedFiles);
  }, [onFilesDrop]);

  const { getRootProps, getInputProps, isDragActive } = useDropzone({ onDrop });

  return (
    <div 
      {...getRootProps()} 
      className={`w-full p-8 border-2 border-dashed rounded-lg text-center cursor-pointer transition-colors
        ${isDragActive 
          ? 'border-blue-500 bg-blue-50' 
          : 'border-gray-300 hover:border-gray-400'
        }`}
    >
      <input {...getInputProps()} />
      {isDragActive ? (
        <p className="text-blue-500">Drop the files here...</p>
      ) : (
        <div>
          <p className="text-gray-600">Drag and drop files here, or click to select files</p>
          <p className="text-sm text-gray-400 mt-2">Supported files: Any</p>
        </div>
      )}
    </div>
  );
};

export default FileDropzone;