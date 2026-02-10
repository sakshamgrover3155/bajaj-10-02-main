# 🚀 DEPLOYMENT GUIDE - Flask Backend API

This guide provides detailed step-by-step instructions for deploying your Flask API to various platforms.

---

## 📋 Pre-Deployment Checklist

Before deploying, ensure you have:

- ✅ Google Gemini API Key ([Get one here](https://makersuite.google.com/app/apikey))
- ✅ Updated `OFFICIAL_EMAIL` in `app.py` to your Chitkara email
- ✅ Tested the API locally
- ✅ Git repository with all files committed

---

## 🎯 OPTION 1: Deploy to Render (Recommended - FREE)

### Step 1: Prepare Your Repository
```bash
# Initialize git if not done
git init

# Add all files
git add .

# Commit
git commit -m "Initial commit"

# Push to GitHub
git remote add origin https://github.com/yourusername/your-repo.git
git push -u origin main
```

### Step 2: Create Render Account
1. Go to [https://render.com](https://render.com)
2. Sign up using GitHub (recommended)

### Step 3: Create New Web Service
1. Click **"New +"** button (top right)
2. Select **"Web Service"**
3. Connect your GitHub repository
4. Select your repository from the list

### Step 4: Configure Service
Fill in the following settings:

| Field | Value |
|-------|-------|
| **Name** | `your-api-name` (e.g., `flask-bfhl-api`) |
| **Region** | Choose closest to you |
| **Branch** | `main` |
| **Root Directory** | Leave empty |
| **Runtime** | `Python 3` |
| **Build Command** | `pip install -r requirements.txt` |
| **Start Command** | `gunicorn app:app` |
| **Instance Type** | `Free` |

### Step 5: Add Environment Variables
1. Scroll to **"Environment Variables"** section
2. Click **"Add Environment Variable"**
3. Add:
   - **Key:** `GEMINI_API_KEY`
   - **Value:** `your_actual_gemini_api_key`

### Step 6: Deploy
1. Click **"Create Web Service"**
2. Wait 2-5 minutes for deployment
3. Your API URL will be: `https://your-api-name.onrender.com`

### Step 7: Test Your Deployment
```bash
# Test health endpoint
curl https://your-api-name.onrender.com/health

# Test fibonacci
curl -X POST https://your-api-name.onrender.com/bfhl \
  -H "Content-Type: application/json" \
  -d '{"fibonacci": 5}'
```

### Important Notes for Render:
- ⏰ Free tier sleeps after 15 minutes of inactivity
- 🔄 First request after sleep takes 30-60 seconds
- 💾 750 hours/month free (sufficient for most use cases)
- 📊 View logs in Render dashboard

---

## 🎯 OPTION 2: Deploy to Railway (FREE)

### Step 1: Create Railway Account
1. Go to [https://railway.app](https://railway.app)
2. Sign up with GitHub

### Step 2: Create New Project
1. Click **"New Project"**
2. Select **"Deploy from GitHub repo"**
3. Authorize Railway to access your repositories
4. Select your repository

### Step 3: Configure Environment Variables
1. Click on your deployment
2. Go to **"Variables"** tab
3. Click **"New Variable"**
4. Add:
   - **Variable:** `GEMINI_API_KEY`
   - **Value:** `your_actual_gemini_api_key`

### Step 4: Deploy
1. Railway automatically detects Python and deploys
2. Wait for deployment (usually 2-3 minutes)
3. Click **"Settings"** → **"Generate Domain"** to get public URL

### Step 5: Test Your Deployment
```bash
# Replace with your Railway URL
curl https://your-app.up.railway.app/health
```

### Important Notes for Railway:
- 💰 $5 free credit per month
- ⚡ Faster cold starts than Render
- 🔄 No sleep on free tier (while credits last)
- 📊 Great dashboard and logging

---

## 🎯 OPTION 3: Deploy to Vercel

### Step 1: Install Vercel CLI
```bash
npm install -g vercel
```

### Step 2: Login to Vercel
```bash
vercel login
```

### Step 3: Deploy
```bash
# From your project directory
vercel --prod
```

### Step 4: Add Environment Variables
1. Go to [https://vercel.com/dashboard](https://vercel.com/dashboard)
2. Select your project
3. Go to **"Settings"** → **"Environment Variables"**
4. Add:
   - **Name:** `GEMINI_API_KEY`
   - **Value:** `your_actual_gemini_api_key`
   - **Environments:** Production, Preview, Development

### Step 5: Redeploy
```bash
vercel --prod
```

### Important Notes for Vercel:
- ⚡ Excellent for serverless functions
- 🌍 Global CDN
- 🔄 Automatic HTTPS
- ⏱️ 10-second timeout on free tier

---

## 🎯 OPTION 4: Deploy to Heroku

### Step 1: Install Heroku CLI
Download from [https://devcenter.heroku.com/articles/heroku-cli](https://devcenter.heroku.com/articles/heroku-cli)

### Step 2: Login
```bash
heroku login
```

### Step 3: Create App
```bash
heroku create your-api-name
```

### Step 4: Add Environment Variables
```bash
heroku config:set GEMINI_API_KEY=your_actual_gemini_api_key
```

### Step 5: Deploy
```bash
git push heroku main
```

### Step 6: Test
```bash
curl https://your-api-name.herokuapp.com/health
```

### Important Notes for Heroku:
- 💰 No longer has free tier (starts at $5/month)
- 🏢 Better for production applications
- 📊 Excellent add-ons ecosystem

---

## 🔧 Post-Deployment Steps

### 1. Update Your Email
Edit `app.py` and replace:
```python
OFFICIAL_EMAIL = "your_email@chitkara.edu.in"
```
with your actual Chitkara email, then redeploy.

### 2. Monitor Your API
- Check logs regularly
- Set up uptime monitoring (e.g., UptimeRobot)
- Monitor API usage

### 3. Test All Endpoints
```bash
# Set your API URL
API_URL="https://your-api.onrender.com"

# Health
curl $API_URL/health

# Fibonacci
curl -X POST $API_URL/bfhl -H "Content-Type: application/json" -d '{"fibonacci": 10}'

# Prime
curl -X POST $API_URL/bfhl -H "Content-Type: application/json" -d '{"prime": [1,2,3,4,5,6,7,8,9,10]}'

# LCM
curl -X POST $API_URL/bfhl -H "Content-Type: application/json" -d '{"lcm": [12,18,24]}'

# HCF
curl -X POST $API_URL/bfhl -H "Content-Type: application/json" -d '{"hcf": [48,64,80]}'

# AI
curl -X POST $API_URL/bfhl -H "Content-Type: application/json" -d '{"AI": "What is Python?"}'
```

---

## 🐛 Common Deployment Issues

### Issue 1: "Application Error" or 500 Error
**Cause:** Missing environment variable or code error

**Solution:**
1. Check deployment logs
2. Verify `GEMINI_API_KEY` is set correctly
3. Check for syntax errors in `app.py`

### Issue 2: "Module not found"
**Cause:** Dependencies not installed

**Solution:**
1. Verify `requirements.txt` is in root directory
2. Check build logs for installation errors
3. Ensure Python version is compatible (3.11+)

### Issue 3: AI Endpoint Returns "Error"
**Cause:** Invalid or missing Gemini API key

**Solution:**
1. Verify API key is correct
2. Check API key has not expired
3. Ensure no extra spaces in environment variable

### Issue 4: Slow Response Times
**Cause:** Cold start (free tier platforms)

**Solution:**
1. Keep API warm with periodic ping
2. Upgrade to paid tier for better performance
3. Use uptime monitoring service

---

## 📊 Monitoring & Maintenance

### Set Up Uptime Monitoring
Use [UptimeRobot](https://uptimerobot.com) (Free):
1. Create account
2. Add new monitor
3. Monitor Type: HTTP(s)
4. URL: `https://your-api.onrender.com/health`
5. Monitoring Interval: 5 minutes

### View Logs
- **Render:** Dashboard → Your Service → Logs
- **Railway:** Dashboard → Your Project → View Logs
- **Vercel:** Dashboard → Your Project → Logs
- **Heroku:** `heroku logs --tail`

---

## 🎓 Best Practices

1. **Environment Variables**
   - Never hardcode API keys
   - Use different keys for dev/prod
   - Rotate keys periodically

2. **Git Practices**
   - Never commit `.env` files
   - Use `.gitignore` properly
   - Keep commits meaningful

3. **Code Quality**
   - Add error logging
   - Implement rate limiting for production
   - Add request validation

4. **Security**
   - Use HTTPS (automatic on most platforms)
   - Implement CORS if needed
   - Add authentication for sensitive endpoints

---

## ✅ Deployment Checklist

Before going live:

- [ ] Updated email in `app.py`
- [ ] Set `GEMINI_API_KEY` environment variable
- [ ] Tested all endpoints locally
- [ ] Committed all files to Git
- [ ] Deployed to chosen platform
- [ ] Tested all endpoints on live URL
- [ ] Set up monitoring
- [ ] Documented API URL
- [ ] Created backup of code

---

## 🆘 Need Help?

- 📚 Check platform documentation
- 🔍 Search error messages
- 💬 Ask on platform community forums
- 📧 Contact platform support

---

**Good luck with your deployment! 🚀**
