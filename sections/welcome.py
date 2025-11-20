from nicegui import ui

def render(): 
    with ui.row().classes("w-full flex flex-row items-center justify-center"):
                # left text
        with ui.column().classes("w-1/2"):
            ui.label("Comfort Food • Modern Twist").classes("text-red-600 italic text-2xl mb-2")
            ui.html("<h1>WELCOME</h1>").classes("text-6xl font-extrabold mb-6 text-gray-900")
            ui.label("At Dannah’s Diner, we serve hearty meals made with love—bringing together classic comfort food and fresh, flavorful twists. Whether you are here for a quick bite or a cozy dinner with friends, our kitchen is always ready to make you feel at home.").classes("text-gray-600 leading-7 mb-8")
            ui.link("OUR STORY →", "/").classes("no-underline font-semibold text-gray-800 hover:text-red-600")
                
                # right-side image
        with ui.element("div").classes("w-1/2"):
            ui.image('/assets/lasagna.jpg').classes('rounded-xl shadow-md-full h-auto')
