// frontend/src/App.js
import React from 'react';
import axios from 'axios';
import Button from './components/Button';

const App = () => {
    const handleButtonClick = async () => {
        try {
            const response = await axios.post('http://localhost:5000/generate-sheet');
            console.log(response.data);
        } catch (error) {
            console.error(error);
            alert('An error occurred while generating the sheet.');
        }
    };
    return (
        <div>
            <h1>Work Attendance Sheet Generator</h1>
            <Button onClick={handleButtonClick} label="Generate Work Attendance Sheet" />
        </div>
    );
};

export default App;