import torch
import os
def get_data_loader(config):
    # Load the dataset from the file
    trainset = torch.load(os.path.join(config['data_preparation']['data_dir'], 'mnist_train.pt'))
    return torch.utils.data.DataLoader(trainset, batch_size=config['data_loader']['batch_size'], shuffle=True)
