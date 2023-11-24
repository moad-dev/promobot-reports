<script>
    let [group, theme, adress, agency] = ["Обработка...","Обработка...","Обработка...","Обработка..."]
</script>

<div style="display: grid; justify-content: center">
    <h1>Результаты обработки</h1>
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
                Мусор
            </th>
        </tr>
        </thead>
        <tbody>
            <tr>
                <th>
                    <button on:click={() => {document.getElementById("modal").showModal()}} style="background: none; border: none; color: #535bf2">Показать текст</button>
                    <dialog id="modal">
                        <p>{localStorage.text}</p>
                        <button on:click={() => {document.getElementById("modal").close()}}>Закрыть</button>
                    </dialog>
                </th>
                <th>
                    <p>{group}</p>
                </th>
                <th>
                    <p>{theme}</p>
                </th>
                <th>
                    <p>{adress}</p>
                </th>
                <th>
                    <p>{agency}</p>
                </th>
                <th>
                    Мусор
                </th>
            </tr>
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

    ::backdrop {
        opacity: 0.5;
    }
</style>