#!/bin/bash

# Update package list and install required packages
sudo apt-get update
sudo apt-get install -y curl apt-transport-https

# Add the Datadog APT repository
echo "deb https://apt.datadoghq.com/ stable 7" | sudo tee /etc/apt/sources.list.d/datadog.list

# Add the Datadog GPG key
curl -fsSL https://keys.datadoghq.com/DATADOG_APT_KEY.public | sudo apt-key add -

# Install the Datadog Agent
sudo apt-get update
sudo apt-get install -y datadog-agent

# Configure the Datadog Agent
sudo cp datadog-agent.yaml /etc/datadog-agent/datadog.yaml

# Start the Datadog Agent
sudo service datadog-agent start

# Verify that the Datadog Agent is running
sudo datadog-agent status

