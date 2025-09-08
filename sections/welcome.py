from nicegui import ui

def render():
     ui.label("Welcome to Theody's Arena!")

with ui.element("div").classes("min-h-screen w-screen flex flex-col bg-gray-50"):
        # navbar
        with ui.element("nav").classes("flex flex-row justify-between items-center w-full fixed left-0 top-0 px-20 py-6 bg-white shadow"):
            # logo
            with ui.link(target='/'):
                ui.html('<span class="border-2 border-red-600 text-red-600 rounded-xl px-3 py-1 font-bold">PATO</span> <span class="ml-2 text-xs text-red-600 font-semibold">RESTAURANT</span>')
            
            # navlinks  
            navlinks = [
                {"title": "Home", "path": "/"}, 
                {"title": "Menu", "path": "/"},
                {"title": "Gallery", "path": "/"},
                {"title": "About", "path": "/"},
                {"title": "Reservation", "path": "/"},
                {"title": "Contact", "path": "/"},
            ]
            with ui.row().classes("gap-8"):
                for item in navlinks:
                    ui.link(item["title"], item["path"]).classes("no-underline text-gray-700 hover:text-red-600 font-semibold uppercase")
            
            # socials
            with ui.row().classes("text-gray-600 gap-4"):
                ui.html('<i class="fa-brands fa-tripadvisor"></i>')
                ui.html('<i class="fa-brands fa-facebook-f"></i>')
                ui.html('<i class="fa-brands fa-instagram"></i>')
                ui.html('<i class="fa-brands fa-twitter"></i>')
                ui.html('<i class="fa-solid fa-bars"></i>')
        
        # content
        with ui.row().classes("flex-1 items-center justify-center px-20 py-40 gap-20"):
            # left text
            with ui.column().classes("w-1/2"):
                ui.label("Comfort Food • Modern Twist").classes("text-red-600 italic text-2xl mb-2")
                ui.html("<h1>WELCOME</h1>").classes("text-6xl font-extrabold mb-6 text-gray-900")
                ui.label("At Dannah’s Diner, we serve hearty meals made with love—bringing together classic comfort food and fresh, flavorful twists. Whether you are here for a quick bite or a cozy dinner with friends, our kitchen is always ready to make you feel at home.").classes("text-gray-600 leading-7 mb-8")
                ui.link("OUR STORY →", "/").classes("no-underline font-semibold text-gray-800 hover:text-red-600")
            
            # right-side image
            with ui.element("div").classes("w-1/2"):
                ui.html('<img src="/assets/welcome.jpg" class="rounded-xl shadow-md w-full h-auto"/>')

