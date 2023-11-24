<script>

</script>

<h1>Promobot <span style="color: rgb(187,22,0)">Reports</span></h1>
<div style="display: grid">
    <textarea placeholder="Введите текст обращения..."></textarea>
    <div class="buttons">
        <button>Обработать</button>
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
        & > button + a {
            margin-left: 12px;
        }
    }
</style>