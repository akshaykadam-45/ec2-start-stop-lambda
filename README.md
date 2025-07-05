# 🚀 EC2 Start/Stop Automation Using AWS Lambda

This project shows how to use a single AWS Lambda function to start or stop EC2 instances by sending a simple input (`start` or `stop`).

---

## 🎯 Objective

Automate EC2 instance control (start/stop) using AWS Lambda to reduce manual work and manage cloud costs efficiently.

---

## 🛠️ Technologies Used

- AWS Lambda  
- Amazon EC2  
- IAM Role & Policy  
- Python (boto3 library)  
- AWS Console

---

## 🔢 Implementation Steps

### 1️⃣ Create IAM Role with EC2 Permissions

- Go to **IAM > Roles > Create Role**
- Choose:
  - Trusted entity: **AWS Service**
  - Use case: **Lambda**
- Attach this policy:

```json
{
    "Version": "2012-10-17",
    "Statement": [
        {
            "Effect": "Allow",
            "Action": [
                "logs:CreateLogGroup",
                "logs:CreateLogStream",
                "logs:PutLogEvents"
            ],
            "Resource": "arn:aws:logs:*:*:*"
        },
        {
            "Effect": "Allow",
            "Action": [
                "ec2:Start*",
                "ec2:Stop*"
            ],
            "Resource": "*"
        }
    ]
}
```

> 💡 You can later replace `"Resource": "*"` with specific instance ARNs.

- Name the role (e.g., `lambda-ec2-role`)

---

### 2️⃣ Create the Lambda Function

- Go to **AWS Lambda > Create Function**
- Select:
  - **Author from scratch**
  - Runtime: **Python 3.x**
  - Execution role: Use existing role → choose `lambda-ec2-role`

---

### 3️⃣ Add Lambda Code and Deploy

Replace the default code with:

```python
import boto3

region = 'us-west-1'  # Replace with your region
instances = ['i-12345cb6de4f78g9h', 'i-08ce9b2d7eccf6d26']  # Replace with your EC2 instance IDs
ec2 = boto3.client('ec2', region_name=region)

def lambda_handler(event, context):
    action = event.get('action')

    if action == 'start':
        ec2.start_instances(InstanceIds=instances)
        print('Started instances:', instances)
    elif action == 'stop':
        ec2.stop_instances(InstanceIds=instances)
        print('Stopped instances:', instances)
    else:
        print('Invalid action. Use "start" or "stop".')
```

Click **Deploy** to save your changes.

---

### 4️⃣ Create and Run Test Events

Click **Test** in the Lambda console and use these event inputs:

✅ Start:
```json
{
  "action": "start"
}
```

✅ Stop:
```json
{
  "action": "stop"
}
```

Check the output/logs and confirm your EC2 instance state changes accordingly.

---

### 5️⃣ (Optional) Monitor via CloudWatch Logs

Logs are available under **Monitor > View logs in CloudWatch** for each test run.

---

## 🙋‍♂️ Author

**Akshay Kadam**  
🔗 [LinkedIn](https://www.linkedin.com/in/akshaykadam45/)  
📂 Full working demo on [LinkedIn post](#)

