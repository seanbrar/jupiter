from pathlib import Path

import kaggle
from dotenv import load_dotenv


def is_dataset_downloaded(dataset_name: str, path: str="./data") -> bool:
    """
    Check if the dataset is already downloaded by comparing the list of files
    in the dataset with the files in the local directory.
    """
    # Create a unique folder name using both the user and dataset name
    user, dataset = dataset_name.split("/")
    dataset_path = Path(path) / f"{user}_{dataset}"

    # Get list of files for the dataset from Kaggle API
    kaggle_files = kaggle.api.dataset_list_files(dataset_name).files
    kaggle_filenames = {file.name for file in kaggle_files}

    # Check if the local folder exists and if it contains all files
    if not dataset_path.exists():
        return False

    local_filenames = {f.name for f in dataset_path.glob("*")}

    # Check if all the Kaggle files are present locally
    return kaggle_filenames.issubset(local_filenames)

def download_dataset(dataset_names: list, path: str="./data"):
    """
    Download one or more datasets from Kaggle if they are not already downloaded.
    """
    for dataset_name in dataset_names:
        user, dataset = dataset_name.split("/")
        # Create a unique folder for each dataset
        dataset_folder = Path(path) / f"{user}_{dataset}"

        if is_dataset_downloaded(dataset_name, path):
            print(f"Dataset '{dataset_name}' is already downloaded in {dataset_folder}.")
        else:
            print(f"Downloading dataset '{dataset_name}'...")
            kaggle.api.dataset_download_files(dataset_name, path=dataset_folder, unzip=True)
            print(f"Dataset '{dataset_name}' downloaded to {dataset_folder}")

if __name__ == "__main__":
    load_dotenv()

    dataset_names = ["promptcloud/indeed-job-posting-dataset",
                    #  "andrewmvd/data-analyst-jobs",  # Temporarily disable most datasets
                    #  "rrkcoder/glassdoor-data-science-job-listings",
                    #  "asaniczka/1-3m-linkedin-jobs-and-skills-2024",
                    #  "promptcloud/indeed-usa-job-listing-dataset",
                    #  "mdkamruzzaman23/machine-learning-job-listings-on-glassdoor",
                    #  "promptcloud/indeed-job-listing-usa",
                    #  "zain280/data-science-job",
                    #  "arshkon/linkedin-job-postings",
                    #  "andrewmvd/data-scientist-jobs",
                    #  "kanchana1990/ai-and-ml-job-listings-usa",
                    #  "arshkon/linkedin-job-postings",
                     "emreksz/data-scientist-job-roles-in-uk"]
    download_dataset(dataset_names)
