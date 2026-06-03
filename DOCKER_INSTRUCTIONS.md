# 🐳 MCP AWS Bot — Docker Setup Guide

---

## 📋 Prerequisites

Before you start, make sure you have:
- ✅ **Docker Desktop** installed and running on your Windows machine
- ✅ All project files in one folder (e.g., `C:\mcp-aws-bot`)
- ✅ **AWS Access Keys** ready (Access Key ID + Secret Access Key)

Your project folder must contain these files:
```
C:\mcp-aws-bot\
├── Dockerfile
├── main.py
├── agent.py
├── aws_tools.py
├── index.html
└── requirements.txt
```

---

## 🔑 Step 1 — Get Your AWS Access Keys

> Skip this step if you already have your Access Key ID and Secret Access Key.

1. Go to [https://aws.amazon.com](https://aws.amazon.com) and log in
2. Click your **account name** (top right corner)
3. Click **Security credentials**
4. Scroll down to **Access keys**
5. Click **Create access key**
6. Copy and save both values:
   ```
   Access Key ID:      AKIA...............
   Secret Access Key:  xxxxxxxxxxxxxxxxxxxxxxx
   ```
   ⚠️ The Secret Access Key is shown **only once** — save it immediately!

---

## 🏗️ Step 2 — Build the Docker Image

Open **PowerShell** and navigate to your project folder:

```powershell
cd C:\mcp-aws-bot (path where the project is installedon local)
```

Build the image:

```powershell
docker build --no-cache -t mcp-aws-bot .
```

⏳ This takes **2-3 minutes** the first time (downloads Python, installs AWS CLI and dependencies).

When it's done you'll see:
```
Successfully tagged mcp-aws-bot:latest
```

---

## 🚀 Step 3 — Run the Container

Run the container with your AWS credentials:

```powershell
docker run -d -p 8000:8000 --name mcp-aws-bot -e AWS_ACCESS_KEY_ID=YOUR_KEY -e AWS_SECRET_ACCESS_KEY=YOUR_SECRET -e AWS_DEFAULT_REGION=ap-south-1 mcp-aws-bot
```

Replace:
- `YOUR_KEY` → your Access Key ID (e.g., `AKIAVWXSK7AF......`)
- `YOUR_SECRET` → your Secret Access Key
- `ap-south-1` → your AWS region (keep this if you're in Mumbai/India)

You'll see a long container ID printed — that means it started successfully:
```
aa4ff88d31711bfee1f840cf85779405685fc13b
```

---
<img width="3839" height="2032" alt="Screenshot 2026-06-03 235015" src="https://github.com/user-attachments/assets/a6082ee7-3cc9-41cf-8ea8-98e94b5055de" />

## ✅ Step 4 — Verify It's Running

Check the logs to confirm the server started:

```powershell
docker logs mcp-aws-bot
```

You should see:
```
INFO:     Started server process [1]
INFO:     Application startup complete.
INFO:     Uvicorn running on http://0.0.0.0:8000
```

---

## 🌐 Step 5 — Open the Bot in Browser

Open your browser and go to:

```
http://localhost:8000
```

You'll see the **MCP AWS Bot** chat interface. Try these commands:

| Command | What it does |
|---|---|
| `list my EC2 instances` | Shows all your EC2 instances |
| `create an EC2 instance` | Creates a new EC2 instance |
| `create EC2 instance named MyServer` | Creates instance with a name |
| `stop MyServer` | Stops instance by name |
| `terminate MyServer` | Deletes instance by name |

---

## 🔄 Step 6 — Updating AWS Credentials

If your credentials expire or you need to change them, run:

```powershell
docker rm -f mcp-aws-bot
docker run -d -p 8000:8000 --name mcp-aws-bot -e AWS_ACCESS_KEY_ID=NEW_KEY -e AWS_SECRET_ACCESS_KEY=NEW_SECRET -e AWS_DEFAULT_REGION=ap-south-1 mcp-aws-bot
```

No rebuild needed — same image, just new credentials.
<img width="3839" height="2036" alt="Screenshot 2026-06-03 234813" src="https://github.com/user-attachments/assets/91985c71-e4ed-4033-b4b9-bafe0a1e3036" />

---

## ⏹️ Stop the Bot

When you're done:

```powershell
docker rm -f mcp-aws-bot
```

---

## 🔁 Restart the Bot Later

If you stopped it and want to start again:

```powershell
docker run -d -p 8000:8000 --name mcp-aws-bot -e AWS_ACCESS_KEY_ID=YOUR_KEY -e AWS_SECRET_ACCESS_KEY=YOUR_SECRET -e AWS_DEFAULT_REGION=ap-south-1 mcp-aws-bot
```
<img width="3839" height="2035" alt="Screenshot 2026-06-03 234825" src="https://github.com/user-attachments/assets/4448e41a-5ae4-4515-85fa-f95baca29c5a" />

<img width="3839" height="2159" alt="Screenshot 2026-06-03 234945" src="https://github.com/user-attachments/assets/701e505e-2292-4cd6-85f5-939045c46a09" />


---

## 🐛 Troubleshooting

### Bot not opening in browser?
```powershell
docker logs mcp-aws-bot
```
Check the logs for errors.

### "AuthFailure" error in the chat?
Your AWS credentials are wrong or expired. Rotate them in AWS Console and rerun Step 3.

### "Name already in use" error?
A container with that name already exists. Remove it first:
```powershell
docker rm -f mcp-aws-bot
```

### Want to rebuild after code changes?
```powershell
docker rm -f mcp-aws-bot
docker rmi mcp-aws-bot
docker build --no-cache -t mcp-aws-bot .
docker run -d -p 8000:8000 --name mcp-aws-bot -e AWS_ACCESS_KEY_ID=YOUR_KEY -e AWS_SECRET_ACCESS_KEY=YOUR_SECRET -e AWS_DEFAULT_REGION=ap-south-1 mcp-aws-bot
```

---

## ⚠️ Security Reminders

- ❌ Never share your AWS Access Keys with anyone
- ❌ Never paste credentials in chat, GitHub, or any public place
- ✅ Rotate your keys regularly in AWS Console
- ✅ Delete keys you no longer use

---

**Built with ❤️ for DevOps automation**
**KISHORE HC**
**kishorehc99@gmail.com**
