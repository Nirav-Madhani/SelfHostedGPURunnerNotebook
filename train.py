import yaml
import argparse
import torch
import torch.optim as optim
import torch.nn as nn
from data_loader import get_data_loader
from model import SimpleCNN
import os

def validate_model(model, criterion, data_loader, device):
    model.eval()
    val_loss = 0.0
    with torch.no_grad():
        for data, target in data_loader:
            data, target = data.to(device), target.to(device)
            output = model(data)
            loss = criterion(output, target)
            val_loss += loss.item()
    return val_loss / len(data_loader)

def train_model(config):
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    print(f"Using device: {device}")
    # Load training and validation data
    train_loader = get_data_loader(config)
    val_loader = get_data_loader(config)  # Assuming the same function can be used for validation

    # Initialize model, loss function, and optimizer
    model = SimpleCNN().to(device)
    criterion = nn.CrossEntropyLoss()
    optimizer = optim.Adam(model.parameters(), lr=config['training']['learning_rate'])

    # Training loop
    for epoch in range(config['training']['epochs']):
        print(f"Epoch {epoch + 1}/{config['training']['epochs']}")
        model.train()
        running_loss = 0.0
        for batch_idx, (data, target) in enumerate(train_loader):
            data, target = data.to(device), target.to(device)
            optimizer.zero_grad()
            output = model(data)
            loss = criterion(output, target)
            loss.backward()
            optimizer.step()
            running_loss += loss.item()

        train_loss = running_loss / len(train_loader)
        val_loss = validate_model(model, criterion, val_loader, device)

        print(f"Training Loss: {train_loss:.4f}, Validation Loss: {val_loss:.4f}")

        # Save checkpoint
        if (epoch + 1) % config['training']['checkpoint_interval'] == 0:
            checkpoint_path = os.path.join(config['training']['checkpoint_dir'], f"checkpoint_epoch_{epoch + 1}.pth")
            torch.save(model.state_dict(), checkpoint_path)
            print(f"Checkpoint saved at {checkpoint_path}")

    # Save the final model
    final_model_path = os.path.join(config['training']['checkpoint_dir'], 'final_model.pth')
    torch.save(model.state_dict(), final_model_path)
    print(f"Final model saved at {final_model_path}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Training")
    parser.add_argument('--config', type=str, default='config.yaml', help='Path to the config file')
    parser.add_argument('--epochs', type=int, help='Number of epochs to overwrite config file')
    parser.add_argument('--checkpoint_interval', type=int, help='Checkpoint interval to overwrite config file')

    args = parser.parse_args()

    with open(args.config, 'r') as file:
        config = yaml.safe_load(file)

    if args.epochs:
        config['training']['epochs'] = args.epochs

    if args.checkpoint_interval:
        config['training']['checkpoint_interval'] = args.checkpoint_interval

    os.makedirs(config['training']['checkpoint_dir'], exist_ok=True)

    train_model(config)
