# LangChain Question-Answering Bot

## Overview

This project is a FastAPI-based Question-Answering (QA) bot that processes questions and documents to generate answers using LangChain.

## Setup

### 1. Clone the Repository

```bash
git clone https://github.com/saurabh0413/Question-Answering-Bot.git
cd Question-Answering-Bot
```
### 2. Create a Virtual Environment and Install Dependencies

```bash
python -m venv venv
source venv/bin/activate  # On Windows: .\venv\Scripts\activate
pip install -r requirements.txt
```
### 3. Set Up Environment Variables

```bash
Create a .env file in the root directory:
OPENAI_API_KEY="your_openai_api_key"

```

### 4. Run the Application

```bash
uvicorn app.main:app --reload
```


### Final Notes:

- Replace `your_openai_api_key` with your actual API key.
- Ensure all dependencies and setup steps are followed for a smooth experience.

Let me know if you have any questions or need further assistance!
