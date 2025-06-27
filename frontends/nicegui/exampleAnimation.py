from nicegui import ui
from nicegui.events import ValueChangeEventArguments




def giveSVG(rot=90):
    return f'''

    <svg
    width="200.839402mm"
    height="108.58428mm"
    viewBox="0 0 11.839402 108.58428"
    version="1.1"
    id="svg1"
    xmlns:inkscape="http://www.inkscape.org/namespaces/inkscape"
    xmlns:sodipodi="http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd"
    xmlns="http://www.w3.org/2000/svg"
    xmlns:svg="http://www.w3.org/2000/svg">
    
    <defs
        id="defs1" />
    <g
        inkscape:label="Capa 1"
        inkscape:groupmode="layer"
        id="layer1"
        transform="translate(-80.84625,12.515943)">
        <g
        id="g2"
        inkscape:export-filename="g2.svg"
        inkscape:export-xdpi="96"
        inkscape:export-ydpi="96"
        transform="rotate({rot},86.765945,41.776196)">
        <rect
            style="fill:#000000;stroke-width:0.264583"
            id="rect1"
            width="108.58428"
            height="3.7209566"
            x="32.473804"
            y="40.930519"
            inkscape:export-filename="rect1.svg"
            inkscape:export-xdpi="96"
            inkscape:export-ydpi="96" />
        <ellipse
            style="fill:#000000;stroke-width:0.264583"
            id="path1"
            cx="88.288155"
            cy="41.776196"
            rx="7.7801819"
            ry="5.919704" />
        </g>
    </g>
    </svg>'''

svg_plot = None
angle_num = None


def change_rot(event: ValueChangeEventArguments):
    svg_plot.content = giveSVG(event.value)
    angle_num.value = event.value

with ui.column().style("width: 300px"):
    svg_plot = ui.html(giveSVG(0))

    ui.label("Ángulo de rotación")
    ui.slider(min=0, max=180,step = 5,value=90,on_change=change_rot)#.bind_value(rot, 'number')
    angle_num = ui.number(label="angle",value=90,on_change=change_rot)



ui.run()