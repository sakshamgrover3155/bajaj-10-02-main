# Flask Backend API - Production Ready

A complete production-ready Flask backend API that handles health checks and BFHL operations including Fibonacci generation, prime number filtering, LCM/HCF calculations, and AI-powered question answering using Google Gemini.

## 📋 Features

- **Health Check Endpoint** (`GET /health`)
- **BFHL Processing Endpoint** (`POST /bfhl`)
  - Fibonacci sequence generation
  - Prime number filtering
  - LCM (Least Common Multiple) calculation
  - HCF (Highest Common Factor) calculation
  - AI-powered single-word answers via Google Gemini
- **Robust Error Handling**
- **Input Validation**
- **Secure Environment Variable Management**
- **Production-Ready Configuration**

## 🚀 API Endpoints

### 1. GET /health
Health check endpoint to verify API status.

**Response:**
```json
{
  "is_success": true,
  "official_email": "your_email@chitkara.edu.in"
}
```

### 2. POST /bfhl
Main processing endpoint. Accepts **exactly ONE** of the following operations:

#### Fibonacci
**Request:**
```json
{
  "fibonacci": 10
}
```
**Response:**
```json
{
  "is_success": true,
  "official_email": "your_email@chitkara.edu.in",
  "data": [0, 1, 1, 2, 3, 5, 8, 13, 21, 34]
}
```

#### Prime
**Request:**
```json
{
  "prime": [2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
}
```
**Response:**
```json
{
  "is_success": true,
  "official_email": "your_email@chitkara.edu.in",
  "data": [2, 3, 5, 7, 11]
}
```

#### LCM
**Request:**
```json
{
  "lcm": [12, 18, 24]
}
```
**Response:**
```json
{
  "is_success": true,
  "official_email": "your_email@chitkara.edu.in",
  "data": 72
}
```

#### HCF
**Request:**
```json
{
  "hcf": [12, 18, 24]
}
```
**Response:**
```json
{
  "is_success": true,
  "official_email": "your_email@chitkara.edu.in",
  "data": 6
}
```

#### AI
**Request:**
```json
{
  "AI": "What is the capital of France?"
}
```
**Response:**
```json
{
  "is_success": true,
  "official_email": "your_email@chitkara.edu.in",
  "data": "Paris"
}
```

### Error Response
**Response (400/500):**
```json
{
  "is_success": false
}
```

## 🛠️ Local Setup & Installation

