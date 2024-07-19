# Hospitality Digitalization

A web application to facilitate digitalizing the hospitality process for group accommodation. The application allows users to upload two CSV files to efficiently allocate rooms in hostels while ensuring group members with the same ID stay together and adhere to hostel capacities and gender-specific accommodations.

## Features

- Upload CSV files for group and hostel information
- Allocate rooms based on group size, gender, and hostel capacity
- Display allocated rooms
- Download allocation details as a CSV file

## Technologies Used

- **Backend**: Flask, Pandas
- **Frontend**: React, Axios
- **Styling**: CSS

## Project Structure

hospitality-digitalization/
├── backend/
│ ├── app.py
│ ├── allocate.py
│ ├── templates/
│ │ └── index.html
│ ├── static/
│ │ ├── css/
│ │ │ └── main.css
│ │ ├── js/
│ │ │ └── bundle.js
│ └── ...
├── frontend/
│ ├── public/
│ │ └── index.html
│ ├── src/
│ │ ├── components/
│ │ │ ├── FileUpload.js
│ │ │ └── ResultsTable.js
│ │ ├── App.js
│ │ ├── App.css
│ │ ├── index.js
│ │ ├── index.css
│ └── ...
├── venv/
├── README.md
└── ...