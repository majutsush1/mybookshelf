from mybookshelf import create_app
app = create_app()

if __name__ == "__main__":
	app.run(host='0.0.0.0', port=8080, use_reloader=True, debug=True)
