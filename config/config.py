site_url = ""

def cell(column_index, value):
    if column_index == 0:
        value = f"<a href=\"/networks/company-co/index.html\">{value}</a>"

    return f"<td>{value}</td>"

headings = "Name", "Status", "Linked sites", "Created"
network_table = html_table_csv("data/networks.csv", headings=headings, cell_fn=cell)

props = (
    ("Name", "company-co"),
    ("Status", "Active"),
    ("Created", "4 hours ago"),
)

network_properties = html_table(props, class_="properties")

def cell(column_index, value):
    if column_index == 0:
        value = f"<a href=\"/networks/company-co/sites/na-east/index.html\">{value}</a>"

    return f"<td>{value}</td>"

headings = "Name", "Type", "Status"
site_table = html_table_csv("data/sites.csv", headings=headings, cell_fn=cell)

def cell(column_index, value):
    if column_index == 0:
        value = f"<a href=\"/networks/company-co/services/frontend/index.html\">{value}</a>"

    return f"<td>{value}</td>"

headings = "Name", "Bindings"
service_table = html_table_csv("data/services.csv", headings=headings, cell_fn=cell)

props = (
    ("Name", "na-east"),
    ("Type", "OpenShift"),
    ("Status", "OK"),
)

site_properties = html_table(props, class_="properties")

def path_nav(page):
    separator = "<span class=\"path-separator\">›</span>"
    links = separator.join(list(page.path_nav_links)[1:])

    return f"<nav class=\"path-nav\">{links}</nav>"
