from nicegui import ui
from nicegui.events import ValueChangeEventArguments
class Demo:
    def __init__(self):
        self.number = 1

demo = Demo()
def show(event: ValueChangeEventArguments):
    name = type(event.sender).__name__
    print(f"evento:{name}")
    ui.notify(f'{name}: {event.value}')

ui.button('Button', on_click=lambda: ui.notify('Click'))
with ui.row():
    ui.checkbox('Checkbox', on_change=show)
    ui.switch('Switch', on_change=show)
    
ui.radio(['A', 'B', 'C'], value='A', on_change=show).props('inline')
with ui.row():
    ui.input('Text input', on_change=show)
    ui.select(['One', 'Two'], value='One', on_change=show)
ui.link('And many more...', '/documentation').classes('mt-8')


v = ui.checkbox('visible', value=True)
with ui.column().bind_visibility_from(v, 'value'):
    ui.slider(min=1, max=3).bind_value(demo, 'number')
    ui.toggle({1: 'A', 2: 'B', 3: 'C'}).bind_value(demo, 'number')
    ui.number().bind_value(demo, 'number')

ui.run()