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

Will create a `_models` folder with all the sub-folders representing different schema. In each schema folder, there will be a file representing a table, and in each table-file, three models, the `database model` the `model initializer` and the `model updater`

User defined Enums are supported and they will be placed in
`user_defined` module as a string representation of the Postgres enum values

### Generator
For now, generated models are [Pydantic](https://pydantic-docs.helpmanual.io/) classes with typechecking, but eventually other generators that implements `IGenerator` interface can be added

### Limitations
A lot. All the types supported are the one that I actually need at work, so I don't have a fully supported Database.
This project also depends from `dbmeta` for database introspection that has all its own limitations. 
