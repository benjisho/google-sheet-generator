// frontend/src/App.js
import React, { useState } from 'react';
import axios from 'axios';
import Button from './components/Button';

const App = () => {
    const [spreadsheetLink, setSpreadsheetLink] = useState(null);

    const handleButtonClick = async () => {
        try {
            const response = await axios.post('http://95.179.193.18:5000/generate-sheet');  // Update this line
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
        <div>
            <h1>Work Attendance Sheet Generator</h1>
            <Button onClick={handleButtonClick} label="Generate Work Attendance Sheet" />
            {spreadsheetLink && (
                <div>
                    <p>Spreadsheet created! <a href={spreadsheetLink} target="_blank" rel="noopener noreferrer">Open Spreadsheet</a></p>
                </div>
            )}
        </div>
    );
};

export default App;
