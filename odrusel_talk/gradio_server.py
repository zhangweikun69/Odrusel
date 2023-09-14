import gradio as gr
import time
from organizer import fake_organizer
from AI_models import AIModels




with gr.Blocks(css=".gradio-container {background-color: red}") as demo:
    with gr.Row():
        with gr.Column(min_width=700):
            chatbot = gr.Chatbot()
            msg = gr.Textbox(label="User Input")
            clear = gr.Button("Clear Chat")
            AI_model = AIModels("gpt-3.5-turbo")

            def user(user_message, history):
                return "", history + [[user_message, None]]
            
            def bot(history):
                print(history)
                user_input = history[-1][0]
                messages = fake_organizer(user_input, history[:-1])
                bot_message = []
                response = AI_model.use_model_chat(messages)
                bot_message.append(response)
                history[-1][1] = ""
                for character in bot_message:
                    history[-1][1] += character
                    time.sleep(0.05)
                    yield history

            msg.submit(user, [msg, chatbot], [msg, chatbot], queue=False).then(bot, chatbot, chatbot)
            clear.click(lambda: None, None, chatbot, queue=False)

        with gr.Column(min_width=700):
            img1 = gr.Image("../odrusel_character/assistant_test/static/skeleton.png",
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
    
demo.queue()
demo.launch()

    