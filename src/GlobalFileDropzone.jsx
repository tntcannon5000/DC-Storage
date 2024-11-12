import { useCallback, useEffect } from 'react';
import { useDropzone } from 'react-dropzone';

const GlobalFileDropzone = ({ onFilesDrop, children }) => {
  const onDrop = useCallback((acceptedFiles) => {
    onFilesDrop(acceptedFiles);
  }, [onFilesDrop]);

  const { getRootProps, getInputProps, isDragActive, open } = useDropzone({
    onDrop,
    noClick: true, // Prevents clicking on the entire page to open file dialog
    noKeyboard: true // Disables keyboard interaction
  });

  useEffect(() => {
    const preventDefault = (e) => e.preventDefault();
    window.addEventListener('dragover', preventDefault);
    window.addEventListener('drop', preventDefault);

    return () => {
      window.removeEventListener('dragover', preventDefault);
      window.removeEventListener('drop', preventDefault);
    };
  }, []);

  return (
    <div {...getRootProps()} style={{ minHeight: '100vh' }}>
      <input {...getInputProps()} />
      
      {/* Drag overlay*/}
      {isDragActive && (
        <div className="fixed inset-0 backdrop-blur-sm bg-black bg-opacity-15 z-50 pointer-events-none">
          <div className="absolute top-1/2 left-1/2 transform -translate-x-1/2 -translate-y-1/2">
            <div className="bg-[#2a0b4284] backdrop-blur-md border border-x-2 border-y-2 border-[#46166b] pt-5 pb-7 px-8 rounded-lg shadow-lg">
              <p className="text-3xl text-stone-200 font-semibold">
                Drop anywhere to upload!
              </p>
            </div>
          </div>
        </div>
      )}

      {children}
    </div>
  );
};

export default GlobalFileDropzone;