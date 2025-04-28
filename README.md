🩺 AI Medical Chatbot
An intelligent AI-powered medical assistant that can analyze medical images (e.g., skin conditions like acne) and text queries to predict possible diseases or conditions. Built using Groq API with the LLaMA 3 model family for fast and accurate AI reasoning.

🚀 Features
🖼️ Accepts image input (e.g., skin conditions, medical reports).

🧠 Accepts text queries along with images.

🔥 Uses Groq's LLaMA 3.1 8B Instant model for fast response.

📦 Clean project structure for easy scalability.

🛠️ Installation
Clone the repository

bash
Copy code
git clone https://github.com/RimshaFayyaz13/ai-medical-chatbot.git
cd ai-medical-chatbot
Create and activate a virtual environment

Windows:

bash
Copy code
python -m venv chatenv
chatenv\Scripts\activate

📸 How It Works
The script reads an image, encodes it in base64, and sends it to Groq API.

Along with the image, a text query (like "What disease is shown?") is sent.

The AI model predicts and sends a response back.

Example image input: images/acne.jpg
Example query: "What is the disease in the image?"

⚙️ Technologies Used
Python 3

Groq API

ffmpeg

Base64 Encoding

🤝 Contributing
Pull requests are welcome!
For major changes, please open an issue first to discuss what you would like to change.

📜 License
This project is licensed under the MIT License.

🚀 Let's build the future of AI-driven healthcare together!
