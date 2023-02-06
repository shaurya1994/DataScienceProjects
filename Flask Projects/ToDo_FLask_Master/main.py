from website import initialize_app # Automatically looks for __init__


app = initialize_app()

if __name__ == '__main__': # Entry point to te app
    app.run(debug=True, port=1000) # If any changes are made it automatically reflects on the web server. (*Use only in development)
