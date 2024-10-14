## YokAtlas Web Scraper

This project is a `web scraper` designed to extract bachelor's degree program details from universities in Turkey using `yokatlas.yok.gov.tr.` It is built using `Python` with `BeautifulSoup` and `Selenium` to efficiently parse and collect the required information.

### 0. Preview

<div style="float: left;">
    <img src="assets/1.png" style="width: 70%;" />
    <img src="assets/2.png" style="width: 70%;" />
    <img src="assets/3.png" style="width: 70%;" />
</div>

### 1. Installation

Ensure you have `Python 3.x`, `pip`, `virtualenv` and `chromedriver` installed on your system.

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

### 2. Usage

| Action                                 | Command                             |
| -------------------------------------- | ----------------------------------- |
| To Get Universities                    | `python main.py --get universities` |
| To Get Degrees                         | `python main.py --get degrees`      |
| To Reset the Database                  | `python main.py --tools reset`      |
| To Manipulate Data for Clean Operation | `python main.py --tools clean`      |
| For More Information                   | `python main.py --h`                |

### 3. Warning

This project is for `educational purposes only`, and `I take no responsibility` for any issues that may arise from its use.
