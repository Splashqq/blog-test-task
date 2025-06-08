Инструкция по запуску
```
git clone https://github.com/Splashqq/blog-test-task.git
cd blog-test-task
```
После этого нужно установить переменные окружения внутри проекта в файле .env (в файле .env.example приведен пример переменных)

Запуск с помощью Docker'а
```
docker-compose up -d --build
```

Swagger будет доступен по http://localhost:8000/api/docs, чтобы воспользоваться API, используйте токен: supersecret