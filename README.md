# 🚀 PlanMate AI - Your Smart Study Buddy

**Powered by Groq AI**

AI-powered learning plan generator that creates personalized study plans with structured steps and direct resource links.

## ✨ Features

- 🤖 **AI-Powered Planning** - Uses Groq's Llama-3.1-8b-instant model
- 📚 **Structured Learning Paths** - Organized steps with time estimates
- 🔗 **Direct Resource Links** - Access to YouTube, GitHub, MDN, Coursera, and more
- 🎨 **Beautiful Interface** - Modern, responsive design

## 🚀 Quick Start

1. **Clone and setup**
   ```bash
   git clone https://github.com/SM-knigt/PlaneMate-AI.git
   cd PlaneMate-AI
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   pip install -r requirements.txt
   ```

2. **Get Groq API key**
   - Sign up at [console.groq.com](https://console.groq.com/)
   - Copy `env.example` to `.env`
   - Add your API key: `GROQ_API_KEY=your_key_here`

3. **Run the app**
   ```bash
   uvicorn main:app --reload --host 0.0.0.0 --port 8000
   ```

4. **Open `index.html` in your browser**

## 🎮 Usage

1. Enter your learning goal (e.g., "Learn Python programming")
2. Click "Generate My Learning Plan"
3. Get structured steps with time estimates and resource links
4. Click resources to access real learning materials

## 🛠️ API

```bash
curl -X POST "http://127.0.0.1:8000/plan" \
     -H "Content-Type: application/json" \
     -d '{"goal": "Learn Python programming"}'
```

## 📁 Files

- `main.py` - FastAPI backend
- `index.html` - Frontend interface
- `requirements.txt` - Dependencies
- `env.example` - Environment template

---

⭐ **Star if helpful!** Made with ❤️ for learners everywhere.
