import React from 'react';

const ResultsTable = ({ allocation }) => {
  if (!allocation) return null;

  return (
    <table>
      <thead>
        <tr>
          <th>Group ID</th>
          <th>Hostel Name</th>
          <th>Room Number</th>
          <th>Members Allocated</th>
        </tr>
      </thead>
      <tbody>
        {allocation.map((row, index) => (
          <tr key={index}>
            <td>{row['Group ID']}</td>
            <td>{row['Hostel Name']}</td>
            <td>{row['Room Number']}</td>
            <td>{row['Members Allocated']}</td>
          </tr>
        ))}
      </tbody>
    </table>
  );
};

export default ResultsTable;
