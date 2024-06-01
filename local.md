1) Нужно подключить poetry "poetry init"
2) Добавить зависимости "poetry add"
3) Определяем структуру папок (app - папка с приложением, docker_compose - инфраструктура)
4) Сделать Makefile
5) Структура:
    - entity (domain) - сущности
    - repositories(infra) - тут лежат наши данные
    - gateways - kafka and etc.
    - services(logic) - логика
    - entrypoints(applications) - точки входа нашего приложения
6) Делаем "git init"
7) Пишем ".gitignore"
8) Делаем yaml файлы (app.yaml)
9) Пишем .env and .env.axample, пропимываем в app.yaml инструкцию
10) Создаем Dockerfile
 
