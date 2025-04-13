# Books Vector Data Base Embedding Script

This script is used to create a vector database of books. It uses the Langchain library to load the books and the OpenAI API to embed them. The vector database is stored in a Chroma database.

The purpose of this project is to serve as a reference for how to create a vector database of documents, to be used for a chatbot. This is a reference project for MR Bookcamp students.

This is a work in progress and will be updated as we add more features to the project.


## Libraries and Their Uses

- **Langchain**: Framework for building applications with language models, used here for document loading and text splitting
- **OpenAI API**: Generates embeddings for the text chunks
- **Chroma**: Vector database for storing and querying embeddings
- **Unstructured**: Helps process unstructured data like markdown files
- **Tika**: Extracts text and metadata from various file formats
- **Dotenv**: Manages environment variables, particularly for the OpenAI API key
- **OS**: Handles file system operations
- **Shutil**: Manages file and directory operations, used for cleaning up the Chroma database

## Usage

1. Clone the repository
2. Install the requirements
3. Run the the following command to create the vector database:

```bash
python create_database.py
```
5. Optionally you can add more documents to books directory and run the script again.
6. Optionally you can clean the database by running:
```bash
python create_database.py --clean
```


## Contributing

1. Fork the repository
2. Create a new branch
3. Make your changes and commit them
4. Push your changes to your fork
5. Create a pull request


### Commit Messages

We use Conventional Commits to format our commit messages.

| Prefix       | Description                                                                 |
|--------------|-----------------------------------------------------------------------------|
| `feat`       | A new feature (triggers a **minor** version bump in SemVer).                |
| `fix`        | A bug fix (triggers a **patch** version bump in SemVer).                    |
| `docs`       | Documentation changes (README, comments, etc.).                             |
| `style`      | Code style changes (formatting, linting, no functional changes).            |
| `refactor`   | Code restructuring (no new features or bug fixes).                          |
| `perf`       | Performance improvements.                                                   |
| `test`       | Adding or modifying tests.                                                  |
| `chore`      | Maintenance tasks (build config, dependencies, CI/CD).                      |
| `revert`     | Reverting a previous commit.                                                |
| `ci`         | Changes to CI/CD pipelines.                                                 |
| `build`      | Changes affecting the build system or dependencies.                         |

---

### Format of a Conventional Commit

```
<type>(<scope>): <description>
[optional body]
[optional footer]
```

```bash
**`<type>`**: The kind of change (`feat`, `fix`, `docs`, etc.).
**`<scope>`** (optional): The part of the codebase affected (e.g., `auth`, `api`, `ui`).
**`<description>`**: A concise summary of changes (imperative tense: "add" instead of "added").
**Body** (optional): Detailed explanation if needed.
**Footer** (optional): References like `BREAKING CHANGE:` or issue links (`Closes #123`).
```

---

### Examples

#### 1. Simple Feature Addition
```bash
git commit -m "feat(auth): add OAuth2 login support"
```

#### 2. Bug Fix with Issue Reference
```bash
git commit -m "fix(api): handle null response in user endpoint

Closes #456"
```
#### 3. Breaking Change (Major Version Bump)
```bash

git commit -m "feat(db): migrate to PostgreSQL

BREAKING CHANGE: drops support for MongoDB"
```
## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.




