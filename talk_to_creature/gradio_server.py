import gradio as gr
from test import test1

def chat(user_input, history):
    history = history or []
    response = test1(user_input)
    history.append((user_input, response))


with gr.Blocks(css=".gradio-container {background-color: red}") as demo:
    with gr.Row():
        with gr.Column(min_width=700):
            text1 = gr.Textbox(label="prompt 1")


        with gr.Column(min_width=700):
            img1 = gr.Image("static/skeleton.png",
                            image_mode='L', 
                            show_download_button = False,
                            interactive = False, 
                            show_share_button = False,
                            show_label= False,
                            width=700, height=700)
            btn = gr.Button("Go")
    with gr.Row():
        text1 = gr.Textbox(label="t1")
        slider2 = gr.Textbox(label="s2")
        drop3 = gr.Dropdown(["a", "b", "c"], label="d3")
    
if __name__ == "__main__":    
    demo.launch()