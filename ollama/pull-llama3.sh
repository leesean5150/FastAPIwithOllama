./bin/ollama serve &

pid=$!

sleep 5

echo "Pulling Llama3 model"
ollama pull llama3

wait $pid