# OpenAI Python Chatbot

A simple command-line chatbot built with Python and the OpenAI API.

## Features

- Loads API key from `.env`
- Interactive chat loop in terminal
- Type `bye` to exit

## Project Structure

- `app.py` - Main chatbot script
- `requirements.txt` - Python dependencies
- `.gitignore` - Excludes local and secret files from Git

## Requirements

- Python 3.10+
- An OpenAI API key

## Setup

1. Create and activate a virtual environment (Windows PowerShell):

```powershell
python -m venv env
.\env\Scripts\Activate.ps1
```

2. Install dependencies:

```powershell
python -m pip install -r requirements.txt
```

3. Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_api_key_here
```

## Run

```powershell
.\env\Scripts\python.exe app.py
```

Then chat in the terminal:

- Enter any message to get a response.
- Enter `bye` to quit.

## Troubleshooting

### `ModuleNotFoundError: No module named 'openai'`

You are likely using a different Python interpreter. Run with your virtual environment Python:

```powershell
.\env\Scripts\python.exe app.py
```

### `openai.RateLimitError` with `insufficient_quota`

Your API key is valid but the account has no available quota. Check billing/usage in your OpenAI account.

## GitHub Notes

- `.env` is ignored by `.gitignore` and should never be committed.
- If `.env` was tracked before, remove it from Git tracking:

```powershell
git rm --cached .env
git commit -m "Stop tracking .env"
```
