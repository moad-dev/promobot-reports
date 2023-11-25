<script>
    let [group, theme, address, agency] = ["Обработка...","Обработка...","Обработка...","Обработка..."];
    let response = fetch(import.meta.env.VITE_API_URL+'/api/processed-messages/' + localStorage.uuid).then(response => response.json())

    function fuzzyAddrToString(fuzzyAddrs) {
        let result = "";

        for (const addr of fuzzyAddrs) {
            const parts = addr['region'] ?? [];


            for (const [key, value] of Object.entries(addr)) {
                if (key !== "region" && value.length !== 0) {
                    parts.push(value);
                }
            }
            
            result += parts.join(", ") + ";";
        }

        return result;
    }

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
            {#await response}
            {:then predict}
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
                        { fuzzyAddrToString(predict["address"]) }
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
            {:catch error}
                <p style="color: red">{error.message}</p>
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
