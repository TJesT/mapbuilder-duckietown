from model.model import DataStock
from view.imgui_view import PygameImguiView

def main():
    stock = DataStock()
    view = PygameImguiView()
    view.setup(stock, size=(800,600))
    view.run()

if __name__ == '__main__':
    main()

