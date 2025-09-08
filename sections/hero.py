from nicegui import ui


def render():
   # big container
    with ui.element("div").style("background-image: url(/assets/table.jpg)").classes("h-screen w-screen flex flex-col bg-cover bg-center justify-center items-center"):
        # navbar
        with ui.element("nav").classes("flex flex-row justify-between items-center w-full fixed left-0 top-0 px-20 py-10"):
            # logo
            with ui.link(target='/'):
                ui.html('<i class=<i class="fa-solid fa-bowl-food"></i>').classes('text-white text-4xl')
            # navlinks  
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
                    ui.link(item["title"], item["path"]).classes("no-underline uppercase text-white font-bold")

            # socials
            with ui.row().classes("text-white"):
                ui.html('<i class="fa-brands fa-facebook-f"></i>')
                ui.html('<i class="fa-brands fa-instagram"></i>')
                ui.html('<i class="fa-brands fa-x-twitter"></i>')
        
        # text
        with ui.element("div").classes('text-white font-bold text-center bg-black/70 h-full w-full flex flex-col items-center justify-center'): 
            ui.label("Welcome to").classes("text-5xl")
            ui.html("<h1>Dannah's Diner</h1>").classes("text-7xl uppercase")
            ui.button("Our Menu", color="red-800").classes("")
            