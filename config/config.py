site_url = ""

def path_nav(page):
    separator = "<span class=\"path-separator\">&#8250;</span>"
    links = [x.replace("href=\"", f"href=\"{site_url}") for x in list(page.path_nav_links)[1:]]
    links = separator.join(links)

    return f"<nav class=\"path-nav\">{links}</nav>"

def table_link(content, href=""):
    return f"<a href=\"{href}\">{content}</a>"

def table_button(content, href=""):
    return f"<a class=\"table-button\" href=\"{href}\">{content}</a>"

def cell(column_index, value):
    if column_index == 0:
        value = table_link(value, href="company-co/index.html")
    elif column_index == 4:
        value = table_button("Console <span class=\"material-icons-outlined small\">open_in_new</span>")

    return f"<td>{value}</td>"

headings = "Name", "Status", "Linked sites", "Created", "Actions"

data = (
    ("company-co", "Active", "na-east, na-west, and headquarters", "4 hours ago", None),
    ("salty-pug", "Active", "store-1, factory-1, and 4 more", "3 days ago", None),
    ("bookinfo", "Disabled", "productpage, details, and 2 more", "1/8/2020", None),
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
        value = table_link(value, href="tokens/company-co-497c/index.html")
    elif column_index == 6:
        value = " ".join((table_button("Download"), table_button("Revoke")))

    return f"<td>{value}</td>"

headings = "Name", "Status", "Use count", "Use limit", "Expires", "Created", "Actions"

data = (
    ("company-co-497c", "Active", 0, 1, "Never", "3 minutes ago", None),
    ("company-co-af89", "Active", "-", "-", "In 6 hours", "2 days ago", None),
    ("company-co-f8fa", "Revoked", "-", "-", "-", "2 days ago", None),
)

token_table = html_table(data, headings=headings, cell_fn=cell)

props = (
    ("Name", "company-co-497c"),
    ("Status", "Active"),
    ("Use count", 0),
    ("Use limit", 1),
    ("Expires", "Never"),
    ("Created", "3 minutes ago"),
)

token_properties = html_table(props, class_="properties")

def cell(column_index, value):
    if column_index == 0:
        value = table_link(value, href="sites/na-east/index.html")
    elif column_index == 5:
        value = table_button("Unlink")

    return f"<td>{value}</td>"

headings = "Name", "Status", "Site type", "Cost", "Linked", "Actions"

data = (
    ("na-east", "OK", "OpenShift", 2, "2 days ago", None),
    ("na-west", "OK", "Podman", 1, "1/8/2020", None),
    ("headquarters", "Error: Unreachable", "OpenShift", 1, "3/15/2020", None),
)

site_table = html_table(data, headings=headings, cell_fn=cell)

props = (
    ("Name", "na-east"),
    ("Status", "OK"),
    ("ID", "e8f4c2ca-90cf-4882-9edc-5e9a802a3dab"),
    ("Version", "1.2.3"),
    ("Site type", "OpenShift"),
    ("Namespace", "na-east-prod"),
    ("Cost", 2),
    ("Linked", "2 days ago",),
)

site_properties = html_table(props, class_="properties")

def cell(column_index, value):
    if column_index == 3:
        value = table_button("Create a binding")

    return f"<td>{value}</td>"

headings = "Name", "Replicas", "Bindings", "Actions"

data = (
    ("frontend", 3, table_link("frontend-2da6", href=f"{site_url}/networks/company-co/services/frontend/bindings/frontend-2da6/index.html"), None),
    ("reviews", 2, "-", None),
    ("orders", 2, "-", None),
)

deployment_table = html_table(data, headings=headings, cell_fn=cell)

def cell(column_index, value):
    if column_index == 0:
        value = table_link(value, href="services/frontend/index.html")
    elif column_index == 4:
        value = table_button("Delete")

    return f"<td>{value}</td>"

headings = "Name", "Status", "Bindings", "Created", "Actions"

data = (
    ("frontend", "OK", 2, "3 minutes ago", None),
    ("inventory", "OK", 1, "4 hours ago", None),
    ("orders", "OK", 1, "2 days ago", None),
    ("database", "OK", 1, "3/15/2020", None),
    ("reviews", "Error: No bindings", 0, "3/15/2020", None),
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
        value = table_link(value, href="bindings/frontend-2da6/index.html")
    elif column_index == 5:
        value = table_button("Delete")

    return f"<td>{value}</td>"

headings = "Name", "Status", "Target", "Site", "Created", "Actions"

data = (
    ("frontend-2da6", "OK", "deployment/frontend", "na-east (OpenShift)", "2 days ago", None),
    ("frontend-45cc", "Error: Unreachable", "container/frontend", "na-west (Podman)", "1 day ago", None),
)

binding_table = html_table(data, headings=headings, cell_fn=cell)

props = (
    ("Name", "frontend-2da6"),
    ("Status", "OK"),
    ("Target", "deployment/frontend"),
    ("Site", table_link("na-east (OpenShift)", href=f"{site_url}/networks/company-co/sites/na-east/index.html")),
    ("Created", "2 days ago",),
)

binding_properties = html_table(props, class_="properties")
