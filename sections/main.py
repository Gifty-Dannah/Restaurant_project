from nicegui import ui, app 
from sections import hero, welcome

# Expose the assets folder to the nicegui server
app.add_static_files("/assets", "assets")

#  link external icons to the head
ui.add_head_html('''
                <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/facebook-nodejs-business-sdk/23.0.1/umd.js"
                 integrity="sha512-qIG6nSgAim6nCb1j+axhgwt+byAzyIjY5srF0XL2zxTNzNsZETRSgnyaHJwffuOIvltDoNImTrmrrJ82sCLLZg==" 
                 crossorigin="anonymous" referrerpolicy="no-referrer" />

                 ''')
ui.add_head_html('<link rel="stylesheet" href="/assets/reset.css"/>')

hero.render()
welcome.render()

ui.run()