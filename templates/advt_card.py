<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>profile</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet"
        integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <style>
        a {
            text-decoration: none;
        }
    </style>
</head>

<body>
    <div class="container">
        <div style='height:50px; background-color: #a8e4a0; display: flex;
        justify-content: space-between; align-items: center;
        padding: 25px;' class="header">
            <div class="left">
                <a href="{{ url_for('get_all_teacher') }}">Главная страница</a>
            </div>
            <div style="width: 200px; display: flex; justify-content: space-around;" class="right">
                <a href="{{ url_for('get_registration_page') }}">Регистрация</a>
                <a href="{{ url_for('get_login_page') }}">Профиль</a>
            </div>
        </div>
        <br>
        {%block body%}
        <ul class="list-group">
            <li class="list-group-item">Название: {{title}}</li>
            <li class="list-group-item">Предмет: {{sub}}</li>
            <li class="list-group-item">Описание: {{desc}}</li>
            <br>
            {% if s_result != None%}
            <h2>Информация о ученике</h2>
            <br>
            <li class="list-group-item">Имя: {{s_result.name}}</li>
            <li class="list-group-item">Фамилия: {{s_result.surname}}</li>
            <li class="list-group-item">Почта: {{s_result.email}}</li>
            <li class="list-group-item">Телефон: {{s_result.phone_number}}</li>
            {% else %}
            <h2>Информация о учителе</h2>
            <br>
            <li class="list-group-item">Имя: {{t_result.name}}</li>
            <li class="list-group-item">Фамилия: {{t_result.surname}}</li>
            <li class="list-group-item">Почта: {{t_result.email}}</li>
            <li class="list-group-item">Телефон: {{t_result.phone_number}}</li>
            <li class="list-group-item">Рейтинг: {{t_result.average_rating}}</li>
            {% endif %}
        </ul>
        {% endblock %}
    </div>
</body>

</html>
