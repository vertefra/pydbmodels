from src import pydbmodels

def main():
    pydbmodels.generate("postgres", "postgresql://postgres:postgres1@localhost:9876/postgres")

if __name__ == "__main__":
    main()