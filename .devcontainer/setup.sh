#!/bin/bash
set -e

# Register Jupyter kernel (sbml env already exists in the image)
/opt/conda/envs/sbml/bin/python -m ipykernel install --user \
  --name sbml --display-name "Python (sbml)"

# Install Claude Code CLI
curl -fsSL https://deb.nodesource.com/setup_20.x | sudo -E bash -
sudo apt-get install -y nodejs
sudo npm install -g @anthropic-ai/claude-code

echo "==> Setup complete."
