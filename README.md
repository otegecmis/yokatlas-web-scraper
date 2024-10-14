## YokAtlas Web Scraper

This project is a `web scraper` designed to extract bachelor's degree program details from universities in Turkey using `yokatlas.yok.gov.tr.` It is built using `Python` with `BeautifulSoup` and `Selenium` to efficiently parse and collect the required information.

### 1. Installation

Ensure you have `Python 3.x`, the `pip` package manager, `virtualenv` and `chromedriver` installed on your system.

1. **Clone the repository**

```sh
git clone https://github.com/otegecmis/yokatlas-web-scraper.git
```

2. **Navigate to the project directory**

```sh
cd yokatlas-web-scraper
```

3. **Create a virtual environment**

```sh
virtualenv env
```

4. **Activate the virtual environment**

```sh
. env/bin/activate
```

5. **Install the required dependencies**

```sh
pip install -r requirements.txt
```

6. **Run the scraper**

```sh
python main.py -h
```
