
### Running the Application
1. Create a virtual environment and install dependencies.
2. In the terminal, run `python3 src/main.py`

### Настройка Alembic для асинхронного драйвера
1. While in the root directory, run
`alembic init -t async migrations`
2. Move the `migrations` folder into the `src` folder.
3. Replace `prepend_sys_path` with `. src` and `script_location` with `src/migrations` inside `alembic.ini`


### API Documentation