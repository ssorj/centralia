site_url = ""

def path_nav(page):
    separator = "<span class=\"path-separator\">&#8250;</span>"
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

headings = "Name", "Status", "Expires", "Created"

data = (
    ("company-co-497c", "Active", "Never", "3 minutes ago"),
    ("company-co-af89", "Active", "In 6 hours", "2 days ago"),
    ("company-co-f8fa", "Revoked", "-", "2 days ago"),
)

token_table = html_table(data, headings=headings, cell_fn=cell)

props = (
    ("Name", "company-co-497c"),
    ("Status", "OK"),
    ("Expires", "Never"),
    ("Created", "3 minutes ago"),
)

token_properties = html_table(props, class_="properties")

def cell(column_index, value):
    if column_index == 0:
        value = f"<a href=\"/networks/company-co/sites/na-east/index.html\">{value}</a>"

    return f"<td>{value}</td>"

headings = "Name", "Status", "Site type", "Cost", "Linked"

data = (
    ("na-east", "OK", "OpenShift", 2, "2 days ago"),
    ("na-west", "OK", "Podman", 1, "1/8/2020"),
    ("headquarters", "Error: Unreachable", "OpenShift", 1, "3/15/2020"),
)

site_table = html_table(data, headings=headings, cell_fn=cell)

props = (
    ("Name", "na-east"),
    ("Status", "OK"),
    ("Site type", "OpenShift"),
    ("Linked", "2 days ago",),
)

site_properties = html_table(props, class_="properties")

headings = "Name", "Replicas", "Bindings", "Actions"

data = (
    ("frontend", 3, "<a href=\"/networks/company-co/services/frontend/bindings/frontend-2da6/index.html\">frontend-2da6</a>", "<a class=\"table-button\" href=\"\">Add binding</a>"),
    ("reviews", 2, "-", "<a class=\"table-button\" href=\"\">Add binding</a>"),
    ("orders", 2, "-", "<a class=\"table-button\" href=\"\">Add binding</a>"),
)

deployment_table = html_table(data, headings=headings)

def cell(column_index, value):
    if column_index == 0:
        value = f"<a href=\"/networks/company-co/services/frontend/index.html\">{value}</a>"

    return f"<td>{value}</td>"

headings = "Name", "Status", "Bindings", "Created", "Actions"

data = (
    ("frontend", "OK", 2, "3 minutes ago", "<a class=\"table-button\" href=\"\">Delete</a>"),
    ("inventory", "OK", 1, "4 hours ago", "<a class=\"table-button\" href=\"\">Delete</a>"),
    ("orders", "OK", 1, "2 days ago", "<a class=\"table-button\" href=\"\">Delete</a>"),
    ("database", "OK", 1, "3/15/2020", "<a class=\"table-button\" href=\"\">Delete</a>"),
    ("reviews", "Error: No bindings", 0, "3/15/2020", "<a class=\"table-button\" href=\"\">Delete</a>"),
)

service_table = html_table(data, headings=headings, cell_fn=cell)

props = (
    ("Name", "frontend"),
    ("Status", "OK"),
    ("Created", "3 minutes ago",),
)

service_properties = html_table(props, class_="properties")

def cell(column_index, value):
    if column_index == 0:
        value = f"<a href=\"/networks/company-co/services/frontend/bindings/frontend-2da6/index.html\">{value}</a>"

    return f"<td>{value}</td>"

headings = "Name", "Status", "Target", "Site", "Created", "Actions"

data = (
    ("frontend-2da6", "OK", "deployment/frontend", "na-east (OpenShift)", "2 days ago", "<a class=\"table-button\" href=\"\">Delete</a>"),
    ("frontend-45cc", "Error: Unreachable", "container/frontend", "na-west (Podman)", "1 day ago", "<a class=\"table-button\" href=\"\">Delete</a>"),
)

binding_table = html_table(data, headings=headings, cell_fn=cell)
