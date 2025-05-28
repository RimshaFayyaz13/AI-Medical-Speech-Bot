## 🩺 AI Medical Chatbot
An intelligent AI-powered medical assistant that can analyze medical images (e.g., skin conditions like acne) and text queries to predict possible diseases or conditions. Built using the Groq API with the LLaMA 3.1 8B Instant model for fast and accurate AI reasoning.

## 🚀 Features
🖼️ Image Input: Analyze medical images (e.g., skin conditions, reports).

🧠 Multimodal Queries: Accepts both text and image input for improved context and prediction.

⚡ Fast Responses: Utilizes Groq's LLaMA 3.1 8B Instant model.

🧩 Modular Design: Clean and scalable project structure for easy enhancements.

## 🛠️ Installation
1. Clone the Repository
   
git clone https://github.com/RimshaFayyaz13/ai-medical-chatbot.git
cd ai-medical-chatbot

3. Create and Activate a Virtual Environment
On Windows:

python -m venv chatenv
chatenv\Scripts\activate
On macOS/Linux:

python3 -m venv chatenv
source chatenv/bin/activate

## 📸 How It Works
The script reads and encodes a medical image (e.g., images/acne.jpg) in Base64.

A text query like "What disease is shown?" is combined with the image.

Both the image and query are sent to the Groq API.

The LLaMA model analyzes the input and returns a diagnostic response.

## ⚙️ Technologies Used
✅ Python 3

✅ Groq API

✅ Base64 Encoding

✅ ffmpeg (for image/audio preprocessing)

🧪 Example
## Input Type	Example
Image	images/acne.jpg
Query	"What is the disease in the image?"
Output	"The condition appears to be acne vulgaris. You may consult a dermatologist."

## 🤝 Contributing
Contributions are welcome! 💬

If you'd like to propose a new feature or improvement, feel free to open an issue.

For pull requests, please make sure your changes are well-tested and documented.
