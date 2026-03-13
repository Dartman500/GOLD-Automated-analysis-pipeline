import requests
from pathlib import Path

def download_file(url, output):
    r = requests.get(url)
    with open(output, "wb") as f:
        f.write(r.content)

def main():
    data_dir = Path("data")
    data_dir.mkdir(exist_ok=True)

    # Example placeholder dataset
    url = "https://gold.cs.ucf.edu/data/search/"
    download_file(url, data_dir / "*.nc")

if __name__ == "__main__":
    main()
