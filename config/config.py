site_url = ""

def path_nav(page):
    separator = "<span class=\"path-separator\">›</span>"
    links = separator.join(list(page.path_nav_links)[1:])

    return f"<nav class=\"path-nav\">{links}</nav>"

def cell(column_index, value):
    if column_index == 0:
        value = f"<a href=\"/networks/company-co/index.html\">{value}</a>"

    return f"<td>{value}</td>"

headings = "Name", "Status", "Linked sites", "Created"

data = (
    ("company-co", "Active", "na-east, na-west, and headquarters", "4 hours ago"),
    ("salty-pug", "Active", "store-1, factory-1, and 4 more", "3 days ago"),
    ("bookinfo", "Disabled", "productpage, details, and 2 more", "1/8/2020"),
)

network_table = html_table(data, headings=headings, cell_fn=cell)

props = (
    ("Name", "company-co"),
    ("Status", "Active"),
    ("Linked sites", "na-east, na-west, and headquarters"),
    ("Created", "4 hours ago"),
)

network_properties = html_table(props, class_="properties")

def cell(column_index, value):
    if column_index == 0:
        value = f"<a href=\"/networks/company-co/links/na-east-d45e/index.html\">{value}</a>"

    return f"<td>{value}</td>"

headings = "Name", "Status", "Site", "Cost", "Created"

data = (
    ("na-east-d45e", "OK", "na-east (OpenShift)", 1, "3 minutes ago"),
    ("na-east-7c7b", "OK", "na-east (OpenShift)", 2, "2 days ago"),
    ("na-west-4f84", "OK", "na-west (Podman)", 1, "1/8/2020"),
    ("headquarters-a96a", "Error", "headquarters (OpenShift)", 1, "3/15/2020"),
)

link_table = html_table(data, headings=headings, cell_fn=cell)

def cell(column_index, value):
    if column_index == 0:
        value = f"<a href=\"/networks/company-co/services/frontend/index.html\">{value}</a>"

    return f"<td>{value}</td>"

headings = "Name", "Bindings"

data = (
    ("frontend", 2),
    ("inventory", 1),
    ("orders", 1),
    ("postgres", 1),
    ("reviews", 1),
    ("strimzi", 1),
)

service_table = html_table(data, headings=headings, cell_fn=cell)

props = (
    ("Name", "na-east-d45e"),
    ("Status", "OK"),
    ("Site", "na-east (OpenShift)"),
    ("Created", "3 minutes ago",),
)

link_properties = html_table(props, class_="properties")
