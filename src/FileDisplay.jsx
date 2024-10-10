import { useState } from 'react';

export default function FileDisplay({ string1, string2 }) {
  return (
    <div className="flex rounded-lg bg-gray-100 p-4 shadow-sm">
      <div className="mr-4">
        {string1}
      </div>
      <div>
        {string2}
      </div>
    </div>
  );
}