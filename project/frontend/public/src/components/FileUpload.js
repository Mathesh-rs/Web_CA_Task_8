import React, { useState } from 'react';
import axios from 'axios';

const FileUpload = () => {
  const [groupFile, setGroupFile] = useState(null);
  const [hostelFile, setHostelFile] = useState(null);
  const [allocation, setAllocation] = useState(null);

  const handleGroupFileChange = (e) => {
    setGroupFile(e.target.files[0]);
  };

  const handleHostelFileChange = (e) => {
    setHostelFile(e.target.files[0]);
  };

  const handleUpload = () => {
    const formData = new FormData();
    formData.append('group_file', groupFile);
    formData.append('hostel_file', hostelFile);

    axios.post('http://127.0.0.1:5000/upload', formData, {
      responseType: 'blob',
    })
    .then(response => {
      const url = window.URL.createObjectURL(new Blob([response.data]));
      const link = document.createElement('a');
      link.href = url;
      link.setAttribute('download', 'allocation.csv');
      document.body.appendChild(link);
      link.click();
    })
    .catch(error => {
      console.error('There was an error uploading the files!', error);
    });
  };

  return (
    <div>
      <input type="file" onChange={handleGroupFileChange} />
      <input type="file" onChange={handleHostelFileChange} />
      <button onClick={handleUpload}>Upload and Allocate</button>
    </div>
  );
};

export default FileUpload;
