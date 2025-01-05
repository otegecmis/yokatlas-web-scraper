from app.scraper import Scraper
from app.cleaner import Cleaner
from tqdm import tqdm
import os, json

class App: 
    def __init__(self) -> None:
        self.scraper = Scraper()
        self.cleaner = Cleaner()

    def universities(self):
        if not os.path.exists("./data"):
            os.makedirs("./data")
        
        if not os.path.exists("./data/universities.json"):
            print("🔄 In Progress: Generating 'universities.json'")

            universities = self.scraper.get_universities()
            
            with open("./data/universities.json", "w") as f:
                json.dump(universities, f, indent=4, ensure_ascii=False)

            print("🟢 Success: 'universities.json' has been generated successfully.")
        else:
            print("🟢 Success: 'universities.json' already exists.")

        print("⚪️ Info: Please remember to manually update the './data/universities.json' file if necessary.")

    def degrees(self):
        if not os.path.exists("./data/degree_ids.json"):

            print("🔄 In Progress: Scraping is starting for degree IDs...")

            universities = []
            degree_ids = []

            with open("./data/universities.json", "r") as f:
                universities = json.load(f)

            for university in tqdm(universities):
                degrees = self.scraper.get_degrees_by_university(university[1])

                for degree in degrees:
                    degree_ids.append(degree[1])

            with open("./data/degree_ids.json", "w") as f:
                json.dump(degree_ids, f, indent=4, ensure_ascii=False)

        if not os.path.exists("./data/degrees.json"):
            print("🔄 In Progress: Scraping is starting for degree data...")

            degree_ids = []
            with open("./data/degree_ids.json", "r") as f:
                degree_ids = json.load(f)

            degrees = []
            for degree_id in tqdm(degree_ids):
                degree_info = self.scraper.get_degree_info(degree_id)
                degrees.append(degree_info)
            
            with open(f"./data/degrees.json", "w") as f:
                json.dump(degrees, f, indent=4, ensure_ascii=False)

        print("👍 Success: Scraping has been completed successfully.")
        print("⚪️ Info: You can find the scraped data in the './data' folder.")
        print("⚪️ Info: If you want a fresh start, please run the '--tools reset' command.")
    
    def reset(self):
        if os.path.exists("./data"):
            os.system("rm -rf ./data")
            print("🟢 Success: The 'data' folder has been deleted.")
    
    def clean(self):
        if self.cleaner.degrees():
            print("🟢 Success: The 'degrees.json' file has been cleaned.")
        else:
            print("🔴 Error: Failed to clean the 'degrees.json' file.")
