#This is the core file of the project that executes the application.

from website import create_app
app = create_app()
if __name__=='__main__':
    app.run(debug=True)