from datetime import datetime
from http.server import HTTPServer, SimpleHTTPRequestHandler
from jinja2 import Environment, FileSystemLoader, select_autoescape


env = Environment(
    loader=FileSystemLoader("."), autoescape=select_autoescape(["html", "xml"])
)
template = env.get_template("template.html")
since_year = 1920
current_year = datetime.now().year
years = current_year - since_year
rendered_page = template.render(years=years)
with open("index.html", "w", encoding="utf8") as file:
    file.write(rendered_page)
server = HTTPServer(("0.0.0.0", 8000), SimpleHTTPRequestHandler)
server.serve_forever()
