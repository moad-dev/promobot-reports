<script>
     let withoutThrashed = false;
</script>

<div style="display: grid; justify-content: center">
    <h1>Результаты обработки</h1>
    <div style="justify-self: end; margin-bottom: 4px">
        <label for="filter">Оставить только обращения</label>
        <input type="checkbox" bind:checked={withoutThrashed} id="filter" name="filter">
    </div>
    <table>
        <thead>
        <tr>
            <th>
                Текст обращения
            </th>
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
                Ведомства для отправки
            </th>
            <th>
                <p>Мусор</p>
            </th>
        </tr>
        </thead>
        <tbody>

        </tbody>
    </table>
    <a href="/" style="margin-top: 20px; justify-self: end">
        <button>
            Назад
        </button>
    </a>
</div>

<style>
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