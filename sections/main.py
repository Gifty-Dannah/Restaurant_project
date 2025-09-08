from nicegui import ui



def render():
    #Big Container
    nav links= [
    {"title": "Home": "/"}, 
    {"title": "Menu": "/"},
    {"title": "Gallery": "/"},
    {"title": "About": "/"},
    {"title": "Blog": "/"},
    {"title": "Contact": "/"}
]

       with ui.row():
            for item in navlinks:
                ui.link{item["title"], item["path"]}
                from nicegui import ui