# doordash-scraper 

This project scrapes menu items from a DoorDash restaurant page using **Playwright** and **Scrapybara**.  

## Features  
-Uses **Scrapybara** for automated browser management  
-Fetches **detailed menu item data** from DoorDash  
-Works on **Windows, macOS, and Linux**  
-Uses **Rye** for package management  

---

## Setup Instructions  

### **1️⃣ Install Rye**  

**Windows (PowerShell)**  
```powershell
irm https://rye.astral.sh/get | iex
```
Then restart your terminal **or** run:  
```powershell
refreshenv
```

**Linux/macOS**  
```sh
curl -sSf https://rye.astral.sh/get | bash
source ~/.rye/env
```

---

### **2️⃣ Clone the Repository**  
```sh
git clone https://github.com/yourusername/doordash_scraper.git
cd doordash_scraper
```

---

### **3️⃣ Sync Dependencies**  
```sh
rye sync
```

---

### **4️⃣ Set Up Environment Variables**  
Create a **.env** file in the project root and add your **Scrapybara API Key**:  
```
SCRAPYBARA_API_KEY=your_api_key_here
```
---

### **5️⃣ Run the Script**  
- **Windows**  
  ```sh
  rye run start
  ```
- **Linux/macOS**  
  ```sh
  rye run start
  ```

---
