<script>
    let text = '';
</script>

<h1>Promobot <span style="color: rgb(187,22,0)">Reports</span></h1>
<div style="display: grid">
    <textarea bind:value={text} placeholder="Введите текст обращения..."></textarea>
    <div class="buttons">
        <a href="/predict">
            <button on:click={() => {localStorage.text = text;
            fetch(import.meta.env.VITE_API_URL+'/api/messages', {
                method:  'POST',
                headers: {
                    'Content-Type': 'application/json'
                },
                body:
                    JSON.stringify({
                        text: text
                    })
                }).then(response => response.json()).then(result => localStorage.uuid = result);
            }}>Обработать</button>
        </a>
        <a href="/results">
            <button>Результаты</button>
        </a>
        <a href="/settings">
            <button>Настройки</button>
        </a>
    </div>
</div>

<style>
    .buttons {
        justify-self: center;
        display: flex;
        margin-top: 20px;
        & a + a {
            margin-left: 12px;
        }
    }
</style>
