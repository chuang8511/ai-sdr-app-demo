# AI Sales SDR

This is a simple email content tools that can generate personalised content and send the email.

👉 Access the demo via [AI Sales SDR]


## Prerequisites
- Python

## Quick Start to Run the App Locally


### Clone the Repository
```bash
```

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Create a Secret File

#### Obtain Instill Cloud API Token
1. Log in to your [Instill Cloud](https://instill.tech) account.
2. Navigate to **Settings > API Tokens** to obtain your API token.

#### Add the Secret for the Demo
1. Create a `.streamlit` directory in your working directory if it doesn't exist.
2. Add a file named `secrets.toml` in the `.streamlit` directory.
3. In the `secrets.toml` file, set your Instill Cloud API token as follows:
    ```toml
    INSTILL_CLOUD_API_TOKEN = "<Your Instill Cloud API Token>"
    ```

### Run the Demo

Run the demo to ask questions about a page:
```bash
streamlit run streamlit_app.py
```
Now, open your browser and go to `http://localhost:8501` to start using the app.