### Prerequisites
- Python 3.11 or higher
- pip (Python package manager)
- Google Gemini API key ([Get it here](https://makersuite.google.com/app/apikey))

### Step 1: Clone the Repository
```bash
git clone <your-repo-url>
cd <project-directory>
```

### Step 2: Create Virtual Environment
```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies
```bash
pip install -r requirements.txt
```

### Step 4: Set Up Environment Variables
```bash
# Copy the example environment file
cp .env.example .env

# Edit .env and add your Gemini API key
# GEMINI_API_KEY=your_actual_api_key_here
```

**On Windows (PowerShell):**
```powershell
$env:GEMINI_API_KEY="your_api_key_here"
```

**On macOS/Linux (Bash):**
```bash
export GEMINI_API_KEY="your_api_key_here"
```

### Step 5: Run the Application
```bash
python app.py
```

The API will be available at `http://localhost:5000`

## 🧪 Testing the API

### Using cURL

**Test Health Endpoint:**
```bash
curl http://localhost:5000/health
```

**Test Fibonacci:**
```bash
curl -X POST http://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d '{"fibonacci": 8}'
```

**Test Prime:**
```bash
curl -X POST http://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d '{"prime": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}'
```

**Test LCM:**
```bash
curl -X POST http://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d '{"lcm": [12, 18, 24]}'
```

**Test HCF:**
```bash
curl -X POST http://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d '{"hcf": [48, 64, 80]}'
```

**Test AI:**
```bash
curl -X POST http://localhost:5000/bfhl \
  -H "Content-Type: application/json" \
  -d '{"AI": "What is the largest planet in our solar system?"}'
```

### Using Python Requests
```python
import requests

# Health check
response = requests.get('http://localhost:5000/health')
print(response.json())

# Fibonacci
response = requests.post('http://localhost:5000/bfhl', 
                        json={"fibonacci": 10})
print(response.json())

# Prime
response = requests.post('http://localhost:5000/bfhl', 
                        json={"prime": [2, 3, 4, 5, 6, 7, 8, 9]})
print(response.json())
```

## 🌐 Deployment Instructions

### Deploy to Render

1. **Create a Render Account** at [render.com](https://render.com)

2. **Create a New Web Service**
   - Click "New +" → "Web Service"
   - Connect your GitHub repository
   - Configure:
     - **Name:** your-api-name
     - **Environment:** Python
     - **Build Command:** `pip install -r requirements.txt`
     - **Start Command:** `gunicorn app:app`

3. **Add Environment Variables**
   - Go to "Environment" tab
   - Add: `GEMINI_API_KEY` = your_api_key

4. **Deploy**
   - Click "Create Web Service"
   - Wait for deployment to complete
   - Your API will be live at: `https://your-api-name.onrender.com`

### Deploy to Railway

1. **Create a Railway Account** at [railway.app](https://railway.app)

2. **Create a New Project**
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository

3. **Configure Environment Variables**
   - Go to "Variables" tab
   - Add: `GEMINI_API_KEY` = your_api_key
   - Add: `PORT` = 5000 (optional)

4. **Deploy**
   - Railway will auto-detect Flask and deploy
   - Your API will be live at the provided Railway URL

### Deploy to Vercel (Alternative)

1. **Install Vercel CLI**
```bash
npm install -g vercel
```

2. **Create `vercel.json`** (already included in project)
```json
{
  "version": 2,
  "builds": [
    {
      "src": "app.py",
      "use": "@vercel/python"
    }
  ],
  "routes": [
    {
      "src": "/(.*)",
      "dest": "app.py"
    }
  ]
}
```

3. **Deploy**
```bash
vercel --prod
```

4. **Add Environment Variable**
   - In Vercel Dashboard → Settings → Environment Variables
   - Add: `GEMINI_API_KEY`

## 📁 Project Structure

```
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── Procfile              # Deployment configuration
├── runtime.txt           # Python version specification
├── .env.example          # Environment variables template
├── .gitignore            # Git ignore rules
└── README.md             # This file
```

## 🔒 Security Best Practices

1. **Never commit `.env` file** - It's in `.gitignore`
2. **Use environment variables** for sensitive data
3. **Keep dependencies updated** - Run `pip list --outdated`
4. **Enable HTTPS** on production (handled by hosting platforms)
5. **Rotate API keys** regularly

## 🐛 Troubleshooting

### Issue: "ModuleNotFoundError: No module named 'flask'"
**Solution:** Make sure you've activated the virtual environment and installed dependencies:
```bash
source venv/bin/activate  # or venv\Scripts\activate on Windows
pip install -r requirements.txt
```

### Issue: AI endpoint returns "Error"
**Solution:** Verify your Gemini API key is set correctly:
```bash
echo $GEMINI_API_KEY  # Should print your API key
```

### Issue: "Address already in use"
**Solution:** Change the port or kill the process using port 5000:
```bash
# Find process
lsof -i :5000  # macOS/Linux
netstat -ano | findstr :5000  # Windows

# Kill process or use different port
PORT=8000 python app.py
```

## 📝 Notes

- Replace `your_email@chitkara.edu.in` in `app.py` with your actual Chitkara email
- The AI endpoint requires a valid Gemini API key to function
- All endpoints include proper error handling and validation
- The API is configured for production with `debug=False`

## 📄 License

This project is created for educational purposes.

## 👨‍💻 Author

Your Name - Chitkara University

---

**Happy Coding! 🚀**
