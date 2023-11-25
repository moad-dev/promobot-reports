<script>
    let rule = {
        uuid: '',
        group: '',
        topic: '',
        address: '',
        agency: '',
    };
    let rules = fetch(import.meta.env.VITE_API_URL+'/api/rules').then(response => response.json());
    let groups_json = fetch(import.meta.env.VITE_API_URL+'/groups').then(response => response.json());
    async function deleteRule(rule) {
        let rules = fetch(import.meta.env.VITE_API_URL + '/api/rules').then(response => response.json());
        let rules_list = await rules.then(result => result);
        fetch(import.meta.env.VITE_API_URL + '/api/rules/' + rules_list.slice(-1)[0]["uuid"], {
            method: 'DELETE',
            headers: {
                'Content-Type': 'application/json'
            },
            body:
                JSON.stringify({
                    uuid: rule["uuid"]
                })
        });
    }

    function addrToString(addrs) {
        let result = "";

        for (const addr of addrs) {
            const parts =  [];


            for (const [key, value] of Object.entries(addr)) {
                parts.push(value);
            }
            
            result += parts.join(", ");
        }

        return result;
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
                            {addrToString(rule["address"])}
                        </th>
                        <th>
                            {rule["agency"]}
                        </th>
                    </tr>
                {/each}
            {/await}
            {#await groups_json then groups_dict}
                <tr>
                    <th>
                        <select bind:value={rule.group}>
                            {#each Object.keys(groups_dict) as key}
                                <option>{key}</option>
                            {/each}
                        </select>
                    </th>
                    <th>
                        <select bind:value={rule.topic}>
                            {#if rule.group !== ''}
                                {#each groups_dict[rule.group] as item}
                                    <option>{item}</option>
                                {/each}
                            {/if}
                        </select>
                    </th>
                    <th>
                        <input type="text" bind:value={rule.address}>
                    </th>
                    <th>
                        <input type="text" bind:value={rule.agency}>
                    </th>
                </tr>
            {/await}
        </tbody>
    </table>

    <div style="margin-top: 20px">
        <a href="/">
            <button style="background: rgb(22,133,0)" on:click={() => {
                fetch(import.meta.env.VITE_API_URL+'/api/rules', {
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
                    }).then(response => response.json());
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
