# 🚀 PlanMate AI - Your Smart Study Buddy

**Powered by Groq AI**

PlanMate AI is an intelligent learning plan generator that creates personalized, structured study plans using advanced AI technology. Simply input your learning goal, and get a comprehensive roadmap with actionable steps, time estimates, and direct links to the best learning resources.

![PlanMate AI Interface](https://img.shields.io/badge/Status-Live-brightgreen) ![FastAPI](https://img.shields.io/badge/FastAPI-005571?style=flat&logo=fastapi) ![Groq AI](https://img.shields.io/badge/Groq-AI-orange) ![Python](https://img.shields.io/badge/Python-3776AB?style=flat&logo=python&logoColor=white)

## ✨ Features

- **🤖 AI-Powered Planning**: Uses Groq's Llama-3.1-8b-instant model for intelligent plan generation
- **📚 Structured Learning Paths**: Get organized steps with realistic time estimates
- **🔗 Direct Resource Links**: Access real learning materials from top platforms
- **🎨 Beautiful Interface**: Modern, responsive design with smooth animations
- **⚡ Fast & Reliable**: Built with FastAPI for high performance
- **🌐 Cross-Platform**: Works on desktop, tablet, and mobile devices

## 🎯 Supported Learning Resources

- **🎥 YouTube** - Video tutorials and courses
- **💻 GitHub** - Open source projects and repositories
- **📚 MDN Docs** - Official web development documentation
- **🌐 W3Schools** - Interactive tutorials and references
- **🎓 Coursera/edX** - University-level courses
- **📖 Khan Academy** - Free educational content
- **💻 FreeCodeCamp** - Coding bootcamp resources
- **❓ Stack Overflow** - Developer Q&A community
- **🐍 Python.org** - Official Python documentation
- **⚛️ React.dev** - Official React learning resources

## 🚀 Quick Start

### Prerequisites

- Python 3.8 or higher
- Groq API key ([Get one here](https://console.groq.com/))

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/planmate-ai.git
   cd planmate-ai
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv .venv
   
   # On Windows
   .venv\Scripts\activate
   
   # On macOS/Linux
   source .venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   # Copy the example file
   cp .env.example .env
   
   # Edit .env and add your Groq API key
   GROQ_API_KEY=your_groq_api_key_here
   ```

5. **Run the application**
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

6. **Open your browser**
   - **API Documentation**: http://127.0.0.1:8000/docs
   - **Web Interface**: Open `index.html` in your browser

## 🎮 How to Use

1. **Open the web interface** (`index.html`)
2. **Enter your learning goal** (e.g., "Learn Python programming", "Master machine learning")
3. **Click "Generate My Learning Plan"**
4. **Get your personalized plan** with:
   - Structured learning steps
   - Time estimates for each step
   - Direct links to learning resources
5. **Click on resources** to access real learning materials

## 🛠️ API Usage

### Generate a Learning Plan

```bash
curl -X POST "http://127.0.0.1:8000/plan" \
     -H "Content-Type: application/json" \
     -d '{"goal": "Learn Python programming in 3 months"}'
```

### Response Format

```json
{
  "title": "Learn Python Programming in 3 Months",
  "steps": [
    {
      "order": 1,
      "task": "Learn Python basics and syntax",
      "duration": "2 weeks",
      "resources": [
        "https://docs.python.org/3/tutorial/",
        "https://www.youtube.com/results?search_query=python+tutorial"
      ]
    }
  ]
}
```

## 🏗️ Project Structure

```
planmate-ai/
├── main.py              # FastAPI backend
├── index.html           # Frontend interface
├── requirements.txt     # Python dependencies
├── .env.example        # Environment variables template
├── .gitignore          # Git ignore rules
└── README.md           # This file
```

## 🔧 Configuration

### Environment Variables

- `GROQ_API_KEY`: Your Groq API key (required)

### Customization

- **Model**: Change the Groq model in `main.py` (line 78)
- **Styling**: Modify CSS in `index.html` for custom themes
- **Resources**: Add more learning platforms in the prompt

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **Groq** for providing the AI model
- **FastAPI** for the excellent web framework
- **All the learning platforms** that make education accessible

## 📞 Support

If you have any questions or need help:

1. Check the [Issues](https://github.com/yourusername/planmate-ai/issues) page
2. Create a new issue if your problem isn't already reported
3. Join our community discussions

---

**Made with ❤️ for learners everywhere**

⭐ **Star this repository if you found it helpful!**
