<script>
     let withoutThrashed = false;
     let reports = fetch('http://localhost:8000/api/processed-messages').then(response => response.json());
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
                    {#if !withoutThrashed}
                        <tr>
                            <th>
                                <button on:click={() => {document.getElementById("modal" + report['uuid']).showModal()}} style="background: none; border: none; color: #535bf2">Показать текст</button>
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
                                {
                                    report["address"]["region"]
                                    + report["address"]["area"].join(", ")
                                    + report["address"]["settlement"].join(", ")
                                    + report["address"]["street"].join(", ")
                                    + report["address"]["building"].join(", ")
                                }
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
