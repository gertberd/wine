from datetime import date
from http.server import HTTPServer, SimpleHTTPRequestHandler

from pandas import read_excel
from jinja2 import Environment, FileSystemLoader, select_autoescape


env = Environment(
    loader=FileSystemLoader("."), autoescape=select_autoescape(["html", "xml"])
)
template = env.get_template("template.html")
wines_file = "wine3.xlsx"
wines = read_excel(wines_file).fillna('').groupby(by=["Категория"])
since_year = 1920
current_year = date.today().year
years = current_year - since_year
rendered_page = template.render(wines=wines, years=years)
with open("index.html", "w", encoding="utf8") as file:
    file.write(rendered_page)
server = HTTPServer(("0.0.0.0", 8000), SimpleHTTPRequestHandler)
server.serve_forever()
