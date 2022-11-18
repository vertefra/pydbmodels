# PYDBModels v0.0.11

## Database Models Generator

### Generates Class models from database introspection

Usage

```python
import pydbmodels

def main():
    pydbmodels.generate("postgres", "postgresql://postgres:postgres1@localhost:9876/postgres")

if __name__ == "__main__":
    main()
```

It Will create a `_models` folder with all the sub-folders representing different schema. In each schema folder, there will be a file representing a table, and in each table-file, three models, the `database model` the `model initializer` and the `model updater`

User defined Enums are supported and they will be placed in
`user_defined` module as a string representation of the Postgres enum values

### Generator
Generated models are [Pydantic](https://pydantic-docs.helpmanual.io/) classes, but eventually other generators that implement `IGenerator` interface can be added.

### Limitations
A lot. All supported types are the one that I actually need. I don't have a fully supported Database.
This project also depends from `dbmeta` for database introspection that has its own limitations. 
