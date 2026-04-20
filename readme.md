
## 🚀 Overview

MCP AWS Bot is an intelligent DevOps automation tool that allows you to manage AWS EC2 instances using **natural language commands**. Built with FastAPI and AWS SDK (boto3), it provides both a REST API and a beautiful chat interface.

### ✨ Features

| Feature | Description |
|---------|-------------|
| 📋 **List Instances** | View all EC2 instances with names and status |
| 🚀 **Create Instances** | Launch new EC2 instances with custom names |
| ⏹️ **Stop Instances** | Stop instances by ID or friendly name |
| 🗑️ **Terminate Instances** | Delete instances by ID or name |
| 🎨 **Modern Web UI** | Beautiful chat interface like ChatGPT |
| 🔌 **REST API** | Easy integration with other tools |
| 🆓 **Free Tier** | Uses AWS free tier eligible instances |

## 🏗️ Architecture

```
┌─────────────┐     ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
│   Browser   │────▶│   FastAPI   │────▶│   Agent     │────▶│   AWS SDK   │
│  (Web UI)   │◀────│  (main.py)  │◀────│  (agent.py) │◀────│ (boto3)     │
└─────────────┘     └─────────────┘     └─────────────┘     └──────┬──────┘
                                                                   │
                                                              ┌────▼──────┐
                                                              │  AWS EC2  │
                                                              └───────────┘
```

## 📋 Prerequisites

- Python 3.10 or higher
- AWS Account (Free Tier)
- AWS CLI configured
- Git (for version control)

## 🛠️ Installation

### 1. Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/mcp-aws-bot.git
cd mcp-aws-bot
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Configure AWS Credentials

```bash
aws configure
```

Enter your credentials:
- **AWS Access Key ID**: Your access key
- **AWS Secret Access Key**: Your secret key
- **Default region name**: `ap-south-1` (or your preferred region)
- **Default output format**: `json`

### 4. Run the Application

```bash
uvicorn main:app --reload
```

### 5. Open Your Browser

Navigate to: `http://127.0.0.1:8000`

## 🎮 Usage Guide

### Web Interface Commands

| Command | Action |
|---------|--------|
| `list my EC2 instances` | Show all instances |
| `create an EC2 instance` | Create default instance |
| `create EC2 instance named MyServer` | Create named instance |
| `stop MyServer` | Stop instance by name |
| `terminate MyServer` | Delete instance by name |
| `stop i-123456789` | Stop instance by ID |
| `terminate i-123456789` | Delete instance by ID |

### Example Workflow

```bash
# Create a named instance
> create EC2 instance named Production

# Response
✅ EC2 Created!
   ID: i-0a1b2c3d4e5f67890
   Name: Production

# List all instances
> list my EC2 instances

# Stop by name
> stop Production

# Terminate by name
> terminate Production
```

### API Endpoints

#### GET `/` 
Returns the web interface.

#### POST `/chat?prompt={command}`
Execute commands programmatically.

**Example using curl:**
```bash
curl -X POST 'http://localhost:8000/chat?prompt=list%20my%20EC2%20instances'
```

**Response:**
```json
{
  "response": "📋 Your EC2 Instances:\n• i-123456789 | Name: MyServer | Status: running"
}
```

## 📁 Project Structure

```
mcp-aws-bot/
├── main.py              # FastAPI server & web interface
├── agent.py             # Natural language processing
├── aws_tools.py         # AWS EC2 operations
├── index.html           # Web UI
├── requirements.txt     # Python dependencies
├── .gitignore          # Git ignore file
└── README.md           # Documentation
```

## 📦 Requirements File

Create `requirements.txt`:

```txt
fastapi==0.136.0
uvicorn==0.44.0
boto3==1.42.92
python-dotenv==1.2.2
```

## 🔧 IAM Policy Required

Your IAM user needs these permissions:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "ec2:RunInstances",
                "ec2:DescribeInstances",
                "ec2:StopInstances",
                "ec2:TerminateInstances",
                "ec2:CreateTags"
            ],
            "Resource": "*"
        }
    ]
}
```

Attach `AmazonEC2FullAccess` policy for simplicity.

## 🛡️ Security Best Practices

| Practice | Why |
|----------|-----|
| ✅ Never commit `.env` files | Contains API keys |
| ✅ Use IAM roles with least privilege | Limits damage if compromised |
| ✅ Rotate access keys regularly | Reduces risk of old keys |
| ✅ Enable MFA on AWS account | Extra security layer |
| ✅ Review CloudTrail logs | Audit all API calls |

## 🐛 Troubleshooting

### Error: "Unable to locate credentials"

```bash
aws configure
```

### Error: "Instance type not available"

Update instance type in `aws_tools.py`:

```python
InstanceType='t3.micro'  # or t2.micro based on your region
```

### Error: "Connection refused"

Ensure uvicorn is running:

```bash
uvicorn main:app --reload
```

### Error: "InvalidParameterCombination"

The instance type is not available in your region. Run:

```bash
aws ec2 describe-instance-types --filters Name=free-tier-eligible,Values=true --region ap-south-1
```

## 🚀 Future Enhancements

- [ ] Support for more AWS services (S3, RDS, Lambda)
- [ ] Voice command support
- [ ] Docker containerization
- [ ] CI/CD pipeline integration
- [ ] Multi-region support
- [ ] Cost tracking dashboard
- [ ] Email/SMS notifications
- [ ] OpenAI integration for advanced NLP

## 🤝 Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

MIT License - feel free to use this project for learning or production!

## 🙏 Acknowledgments

- AWS for the free tier
- FastAPI for the amazing framework
- All contributors and testers
