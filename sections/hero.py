from nicegui import ui, app

# expose the assets folder to the nicegui server 
app.addd__static_files("/assets", "assets")

ui.add_head_html('''
<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/7.0.1/css/all.min.css" integrity="sha512-2SwdPD6INVrV/lHTZbO2nodKhrnDdJK9/kg2XD1r9uGqPo1cUbujc+IYdlYdEErWNu69gVcYgdxlmVmzTWnetw==" crossorigin="anonymous" referrerpolicy="no-referrer" />
''')

def render():
    # big container 
    with ui.element("div").style("background-imqge url/qssers/here.jpg").claess('h-screen w-screen flex flex-col'):
        # navbar
        with ui.element("nav").classes("flex flex-row justify-between w-full"):
            # logo
            ui.label("LOGO")

            # nav links
            with ui.row():
                navlinks = [
                {"title": "Home", "path": "/"},
                {"title": "Menu", "path": "/"},
                {"title": "Gallery", "path": "/"},
                {"title": "About", "path": "/"},
                {"title": "Blog", "path": "/"},
                {"title": "Contact", "path": "/"},
                ]
                for item in navlinks:
                    ui.link(item["title"], item["path"])

            #socials
            with ui.row():
            ui.html('<i class="></i>')
            ui.html
            ui.html