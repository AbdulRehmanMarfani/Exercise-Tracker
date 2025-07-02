
---

# Exercise Tracker 🏋️‍♂️

A Python script that uses the **Nutritionix API** to interpret natural-language workout input and logs the results into a **Google Sheet** using the **Sheety API**.

---

## Features 📋

* **Natural Language Input**: Just type things like "ran 3km and did 20 pushups".
* **Nutritionix API Integration**: Automatically extracts duration, exercise name, and calories burned.
* **Google Sheet Logging**: Stores all data in a clean, timestamped format.
* **Environment Variable Security**: No sensitive info stored in code.
* **Modular & Scalable**: Easily add more logging features if needed.

---

## APIs Used 🔌

* [Nutritionix Exercise API](https://www.nutritionix.com/business/api)
* [Sheety API](https://sheety.co/)

---

## How It Works ⚙️

1. User inputs exercise activities in plain English.
2. Nutritionix returns structured data like:

   * Exercise name
   * Duration (in minutes)
   * Calories burned
3. Data is timestamped and sent to a Google Sheet using Sheety.

---

## Setup 🛠️

### 1. Clone the Repo

```bash
git clone https://github.com/AbdulRehmanMarfani/Exercise-Tracker.git
cd exercise-tracker
```

### 2. Environment Variables

Store the following as environment variables in your system:

| Variable Name         | Description              |
| --------------------- | ------------------------ |
| `NUTRITIONIX_APP_ID`  | Your Nutritionix App ID  |
| `NUTRITIONIX_APP_KEY` | Your Nutritionix App Key |
| `SHEETY_BEARER`       | Your Sheety Bearer Token |

#### For Windows (Command Prompt):

```bash
set NUTRITIONIX_APP_ID=your_app_id
set NUTRITIONIX_APP_KEY=your_app_key
set SHEETY_BEARER=your_bearer_token
```

#### For macOS/Linux (Bash):

```bash
export NUTRITIONIX_APP_ID=your_app_id
export NUTRITIONIX_APP_KEY=your_app_key
export SHEETY_BEARER=your_bearer_token
```

---

## Google Sheets Setup 🧾

1. Go to [sheety.co](https://sheety.co/) and connect your Google Sheet.

2. Create a sheet titled **My Workouts** (or anything you prefer).

3. Add a tab named `workouts` with the following headers in row 1:

   ```
   date | time | exercise | duration | calories
   ```

4. Get your Sheety project endpoint and bearer token.

5. Replace the existing `sheety_endpoint` in the code with your unique URL:

   ```python
   sheety_endpoint = "https://api.sheety.co/<your_project_id>/myWorkouts/workouts"
   ```

---

## Running the Script ▶️

Once everything is set:

```bash
python main.py
```

Example interaction:

```
Tell me which exercises you did: ran 5km and did 50 jumping jacks
```

Each activity gets logged in your Google Sheet with date, time, and calories.

---

## Sample Output 🖨️

| Date       | Time     | Exercise      | Duration | Calories |
| ---------- | -------- | ------------- | -------- | -------- |
| 02/07/2025 | 12:10:33 | Running       | 30       | 320      |
| 02/07/2025 | 12:10:33 | Jumping Jacks | 10       | 80       |

---

## Security 🔐

Keep all API keys in environment variables.
Avoid committing `.env` files or sensitive credentials.

> Learn how to set environment variables and app passwords [here](https://support.google.com/accounts/answer/185833?hl=en).

---
