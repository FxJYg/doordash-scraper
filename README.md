# doordash-scraper 

This project scrapes menu items from a DoorDash restaurant page using **Playwright** and **Scrapybara**.  

## Features  
- Uses **Scrapybara** for automated browser management  
- Fetches **detailed menu item data** from DoorDash  
- Works on **Windows, macOS, and Linux**  
- Uses **Rye** for package management  

---

## Setup Instructions  

### **1. Install Rye**  

https://rye.astral.sh/guide/installation/

---

### **2️. Clone the Repository**  
```sh
git clone https://github.com/yourusername/doordash_scraper.git
cd doordash_scraper
```

---

### **3️. Set Up Environment Variables**  
Create a **.env** file in the project root and add your **Scrapybara API Key**:  
```
SCRAPYBARA_API_KEY=your_api_key_here
```
---

### **4. Run the Script**    
  ```sh
  rye init
  rye sycn
  .venv/Scripts/activate
  rye add scrapybara
  rye add undetected-playwright-patch
  rye add dotenv
  ```

---
