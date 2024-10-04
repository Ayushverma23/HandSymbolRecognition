import torchvision.datasets as datasets

# Download EMNIST dataset
train_dataset = datasets.EMNIST(root='./data', split='letters', train=True, download=True)
test_dataset = datasets.EMNIST(root='./data', split='letters', train=False, download=True)

# Access the data and labels
train_data = train_dataset.data
train_labels = train_dataset.targets
test_data = test_dataset.data
test_labels = test_dataset.targets

# Print some information about the dataset
print("Training dataset size:", len(train_dataset))
print("Test dataset size:", len(test_dataset))
