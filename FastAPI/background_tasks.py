from fastapi import FastAPI, BackgroundTasks
import time

app = FastAPI()


def send_email(email: str):
    print(f"Sending email to {email}")
    time.sleep(5)
    print("Email sent successfully")


@app.post("/register")
async def register_user(
    email: str,
    background_tasks: BackgroundTasks
):
    background_tasks.add_task(send_email, email)

    return {
        "message": "User registered successfully"
    }