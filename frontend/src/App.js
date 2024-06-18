import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
    const [userInput, setUserInput] = useState('');
    const [messages, setMessages] = useState([]);

    const handleSubmit = async (e) => {
        e.preventDefault();

        try {
            // Send user input to backend using Axios
            const response = await axios.post('http://localhost:5000/messages', {
                user_input: userInput,
            }, {
                headers: {
                    'Content-Type': 'application/json',
                },
            });

            // Update messages state with user input and bot response
            setMessages([
                ...messages,
                { text: userInput, user: true },
                { text: response.data.response, user: false },
            ]);

            // Reset input field
            setUserInput('');
        } catch (error) {
            console.error('Error sending message:', error);
            // Handle error state
        }
    };

    const handleChange = (e) => {
        setUserInput(e.target.value);
    };

    return (
        <div className="App">
            <h1>Chatbot</h1>
            <div className="chat-container">
                {messages.map((message, index) => (
                    <div key={index} className={message.user ? 'user-message' : 'bot-message'}>
                        {message.text}
                    </div>
                ))}
                <form className="form" onSubmit={handleSubmit}>
                    <input
                        type="text"
                        value={userInput}
                        onChange={handleChange}
                        placeholder="Type your message..."
                    />
                    <button type="submit">Send</button>
                </form>
            </div>
        </div>
    );
}

export default App;
