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
        value = f"<a href=\"/networks/company-co/tokens/company-co-497c/index.html\">{value}</a>"

    return f"<td>{value}</td>"

headings = "Name", "Status", "Created"

data = (
    ("company-co-497c", "OK", "3 minutes ago"),
    ("company-co-af89", "OK", "2 days ago"),
    ("company-co-f8fa", "Revoked", "2 days ago"),
)

token_table = html_table(data, headings=headings, cell_fn=cell)

props = (
    ("Name", "company-co-497c"),
    ("Status", "OK"),
    ("Created", "3 minutes ago"),
)

token_properties = html_table(props, class_="properties")

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

headings = "Name", "Status", "Bindings", "Created"

data = (
    ("frontend", "OK", 2, "3 minutes ago"),
    ("inventory", "OK", 1, "4 hours ago"),
    ("orders", "OK", 1, "2 days ago"),
    ("postgres", "OK", 1, "3/15/2020"),
    ("reviews", "OK", 1, "3/15/2020"),
    ("strimzi", "Error", 1, "1/01/2021"),
)

service_table = html_table(data, headings=headings, cell_fn=cell)

props = (
    ("Name", "na-east-d45e"),
    ("Status", "OK"),
    ("Site", "na-east (OpenShift)"),
    ("Created", "3 minutes ago",),
)

link_properties = html_table(props, class_="properties")
