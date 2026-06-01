# How to Push This Task to GitHub

Follow these steps exactly. You only need to do them once for this task folder.

## Option A: Upload Using GitHub Website

This is easiest for a beginner.

1. Go to <https://github.com>.
2. Sign in or create an account.
3. Click the **+** button in the top-right corner.
4. Click **New repository**.
5. Repository name: `alfido-zomato-task`
6. Choose **Public**.
7. Click **Create repository**.
8. Click **uploading an existing file**.
9. Open this folder on your computer:
   `C:\Users\DELL\Documents\Alfido Internship Task\zomato_task1`
10. Drag and drop these files/folders into GitHub:
    - `zomato_analysis.ipynb`
    - `zomato_report.md`
    - `zomato_report.pdf`
    - `submission_document.md`
    - `submission_document.html`
    - `executive_summary_1page.md`
    - `requirements.txt`
    - `README.md`
    - `charts` folder
    - `data` folder if GitHub accepts the file size
11. Scroll down and click **Commit changes**.
12. Copy the repository URL from the browser address bar.

Your link will look like:

```text
https://github.com/YOUR_USERNAME/alfido-zomato-task
```

## Option B: Push Using Git Commands

Use this only if Git is installed.

Open PowerShell inside:

```text
C:\Users\DELL\Documents\Alfido Internship Task
```

Then run:

```powershell
cd "C:\Users\DELL\Documents\Alfido Internship Task"
git init
git add zomato_task1
git commit -m "Add Zomato dataset analysis task"
git branch -M main
git remote add origin https://github.com/YOUR_USERNAME/alfido-zomato-task.git
git push -u origin main
```

Replace `YOUR_USERNAME` with your GitHub username.

## If GitHub Rejects Large Dataset Files

GitHub normally allows files up to 100 MB. The Zomato CSV is around 19 MB, so it should be okay. If GitHub upload is slow or fails:

1. Upload `zomato.zip` or `data/zomato.csv` to Google Drive.
2. Right-click the file in Drive.
3. Click **Share**.
4. Change access to **Anyone with the link**.
5. Copy the link.
6. Paste the Google Drive link into your submission document under the dataset section.

## What Link to Share for Internship Submission

Share:

```text
GitHub Repository: https://github.com/YOUR_USERNAME/alfido-zomato-task
Notebook Link: https://github.com/YOUR_USERNAME/alfido-zomato-task/blob/main/zomato_task1/zomato_analysis.ipynb
Report PDF: https://github.com/YOUR_USERNAME/alfido-zomato-task/blob/main/zomato_task1/zomato_report.pdf
```

If you uploaded only the contents of `zomato_task1` directly into the repo, remove `zomato_task1/` from the links.

