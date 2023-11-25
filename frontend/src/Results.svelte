<script>
    let withoutThrashed = false;
    let reports = fetch(import.meta.env.VITE_API_URL+'/api/processed-messages').then(response => response.json());
    
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
            {#await reports then reportsList}
                {#each reportsList as report}
                    {#if !withoutThrashed || !report["is_trash"]}
                        <tr>
                            <th>
                                <button on:click={() => {document.getElementById("modal-" + report['uuid']).showModal()}} style="background: none; border: none; color: #535bf2">Показать текст</button>
                                <dialog id="modal-{report['uuid']}">
                                    <p>{report["text"]}</p>
                                    <button on:click={() => {document.getElementById("modal-" + report['uuid']).close()}}>Закрыть</button>
                                </dialog>
                            </th>
                            <th>
                                {report["group"]}
                            </th>
                            <th>
                                {report["topic"]}
                            </th>
                            <th>
                                {fuzzyAddrToString(report["address"])}
                            </th>
                            <th>
                                {report["agency"]}
                            </th>
                            <th>
                                {#if report["is_trash"] === true}
                                    <p>✔</p>
                                {:else}
                                    <p>X</p>
                                {/if}
                            </th>
                        </tr>
                    {/if}
                {/each}
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
</style>
