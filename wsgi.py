from project_name import create_app
from dotenv import load_dotenv, find_dotenv


load_dotenv(find_dotenv())


app = create_app()


if __name__ == "__main__":
    app.run()
