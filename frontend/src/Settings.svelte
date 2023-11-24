<script>

</script>

<div style="display: grid; justify-content: center">
    <h1>Настройка правил отправки сообщений</h1>
    <table>
        <thead>
            <tr>
                <th>
                    Группа темы обращений
                </th>
                <th>
                    Тема обращения
                </th>
                <th>
                    Адрес обращения
                </th>
                <th>
                    Телефон указанный в обращении
                </th>
                <th>
                    Email отправки
                </th>
            </tr>
        </thead>
        <tbody>
            <tr>
                <th>
                    <select>
                        <option value="1">Группа 1</option>
                        <option value="2">Группа 2</option>
                        <option value="3">Группа 3</option>
                    </select>
                </th>
                <th>
                    <select>
                        <option value="1">Тема 1</option>
                        <option value="2">Тема 2</option>
                        <option value="3">Тема 3</option>
                    </select>
                </th>
                <th>
                    <input type="text">
                </th>
                <th>
                    <input type="tel">
                </th>
                <th>
                    <input type="email">
                </th>
            </tr>
        </tbody>
    </table>

    <div style="margin-top: 20px">
        <button style="background: rgb(22,133,0)">
            +
        </button>
        <button style="background: rgb(187,22,0)">
            –
        </button>
    </div>

    <div class="buttons">
        <a href="/">
            <button>
                Назад
            </button>
        </a>
        <a href="/">
            <button>
                Сохранить
            </button>
        </a>
    </div>
</div>

<style>
    .buttons {
        justify-self: end;
        margin-top: 20px;
    }

    a + a {
        margin-left: 12px;
    }

    table,
    td {
        border: 1px solid #333;
    }

    thead,
    tfoot {
        background-color: #646cff;
        color: #fff;
    }
</style>