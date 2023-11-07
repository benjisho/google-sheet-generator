// frontend/src/App.js
import React, { useState } from 'react';
import axios from 'axios';
// import Button from './components/Button'; // We don't need this import anymore if we use a standard button

const App = () => {
    const [spreadsheetLink, setSpreadsheetLink] = useState(null);

    const handleButtonClick = async () => {
        try {
            const response = await axios.post('http://localhost:5000/generate-sheet');  // Update this line
            const spreadsheetId = response.data.spreadsheetId;
            const link = `https://docs.google.com/spreadsheets/d/${spreadsheetId}`;
            setSpreadsheetLink(link);
            console.log('Spreadsheet created:', link);
        } catch (error) {
            console.error('Error object:', error);
            alert('An error occurred while generating the sheet.');
        }
    };

    return (
        <div className="starter-template">
            {/* Replace Button component with a standard button element */}
            {spreadsheetLink && (
                <div>
                    <p>Spreadsheet created! <a href={spreadsheetLink} target="_blank" rel="noopener noreferrer">Open Spreadsheet</a></p>
                </div>
            )}
        </div>
    );
};

export default App;
    