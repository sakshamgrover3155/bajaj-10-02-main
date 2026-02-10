# 📌 QUICK REFERENCE CARD

## 🚀 Quick Start Commands

```bash
# 1. Setup
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
pip install -r requirements.txt

# 2. Set environment variable
export GEMINI_API_KEY="your_key_here"  # Windows: set GEMINI_API_KEY=your_key_here

# 3. Run
python app.py
```

## 🌐 API Endpoints

### GET /health
```bash
curl http://localhost:5000/health
```
**Response:**
```json
{"is_success": true, "official_email": "your_email@chitkara.edu.in"}
```

### POST /bfhl

#### 1️⃣ Fibonacci
```bash
curl -X POST http://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d '{"fibonacci": 10}'
```

#### 2️⃣ Prime
```bash
curl -X POST http://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d '{"prime": [1,2,3,4,5,6,7,8,9,10]}'
```

#### 3️⃣ LCM
```bash
curl -X POST http://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d '{"lcm": [12,18,24]}'
```

#### 4️⃣ HCF
```bash
curl -X POST http://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d '{"hcf": [48,64,80]}'
```

#### 5️⃣ AI
```bash
curl -X POST http://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d '{"AI": "What is the capital of France?"}'
```

## 📦 Project Files

| File | Purpose |
|------|---------|
| `app.py` | Main application code |
| `requirements.txt` | Python dependencies |
| `Procfile` | Deployment config (Render/Railway) |
| `runtime.txt` | Python version |
| `vercel.json` | Vercel deployment config |
| `.env.example` | Environment variables template |
| `test_api.py` | Automated test script |
| `start.sh` | Quick start script |

## 🔧 Common Commands

```bash
# Run tests
python test_api.py

# Check dependencies
pip list

# Update dependencies
pip install --upgrade -r requirements.txt

# Check Python version
python --version

# Deactivate virtual environment
deactivate
```

## 🚀 Deployment Platforms

| Platform | Free Tier | Command |
|----------|-----------|---------|
| Render | ✅ 750hrs/mo | Push to GitHub → Connect repo |
| Railway | ✅ $5 credit | Push to GitHub → Connect repo |
| Vercel | ✅ Unlimited | `vercel --prod` |
| Heroku | ❌ ($5/mo) | `git push heroku main` |

## 🐛 Troubleshooting

```bash
# Port already in use
lsof -i :5000  # Find process
kill -9 <PID>  # Kill process

# Module not found
pip install -r requirements.txt

# Permission denied
chmod +x start.sh

# Check environment variables
echo $GEMINI_API_KEY
```

## ✅ Before Deployment

- [ ] Update email in `app.py`
- [ ] Set `GEMINI_API_KEY` environment variable
- [ ] Test locally
- [ ] Push to Git
- [ ] Deploy
- [ ] Test live endpoints

## 📝 Response Format

**Success:**
```json
{
  "is_success": true,
  "official_email": "your_email@chitkara.edu.in",
  "data": <result>
}
```

**Error:**
```json
{
  "is_success": false
}
```

## 🔗 Useful Links

- Get Gemini API Key: https://makersuite.google.com/app/apikey
- Render: https://render.com
- Railway: https://railway.app
- Vercel: https://vercel.com

---

**Keep this card handy! 📌**
