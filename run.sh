while true; do
    echo "Starting script..."
    poetry run python src/__init__.py &
    PID=$!
    echo "Script started. Watching for file changes..."
    inotifywait -q -e modify -r --exclude '.git|__pycache__' .
    echo "File change detected. Restarting script..."
    kill $PID
    echo "----------------------------------------"
done