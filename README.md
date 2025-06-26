



# 📡 signalWalker

**A Terminal-Based Phone Number Tracker using API Integration, Logging, and CLI Interaction.**

🎧 _Inspired by Alan Walker’s digital vibes (according to the developer's personal choice)._  
🧠 _Built with Python by a passionate tech enthusiast._

---















## 🔥 Overview

**signalWalker** is a command-line utility that tracks the **primary information** (such as location, carrier, line type, country) of any valid phone number using the **numverify API**. It logs all runtime activity for debugging or analytics and provides a stylish terminal banner to enhance the user experience.

---















## ✨ Features

- 📱 Track phone number metadata via API (location, carrier, country, etc.)  
- 🧪 Built-in unit testing (with room for mocking API calls in the future)  
- 🧾 Logging with timestamps in `signalWalker_logfile.log`  
- 👨‍💻 Fully terminal-based interaction (CLI)  
- 🎨 Custom ASCII art banner  
- ⚙️ Environment variable support for secure API keys  
- ❌ Graceful error handling  

---
















## 🛠️ Setup

### ✅ Requirements

- Python 3.8+  
- Internet connection (for API)  
- `requests` module (install using `pip install requests`)  
- `unittest` or `pytest` module for unit testing purposes  

---

















### 🔐 API Key Setup

1. Go to [numverify.com](https://numverify.com/) and create an account.  
2. Get your **free API key**.  
3. Set the API key in your OS environment variable:

#### For Windows:
```bash```
setx num_verify_API_key "your_api_key_here"


####For Linux/macOS:
```bash```
export num_verify_API_key="your_api_key_here"


---


















🚀 How to Run
Clone this repository:
```bash```

git clone https://github.com/porgrammerSoma880/signalWalker.git
cd signalWalker


python signalWalker.py

or 

python3 signalWalker.py





You'll be prompted to:

Enter your name

Enter a phone number, along with the country code to track its location


---
















🧪 Unit Testing
To run the basic unit test:


```bash```

python -m unittest test_signalWalker.py


or


```bash```

python -m pytest test_signalWalker.py


⚠️ Note: Actual API calls will be made. For better testing, consider mocking responses using unittest.mock.

---


















🧪 Type Checking
You can run mypy to check type safety of the code:

```bash```
python -m mypy signalWalker.py


---
















📂 Project Structure
signalWalker/
├── signalWalker.py                 # Main script
├── test_signalWalker.py            # Unit test
├── signalWalker_ascii_banner.py    # ASCII banner (bonus!)
├── signalWalker_logfile.log        # Runtime logs (auto-created)
├── .gitignore                      # gitignore file
├── README.md                       # You're reading this!


---
















🎯 Future Improvements
✅ Mock API calls in tests

📈 GUI added using Electron.js

🌍 Support for offline/region database

🧠 Integrate with AI for smart data classification

ℹ️ More phone number related information support using a better API


---














⚠️ Disclaimer
This tool uses the numverify API for educational and ethical purposes only. Do not use it for any illegal tracking or privacy violations. The creator/developer will not be responsible for any misuse or damage caused.

---











💡 Contributions
Contributions are sincerely welcome! If you have any ideas, don't hesitate to submit a pull request!

---














📄 License
This project is licensed under the MIT License - see the LICENSE file for details.

---














🧑‍💻 Author
Created by: Soma Jahan Madhobilata

Built with passion to empower developers, investigators, and curious minds. Whether you’re debugging, tracking, or just exploring — signalWalker is here to give you clarity and control.

"Data is power, and power is in your hands."

Stay curious. Stay relentless. Keep walking the digital path. 🚀✨



---




