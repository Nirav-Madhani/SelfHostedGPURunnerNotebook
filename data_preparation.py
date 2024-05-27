import torch
from torchvision import datasets, transforms
import argparse
import yaml
import os

def prepare_data(config):
    # Ensure the data directory exists
    os.makedirs(config['data_preparation']['data_dir'], exist_ok=True)

    # Define a transform to normalize the data
    transform = transforms.Compose([transforms.ToTensor(), transforms.Normalize((0.5,), (0.5,))])

    # Download and load the training data
    trainset = datasets.MNIST(root=config['data_preparation']['data_dir'], train=True, download=True, transform=transform)
    trainloader = torch.utils.data.DataLoader(trainset, batch_size=config['data_loader']['batch_size'], shuffle=True)

    # Save the dataset to a file
    torch.save(trainset, os.path.join(config['data_preparation']['data_dir'], 'mnist_train.pt'))

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Data Preparation")
    parser.add_argument('--config', type=str, default='config.yaml', help='Path to the config file')
    parser.add_argument('--param', type=str, help='Additional parameter to overwrite config file')

    args = parser.parse_args()

    with open(args.config, 'r') as file:
        config = yaml.safe_load(file)

    if args.param:
        # Overwrite config parameters if needed
        config['data_preparation']['param'] = args.param

    prepare_data(config)
