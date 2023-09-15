import gradio as gr



with gr.Blocks(css=".gradio-container {background-color: red}") as demo:
    with gr.Row():
        with gr.Column(min_width=700):
            btn = gr.Button("Go")
    with gr.Row():
        text1 = gr.Textbox(label="t1")
        slider2 = gr.Textbox(label="s2")
        drop3 = gr.Dropdown(["a", "b", "c"], label="d3")
    
demo.queue()
demo.launch(share = True)