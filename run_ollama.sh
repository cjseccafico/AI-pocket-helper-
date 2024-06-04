#!/bin/bash

# This script will first install ollama and then run it with the 'mistral' command.

# Download and execute the installation script
curl -fsSL https://ollama.com/install.sh | sh

# Run ollama with the 'mistral' command
ollama run mistral
