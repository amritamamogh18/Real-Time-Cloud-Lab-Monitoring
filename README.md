# Real-Time Cloud Lab Monitoring System  

A serverless AWS IoT solution to track university lab resources (CPU, RAM, occupancy) and alert admins via SNS when thresholds are exceeded.  

---

## 🛠️ **Tech Stack**  
- **AWS IoT Core**: Collects sensor data from lab computers.  
- **AWS Lambda**: Processes data and triggers alerts.  
- **Amazon SNS**: Sends email/SMS notifications.  
- **Python**: Sensor simulation and Lambda logic.  

---

## 📦 **Setup**  

### 1. **Prerequisites**  
- AWS account with IoT Core, Lambda, and SNS access.  
- Python 3.8+ and `pip` on lab machines.  

### 2. **Deployment**  
1. **AWS IoT Core Setup**:  
   - Create a *Thing* (e.g., `lab1`) and download certificates.  
   - Attach an IoT Policy with `iot:Publish` permissions.  

2. **Lambda & SNS**:  
   - Deploy `lambda_function.py` with an IoT trigger (Rule: `SELECT * FROM 'university/+/monitoring'`).  
   - Create an SNS topic (`lab-alerts`) and subscribe admins.  

3. **Sensor Simulation**:  
   ```bash
   pip install paho-mqtt
   python lab_sensor.py
