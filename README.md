# **LMS Webhook Integration for Course & Grade Sync**  

### **📌 Overview**  
This project enables **real-time course and grade synchronization** between institutions using **webhooks**. Instead of traditional polling-based APIs, institutions receive **event-driven updates** when new grades are available.  

🔹 **Key Features:**  
- **Webhook-based communication** for grade syncing.  
- **Event-driven architecture** (automatic updates instead of polling).  
- **Retry mechanism** for failed webhook deliveries.  
- **Dynamic API support** for multiple institutions.  

---

## **📌 How It Works**  

### **1️⃣ Registering a Webhook**  
An institution registers a **webhook URL** to receive grade updates.  

🔹 **API Request (Register Webhook)**  
```bash
curl -X POST "http://127.0.0.1:5000/register_webhooks" \
-H "Content-Type: application/json" \
-d '{
    "university_id": "INST_A",
    "webhook_url": "http://institutiona.edu/api/receive_grade"
}'
```
✅ **Response**  
```json
{
    "message": "Webhook registered successfully",
    "webhook_url": "http://institutiona.edu/api/receive_grade"
}
```

---

### **2️⃣ Submitting a Grade Update**  
When a student **completes a course**, an institution **sends a grade update**.  

🔹 **API Request (Submit Grade Update)**  
```bash
curl -X POST "http://127.0.0.1:5000/submit_grade" \
-H "Content-Type: application/json" \
-d '{
    "student_id": "123",
    "course_id": "CS101",
    "grade": "A",
    "university_id": "INST_A"
}'
```
✅ **Response**  
```json
{
    "message": "Grade submitted, webhook triggered",
    "webhook_response": "Success"
}
```

---

### **3️⃣ Fetching Registered Webhooks**  
Institutions can retrieve their **registered webhook URLs** dynamically.  

🔹 **API Request (Get Webhooks for a Specific Institution)**  
```bash
curl -X GET "http://127.0.0.1:5000/get_webhooks/INST_A"
```
✅ **Response**  
```json
{
    "university_id": "INST_A",
    "webhooks": ["http://institutiona.edu/api/receive_grade"]
}
```

---

## **📌 Architecture**  
### **🔹 Components & Flow**  
1️⃣ **Webhook Handler** - Stores webhook URLs and triggers them when needed.  
2️⃣ **Event-Driven Processing** - Institutions receive updates automatically instead of polling.  
3️⃣ **Dynamic API Handling** - Institutions can register and retrieve their own webhooks.  

```plaintext
Institution B → (API Call) → Webhook Handler → (Triggers Webhook) → Institution A
```

---

## **📌 Error Handling & Scalability**  
| **Scenario** | **Current Handling** |
|-------------|----------------------|
| Webhook URL is down | **Retries up to 3 times**, then logs failure. |
| Bulk grade updates | **Sequential processing** (not optimized for high volume). |
| API failure | API returns an error response, but no persistent logging. |

---

## **📌 Installation & Setup**  
### **🔹 Prerequisites**  
- Python 3.x  
- Flask  

### **🔹 Install Dependencies (If Required)**  
```bash
pip install flask requests
```

### **🔹 Run the Application**  
```bash
python app.py
```

---

## **📌 Testing the APIs Using Postman**  
To test the API endpoints in **Postman**, follow these steps:

### **1️⃣ Import Postman Collection**  
- **Go to Postman → Import**  
- Upload the file **`webhooks.postman_collection.json`** (included in this repo).  
- This will **pre-load all API requests for easy testing**.  

### **2️⃣ Testing the APIs**  
| **API Name** | **Method** | **Endpoint** | **Test Scenario** |
|-------------|-----------|-------------|----------------|
| **Register Webhook** | `POST` | `http://127.0.0.1:5000/register_webhooks` | Register a webhook for an institution. |
| **Get Webhooks** | `GET` | `http://127.0.0.1:5000/get_webhooks/{{university_id}}` | Retrieve registered webhooks dynamically. |
| **Submit Grade** | `POST` | `http://127.0.0.1:5000/submit_grade` | Submit a grade update and trigger webhooks. |
| **Receive Grade** | `POST` | `http://127.0.0.1:5000/receive_grade` | Simulate a webhook receiving a grade update. |

---

## **📌 Technical Debt**  
While functional, this system has **several areas for improvement**:

1️⃣ **No Persistent Storage:** Webhook registrations are stored **in memory**, meaning they are lost if the server restarts. **Improvement:** Use **Mongo DB** for persistent storage.

2️⃣ **No Authentication or Security Measures:** APIs are **publicly accessible** without authentication. **Improvement:** Implement **OAuth 2.0, JWT authentication, or API keys**.

3️⃣ **No Asynchronous Processing:** Webhook events are handled **synchronously**, leading to delays. **Improvement:** Use **Kafka** for event queueing.

🚀 **Addressing these areas will improve reliability, security, and scalability.**

