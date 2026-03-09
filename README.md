# 🤖 Aiden — AI Startup Advisor

> A dark glassmorphism web app that validates startup ideas using Groq's free Llama 3.3 API.

---

## 📁 Project Structure

```
aiden-ai/
├── backend/
│   └── main.py              ← FastAPI app + Groq AI logic
├── frontend/
│   ├── index.html           ← Full app UI (HTML/CSS/JS)
│   └── logo.png             ← Your robot logo (add this!)
├── .env                     ← Your secret keys (never commit!)
├── .env.example             ← Template for keys
├── .gitignore
├── requirements.txt
├── render.yaml              ← Render.com deploy config
├── Procfile                 ← Heroku/Railway deploy config
└── README.md
```

---

## ⚙️ Local Setup (Step by Step)

### 1. Get the Groq API Key (FREE)
1. Go to https://console.groq.com
2. Sign up (no credit card needed)
3. Click **API Keys** → **Create API Key**
4. Copy the key

### 2. Add Your Logo
- Copy your robot logo image into `frontend/` and name it `logo.png`

### 3. Create Your .env File
```bash
# In the project root, create a .env file:
cp .env.example .env
# Then open .env and paste your key:
GROQ_API_KEY=gsk_your_actual_key_here
```

### 4. Set Up Python Environment
```bash
# Make sure you're using Python 3.11
python3.11 -m venv venv

# Activate (Windows):
venv\Scripts\activate

# Activate (Mac/Linux):
source venv/bin/activate

# Install dependencies:
pip install -r requirements.txt
```

### 5. Run the App
```bash
# From the project root:
uvicorn backend.main:app --reload

# Open your browser:
http://localhost:8000
```

---

## 🚀 Deploy to Render (FREE Hosting)

1. Push your code to GitHub (make sure `.env` is in `.gitignore`!)
2. Go to https://render.com → Sign up → **New Web Service**
3. Connect your GitHub repo
4. Settings:
   - **Build Command:** `pip install -r requirements.txt`
   - **Start Command:** `uvicorn backend.main:app --host 0.0.0.0 --port $PORT`
   - **Environment:** Python
5. Add Environment Variable:
   - Key: `GROQ_API_KEY`
   - Value: your Groq key
6. Click **Deploy** → Done! 🎉

---

## 🛠️ Tech Stack

| Layer | Tech | Why |
|-------|------|-----|
| Backend | FastAPI | Fast, modern, great for portfolios |
| AI | Groq + Llama 3.3 70B | Free, blazing fast |
| Frontend | HTML/CSS/JS | No framework needed, fully portable |
| Deploy | Render.com | Free tier, easy GitHub integration |

---

## 💡 Features

- ✅ Market demand score with animated ring
- ✅ Competitor analysis with threat levels
- ✅ Monetization models
- ✅ Risk assessment
- ✅ Advertising channel recommendations
- ✅ Curated learning resources with links
- ✅ Interactive startup checklist
- ✅ Off-topic guard (business only)
- ✅ Optional step-by-step startup plan
- ✅ 10 real success stories section
- ✅ Dark glassmorphism UI
- ✅ Fully responsive

---

## 🔒 Security Notes

- Never commit your `.env` file
- The `.gitignore` already protects it
- On Render, set `GROQ_API_KEY` as an environment variable in the dashboard, not in code

---

Built with 💙 for portfolio purposes. Powered by Groq + Llama 3.3 70B (free tier).
