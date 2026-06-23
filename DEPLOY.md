# Deploy live demo (resume link)

Use **Streamlit Community Cloud** (free). Your demo URL will look like:

`https://mumbai-real-estate-intelligence.streamlit.app`

## 1. Push code to GitHub

```bash
cd Mumbai_Real_Estate_Intelligence_System-DS_LAB_MP-main
git init
git add .
git commit -m "Prepare app for Streamlit Cloud deployment"
```

Create a new repo on [github.com/new](https://github.com/new), then:

```bash
git remote add origin https://github.com/YOUR_USERNAME/mumbai-real-estate-intelligence.git
git branch -M main
git push -u origin main
```

> **Note:** `model/*.pkl` is gitignored (170 MB, over GitHub limit). The app builds the model automatically on first run (~1 min).

## 2. Deploy on Streamlit Cloud

1. Go to [share.streamlit.io](https://share.streamlit.io)
2. Sign in with GitHub
3. Click **New app**
4. Select your repo, branch `main`
5. **Main file path:** `Real_Estate_Project.py`
6. Click **Deploy**

## 3. Add link to resume

After deploy finishes, copy the app URL from the dashboard, e.g.:

**Live Demo:** https://your-app-name.streamlit.app

## Troubleshooting

- **First load slow:** Price Prediction builds the ML model once; later loads are fast.
- **Build fails:** Ensure `requirements.txt` is the slim app file (not the full notebook stack).
- **Data missing:** Commit the `data/` folder — required CSVs are under 10 MB each.
