
import gradio as gr

def greet(name):
    return f"Hello your name is {name}!"

demo = gr.Interface(
    fn=greet,
    inputs="text",
    outputs="text",
    title="My App"
)
demo.launch()