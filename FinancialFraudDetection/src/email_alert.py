import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_fraud_alert(transaction_id, amount, location):
    # 🛑 SECURITY WARNING: Never push real passwords to GitHub!
    sender_email = "your_email@gmail.com"
    sender_password = "YOUR_APP_PASSWORD" 
    recipient_email = "security_team@bank.com"

    subject = f"🚨 URGENT: Fraudulent Transaction Detected - ID: {transaction_id}"
    
    body = f"""
    ALERT! A high-risk transaction has been flagged by the Machine Learning Pipeline.

    Transaction Details:
    - Transaction ID: {transaction_id}
    - Amount: ${amount}
    - Location: {location}
    - Model Confidence: 98.4% (Random Forest)

    Please freeze this account and investigate immediately.
    """

    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = recipient_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try:
        print(f"Triggering Alert System for Transaction {transaction_id}...")
        
        # --- EMAIL SERVER LOGIC ---
        # To make this live, uncomment the 4 lines below and add a real App Password
        
        # server = smtplib.SMTP("smtp.gmail.com", 587)
        # server.starttls()
        # server.login(sender_email, sender_password)
        # server.sendmail(sender_email, recipient_email, msg.as_string())
        # server.quit()
        
        print("✅ Alert system executed successfully (Simulated).")
    except Exception as e:
        print(f"❌ Failed to send email: {e}")

if __name__ == "__main__":
    # Simulating the ML model flagging a transaction
    send_fraud_alert(transaction_id="TXN_849302", amount=4500.00, location="New York")