<script>
    let [group, theme, address, agency] = ["Обработка...","Обработка...","Обработка...","Обработка..."];
    let response = fetch(API_URL+'/api/processed-messages/' + localStorage.uuid).then(response => response.json())
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
            {#await response then predict}
                <tr>
                    <th>
                        <button on:click={() => {document.getElementById("modal").showModal()}} style="background: none; border: none; color: #535bf2">Показать текст</button>
                        <dialog id="modal">
                            <p>{localStorage.text}</p>
                            <button on:click={() => {document.getElementById("modal").close()}}>Закрыть</button>
                        </dialog>
                    </th>
                    <th>
                        <p>{predict["group"]}</p>
                    </th>
                    <th>
                        <p>{predict["topic"]}</p>
                    </th>
                    <th>
                        <!-- address -->
                    </th>
                    <th>
                        <p>{predict["agency"]}</p>
                    </th>
                    <th>
                        {#if predict["is_trash"] === true}
                            <p>✔</p>
                        {:else}
                            <p>X</p>
                        {/if}
                    </th>
                </tr>
            {/await}
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
