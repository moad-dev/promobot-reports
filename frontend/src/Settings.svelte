<script>
    let rule = {
        uuid: '',
        group: '',
        topic: '',
        address: '',
        agency: '',
    };
    let rules = fetch(API_URL+'/api/rules').then(response => response.json());
    function deleteRule(rule) {
        console.log(rule["uuid"])
        fetch(API_URL+'/api/rules' + rule["uuid"], {
            method:  'DELETE',
            headers: {
                'Content-Type': 'application/json'
            },
            body:
                JSON.stringify({
                    uuid: rule["uuid"]
                })
        }).then(response => response.json())
            .then(result => console.log(result));
    }
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
                    Ведомства для отправки
                </th>
            </tr>
        </thead>
        <tbody>
            {#await rules then rules_list}
                {#each rules_list as rule}
                    <tr>
                        <th>
                            {rule["group"]}
                        </th>
                        <th>
                            {rule["topic"]}
                        </th>
                        <th>
                            {
                                rule["address"]["region"] +
                                rule["address"]["area"] +
                                rule["address"]["settlement"] +
                                rule["address"]["street"] +
                                rule["address"]["building"] || "—"
                            }
                        </th>
                        <th>
                            {rule["agency"]}
                        </th>
                    </tr>
                {/each}
            {/await}
            <tr>
                <th>
                    <select bind:value={rule.group}>
                        <option value="1">Группа 1</option>
                        <option value="2">Группа 2</option>
                        <option value="3">Группа 3</option>
                    </select>
                </th>
                <th>
                    <select bind:value={rule.topic}>
                        <option value="1">Тема 1</option>
                        <option value="2">Тема 2</option>
                        <option value="3">Тема 3</option>
                    </select>
                </th>
                <th>
                    <input type="text" bind:value={rule.address}>
                </th>
                <th>
                    <input type="text" bind:value={rule.agency}>
                </th>
            </tr>
        </tbody>
    </table>

    <div style="margin-top: 20px">
        <a href="/">
            <button style="background: rgb(22,133,0)" on:click={() => {
                fetch(API_URL+'/api/rules', {
                    method:  'POST',
                    headers: {
                      'Content-Type': 'application/json'
                    },
                    body:
                        JSON.stringify({
                            group: rule.group,
                            topic: rule.topic,
                            address: rule.address,
                            agency: rule.agency,
                        })
                    }).then(response => response.json())
                            .then(result => console.log(result));
            }}>
                +
            </button>
        </a>
        <a href="/">
            <button style="background: rgb(187,22,0)" on:click={() => {deleteRule(rule)}}>
                –
            </button>
        </a>
    </div>

    <div class="buttons">
        <a href="/">
            <button>
                Назад
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
