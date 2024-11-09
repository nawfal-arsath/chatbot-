FastAPI DialoGPT Chatbot using http protocol 
A conversational AI chatbot built with FastAPI and Hugging Face's DialoGPT-large model. This API service provides natural language conversation capabilities through a simple REST endpoint.
Features

Real-time chat responses using Microsoft's DialoGPT-large model
Conversation history support
RESTful API interface
Error handling and validation
Asynchronous request processing

Prerequisites
Before running the project, make sure you have the following installed:

Python 3.8+
pip (Python package manager)

Installation

Clone the repository:

bashCopygit clone https://github.com/yourusername/fastapi-dialogpt-chatbot.git
cd fastapi-dialogpt-chatbot

Create a virtual environment:

bashCopypython -m venv venv
source venv/bin/activate  # On Windows, use: venv\Scripts\activate

Install the required dependencies:

bashCopypip install fastapi uvicorn torch transformers pydantic
Usage

Start the server:

bashCopy

uvicorn server:app --reload

The API will be available at http://localhost:8000
Use the /chat/ endpoint to interact with the chatbot:
 
 run : streamlit app.py

to run the client


API Documentation
POST /chat/
Send a message to the chatbot and receive a response.
Request Body
jsonCopy{
    "prompt": "string",
    "history": ["string"]
}

prompt: The user's message to the chatbot
history: List of previous messages in the conversation (optional)

Response
jsonCopy{
    "response": "string"
}
Error Response
jsonCopy{
    "detail": "error message"
}
Project Structure
Copyfastapi-dialogpt-chatbot/
├── main.py           # Main FastAPI application
├── requirements.txt  # Project dependencies
└── README.md        # Project documentation
Dependencies

FastAPI: Web framework for building APIs
Pydantic: Data validation using Python type annotations
Transformers: Hugging Face's transformers library
PyTorch: Deep learning framework
Uvicorn: ASGI server implementation

Error Handling
The API includes error handling for:

Invalid input validation
Model generation errors
Server-side exceptions

All errors return appropriate HTTP status codes and error messages.
Performance Considerations

The model is loaded into memory on startup
First request might be slower due to model initialization
Consider GPU acceleration for better performance
Be mindful of the max_length parameter in the generation step

Contributing

Fork the repository
Create your feature branch (git checkout -b feature/AmazingFeature)
Commit your changes (git commit -m 'Add some AmazingFeature')
Push to the branch (git push origin feature/AmazingFeature)
Open a Pull Request

License
This project is licensed under the MIT License - see the LICENSE file for details.
Acknowledgments

Hugging Face Transformers
Microsoft DialoGPT
FastAPI
