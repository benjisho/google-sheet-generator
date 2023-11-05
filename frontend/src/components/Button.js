// frontend/src/components/Button.js
import React from 'react';
import './Button.css';  // Import the new CSS file

const Button = ({ label, onClick }) => {
    return (
        <button className="button" onClick={onClick}>
            {label}
        </button>
    );
};

export default Button;
