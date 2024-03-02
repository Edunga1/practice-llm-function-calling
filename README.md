# practice-llm-function-calling

## Development Setup

1. Clone the Model from huggingface repository

```bash
$ git lfs install
$ git clone https://huggingface.co/Trelis/Llama-2-7b-chat-hf-function-calling-v2 llama2
```

2. Run ollama with docker

```bash
$ docker run -d \
  -v ollama:/root/.ollama \
  -v ./llama2:/root/llama2 \
  -v ./Modelfile:/root/llama2/Modelfile \
  -p 11434:11434 \
  --name ollama ollama/ollama serve
```

3. Create a model in container

```bash
$ docker exec -it ollama ollama create example -f /root/llama2/Modelfile
```

4. Test the model

```bash
$ curl http://localhost:11434/api/chat -d '{
  "model": "example",
  "prompt": "Why is the sky blue?"
}'
```
